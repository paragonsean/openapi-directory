from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_availability_of_funds200_response import CheckAvailabilityOfFunds200Response
from openapi_server.models.confirmation_of_funds import ConfirmationOfFunds
from openapi_server.models.error400_ais import Error400AIS
from openapi_server.models.error400_ngais import Error400NGAIS
from openapi_server.models.error401_ngpiis import Error401NGPIIS
from openapi_server.models.error401_piis import Error401PIIS
from openapi_server.models.error403_ngpiis import Error403NGPIIS
from openapi_server.models.error403_piis import Error403PIIS
from openapi_server.models.error404_ngpiis import Error404NGPIIS
from openapi_server.models.error404_piis import Error404PIIS
from openapi_server.models.error405_ngpiis import Error405NGPIIS
from openapi_server.models.error405_piis import Error405PIIS
from openapi_server.models.error409_ngpiis import Error409NGPIIS
from openapi_server.models.error409_piis import Error409PIIS
from openapi_server import util


async def check_availability_of_funds(request: web.Request, x_request_id, body, authorization=None, digest=None, signature=None, tpp_signature_certificate=None) -> web.Response:
    """Confirmation of funds request

    Creates a confirmation of funds request at the ASPSP. Checks whether a specific amount is available at point of time of the request on an account linked to a given tuple card issuer(TPP)/card number, or addressed by IBAN and TPP respectively. If the related extended services are used a conditional Consent-ID is contained in the header. This field is contained but commented out in this specification.

    :param x_request_id: ID of the request, unique to the call, as determined by the initiating party.
    :type x_request_id: str
    :param body: Request body for a confirmation of funds request. 
    :type body: dict | bytes
    :param authorization: This field  might be used in case where a consent was agreed between ASPSP and PSU through an OAuth2 based protocol, facilitated by the TPP. 
    :type authorization: str
    :param digest: Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request.
    :type digest: str
    :param signature: A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    :type signature: str
    :param tpp_signature_certificate: The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    :type tpp_signature_certificate: str

    """
    body = ConfirmationOfFunds.from_dict(body)
    return web.Response(status=200)
