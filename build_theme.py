from jinja2 import Environment, FileSystemLoader
import yaml
import glob

files = glob.glob("colors/*.yaml")
themes = []
for color in files:

    with open(color, "r") as file:
        theme = yaml.load(file, Loader=yaml.FullLoader)

    themes.append(theme["id"])

    env = Environment(loader=FileSystemLoader("templates/"))

    data = {"theme": theme, "italics": False}

    scheme = env.get_template("scheme.xml")
    scheme_content = scheme.render(data)

    theme = env.get_template("theme.json")
    theme_content = theme.render(data)

    scheme_output = f"gruvbox-material/resources/theme/{data['theme']['id']}.xml"
    theme_output = f"gruvbox-material/resources/theme/{data['theme']['id']}.theme.json"
    with open(scheme_output, mode="w", encoding="utf-8") as message:
        message.write(scheme_content)
        print(scheme_output)

    with open(theme_output, mode="w", encoding="utf-8") as message:
        message.write(theme_content)
        print(theme_output)

# print(themes)
plugin = env.get_template("plugin.xml")
plugin_content = plugin.render({"themes": themes})
with open("gruvbox-material/resources/META-INF/plugin.xml", mode="w", encoding="utf-8") as message:
    message.write(plugin_content)
    print("gruvbox-material/resources/META-INF/plugin.xml")