from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.file_file_id_lines_get200_response import FileFileIdLinesGet200Response
from openapi_server.models.file_file_id_occurrences_get200_response import FileFileIdOccurrencesGet200Response
from openapi_server.models.file_post200_response import FilePost200Response
from openapi_server import util


async def file_file_id_get(request: web.Request, file_id) -> web.Response:
    """Retorna as informações básicas de um arquivo previamente processado

    

    :param file_id: ID Temporário gerado no endpoint file
    :type file_id: str

    """
    return web.Response(status=200)


async def file_file_id_lines_get(request: web.Request, file_id) -> web.Response:
    """Retorna todas as linhas e seus respectivos campos (de forma não processada, apenas indicando os campos reconhecidos)

    

    :param file_id: ID Temporário gerado no endpoint file
    :type file_id: str

    """
    return web.Response(status=200)


async def file_file_id_occurrences_get(request: web.Request, file_id) -> web.Response:
    """Retorna as informações de baixa de boletos e outros tipos de ocorrências

    

    :param file_id: ID Temporário gerado no endpoint file
    :type file_id: str

    """
    return web.Response(status=200)


async def file_post(request: web.Request, file) -> web.Response:
    """Faz o upload de um arquivo

    Processa um arquivo CNAB para obter informações sobre o mesmo. Retorna um ID temporário para o mesmo. 

    :param file: Arquivo CNAB
    :type file: str

    """
    return web.Response(status=200)
