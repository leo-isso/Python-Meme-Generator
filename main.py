__author__ = "Leonardo Isso"
__version__ = "0.1.0"

from meme_maker import Meme_maker

MK = Meme_maker()

def run_terminal():
    meme = input('Select your meme: ')
    meme = MK.select_img(meme)
    top_text = input('\nSelect the top text: ')
    bot_text = input('\nSelect the bottom text: ')
    meme = MK.img_resize(meme)
    meme = MK.img_text(meme, top_text, bot_text)
    MK.save_meme(meme)

def generate_meme(meme_image, top_text, bot_text):
    meme = MK.select_img(meme_image)
    meme = MK.img_resize(meme)
    meme = MK.img_text(meme, top_text, bot_text)
    MK.save_meme(meme)

if __name__ == '__main__':
    run_terminal()
