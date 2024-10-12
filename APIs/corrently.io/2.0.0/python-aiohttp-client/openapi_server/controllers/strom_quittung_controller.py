from typing import List, Dict
from aiohttp import web

from openapi_server.models.quittung_comit_request import QuittungComitRequest
from openapi_server.models.quittung_create_request import QuittungCreateRequest
from openapi_server.models.quittung_tse200_response import QuittungTSE200Response
from openapi_server import util


async def quittung_comit(request: web.Request, body=None) -> web.Response:
    """Finishs a collection of data and finalizes receipt. Use this method after collecting all data via quittung/prepare

    Uses collected fields or provided fields to create a final receipt (Strom-Quittung). 

    :param body: 
    :type body: dict | bytes

    """
    body = QuittungComitRequest.from_dict(body)
    return web.Response(status=200)


async def quittung_create(request: web.Request, body) -> web.Response:
    """Create a receipt for an energy delivery (only valid in Germany).

    Creates a full featured receipt (Quittung) for an energy delivery as it appears on a charging session or similar events. Allows to embed receipt generation directly into external services. 

    :param body: 
    :type body: dict | bytes

    """
    body = QuittungCreateRequest.from_dict(body)
    return web.Response(status=200)


async def quittung_prepare(request: web.Request, body=None) -> web.Response:
    """Allows to collect data with several requests (or a single) for a receipt.

    During the first call an account parameter will be returned within the result object. Any other parameter will be set inside the preperation. If account is put into body/request in following requests, the existing collection will be extended/updated with the provided body parameters/values. 

    :param body: 
    :type body: dict | bytes

    """
    body = QuittungComitRequest.from_dict(body)
    return web.Response(status=200)


async def quittung_ts_esignature(request: web.Request, account=None) -> web.Response:
    """Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).

    Allows to retrieve digital signature for a given receipt. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)


async def quittung_tse(request: web.Request, account=None) -> web.Response:
    """Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).

    Allows to retrieve all relevant data assiciated to a TSE service call. E.q. Input parameters, public key and signature. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)


async def quittung_tse_data(request: web.Request, account=None) -> web.Response:
    """Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).

    Allows to retrieve input string for a signing process. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)


async def quittung_zugferd(request: web.Request, account=None) -> web.Response:
    """Retrieve Zugferd XML for a given receipt (Strom-Quittung).

    Allows to retrieve XML of the zugferd invoice. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)
