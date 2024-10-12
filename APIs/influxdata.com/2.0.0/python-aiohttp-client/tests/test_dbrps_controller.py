# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dbrp import DBRP
from openapi_server.models.dbrp_update import DBRPUpdate
from openapi_server.models.dbrps import DBRPs
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_delete_dbrpid(client):
    """Test case for delete_dbrpid

    Delete a database retention policy
    """
    params = [('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/dbrps/{dbrp_id}'.format(dbrp_id='dbrp_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dbrps(client):
    """Test case for get_dbrps

    List all database retention policy mappings
    """
    params = [('orgID', 'org_id_example'),
                    ('id', 'id_example'),
                    ('bucketID', 'bucket_id_example'),
                    ('default', True),
                    ('db', 'db_example'),
                    ('rp', 'rp_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dbrps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dbrps_id(client):
    """Test case for get_dbrps_id

    Retrieve a database retention policy mapping
    """
    params = [('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dbrps/{dbrp_id}'.format(dbrp_id='dbrp_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dbrpid(client):
    """Test case for patch_dbrpid

    Update a database retention policy mapping
    """
    body = {"database":"database","default":True,"retention_policy":"retention_policy","links":{"next":"https://openapi-generator.tech","prev":"https://openapi-generator.tech","self":"https://openapi-generator.tech"}}
    params = [('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/dbrps/{dbrp_id}'.format(dbrp_id='dbrp_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_dbrp(client):
    """Test case for post_dbrp

    Add a database retention policy mapping
    """
    body = {"database":"database","default":True,"retention_policy":"retention_policy","org":"org","bucketID":"bucketID","links":{"next":"https://openapi-generator.tech","prev":"https://openapi-generator.tech","self":"https://openapi-generator.tech"},"id":"id","orgID":"orgID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/dbrps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

