# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_model import ClientModel
from openapi_server.models.clients_model import ClientsModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_clients_post_by_model(client):
    """Test case for clients_post_by_model

    
    """
    model = {"factFinderId":0,"planAction":"New","externalDestinationName":"externalDestinationName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Clients',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

