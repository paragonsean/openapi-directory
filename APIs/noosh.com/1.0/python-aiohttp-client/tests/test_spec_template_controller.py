# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.spec_template_expand_vo import SpecTemplateExpandVO
from openapi_server.models.spec_template_list_vo import SpecTemplateListVO


pytestmark = pytest.mark.asyncio

async def test_get_spec_template(client):
    """Test case for get_spec_template

    Get a specific Spec Template
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/specTemplates/{spec_template_id}'.format(workgroup_id='workgroup_id_example', spec_template_id='spec_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spec_template_list(client):
    """Test case for get_spec_template_list

    List Spec Templates of Workgroup Level 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/specTemplates'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

