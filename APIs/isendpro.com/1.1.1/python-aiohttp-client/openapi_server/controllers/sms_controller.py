from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.sms_reponse import SMSReponse
from openapi_server.models.sms_request import SMSRequest
from openapi_server.models.sms_unique_request import SmsUniqueRequest
from openapi_server import util


async def send_sms(request: web.Request, body) -> web.Response:
    """Envoyer un sms

    Envoi un sms vers un unique destinataire

    :param body: sms request
    :type body: dict | bytes

    """
    body = SmsUniqueRequest.from_dict(body)
    return web.Response(status=200)


async def send_sms_multi(request: web.Request, body) -> web.Response:
    """Envoyer des SMS

    Envoi de SMS vers 1 ou plusieurs destinataires 

    :param body: sms request
    :type body: dict | bytes

    """
    body = SMSRequest.from_dict(body)
    return web.Response(status=200)
