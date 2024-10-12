# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_annotation_info import AlertAnnotationInfo
from openapi_server.models.alert_attachment_info import AlertAttachmentInfo
from openapi_server.models.alert_filter_public import AlertFilterPublic
from openapi_server.models.alert_info import AlertInfo
from openapi_server.models.alert_notification_info import AlertNotificationInfo
from openapi_server.models.alert_report import AlertReport
from openapi_server.models.change_alert_status_filter_info import ChangeAlertStatusFilterInfo
from openapi_server.models.change_alert_status_info import ChangeAlertStatusInfo
from openapi_server.models.change_alert_status_multiple_info import ChangeAlertStatusMultipleInfo
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.overview_alert import OverviewAlert
from openapi_server.models.overview_alert_paged_results_public import OverviewAlertPagedResultsPublic
from openapi_server.models.raise_alert_info import RaiseAlertInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_acknowledge_all_post(client):
    """Test case for alerts_acknowledge_all_post

    Confirms all visible alerts
    """
    body = {"categoryIds":["categoryIds","categoryIds"],"minDate":"2000-01-23T04:56:07.000+00:00","scope":0,"maxDate":"2000-01-23T04:56:07.000+00:00","teamIds":["teamIds","teamIds"]}
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/acknowledgeAll',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_acknowledge_multiple_post(client):
    """Test case for alerts_acknowledge_multiple_post

    Acknowlegde multiple alerts
    """
    body = {"alertIds":["alertIds","alertIds"],"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/acknowledgeMultiple',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_alert_id_acknowledge_post(client):
    """Test case for alerts_alert_id_acknowledge_post

    Acknowledge an alert
    """
    body = {"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/{alert_id}/acknowledge'.format(alert_id='alert_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_alert_id_annotate_post(client):
    """Test case for alerts_alert_id_annotate_post

    Annotate Alert
    """
    body = {"annotationType":0,"id":"id","text":"text","userId":"userId","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/{alert_id}/annotate'.format(alert_id='alert_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_alert_id_annotations_get(client):
    """Test case for alerts_alert_id_annotations_get

    Get annotations of an alert
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alerts/{alert_id}/annotations'.format(alert_id='alert_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_alert_id_attachments_attachment_id_get(client):
    """Test case for alerts_alert_id_attachments_attachment_id_get

    Gets a specified attachment of a specified alert.
    """
    params = [('width', 56),
                    ('height', 56),
                    ('scale', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alerts/{alert_id}/attachments/{attachment_id}'.format(alert_id='alert_id_example', attachment_id='attachment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_alert_id_attachments_get(client):
    """Test case for alerts_alert_id_attachments_get

    Get attachments of an alert
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alerts/{alert_id}/attachments'.format(alert_id='alert_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_alert_id_close_post(client):
    """Test case for alerts_alert_id_close_post

    Close an alert
    """
    body = {"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/{alert_id}/close'.format(alert_id='alert_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_alert_id_get(client):
    """Test case for alerts_alert_id_get

    Get Alert
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alerts/{alert_id}'.format(alert_id='alert_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_alert_id_notifications_get(client):
    """Test case for alerts_alert_id_notifications_get

    Get alert notifications
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alerts/{alert_id}/notifications'.format(alert_id='alert_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_alert_id_overview_get(client):
    """Test case for alerts_alert_id_overview_get

    Get an overview alert.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alerts/{alert_id}/overview'.format(alert_id='alert_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_alert_id_undo_acknowledge_post(client):
    """Test case for alerts_alert_id_undo_acknowledge_post

    Undo the acknowledgement of an alert.
    """
    body = {"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/{alert_id}/undoAcknowledge'.format(alert_id='alert_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_alert_id_undo_close_post(client):
    """Test case for alerts_alert_id_undo_close_post

    Undo the closure of an alert.
    """
    body = {"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/{alert_id}/undoClose'.format(alert_id='alert_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_close_all_post(client):
    """Test case for alerts_close_all_post

    Close all acknowledged alerts.
    """
    body = {"categoryIds":["categoryIds","categoryIds"],"minDate":"2000-01-23T04:56:07.000+00:00","scope":0,"maxDate":"2000-01-23T04:56:07.000+00:00","teamIds":["teamIds","teamIds"]}
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/closeAll',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_close_multiple_post(client):
    """Test case for alerts_close_multiple_post

    Close multiple alerts
    """
    body = {"alertIds":["alertIds","alertIds"],"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/closeMultiple',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_paged_post(client):
    """Test case for alerts_paged_post

    Gets alerts paged
    """
    body = {"statusCodes":0,"showPersonalHiddenCategories":True,"categoryIds":["categoryIds","categoryIds"],"minCreationDate":"2000-01-23T04:56:07.000+00:00","modifiedSince":"2000-01-23T04:56:07.000+00:00","alertIds":["alertIds","alertIds"],"alertsAfterId":"alertsAfterId","teamId":"teamId","maxCreationDate":"2000-01-23T04:56:07.000+00:00","textToSearch":"textToSearch","continuationToken":{"nextTableName":"nextTableName","nextRowKey":"nextRowKey","nextPartitionKey":"nextPartitionKey"}}
    params = [('maxResults', 56),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/paged',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_post(client):
    """Test case for alerts_post

    Trigger Alert
    """
    body = {"severity":6,"attachments":[{"name":"name","id":"id","encoding":6,"contentType":"contentType","content":"content"},{"name":"name","id":"id","encoding":6,"contentType":"contentType","content":"content"}],"flags":0,"externalId":"externalId","text":"text","category":"category","title":"title","parameters":[{"name":"name","type":7,"value":"value","order":2},{"name":"name","type":7,"value":"value","order":2}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_report_get(client):
    """Test case for alerts_report_get

    Get Alert Report
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alerts/report',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_undo_acknowledge_multiple_post(client):
    """Test case for alerts_undo_acknowledge_multiple_post

    Queue undo of multiple acknowledgments.
    """
    body = {"alertIds":["alertIds","alertIds"],"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/undoAcknowledgeMultiple',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_alerts_undo_close_multiple_post(client):
    """Test case for alerts_undo_close_multiple_post

    Withdraw closure of multiple alerts
    """
    body = {"alertIds":["alertIds","alertIds"],"description":"description","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alerts/undoCloseMultiple',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

