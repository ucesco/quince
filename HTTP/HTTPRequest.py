class HTTPRequest:
    def __init__(self, raw):
        self.__type = None
        self.__path = None

        if len(raw.strip()) != 0:
            self.parse(raw)

    @property
    def type(self):
        return self.__type

    @property
    def path(self):
        return self.__path

    def parse(self, raw):
        # TODO: Need to validate the string

        tokens = raw.split(' ')

        self.__type = tokens[0]
        self.__path = tokens[1]
