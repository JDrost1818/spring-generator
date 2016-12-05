import data.settings as settings
import template.util as util
from current import TEMPLATE as TEMPLATE
from current_lombok import TEMPLATE as LOMBOK_TEMPLATE
from domain.field import Field

_field_template = '''
    private {type} {name};
'''

_getter_setter_template = '''
    public {type} get{cap_name}() {{
        return this.{name};
    }}

    public void set{cap_name}({type} {name}) {{
        this.{name} = {name};
    }}
'''

_dependency_template = 'import {dep};\n'


def get_template(enable_lombok):
    return LOMBOK_TEMPLATE if enable_lombok else TEMPLATE


def gen_contents(file_info, id_type='Integer'):
    dependencies = ''
    body = ''

    # Enters all the fields to be associated with the model
    for field in file_info.fields:
        body += _field_template.format(type=field.field_type.class_name, name=field.name)

    # If lombok is not supported, we must manually
    # enter in the getters and the setters
    if not settings.IS_LOMBOK_SUPPORTED:
        for field in [Field('id', 'Integer')] + file_info.fields:
            body += _getter_setter_template.format(
                type=field.field_type.class_name,
                name=field.name,
                cap_name=field.name.capitalize())

            if field.field_type.has_dependency():
                dependencies += _dependency_template.format(dep=field.field_type.dependency)

    return util.format_template(get_template(settings.IS_LOMBOK_SUPPORTED).format(
        package=file_info.package,
        dependencies=dependencies,
        class_name=file_info.class_name,
        id_type=id_type,
        header='',
        body=body))
