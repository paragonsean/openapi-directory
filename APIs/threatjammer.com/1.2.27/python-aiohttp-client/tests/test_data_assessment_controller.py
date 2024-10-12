# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.ip_assessment_collection_output import IPAssessmentCollectionOutput
from openapi_server.models.ip_assessment_output import IPAssessmentOutput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_assess_ip_set_csv_v1_assess_ip_csv_post(client):
    """Test case for assess_ip_set_csv_v1_assess_ip_csv_post

    Get the risk score of all IP address uploaded and other data signals.
    """
    params = [('strict_parse', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('csv_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/assess/ip/csv',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assess_ip_set_v1_assess_ip_post(client):
    """Test case for assess_ip_set_v1_assess_ip_post

    Get the risk score of all IP address passed in the body and other data signals.
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/assess/ip',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assess_ip_v1_assess_ip_ip_address_get(client):
    """Test case for assess_ip_v1_assess_ip_ip_address_get

    Get a risk score of the IP address and different data signals.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/assess/ip/{ip_address}'.format(ip_address='ip_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

