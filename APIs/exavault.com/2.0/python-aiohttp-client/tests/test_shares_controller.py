# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_share_request_body import AddShareRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.share_collection_response import ShareCollectionResponse
from openapi_server.models.share_response import ShareResponse
from openapi_server.models.update_share_request_body import UpdateShareRequestBody


pytestmark = pytest.mark.asyncio

async def test_add_share(client):
    """Test case for add_share

    Creates a share
    """
    body = {"messageBody":"messageBody","messageSubject":"Invitation to a shared folder","resources":["/testfolder"],"hasNotification":False,"accessMode":{"modify":True,"download":True,"upload":True,"delete":True},"type":"shared_folder","fileDropCreateFolders":False,"password":"password","requireEmail":False,"recipients":[{"type":"type","email":"email"},{"type":"type","email":"email"}],"name":"Shared Folder","sendingLocalFiles":True,"isPublic":True,"expiration":"2017-09-25T14:12:10Z","embed":False,"notificationEmails":["notify@example.com","notify2@example.com"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/shares',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_direct_send(client):
    """Test case for complete_direct_send

    Complete send files
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/shares/complete-send/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_share_by_id(client):
    """Test case for delete_share_by_id

    Deactivate a share
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/shares/{id}'.format(id=23241),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_share_by_id(client):
    """Test case for get_share_by_id

    Get a share
    """
    params = [('include', 'owner,notifications')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/shares/{id}'.format(id=23241),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_shares(client):
    """Test case for list_shares

    Get a list of shares
    """
    params = [('offset', 100),
                    ('limit', 100),
                    ('scope', 'active'),
                    ('sort', 'created'),
                    ('type', 'receive'),
                    ('include', 'owner,notifications'),
                    ('name', 'Customer*'),
                    ('recipient', 'test@example.com'),
                    ('message', 'submitted'),
                    ('username', 'example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/shares',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_share_by_id(client):
    """Test case for update_share_by_id

    Update a share
    """
    body = {"messageBody":"messageBody","messageSubject":"Invitation to a shared folder","resources":["/testfolder"],"hasNotification":False,"accessMode":{"modify":True,"download":True,"upload":True,"delete":True},"fileDropCreateFolders":False,"password":"password","requireEmail":False,"recipients":[{"type":"type","email":"email"},{"type":"type","email":"email"}],"name":"Shared Folder","isPublic":True,"expiration":"2017-09-25T14:12:10Z","embed":False,"notificationEmails":["notify@example.com","notify2@example.com"],"status":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/shares/{id}'.format(id=23241),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

