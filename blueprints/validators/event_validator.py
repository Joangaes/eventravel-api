from cerberus import Validator, schema;

class EventValidator(object):
    def __init__(self) -> None:
        super().__init__()
        self.schema = {'_foreign_id':{'type':'string'}}
    def validate(self,document):
        return Validator(self.schema).validate(document)