# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message import Message
from openapi_server.models.send_message_request import SendMessageRequest


pytestmark = pytest.mark.asyncio

async def test_fcm_projects_messages_send(client):
    """Test case for fcm_projects_messages_send

    
    """
    body = {"validateOnly":True,"message":{"notification":{"image":"image","body":"body","title":"title"},"condition":"condition","data":{"key":"data"},"webpush":{"headers":{"key":"headers"},"notification":{"key":""},"data":{"key":"data"},"fcmOptions":{"analyticsLabel":"analyticsLabel","link":"link"}},"android":{"notification":{"color":"color","lightSettings":{"color":{"red":5.962134,"green":1.4658129,"blue":6.0274563,"alpha":0.8008282},"lightOnDuration":"lightOnDuration","lightOffDuration":"lightOffDuration"},"sound":"sound","icon":"icon","notificationPriority":"PRIORITY_UNSPECIFIED","bodyLocKey":"bodyLocKey","body":"body","title":"title","localOnly":True,"defaultVibrateTimings":True,"vibrateTimings":["vibrateTimings","vibrateTimings"],"bodyLocArgs":["bodyLocArgs","bodyLocArgs"],"eventTime":"eventTime","tag":"tag","titleLocArgs":["titleLocArgs","titleLocArgs"],"defaultSound":True,"channelId":"channelId","image":"image","ticker":"ticker","visibility":"VISIBILITY_UNSPECIFIED","notificationCount":5,"titleLocKey":"titleLocKey","bypassProxyNotification":True,"sticky":True,"defaultLightSettings":True,"clickAction":"clickAction"},"restrictedPackageName":"restrictedPackageName","data":{"key":"data"},"collapseKey":"collapseKey","fcmOptions":{"analyticsLabel":"analyticsLabel"},"directBootOk":True,"priority":"NORMAL","ttl":"ttl"},"fcmOptions":{"analyticsLabel":"analyticsLabel"},"name":"name","apns":{"headers":{"key":"headers"},"payload":{"key":""},"fcmOptions":{"image":"image","analyticsLabel":"analyticsLabel"}},"topic":"topic","token":"token"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/messages:send'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

