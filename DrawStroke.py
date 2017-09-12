from PIL import Image, ImageDraw, ImageFont


def DrawTextStroke(base_image, pos_x, pos_y,  text, text_font, stroke_size=None, text_color=None, shadow_color=None):

    if stroke_size == None:
        stroke_size = 1

    if text_color == None:
        text_color = 'white'
    
    if shadow_color == None:
        shadow_color = 'black'

    image = base_image
    draw = ImageDraw.Draw(image)

    shadow_left = pos_x - stroke_size
    shadow_right = pos_x + stroke_size
    shadow_top = pos_y - stroke_size
    shadow_bottom = pos_y + stroke_size
    
    #ImageDraw.Draw(Image.open('link')).text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left")
    draw = ImageDraw.Draw(base_image)
    draw.text((shadow_left, shadow_top), text, font=text_font, fill=shadow_color)
    draw.text((shadow_left, shadow_bottom), text, font=text_font, fill=shadow_color)
    draw.text((shadow_right, shadow_top), text, font=text_font, fill=shadow_color)
    draw.text((shadow_right, shadow_bottom), text, font=text_font, fill=shadow_color)
    draw.text((pos_x, pos_y), text, font=text_font, fill=text_color)

    return image