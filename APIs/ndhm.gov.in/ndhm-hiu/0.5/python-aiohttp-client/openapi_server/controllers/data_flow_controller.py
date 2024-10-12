from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_notification import DataNotification
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
from openapi_server import util


async def v05_health_information_hiu_on_request_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Health information data request

    Callback API for acknowledgement of Health information request made by HIU. Gateway calls this API when request has validated for the specified  consent id. Either the **hiRequest** or **error** would be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUHealthInformationRequestResponse.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_transfer_post(request: web.Request, authorization, body) -> web.Response:
    """health information transfer API

    **NOTE**: This API is actually the callback URL that is passed as **dataPushUrl** in the data request API - /v0.5/health-information/hip/request. This API is directly called by HIP Data Bridge and is not mediated via CM, and hence not routed through the Gateway.    1. This API should be implemented at HIU side. It maybe implemented by the Data Bridge representing the HIU.    2. Entry elements maybe ***content*** or ***link***, although for version 1, entry ***content*** is preferred.    3. Entry ***content*** (or even link reference content) must be encrypted by means of Elliptic-curve Diffie–Hellman Key Exchange, utilizing the HIU keymaterials that are passed through the data request API - /v0.5/health-information/hip/request.    4. Media contains the mimetype of content, and for v1, it is \&quot;application/fhir+json\&quot;   5. checksum is Md5 checksum of the data conent, before encryption   6. Please refer to the NDHM Sandbox documentation for the format of FHIR bundle that is passed through content  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = DataNotification.from_dict(body)
    return web.Response(status=200)
