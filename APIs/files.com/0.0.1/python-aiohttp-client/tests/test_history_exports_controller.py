# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.history_export_entity import HistoryExportEntity


pytestmark = pytest.mark.asyncio

async def test_get_history_exports_id(client):
    """Test case for get_history_exports_id

    Show History Export
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/history_exports/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_history_exports(client):
    """Test case for post_history_exports

    Create History Export
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('end_at', '2013-10-20T19:20:30+01:00')
    data.add_field('query_action', 'query_action_example')
    data.add_field('query_destination', 'query_destination_example')
    data.add_field('query_failure_type', 'query_failure_type_example')
    data.add_field('query_file_id', 'query_file_id_example')
    data.add_field('query_folder', 'query_folder_example')
    data.add_field('query_interface', 'query_interface_example')
    data.add_field('query_ip', 'query_ip_example')
    data.add_field('query_parent_id', 'query_parent_id_example')
    data.add_field('query_path', 'query_path_example')
    data.add_field('query_src', 'query_src_example')
    data.add_field('query_target_id', 'query_target_id_example')
    data.add_field('query_target_name', 'query_target_name_example')
    data.add_field('query_target_permission', 'query_target_permission_example')
    data.add_field('query_target_permission_set', 'query_target_permission_set_example')
    data.add_field('query_target_platform', 'query_target_platform_example')
    data.add_field('query_target_user_id', 'query_target_user_id_example')
    data.add_field('query_target_username', 'query_target_username_example')
    data.add_field('query_user_id', 'query_user_id_example')
    data.add_field('query_username', 'query_username_example')
    data.add_field('start_at', '2013-10-20T19:20:30+01:00')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/history_exports',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

