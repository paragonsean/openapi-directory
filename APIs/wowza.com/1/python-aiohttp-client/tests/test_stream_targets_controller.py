# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_stream_target200_response import CreateStreamTarget200Response
from openapi_server.models.create_stream_target_property200_response import CreateStreamTargetProperty200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.geoblock_create_input import GeoblockCreateInput
from openapi_server.models.geoblock_update_input import GeoblockUpdateInput
from openapi_server.models.regenerate_connection_code_stream_target200_response import RegenerateConnectionCodeStreamTarget200Response
from openapi_server.models.show_stream_target_geoblock200_response import ShowStreamTargetGeoblock200Response
from openapi_server.models.show_stream_target_metrics_current200_response import ShowStreamTargetMetricsCurrent200Response
from openapi_server.models.show_stream_target_metrics_historic200_response import ShowStreamTargetMetricsHistoric200Response
from openapi_server.models.show_stream_target_token_auth200_response import ShowStreamTargetTokenAuth200Response
from openapi_server.models.stream_target_create_input import StreamTargetCreateInput
from openapi_server.models.stream_target_properties import StreamTargetProperties
from openapi_server.models.stream_target_property_create_input import StreamTargetPropertyCreateInput
from openapi_server.models.stream_target_update_input import StreamTargetUpdateInput
from openapi_server.models.stream_targets import StreamTargets
from openapi_server.models.token_auth_create_input import TokenAuthCreateInput
from openapi_server.models.token_auth_update_input import TokenAuthUpdateInput
from openapi_server.models.wowza_stream_target_input import WowzaStreamTargetInput


pytestmark = pytest.mark.asyncio

async def test_add_stream_target(client):
    """Test case for add_stream_target

    Deprecated operation
    """
    stream_target = openapi_server.WowzaStreamTargetInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/stream_targets/add',
        headers=headers,
        json=stream_target,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_stream_target(client):
    """Test case for create_stream_target

    Create a stream target
    """
    stream_target = openapi_server.StreamTargetCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/stream_targets',
        headers=headers,
        json=stream_target,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_stream_target_geoblock(client):
    """Test case for create_stream_target_geoblock

    Create geo-blocking for a stream target
    """
    geoblock = openapi_server.GeoblockCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/stream_targets/{stream_target_id}/geoblock'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        json=geoblock,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_stream_target_property(client):
    """Test case for create_stream_target_property

    Create a property for a stream target
    """
    _property = openapi_server.StreamTargetPropertyCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/stream_targets/{stream_target_id}/properties'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        json=_property,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_stream_target_token_auth(client):
    """Test case for create_stream_target_token_auth

    Create token authorization for a stream target
    """
    token_auth = openapi_server.TokenAuthCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/stream_targets/{stream_target_id}/token_auth'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        json=token_auth,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_stream_target(client):
    """Test case for delete_stream_target

    Delete a stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/stream_targets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_stream_target_property(client):
    """Test case for delete_stream_target_property

    Delete a stream target property
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/stream_targets/{stream_target_id}/properties/{id}'.format(stream_target_id='stream_target_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_stream_target_properties(client):
    """Test case for list_stream_target_properties

    Fetch all properties of a stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets/{stream_target_id}/properties'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_stream_targets(client):
    """Test case for list_stream_targets

    Fetch all stream targets
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regenerate_connection_code_stream_target(client):
    """Test case for regenerate_connection_code_stream_target

    Regenerate the connection code for a stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/stream_targets/{id}/regenerate_connection_code'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_stream_target(client):
    """Test case for show_stream_target

    Fetch a stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_stream_target_geoblock(client):
    """Test case for show_stream_target_geoblock

    Fetch geo-blocking for a stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets/{stream_target_id}/geoblock'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_stream_target_metrics_current(client):
    """Test case for show_stream_target_metrics_current

    Fetch current health metrics for an active Wowza ultra low latency stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets/{id}/metrics/current'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_stream_target_metrics_historic(client):
    """Test case for show_stream_target_metrics_historic

    Fetch historic health metrics for a Wowza ultra low latency stream target
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example'),
                    ('interval', 'interval_example')]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets/{id}/metrics/historic'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_stream_target_property(client):
    """Test case for show_stream_target_property

    Fetch a property of a stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets/{stream_target_id}/properties/{id}'.format(stream_target_id='stream_target_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_stream_target_token_auth(client):
    """Test case for show_stream_target_token_auth

    Fetch token authorization for a stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stream_targets/{stream_target_id}/token_auth'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_stream_target(client):
    """Test case for update_stream_target

    Update a stream target
    """
    stream_target = openapi_server.StreamTargetUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/stream_targets/{id}'.format(id='id_example'),
        headers=headers,
        json=stream_target,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_stream_target_geoblock(client):
    """Test case for update_stream_target_geoblock

    Update geo-blocking for a stream target
    """
    geoblock = openapi_server.GeoblockUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/stream_targets/{stream_target_id}/geoblock'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        json=geoblock,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_stream_target_token_auth(client):
    """Test case for update_stream_target_token_auth

    Update token authorization for a stream target
    """
    token_auth = openapi_server.TokenAuthUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/stream_targets/{stream_target_id}/token_auth'.format(stream_target_id='stream_target_id_example'),
        headers=headers,
        json=token_auth,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

