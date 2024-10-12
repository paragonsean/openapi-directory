# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.importer_exporter_code_verification_api200_response import ImporterExporterCodeVerificationAPI200Response
from openapi_server.models.importer_exporter_code_verification_api400_response import ImporterExporterCodeVerificationAPI400Response
from openapi_server.models.importer_exporter_code_verification_api401_response import ImporterExporterCodeVerificationAPI401Response
from openapi_server.models.importer_exporter_code_verification_api404_response import ImporterExporterCodeVerificationAPI404Response
from openapi_server.models.importer_exporter_code_verification_api500_response import ImporterExporterCodeVerificationAPI500Response
from openapi_server.models.importer_exporter_code_verification_api502_response import ImporterExporterCodeVerificationAPI502Response
from openapi_server.models.importer_exporter_code_verification_api503_response import ImporterExporterCodeVerificationAPI503Response
from openapi_server.models.importer_exporter_code_verification_api504_response import ImporterExporterCodeVerificationAPI504Response


pytestmark = pytest.mark.asyncio

async def test_importer_exporter_code_verification_api(client):
    """Test case for importer_exporter_code_verification_api

    Importer-Exporter Code (IEC) Verification API.
    """
    headers = { 
        'Accept': 'application/json',
        'clientId': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/dgft/v1/iec/{iec}'.format(iec='iec_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

