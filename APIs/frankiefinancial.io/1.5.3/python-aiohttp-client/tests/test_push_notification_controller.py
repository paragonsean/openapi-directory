# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_result_object import NotificationResultObject


pytestmark = pytest.mark.asyncio

async def test_notify_result(client):
    """Test case for notify_result

    Push Notification Payload
    """
    notifcation_result = {"functionResult":"COMPLETED","entityCustomerReference":"AU0123456","requestId":"01BFJA617JMJXEW6G7TDDXNSHX","function":"entity.create","linkReference":"https://portal.frankiefinancial.io/entity/3fa85f64-5717-4562-b3fc-2c963f66afa6","documentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","entityId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","notificationType":"FUNCTION","message":"Entity successfully created","checkId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","username":"username"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/compliance/v1.2/your/configured/path/{request_id}'.format(request_id='request_id_example'),
        headers=headers,
        json=notifcation_result,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

