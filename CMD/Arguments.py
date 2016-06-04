import re


class Arguments:
    def __init__(self, args=None):
        self.__args = {}
        self.__switches = []

        if args is not None:
            self.__parse(args)

    def __parse(self, args):
        index = 1

        while index < len(args):
            token = args[index]

            if self.__is_arg(token):
                key, val = self.__get_arg(token, args, index)
                self.__args[key] = val
                index += 1
            elif self.__is_switch(token):
                val = self.__get_switch(token)
                self.__switches.append(val)
                index += 1

            index += 1

    def __is_arg(self, token):
        return re.match(r'^-\w+$', token)

    def __is_switch(self, token):
        return re.match(r'^--\w+$', token)

    def __get_arg(self, token, args, index):
        key = token.strip().lstrip('-')
        val = None

        # see if arg got value
        if index + 1 < len(args):
            v_token = args[index + 1].strip()

            if not self.__is_arg(v_token) and not self.__is_switch(v_token):
                val = v_token

        return key, val

    def __get_switch(self, token):
        return token.strip().lstrip('--')

    def has_arg(self, v):
        return self.arg(v) is not None

    def arg(self, v):
        if v in self.__args:
            return self.__args[v]
        else:
            return None

    def switch(self, v):
        return v in self.__switches
