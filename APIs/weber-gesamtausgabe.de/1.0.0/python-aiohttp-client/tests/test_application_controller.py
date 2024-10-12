# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_new_id_get200_response import ApplicationNewIDGet200Response
from openapi_server.models.application_new_id_get403_response import ApplicationNewIDGet403Response
from openapi_server.models.application_status_get200_response import ApplicationStatusGet200Response
from openapi_server.models.application_status_get500_response import ApplicationStatusGet500Response
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_application_new_idget(client):
    """Test case for application_new_idget

    Create a new WeGA ID
    """
    params = [('docType', ['doc_type_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/application/newID',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_status_get(client):
    """Test case for application_status_get

    Get status information about the running WeGA-WebApp
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/application/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

