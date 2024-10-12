# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_download_share_request import CreateDownloadShareRequest
from openapi_server.models.create_upload_share_request import CreateUploadShareRequest
from openapi_server.models.delete_download_shares_request import DeleteDownloadSharesRequest
from openapi_server.models.delete_upload_shares_request import DeleteUploadSharesRequest
from openapi_server.models.download_share import DownloadShare
from openapi_server.models.download_share_link_email import DownloadShareLinkEmail
from openapi_server.models.download_share_list import DownloadShareList
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.update_download_share_request import UpdateDownloadShareRequest
from openapi_server.models.update_download_shares_bulk_request import UpdateDownloadSharesBulkRequest
from openapi_server.models.update_upload_share_request import UpdateUploadShareRequest
from openapi_server.models.update_upload_shares_bulk_request import UpdateUploadSharesBulkRequest
from openapi_server.models.upload_share import UploadShare
from openapi_server.models.upload_share_link_email import UploadShareLinkEmail
from openapi_server.models.upload_share_list import UploadShareList


pytestmark = pytest.mark.asyncio

async def test_create_download_share(client):
    """Test case for create_download_share

    Create new Download Share
    """
    body = {"mailBody":"mailBody","notes":"notes","receiverLanguage":"receiverLanguage","sendMail":False,"smsRecipients":"smsRecipients","fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"internalNotes":"internalNotes","showCreatorName":False,"notifyCreator":False,"showCreatorUsername":False,"maxDownloads":0,"mailSubject":"mailSubject","password":"password","sendSms":False,"name":"name","creatorLanguage":"creatorLanguage","expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"keyPair":{"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}},"mailRecipients":"mailRecipients","textMessageRecipients":["textMessageRecipients","textMessageRecipients"],"nodeId":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/shares/downloads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_upload_share(client):
    """Test case for create_upload_share

    Create new Upload Share
    """
    body = {"mailBody":"mailBody","notes":"notes","receiverLanguage":"receiverLanguage","targetId":5,"sendMail":False,"smsRecipients":"smsRecipients","maxSize":6,"internalNotes":"internalNotes","showCreatorName":False,"notifyCreator":False,"showCreatorUsername":False,"mailSubject":"mailSubject","password":"password","filesExpiryPeriod":0,"sendSms":False,"maxSlots":1,"name":"name","showUploadedFiles":False,"creatorLanguage":"creatorLanguage","expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"mailRecipients":"mailRecipients","textMessageRecipients":["textMessageRecipients","textMessageRecipients"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/shares/uploads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_download_shares(client):
    """Test case for delete_download_shares

    Remove Download Shares
    """
    body = {"shareIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/shares/downloads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_upload_shares(client):
    """Test case for delete_upload_shares

    Remove Upload Shares
    """
    body = {"shareIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/shares/uploads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_download_share(client):
    """Test case for remove_download_share

    Remove Download Share
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/shares/downloads/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_upload_share(client):
    """Test case for remove_upload_share

    Remove Upload Share
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/shares/uploads/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_download_share(client):
    """Test case for request_download_share

    Request Download Share
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/shares/downloads/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_download_share_qr(client):
    """Test case for request_download_share_qr

    Request Download Share via QR Code
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/shares/downloads/{share_id}/qr'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_download_shares(client):
    """Test case for request_download_shares

    Request list of Download Shares
    """
    params = [('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/shares/downloads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_upload_share(client):
    """Test case for request_upload_share

    Request Upload Share
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/shares/uploads/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_upload_share_qr(client):
    """Test case for request_upload_share_qr

    Request Upload Share via QR Code
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/shares/uploads/{share_id}/qr'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_upload_shares(client):
    """Test case for request_upload_shares

    Request list of Upload Shares
    """
    params = [('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/shares/uploads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_download_share_link_via_email(client):
    """Test case for send_download_share_link_via_email

    Send an existing Download Share link via email
    """
    body = {"receiverLanguage":"receiverLanguage","recipients":["recipients","recipients"],"body":"body"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/shares/downloads/{share_id}/email'.format(share_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_upload_share_link_via_email(client):
    """Test case for send_upload_share_link_via_email

    Send an existing Upload Share link via email
    """
    body = {"receiverLanguage":"receiverLanguage","recipients":["recipients","recipients"],"body":"body"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/shares/uploads/{share_id}/email'.format(share_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_download_share(client):
    """Test case for update_download_share

    Update Download Share
    """
    body = {"resetPassword":True,"notes":"notes","resetMaxDownloads":True,"receiverLanguage":"receiverLanguage","internalNotes":"internalNotes","showCreatorName":True,"notifyCreator":True,"showCreatorUsername":True,"maxDownloads":0,"password":"password","name":"name","expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"textMessageRecipients":["textMessageRecipients","textMessageRecipients"],"defaultCountry":"defaultCountry"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/shares/downloads/{share_id}'.format(share_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_download_shares(client):
    """Test case for update_download_shares

    Update a list of Download Shares
    """
    body = {"resetMaxDownloads":True,"expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"showCreatorName":True,"showCreatorUsername":True,"maxDownloads":0,"objectIds":[6,6]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/shares/downloads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_upload_share(client):
    """Test case for update_upload_share

    Update Upload Share
    """
    body = {"resetPassword":True,"notes":"notes","receiverLanguage":"receiverLanguage","resetMaxSlots":True,"maxSize":6,"internalNotes":"internalNotes","showCreatorName":True,"notifyCreator":True,"showCreatorUsername":True,"password":"password","resetMaxSize":True,"filesExpiryPeriod":0,"resetFilesExpiryPeriod":True,"maxSlots":1,"name":"name","showUploadedFiles":True,"expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"textMessageRecipients":["textMessageRecipients","textMessageRecipients"],"defaultCountry":"defaultCountry"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/shares/uploads/{share_id}'.format(share_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_upload_shares(client):
    """Test case for update_upload_shares

    Update List of Upload Shares
    """
    body = {"resetMaxSize":True,"filesExpiryPeriod":0,"resetFilesExpiryPeriod":True,"maxSlots":1,"resetMaxSlots":True,"showUploadedFiles":True,"expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"maxSize":6,"showCreatorName":True,"showCreatorUsername":True,"objectIds":[5,5]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/shares/uploads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

