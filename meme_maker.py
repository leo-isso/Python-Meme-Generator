import os
import textwrap

from DrawStroke import DrawTextStroke

from PIL import Image, ImageDraw, ImageFont

class Meme_maker():

    def __init__(self):

        #default variables (free to change)
        self.default_meme = 'default_meme'
        self.generated_meme = 'new_memes'
        
        self.default_font_path = 'font/impact.ttf'
        #default_font_size, default_font, changes depending on image size, function 'img_resize'
        self.default_font_size = 32
        self.default_font = ImageFont.truetype(self.default_font_path, self.default_font_size)

        self.max_img_size = (500,500)
        self.meme_text_color = 'white'
        self.meme_text_shadow = 'black'

        self.max_letter_line = 30
        self.top_text_margin = 5
        self.bot_text_margin = 10
        self.text_padding = 3

    def select_img(self, img_location):

        #Check if the file is valid as a command or an link, and open
        local_meme = '{}\\{}.jpg'.format(self.default_meme,img_location)
        external_meme = img_location
    
        if os.path.isfile(local_meme):
            print(local_meme)
            print('Valid file... (local meme)')
            return Image.open(local_meme)

        elif os.path.isfile(external_meme):
            print(external_meme)
            print('Valid file...(external meme)')
            return Image.open(external_meme)
    

    def img_resize(self, img):

        #resize image
        meme = img
        size = self.max_img_size
        meme.thumbnail(size)
        
        #checking meme dimensions and changing font-size
        meme_width, meme_height = meme.size
        if meme_width > meme_height:
            self.default_font_size = 30
            self.max_letter_line = 32
            self.default_font = ImageFont.truetype(self.default_font_path, self.default_font_size)

        elif meme_height > meme_width:
            self.default_font_size = 42
            self.max_letter_line = 18
            self.default_font = ImageFont.truetype(self.default_font_path, self.default_font_size)

        return meme

    def img_text(self, img, top_text, bot_text):
        
        meme = img
        top_text = top_text
        bot_text = bot_text
        draw = ImageDraw.Draw(meme)
        meme_width, meme_height = meme.size

        #formating text
        formated_top_text = textwrap.wrap(top_text, width=self.max_letter_line)
        formated_bot_text = textwrap.wrap(bot_text, width=self.max_letter_line)

        #draw top text (center)
        top_line_height = self.top_text_margin
        padding = self.text_padding
        top_line_coords = [top_line_height]

        #generate top text coordinates
        for line in formated_top_text:
            text_width, text_height = draw.textsize(line, font=self.default_font)
            top_line_height += text_height + padding
            top_line_coords.append(top_line_height)
        current_coord = 0

        for line in formated_top_text:
            text_width, text_height = draw.textsize(line, font=self.default_font)
            pos_x = (meme_width - text_width) / 2
            pos_y = top_line_coords[current_coord]
            DrawTextStroke(meme, pos_x, pos_y, line, self.default_font, 2)
            current_coord += 1

        #draw bot text (center)
        bot_line_height = (meme_height - self.bot_text_margin)
        bot_line_coords = [bot_line_height]

        #generate bot text coordinates
        for line in formated_bot_text:
            text_width, text_height = draw.textsize(line, font=self.default_font)
            bot_line_height -= text_height - padding
            bot_line_coords.append(bot_line_height)
        bot_line_coords.reverse()
        current_coord = 0

        for line in formated_bot_text:
            text_width, text_height = draw.textsize(line, font=self.default_font)
            pos_x = (meme_width - text_width) / 2
            pos_y = bot_line_coords[current_coord]
            DrawTextStroke(meme, pos_x, pos_y, line, self.default_font, 2)
            current_coord += 1
        

        return meme

    def save_meme(self, img):

        meme = img
        
        #generate name
        save_path = self.generated_meme
        meme_name = 'new_meme'
        meme_id = len(os.listdir(self.generated_meme))

        name_template = '{}{}.jpg'.format(meme_name,str(meme_id))
        path_template = save_path + '\\' + name_template

        if os.path.isfile(path_template):
            while os.path.isfile(path_template):
                meme_id += 1
                name_template = '{}{}.jpg'.format(meme_name,str(meme_id))
                path_template = save_path + '\\' + name_template

        #save
        meme.save(path_template, 'jpeg')
        print('\n Dank meme generated as: {}'.format(name_template))
