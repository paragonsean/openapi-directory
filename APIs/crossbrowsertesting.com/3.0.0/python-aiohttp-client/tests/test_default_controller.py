# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.full_comparison_test import FullComparisonTest
from openapi_server.models.single_comparison_test import SingleComparisonTest


pytestmark = pytest.mark.asyncio

async def test_screenshots_target_screenshot_test_id_target_version_id_comparison_base_result_id_get(client):
    """Test case for screenshots_target_screenshot_test_id_target_version_id_comparison_base_result_id_get

    Compare Full Screenshot Test
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('tolerance', 30)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/screenshots/{target_screenshot_test_id}/{target_version_id}/comparison/{base_result_id}'.format(target_screenshot_test_id=56, target_version_id=56, base_result_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_screenshots_target_screenshot_test_id_target_version_id_comparison_parallel_base_version_id_get(client):
    """Test case for screenshots_target_screenshot_test_id_target_version_id_comparison_parallel_base_version_id_get

    Compare Screenshot Test Versions
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('tolerance', 30)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/screenshots/{target_screenshot_test_id}/{target_version_id}/comparison/parallel/{base_version_id}'.format(target_screenshot_test_id=56, target_version_id=56, base_version_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_screenshots_target_screenshot_test_id_target_version_id_target_result_id_comparison_base_result_id_get(client):
    """Test case for screenshots_target_screenshot_test_id_target_version_id_target_result_id_comparison_base_result_id_get

    Compare Single Screenshot
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('tolerance', 30)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/screenshots/{target_screenshot_test_id}/{target_version_id}/{target_result_id}/comparison/{base_result_id}'.format(target_screenshot_test_id=56, target_version_id=56, target_result_id=56, base_result_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

