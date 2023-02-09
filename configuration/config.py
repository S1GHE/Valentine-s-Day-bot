import json
from pathlib import Path


class Config:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Config.__instance:
            Config.__instance = super(Config, cls).__new__(cls)
        return Config.__instance

    def __init__(self, index_admin_id: int = 0):
        self.__bot_token: str = Config.__get_bot_token()
        self.__id_compliment: int = 0
        self.__admin_id: int | list = Config.__get_admin_id(index_id=index_admin_id)
        self.__user_love: int = Config.__get_user_love()

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
    def user_love(self, new_user_love: int = None) -> None:
        if new_user_love:
            if not type(new_user_love) is int:
                raise ValueError('Ожидается целочисленный тип данных')

        Config.__set_user_love(new_user_love)

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

    @staticmethod
    def __get_user_love() -> int:
        with open(Path('configuration', 'configuration.json'), 'r', encoding='utf-8') as configuration_file:
            return json.load(configuration_file)['user_love']

    @staticmethod
    def __set_user_love(new_user_love: int) -> None:
        with open(Path('configuration', 'configuration.json'), 'r', encoding='utf-8') as configuration_file:
            configuration_dict = json.load(configuration_file)

        configuration_dict['user_love'] = new_user_love

        with open(Path('configuration', 'configuration.json'), 'w', encoding='utf-8') as configuration_file:
            json.dump(configuration_dict, configuration_file, indent=4, ensure_ascii=False)