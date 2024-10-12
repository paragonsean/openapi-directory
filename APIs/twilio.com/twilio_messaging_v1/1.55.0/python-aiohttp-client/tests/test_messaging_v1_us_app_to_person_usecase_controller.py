# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_service_us_app_to_person_usecase import MessagingV1ServiceUsAppToPersonUsecase


pytestmark = pytest.mark.asyncio

async def test_fetch_us_app_to_person_usecase(client):
    """Test case for fetch_us_app_to_person_usecase

    
    """
    params = [('BrandRegistrationSid', 'brand_registration_sid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{messaging_service_sid}/Compliance/Usa2p/Usecases'.format(messaging_service_sid='messaging_service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

