# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_stream_target_to_transcoder_output200_response import AddStreamTargetToTranscoderOutput200Response
from openapi_server.models.create_transcoder200_response import CreateTranscoder200Response
from openapi_server.models.create_transcoder_output200_response import CreateTranscoderOutput200Response
from openapi_server.models.create_transcoder_property200_response import CreateTranscoderProperty200Response
from openapi_server.models.disable_all_stream_targets_transcoder200_response import DisableAllStreamTargetsTranscoder200Response
from openapi_server.models.disable_transcoder_output_output_stream_target200_response import DisableTranscoderOutputOutputStreamTarget200Response
from openapi_server.models.enable_transcoder_output_output_stream_target200_response import EnableTranscoderOutputOutputStreamTarget200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.list_transcoder_recordings200_response import ListTranscoderRecordings200Response
from openapi_server.models.list_transcoder_schedules200_response import ListTranscoderSchedules200Response
from openapi_server.models.output_add_stream_target_input import OutputAddStreamTargetInput
from openapi_server.models.output_create_input import OutputCreateInput
from openapi_server.models.output_remove_stream_target_input import OutputRemoveStreamTargetInput
from openapi_server.models.output_stream_target import OutputStreamTarget
from openapi_server.models.output_stream_target_create_input import OutputStreamTargetCreateInput
from openapi_server.models.output_stream_target_update_input import OutputStreamTargetUpdateInput
from openapi_server.models.output_update_input import OutputUpdateInput
from openapi_server.models.outputs import Outputs
from openapi_server.models.reset_transcoder200_response import ResetTranscoder200Response
from openapi_server.models.restart_transcoder_output_output_stream_target200_response import RestartTranscoderOutputOutputStreamTarget200Response
from openapi_server.models.show_transcoder_state200_response import ShowTranscoderState200Response
from openapi_server.models.show_transcoder_stats200_response import ShowTranscoderStats200Response
from openapi_server.models.show_transcoder_thumbnail_url200_response import ShowTranscoderThumbnailUrl200Response
from openapi_server.models.show_uptime_metrics_current200_response import ShowUptimeMetricsCurrent200Response
from openapi_server.models.show_uptime_metrics_historic200_response import ShowUptimeMetricsHistoric200Response
from openapi_server.models.start_transcoder200_response import StartTranscoder200Response
from openapi_server.models.transcoder_create_input import TranscoderCreateInput
from openapi_server.models.transcoder_properties import TranscoderProperties
from openapi_server.models.transcoder_property_create_input import TranscoderPropertyCreateInput
from openapi_server.models.transcoder_update_input import TranscoderUpdateInput
from openapi_server.models.transcoders import Transcoders
from openapi_server.models.uptime import Uptime
from openapi_server.models.uptimes import Uptimes


pytestmark = pytest.mark.asyncio

async def test_add_stream_target_to_transcoder_output(client):
    """Test case for add_stream_target_to_transcoder_output

    Deprecated operation
    """
    output_stream_target = openapi_server.OutputAddStreamTargetInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{id}/add_stream_target'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        json=output_stream_target,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_transcoder(client):
    """Test case for create_transcoder

    Create a transcoder
    """
    transcoder = openapi_server.TranscoderCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transcoders',
        headers=headers,
        json=transcoder,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_transcoder_output(client):
    """Test case for create_transcoder_output

    Create an output
    """
    output = openapi_server.OutputCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transcoders/{transcoder_id}/outputs'.format(transcoder_id='transcoder_id_example'),
        headers=headers,
        json=output,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_transcoder_output_output_stream_target(client):
    """Test case for create_transcoder_output_output_stream_target

    Create an output stream target
    """
    output_stream_target = openapi_server.OutputStreamTargetCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets'.format(transcoder_id='transcoder_id_example', output_id='output_id_example'),
        headers=headers,
        json=output_stream_target,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_transcoder_property(client):
    """Test case for create_transcoder_property

    Create a property for a transcoder
    """
    _property = openapi_server.TranscoderPropertyCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transcoders/{transcoder_id}/properties'.format(transcoder_id='transcoder_id_example'),
        headers=headers,
        json=_property,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transcoder(client):
    """Test case for delete_transcoder

    Delete a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/transcoders/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transcoder_output(client):
    """Test case for delete_transcoder_output

    Delete an output
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{id}'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transcoder_output_output_stream_target(client):
    """Test case for delete_transcoder_output_output_stream_target

    Delete an output stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}'.format(transcoder_id='transcoder_id_example', output_id='output_id_example', stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transcoder_property(client):
    """Test case for delete_transcoder_property

    Delete a transcoder's property
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/transcoders/{transcoder_id}/properties/{id}'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_all_stream_targets_transcoder(client):
    """Test case for disable_all_stream_targets_transcoder

    Disable a transcoder's stream targets
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{id}/disable_all_stream_targets'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_transcoder_output_output_stream_target(client):
    """Test case for disable_transcoder_output_output_stream_target

    Disable an output stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/disable'.format(transcoder_id='transcoder_id_example', output_id='output_id_example', stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_all_stream_targets_transcoder(client):
    """Test case for enable_all_stream_targets_transcoder

    Enable a transcoder's stream targets
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{id}/enable_all_stream_targets'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_transcoder_output_output_stream_target(client):
    """Test case for enable_transcoder_output_output_stream_target

    Enable an output stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/enable'.format(transcoder_id='transcoder_id_example', output_id='output_id_example', stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_index_uptimes(client):
    """Test case for index_uptimes

    Fetch all uptime records for a transcoder
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
        path='/api/v1/transcoders/{transcoder_id}/uptimes'.format(transcoder_id='transcoder_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcoder_output_output_stream_targets(client):
    """Test case for list_transcoder_output_output_stream_targets

    Fetch all output stream targets of an output of a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets'.format(transcoder_id='transcoder_id_example', output_id='output_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcoder_outputs(client):
    """Test case for list_transcoder_outputs

    Fetch all outputs of a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/outputs'.format(transcoder_id='transcoder_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcoder_properties(client):
    """Test case for list_transcoder_properties

    Fetch a transcoder's properties
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/properties'.format(transcoder_id='transcoder_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcoder_recordings(client):
    """Test case for list_transcoder_recordings

    Fetch a transcoder's recordings
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{id}/recordings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcoder_schedules(client):
    """Test case for list_transcoder_schedules

    Fetch transcoder's schedules
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{id}/schedules'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transcoders(client):
    """Test case for list_transcoders

    Fetch all transcoders
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
        path='/api/v1/transcoders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_stream_target_to_transcoder_output(client):
    """Test case for remove_stream_target_to_transcoder_output

    Deprecated operation
    """
    output_stream_target = openapi_server.OutputRemoveStreamTargetInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{id}/remove_stream_target'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        json=output_stream_target,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_transcoder(client):
    """Test case for reset_transcoder

    Reset a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{id}/reset'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restart_transcoder_output_output_stream_target(client):
    """Test case for restart_transcoder_output_output_stream_target

    Restart an output stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/restart'.format(transcoder_id='transcoder_id_example', output_id='output_id_example', stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_transcoder(client):
    """Test case for show_transcoder

    Fetch a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_transcoder_output(client):
    """Test case for show_transcoder_output

    Fetch an output
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{id}'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_transcoder_output_output_stream_target(client):
    """Test case for show_transcoder_output_output_stream_target

    Fetch an output stream target
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}'.format(transcoder_id='transcoder_id_example', output_id='output_id_example', stream_target_id='stream_target_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_transcoder_property(client):
    """Test case for show_transcoder_property

    Fetch a property for a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/properties/{id}'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_transcoder_state(client):
    """Test case for show_transcoder_state

    Fetch the state and uptime ID of a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{id}/state'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_transcoder_stats(client):
    """Test case for show_transcoder_stats

    Fetch statistics for a current transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{id}/stats'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_transcoder_thumbnail_url(client):
    """Test case for show_transcoder_thumbnail_url

    Fetch the thumbnail URL of a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{id}/thumbnail_url'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_uptime(client):
    """Test case for show_uptime

    Fetch an uptime record
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/uptimes/{id}'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_uptime_metrics_current(client):
    """Test case for show_uptime_metrics_current

    Fetch current stream health metrics for an active transcoder
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/uptimes/{id}/metrics/current'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_uptime_metrics_historic(client):
    """Test case for show_uptime_metrics_historic

    Fetch historic stream health metrics for a transcoder
    """
    params = [('fields', 'fields_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example')]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transcoders/{transcoder_id}/uptimes/{id}/metrics/historic'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_transcoder(client):
    """Test case for start_transcoder

    Start a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{id}/start'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_transcoder(client):
    """Test case for stop_transcoder

    Stop a transcoder
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transcoders/{id}/stop'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transcoder(client):
    """Test case for update_transcoder

    Update a transcoder
    """
    transcoder = openapi_server.TranscoderUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/transcoders/{id}'.format(id='id_example'),
        headers=headers,
        json=transcoder,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transcoder_output(client):
    """Test case for update_transcoder_output

    Update an output
    """
    output = openapi_server.OutputUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{id}'.format(transcoder_id='transcoder_id_example', id='id_example'),
        headers=headers,
        json=output,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transcoder_output_output_stream_target(client):
    """Test case for update_transcoder_output_output_stream_target

    Update an output stream target
    """
    output_stream_target = openapi_server.OutputStreamTargetUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}'.format(transcoder_id='transcoder_id_example', output_id='output_id_example', stream_target_id='stream_target_id_example'),
        headers=headers,
        json=output_stream_target,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

