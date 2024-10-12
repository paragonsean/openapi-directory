from typing import List, Dict
from aiohttp import web

from openapi_server.models.academic_certificate_schema import AcademicCertificateSchema
from openapi_server.models.driving_license_schema import DrivingLicenseSchema
from openapi_server.models.drvlc400_response import Drvlc400Response
from openapi_server.models.drvlc401_response import Drvlc401Response
from openapi_server.models.drvlc404_response import Drvlc404Response
from openapi_server.models.drvlc500_response import Drvlc500Response
from openapi_server.models.drvlc502_response import Drvlc502Response
from openapi_server.models.drvlc503_response import Drvlc503Response
from openapi_server.models.drvlc504_response import Drvlc504Response
from openapi_server.models.drvlc_request import DrvlcRequest
from openapi_server.models.fitcer_request import FitcerRequest
from openapi_server.models.rvcer_request import RvcerRequest
from openapi_server.models.vehicle_registration_schema import VehicleRegistrationSchema
from openapi_server.models.vhinsc_request import VhinscRequest
from openapi_server.models.vhtax_request import VhtaxRequest
from openapi_server import util


async def drvlc(request: web.Request, body=None) -> web.Response:
    """Driving License

    API to verify Driving License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DrvlcRequest.from_dict(body)
    return web.Response(status=200)


async def fitcer(request: web.Request, body=None) -> web.Response:
    """Fitness Certificate

    API to verify Fitness Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = FitcerRequest.from_dict(body)
    return web.Response(status=200)


async def rvcer(request: web.Request, body=None) -> web.Response:
    """Registration of Vehicles

    API to verify Registration of Vehicles.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RvcerRequest.from_dict(body)
    return web.Response(status=200)


async def vhinsc(request: web.Request, body=None) -> web.Response:
    """Vehicle Insurance Certificate

    API to verify Vehicle Insurance Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = VhinscRequest.from_dict(body)
    return web.Response(status=200)


async def vhtax(request: web.Request, body=None) -> web.Response:
    """Vehicle Tax Receipt

    API to verify Vehicle Tax Receipt.

    :param body: Request format
    :type body: dict | bytes

    """
    body = VhtaxRequest.from_dict(body)
    return web.Response(status=200)
