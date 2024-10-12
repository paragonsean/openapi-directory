# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.bundle_entity import BundleEntity


pytestmark = pytest.mark.asyncio

async def test_delete_bundles_id(client):
    """Test case for delete_bundles_id

    Delete Bundle
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/bundles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bundles(client):
    """Test case for get_bundles

    List Bundles
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/bundles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bundles_id(client):
    """Test case for get_bundles_id

    Show Bundle
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/bundles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_bundles_id(client):
    """Test case for patch_bundles_id

    Update Bundle
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('clickwrap_id', 56)
    data.add_field('code', 'code_example')
    data.add_field('description', 'description_example')
    data.add_field('dont_separate_submissions_by_folder', True)
    data.add_field('expires_at', '2013-10-20T19:20:30+01:00')
    data.add_field('form_field_set_id', 56)
    data.add_field('inbox_id', 56)
    data.add_field('max_uses', 56)
    data.add_field('note', 'note_example')
    data.add_field('password', 'password_example')
    data.add_field('path_template', 'path_template_example')
    data.add_field('paths', ['paths_example'])
    data.add_field('permissions', 'permissions_example')
    data.add_field('preview_only', True)
    data.add_field('require_registration', True)
    data.add_field('require_share_recipient', True)
    data.add_field('send_email_receipt_to_uploader', True)
    data.add_field('skip_company', True)
    data.add_field('skip_email', True)
    data.add_field('skip_name', True)
    data.add_field('watermark_attachment_delete', True)
    data.add_field('watermark_attachment_file', '/path/to/file')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/bundles/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_bundles(client):
    """Test case for post_bundles

    Create Bundle
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('clickwrap_id', 56)
    data.add_field('code', 'code_example')
    data.add_field('description', 'description_example')
    data.add_field('dont_separate_submissions_by_folder', True)
    data.add_field('expires_at', '2013-10-20T19:20:30+01:00')
    data.add_field('form_field_set_id', 56)
    data.add_field('inbox_id', 56)
    data.add_field('max_uses', 56)
    data.add_field('note', 'note_example')
    data.add_field('password', 'password_example')
    data.add_field('path_template', 'path_template_example')
    data.add_field('paths', ['paths_example'])
    data.add_field('permissions', 'permissions_example')
    data.add_field('preview_only', True)
    data.add_field('require_registration', True)
    data.add_field('require_share_recipient', True)
    data.add_field('send_email_receipt_to_uploader', True)
    data.add_field('skip_company', True)
    data.add_field('skip_email', True)
    data.add_field('skip_name', True)
    data.add_field('user_id', 56)
    data.add_field('watermark_attachment_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/bundles',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_bundles_id_share(client):
    """Test case for post_bundles_id_share

    Send email(s) with a link to bundle
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('note', 'note_example')
    data.add_field('recipients', None)
    data.add_field('to', ['to_example'])
    response = await client.request(
        method='POST',
        path='/api/rest/v1/bundles/{id}/share'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

