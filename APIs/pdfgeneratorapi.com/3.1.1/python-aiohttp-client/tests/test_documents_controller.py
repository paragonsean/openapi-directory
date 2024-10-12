# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_data_inner import BatchDataInner
from openapi_server.models.data import Data
from openapi_server.models.get_templates401_response import GetTemplates401Response
from openapi_server.models.get_templates403_response import GetTemplates403Response
from openapi_server.models.get_templates404_response import GetTemplates404Response
from openapi_server.models.get_templates422_response import GetTemplates422Response
from openapi_server.models.get_templates500_response import GetTemplates500Response
from openapi_server.models.merge_templates200_response import MergeTemplates200Response


pytestmark = pytest.mark.asyncio

async def test_merge_template(client):
    """Test case for merge_template

    Generate document
    """
    body = {"name":"Sample Data","id":12312}
    params = [('templateId', 19375),
                    ('name', 'My document'),
                    ('format', pdf),
                    ('output', base64)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/templates/templateId/output',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_merge_templates(client):
    """Test case for merge_templates

    Generate document (multiple templates)
    """
    body = [openapi_server.BatchDataInner()]
    params = [('name', 'My document'),
                    ('format', pdf),
                    ('output', base64)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/templates/output',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

