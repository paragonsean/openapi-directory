# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_response import AccountResponse
from openapi_server.models.link_application403_response import LinkApplication403Response
from openapi_server.models.link_application409_response import LinkApplication409Response
from openapi_server.models.link_application_request import LinkApplicationRequest
from openapi_server.models.model401_response import Model401Response
from openapi_server.models.unli_without_applicationnk_application403_response import UnliWithoutApplicationnkApplication403Response
from openapi_server.models.unli_without_applicationnk_application409_response import UnliWithoutApplicationnkApplication409Response


pytestmark = pytest.mark.asyncio

async def test_link_application(client):
    """Test case for link_application

    Link application to an account
    """
    body = openapi_server.LinkApplicationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/beta/chatapp-accounts/{provider}/{external_id}/applications'.format(provider='provider_example', external_id='external_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unli_without_applicationnk_application(client):
    """Test case for unli_without_applicationnk_application

    Unlink application from an account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/beta/chatapp-accounts/{provider}/{external_id}/applications/{application_id}'.format(provider='provider_example', external_id='external_id_example', application_id='application_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

