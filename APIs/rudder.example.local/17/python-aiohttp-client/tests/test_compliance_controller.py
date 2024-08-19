# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_directive_compliance_id200_response import GetDirectiveComplianceId200Response
from openapi_server.models.get_directives_compliance200_response import GetDirectivesCompliance200Response
from openapi_server.models.get_global_compliance200_response import GetGlobalCompliance200Response
from openapi_server.models.get_node_compliance200_response import GetNodeCompliance200Response
from openapi_server.models.get_nodes_compliance200_response import GetNodesCompliance200Response
from openapi_server.models.get_rule_compliance200_response import GetRuleCompliance200Response
from openapi_server.models.get_rules_compliance200_response import GetRulesCompliance200Response


pytestmark = pytest.mark.asyncio

async def test_get_directive_compliance_id(client):
    """Test case for get_directive_compliance_id

    Compliance details by directive
    """
    params = [('format', '[\"csv\"]')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/compliance/directives/{directive_id}'.format(directive_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_directives_compliance(client):
    """Test case for get_directives_compliance

    Compliance details for all directives
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/compliance/directives',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_global_compliance(client):
    """Test case for get_global_compliance

    Global compliance
    """
    params = [('precision', 2)]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/compliance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_compliance(client):
    """Test case for get_node_compliance

    Compliance details by node
    """
    params = [('level', 10),
                    ('precision', 2)]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/compliance/nodes/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nodes_compliance(client):
    """Test case for get_nodes_compliance

    Compliance details for all nodes
    """
    params = [('level', 10),
                    ('precision', 2)]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/compliance/nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_compliance(client):
    """Test case for get_rule_compliance

    Compliance details by rule
    """
    params = [('level', 10),
                    ('precision', 2)]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/compliance/rules/{rule_id}'.format(rule_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rules_compliance(client):
    """Test case for get_rules_compliance

    Compliance details for all rules
    """
    params = [('level', 10),
                    ('precision', 2)]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/compliance/rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

