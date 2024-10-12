# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.extended_timed_value import ExtendedTimedValue
from openapi_server.models.extended_timed_values import ExtendedTimedValues
from openapi_server.models.items_stream_values import ItemsStreamValues
from openapi_server.models.items_substatus import ItemsSubstatus
from openapi_server.models.items_summary_value import ItemsSummaryValue
from openapi_server.models.stream_updates_register import StreamUpdatesRegister
from openapi_server.models.stream_updates_retrieve import StreamUpdatesRetrieve
from openapi_server.models.timed_value import TimedValue
from openapi_server.models.timed_values import TimedValues


pytestmark = pytest.mark.asyncio

async def test_stream_get_channel(client):
    """Test case for stream_get_channel

    Opens a channel that will send messages about any value changes for the specified stream.
    """
    params = [('heartbeatRate', 56),
                    ('includeInitialValues', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/channel'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_end(client):
    """Test case for stream_get_end

    Returns the end-of-stream value of the stream.
    """
    params = [('desiredUnits', 'desired_units_example'),
                    ('selectedFields', 'selected_fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/end'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_interpolated(client):
    """Test case for stream_get_interpolated

    Retrieves interpolated values over the specified time range at the specified sampling interval.
    """
    params = [('desiredUnits', 'desired_units_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('interval', 'interval_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('syncTime', 'sync_time_example'),
                    ('syncTimeBoundaryType', 'sync_time_boundary_type_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/interpolated'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_interpolated_at_times(client):
    """Test case for stream_get_interpolated_at_times

    Retrieves interpolated values over the specified time range at the specified sampling interval.
    """
    params = [('time', ['time_example']),
                    ('desiredUnits', 'desired_units_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/interpolatedattimes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_plot(client):
    """Test case for stream_get_plot

    Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
    """
    params = [('desiredUnits', 'desired_units_example'),
                    ('endTime', 'end_time_example'),
                    ('intervals', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/plot'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_recorded(client):
    """Test case for stream_get_recorded

    Returns a list of compressed values for the requested time range from the source provider.
    """
    params = [('associations', 'associations_example'),
                    ('boundaryType', 'boundary_type_example'),
                    ('desiredUnits', 'desired_units_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('maxCount', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/recorded'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_recorded_at_time(client):
    """Test case for stream_get_recorded_at_time

    Returns a single recorded value based on the passed time and retrieval mode from the stream.
    """
    params = [('time', 'time_example'),
                    ('associations', 'associations_example'),
                    ('desiredUnits', 'desired_units_example'),
                    ('retrievalMode', 'retrieval_mode_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/recordedattime'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_recorded_at_times(client):
    """Test case for stream_get_recorded_at_times

    Retrieves recorded values at the specified times.
    """
    params = [('time', ['time_example']),
                    ('associations', 'associations_example'),
                    ('desiredUnits', 'desired_units_example'),
                    ('retrievalMode', 'retrieval_mode_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/recordedattimes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_summary(client):
    """Test case for stream_get_summary

    Returns a summary over the specified time range for the stream.
    """
    params = [('calculationBasis', 'calculation_basis_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('sampleInterval', 'sample_interval_example'),
                    ('sampleType', 'sample_type_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('summaryDuration', 'summary_duration_example'),
                    ('summaryType', ['summary_type_example']),
                    ('timeType', 'time_type_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/summary'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_get_value(client):
    """Test case for stream_get_value

    Returns the value of the stream at the specified time. By default, this is usually the current value.
    """
    params = [('desiredUnits', 'desired_units_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('time', 'time_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/{web_id}/value'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_register_stream_update(client):
    """Test case for stream_register_stream_update

    Register for stream updates
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streams/{web_id}/updates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_retrieve_stream_update(client):
    """Test case for stream_retrieve_stream_update

    Receive stream updates
    """
    params = [('desiredUnits', 'desired_units_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streams/updates/{marker}'.format(marker='marker_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stream_update_value(client):
    """Test case for stream_update_value

    Updates a value for the specified stream.
    """
    value = {"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False}
    params = [('bufferOption', 'buffer_option_example'),
                    ('updateOption', 'update_option_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streams/{web_id}/value'.format(web_id='web_id_example'),
        headers=headers,
        json=value,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stream_update_values(client):
    """Test case for stream_update_values

    Updates multiple values for the specified stream.
    """
    values = {"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False}
    params = [('bufferOption', 'buffer_option_example'),
                    ('updateOption', 'update_option_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streams/{web_id}/recorded'.format(web_id='web_id_example'),
        headers=headers,
        json=values,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

