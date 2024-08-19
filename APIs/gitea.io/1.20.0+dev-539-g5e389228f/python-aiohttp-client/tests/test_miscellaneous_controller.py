# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.markdown_option import MarkdownOption
from openapi_server.models.markup_option import MarkupOption
from openapi_server.models.node_info import NodeInfo
from openapi_server.models.server_version import ServerVersion


pytestmark = pytest.mark.asyncio

async def test_get_node_info(client):
    """Test case for get_node_info

    Returns the nodeinfo of the Gitea application
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/nodeinfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_signing_key(client):
    """Test case for get_signing_key

    Get default signing-key.gpg
    """
    headers = { 
        'Accept': 'text/plain',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/signing-key.gpg',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version(client):
    """Test case for get_version

    Returns the version of the Gitea application
    """
    headers = { 
        'Accept': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_render_markdown(client):
    """Test case for render_markdown

    Render a markdown document as HTML
    """
    body = {"Context":"Context","Mode":"Mode","Wiki":True,"Text":"Text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/markdown',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_render_markdown_raw(client):
    """Test case for render_markdown_raw

    Render raw markdown as HTML
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/markdown/raw',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_render_markup(client):
    """Test case for render_markup

    Render a markup document as HTML
    """
    body = {"Context":"Context","FilePath":"FilePath","Mode":"Mode","Wiki":True,"Text":"Text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TOTPHeader': 'special-key',
        'AuthorizationHeaderToken': 'special-key',
        'SudoHeader': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
        'AccessToken': 'special-key',
        'SudoParam': 'special-key',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/markup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

