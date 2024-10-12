# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2_metapub_program_information_batch_post_request import ApiV2MetapubProgramInformationBatchPostRequest
from openapi_server.models.program_information_batch import ProgramInformationBatch


pytestmark = pytest.mark.asyncio

async def test_api_v2_metapub_program_information_batch_batch_id_get(client):
    """Test case for api_v2_metapub_program_information_batch_batch_id_get

    Get an EPG batch operation.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/metapub/program-information/batch/{batch_id}'.format(batch_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_metapub_program_information_batch_post(client):
    """Test case for api_v2_metapub_program_information_batch_post

    Create a batch operation on EPG information.
    """
    body = openapi_server.ApiV2MetapubProgramInformationBatchPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/metapub/program-information/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

