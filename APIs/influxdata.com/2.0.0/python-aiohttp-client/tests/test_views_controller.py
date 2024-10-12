# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.view import View


pytestmark = pytest.mark.asyncio

async def test_get_dashboards_id_cells_id_view_1(client):
    """Test case for get_dashboards_id_cells_id_view_1

    Retrieve the view for a cell
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dashboards/{dashboard_id}/cells/{cell_id}/view'.format(dashboard_id='dashboard_id_example', cell_id='cell_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dashboards_id_cells_id_view_1(client):
    """Test case for patch_dashboards_id_cells_id_view_1

    Update the view for a cell
    """
    body = {"name":"name","links":{"self":"self"},"id":"id","properties":{"note":"note","xTickStep":1.0246457,"legendColorizeRows":True,"staticLegend":{"valueAxis":"valueAxis","hide":True,"widthRatio":7.386282,"colorizeRows":True,"orientationThreshold":4,"heightRatio":3.6160767,"opacity":2.027123},"prefix":"prefix","yTickStep":7.4577446,"axes":{"x":{"prefix":"prefix","bounds":["bounds","bounds"],"scale":"log","label":"label","suffix":"suffix","base":""},"y":{"prefix":"prefix","bounds":["bounds","bounds"],"scale":"log","label":"label","suffix":"suffix","base":""}},"xTickStart":1.2315135,"suffix":"suffix","type":"line-plus-single-stat","colors":[{"name":"name","hex":"hex","id":"id","type":"min","value":5.637377},{"name":"name","hex":"hex","id":"id","type":"min","value":5.637377}],"generateXAxisTicks":["generateXAxisTicks","generateXAxisTicks"],"legendOrientationThreshold":9,"yTotalTicks":1,"legendOpacity":7.0614014,"yColumn":"yColumn","xColumn":"xColumn","yTickStart":6.846853,"hoverDimension":"auto","shape":"chronograf-v2","legendHide":True,"queries":[{"builderConfig":{"functions":[{"name":"name"},{"name":"name"}],"buckets":["buckets","buckets"],"aggregateWindow":{"period":"period","fillValues":True},"tags":[{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"},{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"}]},"editMode":"builder","name":"name","text":"text"},{"builderConfig":{"functions":[{"name":"name"},{"name":"name"}],"buckets":["buckets","buckets"],"aggregateWindow":{"period":"period","fillValues":True},"tags":[{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"},{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"}]},"editMode":"builder","name":"name","text":"text"}],"xTotalTicks":1,"decimalPlaces":{"isEnforced":True,"digits":2},"shadeBelow":True,"timeFormat":"timeFormat","generateYAxisTicks":["generateYAxisTicks","generateYAxisTicks"],"position":"overlaid","showNoteWhenEmpty":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/dashboards/{dashboard_id}/cells/{cell_id}/view'.format(dashboard_id='dashboard_id_example', cell_id='cell_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

