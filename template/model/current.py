TEMPLATE = '''package {package};

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
{header}
@Entity
public class {class_name} {{

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private {id_type} id;
    {body}

}}

'''
