from cerberus import Validator, schema;

class EventValidator(object):
    def __init__(self) -> None:
        super().__init__()
        self.schema = {'test':{'type':'integer'}}
    def validate(self,document):
        return Validator(self.schema).validate(document)