# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.codat_error_message import CodatErrorMessage
from openapi_server.models.post_sync import PostSync
from openapi_server.models.sync_initiated import SyncInitiated


pytestmark = pytest.mark.asyncio

async def test_intiate_sync(client):
    """Test case for intiate_sync

    Initiate sync
    """
    body = {"datasetIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/companies/{company_id}/sync/expenses/syncs'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002', company_id2='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

