# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.paginated_change_descriptions import PaginatedChangeDescriptions


pytestmark = pytest.mark.asyncio

async def test_changelog_adhoc_get(client):
    """Test case for changelog_adhoc_get

    Allows an arbitrary filter to be specified and applied to the org\\'s change log.
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/changelog/adhoc',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changelog_cluster_graph_cluster_key_get(client):
    """Test case for changelog_cluster_graph_cluster_key_get

    get changes related to the indicated cluster
    """
    params = [('start', 3.4),
                    ('end', 3.4),
                    ('max_results', 3.4),
                    ('ref_id', 'ref_id_example'),
                    ('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/changelog/cluster-graph/{cluster_key}'.format(cluster_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changelog_domain_graph_domain_key_get(client):
    """Test case for changelog_domain_graph_domain_key_get

    get changes related to the indicated domain
    """
    params = [('start', 3.4),
                    ('end', 3.4),
                    ('max_results', 3.4),
                    ('ref_id', 'ref_id_example'),
                    ('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/changelog/domain-graph/{domain_key}'.format(domain_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changelog_route_graph_route_key_get(client):
    """Test case for changelog_route_graph_route_key_get

    get changes related to the indicated route
    """
    params = [('start', 3.4),
                    ('end', 3.4),
                    ('max_results', 3.4),
                    ('ref_id', 'ref_id_example'),
                    ('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/changelog/route-graph/{route_key}'.format(route_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changelog_shared_rules_graph_shared_rules_key_get(client):
    """Test case for changelog_shared_rules_graph_shared_rules_key_get

    get changes related to the indicated SharedRules
    """
    params = [('start', 3.4),
                    ('end', 3.4),
                    ('max_results', 3.4),
                    ('ref_id', 'ref_id_example'),
                    ('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/changelog/shared-rules-graph/{shared_rules_key}'.format(shared_rules_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changelog_zone_zone_key_get(client):
    """Test case for changelog_zone_zone_key_get

    get changes in a specified zone
    """
    params = [('start', 3.4),
                    ('end', 3.4),
                    ('max_results', 3.4),
                    ('ref_id', 'ref_id_example'),
                    ('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/changelog/zone/{zone_key}'.format(zone_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

