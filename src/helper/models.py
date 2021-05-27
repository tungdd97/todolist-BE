from peewee import *
from src.api import sys_log


class ModelHelper:

    def __init__(self):
        self.log = sys_log.logger

    def get_dictionary_from_model(self, model, fields=None, exclude=None):
        try:
            model_class = type(model)
            data = {}

            fields = fields or {}
            exclude = exclude or {}
            curr_exclude = exclude.get(model_class, [])
            curr_fields = fields.get(model_class, model._meta.sorted_field_names)

            for field_name in curr_fields:
                if field_name in curr_exclude:
                    continue
                field_obj = model_class._meta.fields[field_name]
                field_data = model._data.get(field_name)

                if isinstance(field_obj, ForeignKeyField) and field_data and field_obj.rel_model in fields:
                    rel_obj = getattr(model, field_name)
                    data[field_name] = self.get_dictionary_from_model(rel_obj, fields, exclude)
                elif isinstance(field_obj, DateTimeField) and field_data is not None:
                    data[field_name] = field_data.strftime("")
                elif isinstance(field_obj, BlobField) and field_data is not None:
                    data[field_name] = field_data.decode('utf-8')
                else:
                    data[field_name] = field_data
            return data
        except Exception as e:
            self.log.error('error when convert model to dict' + str(e))
            raise

    def get_model_from_dictionary(self, model, field_dict):
        if isinstance(model, Model):
            model_instance = model
            check_fks = True
        else:
            model_instance = model()
            check_fks = False
        models = [model_instance]
        for field_name, value in field_dict.items():
            field_obj = model._meta.fields[field_name]
            if isinstance(value, dict):
                rel_obj = field_obj.rel_model
                if check_fks:
                    try:
                        rel_obj = getattr(model, field_name)
                    except field_obj.rel_model.DoesNotExist:
                        pass
                    if rel_obj is None:
                        rel_obj = field_obj.rel_model
                rel_inst, rel_models = self.get_model_from_dictionary(rel_obj, value)
                models.extend(rel_models)
                setattr(model_instance, field_name, rel_inst)
            else:
                setattr(model_instance, field_name, field_obj.python_value(value))
        return model_instance, models
