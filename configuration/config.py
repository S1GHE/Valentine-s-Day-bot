import json
from pathlib import Path


class Config:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Config.__instance:
            Config.__instance = super(Config, cls).__new__(cls, **args, **kwargs)
        return Config.__instance

    def __init__(self):
        self.__bot_token: str = Config.__get_bot_token()
        self.__id_compliment: int = 0
        self.__admin_id: int | list = 0
        self.__user_love: int = 0

    @property
    def bot_token(self) -> str:
        return self.__bot_token

    @property
    def id_compliment(self) -> int:
        return self.__id_compliment

    @id_compliment.setter
    def id_compliment(self, new_id_compliment: int) -> None:
        if not type(new_id_compliment) is int:
            raise ValueError('Ожидается целочисленный тип данных')

        if new_id_compliment != self.__id_compliment:
            self.__id_compliment = new_id_compliment
        else:
            raise IOError('Совпадение id_compliment')

    @property
    def admin_id(self) -> int | list:
        return self.__admin_id

    @property
    def user_love(self) -> int:
        return self.__user_love

    @user_love.setter
    def user_love(self, new_user_love: int = None, status_update: bool = False) -> None:
        if new_user_love:
            pass

    @staticmethod
    def __get_bot_token() -> str:
        with open(Path('configuration', 'configuration.json'), 'r', encoding='utf-8') as configuration_file:
            return json.load(configuration_file)['bot_token']

    @staticmethod
    def __get_admin_id(get_type: int | list = int, index_id: int = 0) -> int | list:
        with open(Path('configuration', 'configuration.json'), 'r', encoding='utf-8') as configuration_file:
            if get_type is int:
                return json.load(configuration_file)['admin_list'][index_id]
            elif get_type is list:
                return json.load(configuration_file)['admin_list']
            else:
                raise TypeError('Ожидается тип данных int или list')