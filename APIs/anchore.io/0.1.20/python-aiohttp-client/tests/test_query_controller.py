# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.paginated_image_list import PaginatedImageList
from openapi_server.models.paginated_vulnerability_list import PaginatedVulnerabilityList
from openapi_server.models.paginated_vulnerable_image_list import PaginatedVulnerableImageList


pytestmark = pytest.mark.asyncio

async def test_query_images_by_package(client):
    """Test case for query_images_by_package

    List of images containing given package
    """
    params = [('name', 'name_example'),
                    ('package_type', 'package_type_example'),
                    ('version', 'version_example'),
                    ('page', 'page_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/query/images/by_package',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_images_by_vulnerability(client):
    """Test case for query_images_by_vulnerability

    List images vulnerable to the specific vulnerability ID.
    """
    params = [('vulnerability_id', 'vulnerability_id_example'),
                    ('namespace', 'namespace_example'),
                    ('affected_package', 'affected_package_example'),
                    ('severity', 'severity_example'),
                    ('vendor_only', True),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/query/images/by_vulnerability',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vulnerabilities(client):
    """Test case for query_vulnerabilities

    Listing information about given vulnerability
    """
    params = [('id', ['id_example']),
                    ('affected_package', 'affected_package_example'),
                    ('affected_package_version', 'affected_package_version_example'),
                    ('page', '1'),
                    ('limit', 56),
                    ('namespace', ['namespace_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/query/vulnerabilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

