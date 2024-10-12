# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_load_balancer_request import CreateLoadBalancerRequest
from openapi_server.models.load_balancers_get200_response import LoadBalancersGet200Response
from openapi_server.models.load_balancers_id_get200_response import LoadBalancersIdGet200Response
from openapi_server.models.load_balancers_id_metrics_get200_response import LoadBalancersIdMetricsGet200Response
from openapi_server.models.load_balancers_id_put_request import LoadBalancersIdPutRequest
from openapi_server.models.load_balancers_post201_response import LoadBalancersPost201Response


pytestmark = pytest.mark.asyncio

async def test_load_balancers_get(client):
    """Test case for load_balancers_get

    Get all Load Balancers
    """
    params = [('sort', 'sort_example'),
                    ('name', 'name_example'),
                    ('label_selector', 'label_selector_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/load_balancers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_delete(client):
    """Test case for load_balancers_id_delete

    Delete a Load Balancer
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/load_balancers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_get(client):
    """Test case for load_balancers_id_get

    Get a Load Balancer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/load_balancers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_metrics_get(client):
    """Test case for load_balancers_id_metrics_get

    Get Metrics for a LoadBalancer
    """
    params = [('type', 'type_example'),
                    ('start', 'start_example'),
                    ('end', 'end_example'),
                    ('step', 'step_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/load_balancers/{id}/metrics'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_put(client):
    """Test case for load_balancers_id_put

    Update a Load Balancer
    """
    body = openapi_server.LoadBalancersIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/load_balancers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_post(client):
    """Test case for load_balancers_post

    Create a Load Balancer
    """
    body = {"network_zone":"eu-central","load_balancer_type":"lb11","name":"Web Frontend","public_interface":True,"location":"location","services":[{"protocol":"https","listen_port":443,"destination_port":80,"http":{"redirect_http":True,"sticky_sessions":True,"certificates":[897],"cookie_lifetime":300,"cookie_name":"HCLBSTICKY"},"health_check":{"retries":3,"protocol":"http","port":4711,"http":{"path":"/","response":"{\"status\": \"ok\"}","domain":"example.com","status_codes":["2??","3??"],"tls":False},"interval":15,"timeout":10},"proxyprotocol":False},{"protocol":"https","listen_port":443,"destination_port":80,"http":{"redirect_http":True,"sticky_sessions":True,"certificates":[897],"cookie_lifetime":300,"cookie_name":"HCLBSTICKY"},"health_check":{"retries":3,"protocol":"http","port":4711,"http":{"path":"/","response":"{\"status\": \"ok\"}","domain":"example.com","status_codes":["2??","3??"],"tls":False},"interval":15,"timeout":10},"proxyprotocol":False}],"targets":[{"use_private_ip":True,"server":{"id":80},"label_selector":{"selector":"env=prod"},"ip":{"ip":"203.0.113.1"},"health_status":[{"listen_port":443,"status":"healthy"},{"listen_port":443,"status":"healthy"}],"type":"server","targets":[{"use_private_ip":True,"server":{"id":80},"health_status":[{"listen_port":443,"status":"healthy"},{"listen_port":443,"status":"healthy"}],"type":"server"},{"use_private_ip":True,"server":{"id":80},"health_status":[{"listen_port":443,"status":"healthy"},{"listen_port":443,"status":"healthy"}],"type":"server"}]},{"use_private_ip":True,"server":{"id":80},"label_selector":{"selector":"env=prod"},"ip":{"ip":"203.0.113.1"},"health_status":[{"listen_port":443,"status":"healthy"},{"listen_port":443,"status":"healthy"}],"type":"server","targets":[{"use_private_ip":True,"server":{"id":80},"health_status":[{"listen_port":443,"status":"healthy"},{"listen_port":443,"status":"healthy"}],"type":"server"},{"use_private_ip":True,"server":{"id":80},"health_status":[{"listen_port":443,"status":"healthy"},{"listen_port":443,"status":"healthy"}],"type":"server"}]}],"algorithm":{"type":"round_robin"},"labels":{"labelkey":"value"},"network":123}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

