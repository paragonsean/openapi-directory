# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_list_available_content_blocks(client):
    """Test case for list_available_content_blocks

    List Available Content Blocks
    """
    params = [('modified_after', '2020-01-01T01:01:01.000000'),
                    ('modified_before', '2020-02-01T01:01:01.000000'),
                    ('limit', '100'),
                    ('offset', '1')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/content_blocks/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_available_email_templates(client):
    """Test case for list_available_email_templates

    List Available Email Templates
    """
    params = [('modified_after', '2020-01-01T01:01:01.000000'),
                    ('modified_before', '2020-02-01T01:01:01.000000'),
                    ('limit', '1'),
                    ('offset', '0')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/templates/email/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_see_content_block_information(client):
    """Test case for see_content_block_information

    See Content Block Information
    """
    params = [('content_block_id', '{{content_block_id}}'),
                    ('include_inclusion_data', 'false')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/content_blocks/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_see_email_template_information(client):
    """Test case for see_email_template_information

    See Email Template Information
    """
    params = [('email_template_id', '{{email_template_id}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/templates/email/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

