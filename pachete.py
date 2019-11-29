class CONNECT:
    def __init__(self,parola):
        self.parola=parola

class CONNACK:
    def __init__(self,confirm_flag):
        self.confirm_flag=confirm_flag

class PUBLISH:
    def __init__(self,topic,payload):
        self.topic=topic
        self.payload=payload
