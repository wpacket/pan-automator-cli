from jinja2 import Environment, FileSystemLoader
import yaml
 
config = yaml.load(open('./template.yml'))
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('panorama_DG_cli.j2')
 
print(template.render(config))
