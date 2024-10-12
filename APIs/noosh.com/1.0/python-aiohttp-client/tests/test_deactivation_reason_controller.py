# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deactivation_reason_list_vo import DeactivationReasonListVO
from openapi_server.models.http_status_vo import HTTPStatusVO


pytestmark = pytest.mark.asyncio

async def test_get_deactivation_reason_list(client):
    """Test case for get_deactivation_reason_list

    List all deactivation reasons
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/deactivationReasons'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

