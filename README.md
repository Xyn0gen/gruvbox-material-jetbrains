# Gruvbox Material

This is a port of the [Gruvbox Material theme by sainnhe](https://github.com/sainnhe/gruvbox-material/) using [subtheme-dev's monokai-pro](https://github.com/subtheme-dev/monokai-pro) as a base for intellij IDEs. 

It is somewhat modified from the original colorscheme to match the VSCode port a little more.

Reads colorscheme from a yaml file in the colours folder and uses jinja2 to render the templates

## Building the theme
Render the template then open `gruvbox-material` in Intellij to build the .jar plugin file.

```
pip install -r requirements.txt
python build_theme.py
```

Light themes aren't properly implemented. Just slapped them in a yaml file and called it a day since I don't actually use light themes (ง •_•)ง
