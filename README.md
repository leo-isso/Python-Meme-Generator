# Pyhton Meme Generator

Pyhton Meme Generator was created with the objective of studying python's "[Pillow (PIL)](http://pillow.readthedocs.io/en/3.4.x/index.html)" library.

You can run the script through the teminal using the `main.py` file.

Or you can use a `main.py` function with some arguments:
```
generate_meme(meme_image, top_text, bot_text)
```
`meme_image` is the path to the meme image (with the extension). You can also use one of the images in the `default_meme` folder (only the file name, without path or extension (jpg only)).

`top_text` is the text to be written on the top of the meme.

`bot_text` is the text to be written on the bottom of the meme.

#### E.g:

```
generate_meme('grumpycat', 'LOVE IS IN THE AIR', 'GET THE GAS MASK')
```

Generated meme:

![grumpycat](/new_memes/new_meme1.jpg)

### Future implementation:

- [ ] Get image from URL using `Requests`
- [ ] `local_memes` use any image extension `Requests`