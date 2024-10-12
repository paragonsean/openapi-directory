# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.meter_folder_information import MeterFolderInformation
from openapi_server.models.meter_folder_information_to_post import MeterFolderInformationToPost


pytestmark = pytest.mark.asyncio

async def test_meter_folder_information_get(client):
    """Test case for meter_folder_information_get

    Beta: Gets the General Information for a Meter or a Folder
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/MeterFolderInformation/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_meter_folder_information_post(client):
    """Test case for meter_folder_information_post

    Sets the Name of a Meter or a Folder
    """
    body = {"Id":"Id","Name":"Name"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/MeterFolderInformation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

