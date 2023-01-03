import uuid

from django.shortcuts import redirect, render
from PIL import Image, ImageDraw, ImageFont
from requests import request

from .models import ImageModel

# Create your views here.

def copy(input_path,text)->str:
    photo = Image.open(input_path)
    w , h = photo.size
    draw = ImageDraw.Draw(photo)
    Text = text
    font = ImageFont.truetype("Game of Thrones.ttf",50)
    text_w , text_h = draw.textsize(text , font)
    pos = w - text_w , (h - text_h) - 50
    c_text = Image.new('RGB',(text_w , text_h),color="#000000")
    draw = ImageDraw.Draw(c_text)
    draw.text((0,0),Text,fill="#fff", font = font)
    c_text.putalpha(100) 
    photo.paste(c_text, pos, c_text) 
    file_name = f'{uuid.uuid4()}.png'
    output_path = f'public/static/output/{file_name}'
    photo.save(output_path)

    return f'http://localhost:8000/media/output/{file_name}'


def index(request): 
    if request.method == "POST":
        image = request.FILES['image']
        water_mark = request.POST.get("water_mark")
        image = ImageModel.objects.create(image=image, water_mark=water_mark)
        output_path = copy(f'public/static/{image.image}', water_mark)
 
        return redirect(output_path)

    return render(request, "index.html")