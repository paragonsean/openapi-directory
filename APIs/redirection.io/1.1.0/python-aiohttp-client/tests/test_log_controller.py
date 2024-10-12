# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.log_read import LogRead


pytestmark = pytest.mark.asyncio

async def test_get_log_collection(client):
    """Test case for get_log_collection

    Retrieves the collection of Log resources.
    """
    params = [('page', 56),
                    ('projectId', 'project_id_example'),
                    ('createdAt', 'created_at_example'),
                    ('source', 'source_example'),
                    ('target', 'target_example'),
                    ('statusCode', 'status_code_example'),
                    ('referrer', 'referrer_example'),
                    ('userAgent', 'user_agent_example'),
                    ('userAgentType', 'user_agent_type_example'),
                    ('simplifiedUserAgent', 'simplified_user_agent_example'),
                    ('ruleId', 'rule_id_example'),
                    ('instanceName', 'instance_name_example'),
                    ('excludeUrls', 'exclude_urls_example'),
                    ('excludeEmptyReferrer', 'exclude_empty_referrer_example'),
                    ('createdAt_gt', 'created_at_gt_example'),
                    ('createdAt_gte', 'created_at_gte_example'),
                    ('createdAt_lt', 'created_at_lt_example'),
                    ('createdAt_lte', 'created_at_lte_example'),
                    ('statusCode_gt', 'status_code_gt_example'),
                    ('statusCode_gte', 'status_code_gte_example'),
                    ('statusCode_lt', 'status_code_lt_example'),
                    ('statusCode_lte', 'status_code_lte_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/logs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_log_item(client):
    """Test case for get_log_item

    Retrieves a Log resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/logs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

