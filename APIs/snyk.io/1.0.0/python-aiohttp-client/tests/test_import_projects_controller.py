# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_import_job_details200_response import GetImportJobDetails200Response
from openapi_server.models.import_targets_request import ImportTargetsRequest


pytestmark = pytest.mark.asyncio

async def test_get_import_job_details(client):
    """Test case for get_import_job_details

    Get import job details
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/integrations/{integration_id}/import/{job_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='9a3e5d90-b782-468a-a042-9a2073736f0b', job_id='1a325d9d-b782-468a-a242-9a2073734f0b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_targets(client):
    """Test case for import_targets

    Import targets
    """
    body = openapi_server.ImportTargetsRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/integrations/{integration_id}/import'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='9a3e5d90-b782-468a-a042-9a2073736f0b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

