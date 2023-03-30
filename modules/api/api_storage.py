from typing import Optional, List

from modules.api.async_client import HTTPClient
from modules.api.errors import StatusCodeErrorException
from modules.models.api_links import MethodEnum
from modules.models.schema import Person, SearchSchema


class HTTPRequestsMethods:
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ApiStorage:
    def __init__(self, api_host: str):
        self.api_host = api_host
        self.__http_client = HTTPClient()

    async def __make_request(self, url: str, method: str, **kwargs) -> dict:
        if method == 'POST':
            resp = await self.__http_client.post(url, **kwargs)
        elif method == 'GET':
            resp = await self.__http_client.get(url, **kwargs)
        elif method == 'PUT':
            resp = await self.__http_client.put(url, **kwargs)

        return resp

    # async def create_client(self, client_schema: CreateClientSchema) -> ClientSchema:
    #     url = self.api_host + MethodEnum.USER
    #     try:
    #         response_json = await self.__make_request(
    #             url,
    #             HTTPRequestsMethods.POST,
    #             json=client_schema.dict()
    #         )
    #     except StatusCodeErrorException:
    #         Exception("Bad request")
    #     except Exception as e:
    #         print(e)
    #     else:
    #         return ClientSchema.parse_obj(response_json)

    # async def update_client(self, user_schema: CreateClientSchema | UpdateClientSchema) -> ClientSchema:
    #     url = self.api_host + MethodEnum.USER + str(user_schema.user_id) + '/'
    #     try:
    #         response_json = await self.__make_request(
    #             url,
    #             HTTPRequestsMethods.PUT,
    #             json=user_schema.dict()
    #         )
    #     except StatusCodeErrorException:
    #         Exception("Bad request")
    #     except Exception as e:
    #         print(e)
    #     else:
    #         return ClientSchema.parse_obj(response_json)

    async def get_person(self, search_person: SearchSchema) -> list[Person] | None:
        get_params = f'?first_name={search_person.first_name}' \
                     f'&last_name={search_person.last_name}' \
                     f'&middle_name={"" if search_person.middle_name is None else search_person.middle_name}' \
                     f'&birthday={"" if search_person.birthday is None else search_person.birthday}' \
                     f'&post_status=PUBLISHED'
        url = self.api_host + MethodEnum.PERSON + get_params
        try:
            response_json = await self.__make_request(
                url,
                HTTPRequestsMethods.GET
            )
        except StatusCodeErrorException:
            Exception("Bad request")
        except Exception as e:
            print(e)
        else:
            # print()
            # return response_json
            if response_json.get('results'):
                return [Person(**item) for item in response_json.get('results')]
            else:
                return None
