# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.boundaries import Boundaries
from openapi_server.models.boundaries_query import BoundariesQuery
from openapi_server.models.boundary import Boundary
from openapi_server.models.boundary_upload import BoundaryUpload
from openapi_server.models.error import Error
from openapi_server.models.uploaded_boundary_id import UploadedBoundaryId


pytestmark = pytest.mark.asyncio

async def test_fetch_boundaries(client):
    """Test case for fetch_boundaries

    Retrieve Boundaries in batch
    """
    body = {"ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/boundaries/query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_boundary_by_id(client):
    """Test case for fetch_boundary_by_id

    Retrieve a Boundary by ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/boundaries/{boundary_id}'.format(boundary_id='boundary_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_boundary(client):
    """Test case for upload_boundary

    Upload a boundary
    """
    body = {"geometry":{"coordinates":[0,0],"type":"Point"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/boundaries',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

