import converter.controller as controller_converter
import converter.model as model_converter
import converter.service as service_converter
import util.util as util

_template = """package {package};

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import {service_package}.{service_class};
import {model_package}.{model_class};

@RestController
public class {class_name} {{

    private final {service_class} {service_var};

    @Autowired
    public {class_name}({service_class} {service_var}) {{
        this.{service_var} = {service_var};
    }}

    @RequestMapping(value = "/{base_route}/{{id}}", method = RequestMethod.POST)
    public {model_class} create(@PathVariable {id_type} id, @RequestBody {model_class} {model_var}) {{
        return this.{service_var}.create({model_var});
    }}

    @RequestMapping(value = "/{base_route}/{{id}}", method = RequestMethod.GET)
    public {model_class} read(@PathVariable {id_type} id) {{
        return this.{service_var}.read(id);
    }}

    @RequestMapping(value = "/{base_route}/{{id}}", method = RequestMethod.PUT)
    public {model_class} update(@PathVariable {id_type} id, @RequestBody {model_class} {model_var}) {{
        return this.{service_var}.update({model_var});
    }}

    @RequestMapping(value = "/{base_route}/{{id}}", method = RequestMethod.DELETE)
    public void delete(@PathVariable {id_type} id) {{
        this.{service_var}.delete(id);
    }}

}}

"""


def gen_contents(file_info, id_type='Integer'):
    service_package = service_converter.gen_package_name()
    service_class = service_converter.gen_class_name(file_info.seed_name)
    model_package = model_converter.gen_package_name()
    model_class = model_converter.gen_class_name(file_info.seed_name)

    return _template.format(
        base_route=util.type_to_snake_case(controller_converter.gen_root_name(file_info.seed_name)),
        package=file_info.package,
        class_name=file_info.class_name,
        model_package=model_package,
        model_class=model_class,
        model_var=util.type_to_var(model_class),
        service_package=service_package,
        service_class=service_class,
        service_var=util.type_to_var(service_class),
        id_type=id_type)