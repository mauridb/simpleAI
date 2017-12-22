class Chatbot(object):
    def __init__(self, name, role='robot', description='', *args, **kwargs):
        self.name = name
        self.role = role
        self.description = description

        for key, value in kwargs.items():
            setattr(self, key, value)

    def talk(self):
        return 'hello'

class ChatbotInspector(Chatbot):
    def __init__(self, *args, **kwargs):
        super(ChatbotInspector, self).__init__(*args, **kwargs)

    def listen(self):
        return 'i am listening someone'

    # hide property of the subclass ChatbotInspector
    @property
    def __is_hide(self):
        if self.role == 'spy':
            return True
        else:
            return False
        
