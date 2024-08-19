# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_items_substatus import ItemsItemsSubstatus
from openapi_server.models.items_stream_summaries import ItemsStreamSummaries
from openapi_server.models.items_stream_updates_register import ItemsStreamUpdatesRegister
from openapi_server.models.items_stream_updates_retrieve import ItemsStreamUpdatesRetrieve
from openapi_server.models.items_stream_value import ItemsStreamValue
from openapi_server.models.items_stream_values import ItemsStreamValues
from openapi_server.models.items_substatus import ItemsSubstatus
from openapi_server.models.stream_value import StreamValue
from openapi_server.models.stream_values import StreamValues


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_channel(client):
    """Test case for stream_set_get_channel

    Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.
    """
    params = [('categoryName', 'category_name_example'),
                    ('heartbeatRate', 56),
                    ('includeInitialValues', True),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('templateName', 'template_name_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/channel'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_channel_ad_hoc(client):
    """Test case for stream_set_get_channel_ad_hoc

    Opens a channel that will send messages about any value changes for the specified streams.
    """
    params = [('webId', ['web_id_example']),
                    ('heartbeatRate', 56),
                    ('includeInitialValues', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/channel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_end(client):
    """Test case for stream_set_get_end

    Returns End of stream values of the attributes for an Element, Event Frame or Attribute
    """
    params = [('categoryName', 'category_name_example'),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('templateName', 'template_name_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/end'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_end_ad_hoc(client):
    """Test case for stream_set_get_end_ad_hoc

    Returns End Of Stream values for attributes of the specified streams
    """
    params = [('webId', ['web_id_example']),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/end',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_interpolated(client):
    """Test case for stream_set_get_interpolated

    Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.
    """
    params = [('categoryName', 'category_name_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('interval', 'interval_example'),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startTime', 'start_time_example'),
                    ('syncTime', 'sync_time_example'),
                    ('syncTimeBoundaryType', 'sync_time_boundary_type_example'),
                    ('templateName', 'template_name_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/interpolated'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_interpolated_ad_hoc(client):
    """Test case for stream_set_get_interpolated_ad_hoc

    Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.
    """
    params = [('webId', ['web_id_example']),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('interval', 'interval_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startTime', 'start_time_example'),
                    ('syncTime', 'sync_time_example'),
                    ('syncTimeBoundaryType', 'sync_time_boundary_type_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/interpolated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_interpolated_at_times(client):
    """Test case for stream_set_get_interpolated_at_times

    Returns interpolated values of attributes for an element, event frame or attribute at the specified times.
    """
    params = [('time', ['time_example']),
                    ('categoryName', 'category_name_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortOrder', 'sort_order_example'),
                    ('templateName', 'template_name_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/interpolatedattimes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_interpolated_at_times_ad_hoc(client):
    """Test case for stream_set_get_interpolated_at_times_ad_hoc

    Returns interpolated values of the specified streams at the specified times.
    """
    params = [('time', ['time_example']),
                    ('webId', ['web_id_example']),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/interpolatedattimes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_joined(client):
    """Test case for stream_set_get_joined

    Returns the base stream's recorded values and subordinate streams' interpolated values at times matching the recorded values' timestamps.
    """
    params = [('baseWebId', 'base_web_id_example'),
                    ('subordinateWebId', ['subordinate_web_id_example']),
                    ('boundaryType', 'boundary_type_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('maxCount', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/joined',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_plot(client):
    """Test case for stream_set_get_plot

    Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
    """
    params = [('categoryName', 'category_name_example'),
                    ('endTime', 'end_time_example'),
                    ('intervals', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startTime', 'start_time_example'),
                    ('templateName', 'template_name_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/plot'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_plot_ad_hoc(client):
    """Test case for stream_set_get_plot_ad_hoc

    Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
    """
    params = [('webId', ['web_id_example']),
                    ('endTime', 'end_time_example'),
                    ('intervals', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startTime', 'start_time_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/plot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_recorded(client):
    """Test case for stream_set_get_recorded

    Returns recorded values of the attributes for an element, event frame, or attribute.
    """
    params = [('boundaryType', 'boundary_type_example'),
                    ('categoryName', 'category_name_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startTime', 'start_time_example'),
                    ('templateName', 'template_name_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/recorded'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_recorded_ad_hoc(client):
    """Test case for stream_set_get_recorded_ad_hoc

    Returns recorded values of the specified streams.
    """
    params = [('webId', ['web_id_example']),
                    ('boundaryType', 'boundary_type_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('includeFilteredValues', True),
                    ('maxCount', 56),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startTime', 'start_time_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/recorded',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_recorded_at_time(client):
    """Test case for stream_set_get_recorded_at_time

    Returns recorded values of the attributes for an element, event frame, or attribute.
    """
    params = [('time', 'time_example'),
                    ('categoryName', 'category_name_example'),
                    ('nameFilter', 'name_filter_example'),
                    ('retrievalMode', 'retrieval_mode_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('templateName', 'template_name_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/recordedattime'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_recorded_at_time_ad_hoc(client):
    """Test case for stream_set_get_recorded_at_time_ad_hoc

    Returns recorded values based on the passed time and retrieval mode.
    """
    params = [('time', 'time_example'),
                    ('webId', ['web_id_example']),
                    ('retrievalMode', 'retrieval_mode_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/recordedattime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_recorded_at_times(client):
    """Test case for stream_set_get_recorded_at_times

    Returns recorded values of attributes for an element, event frame or attribute at the specified times.
    """
    params = [('time', ['time_example']),
                    ('categoryName', 'category_name_example'),
                    ('nameFilter', 'name_filter_example'),
                    ('retrievalMode', 'retrieval_mode_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortOrder', 'sort_order_example'),
                    ('templateName', 'template_name_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/recordedattimes'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_recorded_at_times_ad_hoc(client):
    """Test case for stream_set_get_recorded_at_times_ad_hoc

    Returns recorded values of the specified streams at the specified times.
    """
    params = [('time', ['time_example']),
                    ('webId', ['web_id_example']),
                    ('retrievalMode', 'retrieval_mode_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/recordedattimes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_summaries(client):
    """Test case for stream_set_get_summaries

    Returns summary values of the attributes for an element, event frame or attribute.
    """
    params = [('calculationBasis', 'calculation_basis_example'),
                    ('categoryName', 'category_name_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('nameFilter', 'name_filter_example'),
                    ('sampleInterval', 'sample_interval_example'),
                    ('sampleType', 'sample_type_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('startTime', 'start_time_example'),
                    ('summaryDuration', 'summary_duration_example'),
                    ('summaryType', ['summary_type_example']),
                    ('templateName', 'template_name_example'),
                    ('timeType', 'time_type_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/summary'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_summaries_ad_hoc(client):
    """Test case for stream_set_get_summaries_ad_hoc

    Returns summary values of the specified streams.
    """
    params = [('webId', ['web_id_example']),
                    ('calculationBasis', 'calculation_basis_example'),
                    ('endTime', 'end_time_example'),
                    ('filterExpression', 'filter_expression_example'),
                    ('sampleInterval', 'sample_interval_example'),
                    ('sampleType', 'sample_type_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('summaryDuration', 'summary_duration_example'),
                    ('summaryType', ['summary_type_example']),
                    ('timeType', 'time_type_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_values(client):
    """Test case for stream_set_get_values

    Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.
    """
    params = [('categoryName', 'category_name_example'),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('showExcluded', True),
                    ('showHidden', True),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('templateName', 'template_name_example'),
                    ('time', 'time_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/{web_id}/value'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_get_values_ad_hoc(client):
    """Test case for stream_set_get_values_ad_hoc

    Returns values of the specified streams.
    """
    params = [('webId', ['web_id_example']),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('time', 'time_example'),
                    ('timeZone', 'time_zone_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/value',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_register_stream_set_updates(client):
    """Test case for stream_set_register_stream_set_updates

    Register for stream updates
    """
    params = [('webId', ['web_id_example']),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streamsets/updates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_set_retrieve_stream_set_updates(client):
    """Test case for stream_set_retrieve_stream_set_updates

    Receive stream updates
    """
    params = [('marker', ['marker_example']),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/streamsets/updates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stream_set_update_value(client):
    """Test case for stream_set_update_value

    Updates a single value for the specified streams.
    """
    values = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement|Water","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Value":{"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False},"Links":{"Source":"Source"},"Name":"Water"}
    params = [('bufferOption', 'buffer_option_example'),
                    ('updateOption', 'update_option_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streamsets/{web_id}/value'.format(web_id='web_id_example'),
        headers=headers,
        json=values,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stream_set_update_value_ad_hoc(client):
    """Test case for stream_set_update_value_ad_hoc

    Updates a single value for the specified streams.
    """
    values = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement|Water","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Value":{"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False},"Links":{"Source":"Source"},"Name":"Water"}
    params = [('bufferOption', 'buffer_option_example'),
                    ('updateOption', 'update_option_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streamsets/value',
        headers=headers,
        json=values,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stream_set_update_values(client):
    """Test case for stream_set_update_values

    Updates multiple values for the specified streams.
    """
    values = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement|Water","UnitsAbbreviation":"m","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Links":{"Source":"Source"},"Items":[{"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False},{"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False}],"Name":"Water"}
    params = [('bufferOption', 'buffer_option_example'),
                    ('updateOption', 'update_option_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streamsets/{web_id}/recorded'.format(web_id='web_id_example'),
        headers=headers,
        json=values,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stream_set_update_values_ad_hoc(client):
    """Test case for stream_set_update_values_ad_hoc

    Updates multiple values for the specified streams.
    """
    values = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement|Water","UnitsAbbreviation":"m","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1AbEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Links":{"Source":"Source"},"Items":[{"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False},{"Annotated":False,"Errors":[{"Message":["An error has occurred."],"FieldName":"Value"},{"Message":["An error has occurred."],"FieldName":"Value"}],"UnitsAbbreviation":"m","Substituted":False,"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Value":12.3,"Good":True,"Timestamp":"2014-07-22T14:00:00Z","Questionable":False}],"Name":"Water"}
    params = [('bufferOption', 'buffer_option_example'),
                    ('updateOption', 'update_option_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/streamsets/recorded',
        headers=headers,
        json=values,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

