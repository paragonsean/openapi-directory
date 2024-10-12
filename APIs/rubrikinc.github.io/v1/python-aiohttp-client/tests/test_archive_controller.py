# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.reader_refresh_data_sources_request import ReaderRefreshDataSourcesRequest
from openapi_server.models.string_response import StringResponse


pytestmark = pytest.mark.asyncio

async def test_disable_archival_location(client):
    """Test case for disable_archival_location

    Disable location for archival and modification operations
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/archive/location/{id}/owner/disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_archival_location(client):
    """Test case for enable_archival_location

    Enable archival location for archival and modification operations
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/archive/location/{id}/owner/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_aws_account_id(client):
    """Test case for get_aws_account_id

    Get the AWS account ID of an AWS S3 archival location
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/archive/aws/s3/{id}/account_id'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_archival_location_data_sources(client):
    """Test case for refresh_archival_location_data_sources

    Refresh archive information for a list of data sources
    """
    body = {"localDataSourceIds":["localDataSourceIds","localDataSourceIds"],"archivalDataSourceIds":["archivalDataSourceIds","archivalDataSourceIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/archive/location/{location_id}/reader/refresh/data_sources'.format(location_id='location_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

