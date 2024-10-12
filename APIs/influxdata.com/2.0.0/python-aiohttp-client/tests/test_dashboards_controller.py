# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.cell import Cell
from openapi_server.models.cell_update import CellUpdate
from openapi_server.models.create_cell import CreateCell
from openapi_server.models.create_dashboard_request import CreateDashboardRequest
from openapi_server.models.dashboard import Dashboard
from openapi_server.models.dashboards import Dashboards
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.patch_dashboard_request import PatchDashboardRequest
from openapi_server.models.post_dashboards201_response import PostDashboards201Response
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server.models.view import View


pytestmark = pytest.mark.asyncio

async def test_delete_dashboards_id(client):
    """Test case for delete_dashboards_id

    Delete a dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/dashboards/{dashboard_id}'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dashboards_id_cells_id_0(client):
    """Test case for delete_dashboards_id_cells_id_0

    Delete a dashboard cell
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/dashboards/{dashboard_id}/cells/{cell_id}'.format(dashboard_id='dashboard_id_example', cell_id='cell_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dashboards_id_labels_id(client):
    """Test case for delete_dashboards_id_labels_id

    Delete a label from a dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/dashboards/{dashboard_id}/labels/{label_id}'.format(dashboard_id='dashboard_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dashboards_id_members_id(client):
    """Test case for delete_dashboards_id_members_id

    Remove a member from a dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/dashboards/{dashboard_id}/members/{user_id}'.format(user_id='user_id_example', dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dashboards_id_owners_id(client):
    """Test case for delete_dashboards_id_owners_id

    Remove an owner from a dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/dashboards/{dashboard_id}/owners/{user_id}'.format(user_id='user_id_example', dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboards(client):
    """Test case for get_dashboards

    List all dashboards
    """
    params = [('offset', 56),
                    ('limit', 20),
                    ('descending', False),
                    ('owner', 'owner_example'),
                    ('sortBy', 'sort_by_example'),
                    ('id', ['id_example']),
                    ('orgID', 'org_id_example'),
                    ('org', 'org_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dashboards',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboards_id(client):
    """Test case for get_dashboards_id

    Retrieve a Dashboard
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dashboards/{dashboard_id}'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboards_id_cells_id_view_0(client):
    """Test case for get_dashboards_id_cells_id_view_0

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

async def test_get_dashboards_id_labels(client):
    """Test case for get_dashboards_id_labels

    List all labels for a dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dashboards/{dashboard_id}/labels'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboards_id_members(client):
    """Test case for get_dashboards_id_members

    List all dashboard members
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dashboards/{dashboard_id}/members'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboards_id_owners(client):
    """Test case for get_dashboards_id_owners

    List all dashboard owners
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/dashboards/{dashboard_id}/owners'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dashboards_id(client):
    """Test case for patch_dashboards_id

    Update a dashboard
    """
    body = {"cells":{"viewID":"viewID","w":6,"h":0,"x":1,"name":"name","y":5,"links":{"view":"view","self":"self"},"id":"id","properties":{"note":"note","xTickStep":1.0246457,"legendColorizeRows":True,"staticLegend":{"valueAxis":"valueAxis","hide":True,"widthRatio":7.386282,"colorizeRows":True,"orientationThreshold":4,"heightRatio":3.6160767,"opacity":2.027123},"prefix":"prefix","yTickStep":7.4577446,"axes":{"x":{"prefix":"prefix","bounds":["bounds","bounds"],"scale":"log","label":"label","suffix":"suffix","base":""},"y":{"prefix":"prefix","bounds":["bounds","bounds"],"scale":"log","label":"label","suffix":"suffix","base":""}},"xTickStart":1.2315135,"suffix":"suffix","type":"line-plus-single-stat","colors":[{"name":"name","hex":"hex","id":"id","type":"min","value":5.637377},{"name":"name","hex":"hex","id":"id","type":"min","value":5.637377}],"generateXAxisTicks":["generateXAxisTicks","generateXAxisTicks"],"legendOrientationThreshold":9,"yTotalTicks":1,"legendOpacity":7.0614014,"yColumn":"yColumn","xColumn":"xColumn","yTickStart":6.846853,"hoverDimension":"auto","shape":"chronograf-v2","legendHide":True,"queries":[{"builderConfig":{"functions":[{"name":"name"},{"name":"name"}],"buckets":["buckets","buckets"],"aggregateWindow":{"period":"period","fillValues":True},"tags":[{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"},{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"}]},"editMode":"builder","name":"name","text":"text"},{"builderConfig":{"functions":[{"name":"name"},{"name":"name"}],"buckets":["buckets","buckets"],"aggregateWindow":{"period":"period","fillValues":True},"tags":[{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"},{"aggregateFunctionType":"filter","values":["values","values"],"key":"key"}]},"editMode":"builder","name":"name","text":"text"}],"xTotalTicks":1,"decimalPlaces":{"isEnforced":True,"digits":2},"shadeBelow":True,"timeFormat":"timeFormat","generateYAxisTicks":["generateYAxisTicks","generateYAxisTicks"],"position":"overlaid","showNoteWhenEmpty":True}},"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/dashboards/{dashboard_id}'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dashboards_id_cells_id_0(client):
    """Test case for patch_dashboards_id_cells_id_0

    Update the non-positional information related to a cell
    """
    body = {"w":6,"h":0,"x":1,"y":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/dashboards/{dashboard_id}/cells/{cell_id}'.format(dashboard_id='dashboard_id_example', cell_id='cell_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dashboards_id_cells_id_view_0(client):
    """Test case for patch_dashboards_id_cells_id_view_0

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


pytestmark = pytest.mark.asyncio

async def test_post_dashboards(client):
    """Test case for post_dashboards

    Create a dashboard
    """
    body = {"name":"name","description":"description","orgID":"orgID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/dashboards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_dashboards_id_cells_0(client):
    """Test case for post_dashboards_id_cells_0

    Create a dashboard cell
    """
    body = {"w":6,"h":0,"name":"name","x":1,"y":5,"usingView":"usingView"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/dashboards/{dashboard_id}/cells'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_dashboards_id_labels(client):
    """Test case for post_dashboards_id_labels

    Add a label to a dashboard
    """
    body = {"labelID":"labelID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/dashboards/{dashboard_id}/labels'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_dashboards_id_members(client):
    """Test case for post_dashboards_id_members

    Add a member to a dashboard
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/dashboards/{dashboard_id}/members'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_dashboards_id_owners(client):
    """Test case for post_dashboards_id_owners

    Add an owner to a dashboard
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/dashboards/{dashboard_id}/owners'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_dashboards_id_cells_0(client):
    """Test case for put_dashboards_id_cells_0

    Replace cells in a dashboard
    """
    body = {"viewID":"viewID","w":6,"h":0,"x":1,"y":5,"links":{"view":"view","self":"self"},"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/dashboards/{dashboard_id}/cells'.format(dashboard_id='dashboard_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

