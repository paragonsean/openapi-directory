from typing import List, Dict
from aiohttp import web

from openapi_server.models.importer_exporter_code_verification_api200_response import ImporterExporterCodeVerificationAPI200Response
from openapi_server.models.importer_exporter_code_verification_api400_response import ImporterExporterCodeVerificationAPI400Response
from openapi_server.models.importer_exporter_code_verification_api401_response import ImporterExporterCodeVerificationAPI401Response
from openapi_server.models.importer_exporter_code_verification_api404_response import ImporterExporterCodeVerificationAPI404Response
from openapi_server.models.importer_exporter_code_verification_api500_response import ImporterExporterCodeVerificationAPI500Response
from openapi_server.models.importer_exporter_code_verification_api502_response import ImporterExporterCodeVerificationAPI502Response
from openapi_server.models.importer_exporter_code_verification_api503_response import ImporterExporterCodeVerificationAPI503Response
from openapi_server.models.importer_exporter_code_verification_api504_response import ImporterExporterCodeVerificationAPI504Response
from openapi_server import util


async def importer_exporter_code_verification_api(request: web.Request, iec) -> web.Response:
    """Importer-Exporter Code (IEC) Verification API.

    Description of Importer-Exporter Code (IEC) Verification API.

    :param iec: Importer-Exporter code
    :type iec: str

    """
    return web.Response(status=200)
