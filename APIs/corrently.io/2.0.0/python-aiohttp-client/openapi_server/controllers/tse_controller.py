from typing import List, Dict
from aiohttp import web

from openapi_server.models.quittung_tse200_response import QuittungTSE200Response
from openapi_server import util


async def quittung_ts_esignature_0(request: web.Request, account=None) -> web.Response:
    """Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).

    Allows to retrieve digital signature for a given receipt. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)


async def quittung_tse_0(request: web.Request, account=None) -> web.Response:
    """Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).

    Allows to retrieve all relevant data assiciated to a TSE service call. E.q. Input parameters, public key and signature. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)


async def quittung_tse_data_0(request: web.Request, account=None) -> web.Response:
    """Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).

    Allows to retrieve input string for a signing process. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)


async def quittung_zugferd_0(request: web.Request, account=None) -> web.Response:
    """Retrieve Zugferd XML for a given receipt (Strom-Quittung).

    Allows to retrieve XML of the zugferd invoice. 

    :param account: Quittung Identifier  (serialnumber generated during receipt generation process)
    :type account: str

    """
    return web.Response(status=200)
