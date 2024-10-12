# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_check_availability_of_funds(client):
    """Test case for check_availability_of_funds

    Confirmation of funds request
    """
    body = openapi_server.ConfirmationOfFunds()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_request_id': '99391c7e-ad88-49ec-a2ad-99ddcb1f7721',
        'authorization': 'authorization_example',
        'digest': 'SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=',
        'signature': 'keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ',
        'tpp_signature_certificate': 'tpp_signature_certificate_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/funds-confirmations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

