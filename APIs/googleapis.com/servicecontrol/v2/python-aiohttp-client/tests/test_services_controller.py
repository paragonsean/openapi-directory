# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_request import CheckRequest
from openapi_server.models.check_response import CheckResponse
from openapi_server.models.report_request import ReportRequest


pytestmark = pytest.mark.asyncio

async def test_servicecontrol_services_check(client):
    """Test case for servicecontrol_services_check

    
    """
    body = {"serviceConfigId":"serviceConfigId","flags":"flags","resources":[{"container":"container","name":"name","location":"location","permission":"permission","type":"type"},{"container":"container","name":"name","location":"location","permission":"permission","type":"type"}],"attributes":{"request":{"headers":{"key":"headers"},"path":"path","reason":"reason","protocol":"protocol","method":"method","scheme":"scheme","size":"size","auth":{"principal":"principal","accessLevels":["accessLevels","accessLevels"],"presenter":"presenter","claims":{"key":""},"audiences":["audiences","audiences"]},"query":"query","host":"host","id":"id","time":"time"},"extensions":[{"key":""},{"key":""}],"resource":{"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","displayName":"displayName","service":"service","name":"name","annotations":{"key":"annotations"},"etag":"etag","location":"location","updateTime":"updateTime","type":"type","labels":{"key":"labels"}},"response":{"headers":{"key":"headers"},"code":"code","size":"size","backendLatency":"backendLatency","time":"time"},"origin":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}},"destination":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}},"api":{"protocol":"protocol","service":"service","operation":"operation","version":"version"},"source":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}}}}
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
        path='/v2/services/{service_namechec}'.format(service_name='service_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicecontrol_services_report(client):
    """Test case for servicecontrol_services_report

    
    """
    body = {"operations":[{"request":{"headers":{"key":"headers"},"path":"path","reason":"reason","protocol":"protocol","method":"method","scheme":"scheme","size":"size","auth":{"principal":"principal","accessLevels":["accessLevels","accessLevels"],"presenter":"presenter","claims":{"key":""},"audiences":["audiences","audiences"]},"query":"query","host":"host","id":"id","time":"time"},"extensions":[{"key":""},{"key":""}],"resource":{"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","displayName":"displayName","service":"service","name":"name","annotations":{"key":"annotations"},"etag":"etag","location":"location","updateTime":"updateTime","type":"type","labels":{"key":"labels"}},"response":{"headers":{"key":"headers"},"code":"code","size":"size","backendLatency":"backendLatency","time":"time"},"origin":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}},"destination":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}},"api":{"protocol":"protocol","service":"service","operation":"operation","version":"version"},"source":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}}},{"request":{"headers":{"key":"headers"},"path":"path","reason":"reason","protocol":"protocol","method":"method","scheme":"scheme","size":"size","auth":{"principal":"principal","accessLevels":["accessLevels","accessLevels"],"presenter":"presenter","claims":{"key":""},"audiences":["audiences","audiences"]},"query":"query","host":"host","id":"id","time":"time"},"extensions":[{"key":""},{"key":""}],"resource":{"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","displayName":"displayName","service":"service","name":"name","annotations":{"key":"annotations"},"etag":"etag","location":"location","updateTime":"updateTime","type":"type","labels":{"key":"labels"}},"response":{"headers":{"key":"headers"},"code":"code","size":"size","backendLatency":"backendLatency","time":"time"},"origin":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}},"destination":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}},"api":{"protocol":"protocol","service":"service","operation":"operation","version":"version"},"source":{"principal":"principal","regionCode":"regionCode","port":"port","ip":"ip","labels":{"key":"labels"}}}],"serviceConfigId":"serviceConfigId"}
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
        path='/v2/services/{service_namerepor}'.format(service_name='service_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

