# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hdfs_template_create import HdfsTemplateCreate
from openapi_server.models.hdfs_template_detail import HdfsTemplateDetail
from openapi_server.models.hdfs_template_detail_list_response import HdfsTemplateDetailListResponse
from openapi_server.models.hdfs_template_patch import HdfsTemplatePatch


pytestmark = pytest.mark.asyncio

async def test_create_hdfs_template(client):
    """Test case for create_hdfs_template

    Create a HDFS directory template
    """
    body = {"excludes":["excludes","excludes"],"name":"name","includes":["includes","includes"],"exceptions":["exceptions","exceptions"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hdfs_template',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hdfs_template(client):
    """Test case for delete_hdfs_template

    Delete a HDFS directory template
    """
    params = [('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/hdfs_template/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hdfs_template(client):
    """Test case for get_hdfs_template

    Get information for a HDFS directory template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs_template/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_hdfs_template(client):
    """Test case for query_hdfs_template

    Get summary information for all HDFS directory templates
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('name', 'name_example'),
                    ('sort_by', name),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs_template',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_hdfs_template(client):
    """Test case for update_hdfs_template

    Modify a HDFS directory template
    """
    body = {"excludes":["excludes","excludes"],"name":"name","includes":["includes","includes"],"id":"id","exceptions":["exceptions","exceptions"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/hdfs_template/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

