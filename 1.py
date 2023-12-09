from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('template_task1.html')

select_name = "color"
val_list = ["синий", "зеленый", "красный"]
selected_num = 2

result_html = template.render(
    val_list=val_list,
    select_name=select_name,
    selected_num=2,
    range=range
)

with open('res_task1.html', 'w', encoding='utf-8-sig') as res:
  res.write(result_html)