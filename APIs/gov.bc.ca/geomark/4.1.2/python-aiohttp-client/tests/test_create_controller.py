# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_geomarks_copy_post(client):
    """Test case for geomarks_copy_post

    Create a new geomark by copying the geometries from one or more existing geomarks from the current server.
    """
    params = [('geomarkUrl', 'https://apps.gov.bc.ca/pub/geomark/geomarks/gm-abcdefghijklmnopqrstuv0bcislands'),
                    ('resultFormat', 'json'),
                    ('allowOverlap', False),
                    ('callback', 'param_callback_example'),
                    ('redirectUrl', 'redirect_url_example'),
                    ('failureRedirectUrl', 'failure_redirect_url_example'),
                    ('bufferMetres', 56),
                    ('bufferJoin', ROUND),
                    ('bufferCap', ROUND),
                    ('bufferMitreLimit', 5),
                    ('bufferSegments', 8)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/pub/geomark/geomarks/copy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_geomarks_new_post(client):
    """Test case for geomarks_new_post

    Create a new geomark
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'allow_overlap': False,
        'body': 'body_example',
        'buffer_cap': ROUND,
        'buffer_join': ROUND,
        'buffer_metres': 56,
        'buffer_mitre_limit': 5,
        'buffer_segments': 8,
        'param_callback': 'param_callback_example',
        'failure_redirect_url': 'failure_redirect_url_example',
        'format': 'format_example',
        'multiple': False,
        'redirect_url': 'redirect_url_example',
        'result_format': 'result_format_example',
        'srid': 4326
        }
    response = await client.request(
        method='POST',
        path='/pub/geomark/geomarks/new',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

