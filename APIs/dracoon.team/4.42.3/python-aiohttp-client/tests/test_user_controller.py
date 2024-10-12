# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.attributes_response import AttributesResponse
from openapi_server.models.avatar import Avatar
from openapi_server.models.change_user_password_request import ChangeUserPasswordRequest
from openapi_server.models.create_key_pair_request import CreateKeyPairRequest
from openapi_server.models.customer_data import CustomerData
from openapi_server.models.enable_customer_encryption_request import EnableCustomerEncryptionRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.mfa_totp_confirmation_request import MfaTotpConfirmationRequest
from openapi_server.models.notification_config import NotificationConfig
from openapi_server.models.notification_config_change_request import NotificationConfigChangeRequest
from openapi_server.models.notification_config_list import NotificationConfigList
from openapi_server.models.o_auth_approval import OAuthApproval
from openapi_server.models.o_auth_authorization import OAuthAuthorization
from openapi_server.models.profile_attributes import ProfileAttributes
from openapi_server.models.profile_attributes_request import ProfileAttributesRequest
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.subscribed_download_share import SubscribedDownloadShare
from openapi_server.models.subscribed_download_share_list import SubscribedDownloadShareList
from openapi_server.models.subscribed_node import SubscribedNode
from openapi_server.models.subscribed_node_list import SubscribedNodeList
from openapi_server.models.subscribed_upload_share import SubscribedUploadShare
from openapi_server.models.subscribed_upload_share_list import SubscribedUploadShareList
from openapi_server.models.totp_setup_response import TotpSetupResponse
from openapi_server.models.update_subscriptions_bulk_request import UpdateSubscriptionsBulkRequest
from openapi_server.models.update_user_account_request import UpdateUserAccountRequest
from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_key_pair_container import UserKeyPairContainer
from openapi_server.models.user_mfa_status_response import UserMfaStatusResponse


pytestmark = pytest.mark.asyncio

async def test_change_user_password(client):
    """Test case for change_user_password

    Change user's password
    """
    body = {"oldPassword":"oldPassword","newPassword":"newPassword"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/account/password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_totp_setup(client):
    """Test case for confirm_totp_setup

    Confirm second factor TOTP setup with a generated OTP
    """
    body = {"otp":"otp","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/account/mfa/totp',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_and_preserve_user_key_pair(client):
    """Test case for create_and_preserve_user_key_pair

    Create key pair and preserve copy of old private key
    """
    body = {"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"previousPrivateKey":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/account/keypairs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_mfa_totp_setup(client):
    """Test case for delete_mfa_totp_setup

    Disable a MFA TOTP setup with generated OTP
    """
    params = [('valid_otp', 'valid_otp_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/account/mfa/totp/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_customer_encryption(client):
    """Test case for enable_customer_encryption

    Activate client-side encryption for customer
    """
    body = {"enableCustomerEncryption":True,"dataSpaceRescueKey":{"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/account/customer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mfa_status_for_user(client):
    """Test case for get_mfa_status_for_user

    Request information about the user's mfa status
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account/mfa',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_totp_setup_information(client):
    """Test case for get_totp_setup_information

    Request information to setup TOTP as second authentication factor
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account/mfa/totp',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_download_share_subscriptions(client):
    """Test case for list_download_share_subscriptions

    List Download Share subscriptions
    """
    params = [('filter', 'filter_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/subscriptions/download_shares',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_node_subscriptions(client):
    """Test case for list_node_subscriptions

    List node subscriptions
    """
    params = [('filter', 'filter_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/subscriptions/nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_upload_share_subscriptions(client):
    """Test case for list_upload_share_subscriptions

    List Upload Share subscriptions
    """
    params = [('filter', 'filter_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/subscriptions/upload_shares',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    Invalidate authentication token
    """
    params = [('everywhere', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/logout',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ping_user(client):
    """Test case for ping_user

    (authenticated) Ping
    """
    headers = { 
        'Accept': 'text/plain',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_o_auth_approval(client):
    """Test case for remove_o_auth_approval

    Remove OAuth client approval
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/oauth/approvals/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_o_auth_authorization(client):
    """Test case for remove_o_auth_authorization

    Remove a OAuth authorization
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/oauth/authorizations/{client_id}/{authorization_id}'.format(client_id='client_id_example', authorization_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_o_auth_authorizations(client):
    """Test case for remove_o_auth_authorizations

    Remove all OAuth authorizations of a client
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/oauth/authorizations/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_profile_attribute(client):
    """Test case for remove_profile_attribute

    Remove user profile attribute
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/profileAttributes/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_key_pair(client):
    """Test case for remove_user_key_pair

    Remove user's key pair
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/account/keypair',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_avatar(client):
    """Test case for request_avatar

    Request avatar
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account/avatar',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_customer_info(client):
    """Test case for request_customer_info

    Request customer information for user
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account/customer',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_customer_key_pair(client):
    """Test case for request_customer_key_pair

    Request customer's key pair
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account/customer/keypair',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_list_of_notification_configs(client):
    """Test case for request_list_of_notification_configs

    Request list of notification configurations
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/notifications/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_o_auth_approvals(client):
    """Test case for request_o_auth_approvals

    Request list of OAuth client approvals
    """
    params = [('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/oauth/approvals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_o_auth_authorizations(client):
    """Test case for request_o_auth_authorizations

    Request list of OAuth client authorizations
    """
    params = [('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/oauth/authorizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_profile_attributes(client):
    """Test case for request_profile_attributes

    Request user profile attributes
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/profileAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_info(client):
    """Test case for request_user_info

    Request user account information
    """
    params = [('more_info', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_key_pair(client):
    """Test case for request_user_key_pair

    Request user's key pair
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account/keypair',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_key_pairs(client):
    """Test case for request_user_key_pairs

    Request all user key pairs
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/account/keypairs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_avatar(client):
    """Test case for reset_avatar

    Reset avatar
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/account/avatar',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_profile_attributes(client):
    """Test case for set_profile_attributes

    Set user profile attributes
    """
    body = {"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/profileAttributes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_user_key_pair(client):
    """Test case for set_user_key_pair

    Set user's key pair
    """
    body = {"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/account/keypair',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_download_share(client):
    """Test case for subscribe_download_share

    Subscribe Download Share for notifications
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/subscriptions/download_shares/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_download_shares(client):
    """Test case for subscribe_download_shares

    Subscribe or Unsubscribe a List of Download Shares for notifications
    """
    body = {"isSubscribed":True,"objectIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/subscriptions/download_shares',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_node(client):
    """Test case for subscribe_node

    Subscribe node for notifications
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/subscriptions/nodes/{node_id}'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_upload_share(client):
    """Test case for subscribe_upload_share

    Subscribe Upload Share for notifications
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/subscriptions/upload_shares/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe_upload_shares(client):
    """Test case for subscribe_upload_shares

    Subscribe or Unsubscribe a List of Upload Shares for notifications
    """
    body = {"isSubscribed":True,"objectIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/subscriptions/upload_shares',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_download_share(client):
    """Test case for unsubscribe_download_share

    Unsubscribe Download Share from notifications
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/subscriptions/download_shares/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_node(client):
    """Test case for unsubscribe_node

    Unsubscribe node from notifications
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/subscriptions/nodes/{node_id}'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe_upload_share(client):
    """Test case for unsubscribe_upload_share

    Unsubscribe Upload Share from notifications
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/subscriptions/upload_shares/{share_id}'.format(share_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_node_subscriptions(client):
    """Test case for update_node_subscriptions

    Subscribe or Unsubscribe a List of nodes for notifications
    """
    body = {"isSubscribed":True,"objectIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/subscriptions/nodes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_notification_config(client):
    """Test case for update_notification_config

    Update notification configuration
    """
    body = {"channelIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/notifications/config/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_profile_attributes(client):
    """Test case for update_profile_attributes

    Add or edit user profile attributes
    """
    body = {"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/profileAttributes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user_account(client):
    """Test case for update_user_account

    Update user account
    """
    body = {"firstName":"firstName","lastName":"lastName","gender":"n","phone":"phone","language":"language","acceptEULA":True,"login":"login","title":"title","userName":"userName","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/account',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_avatar_as_multipart(client):
    """Test case for upload_avatar_as_multipart

    Change avatar
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v4/user/account/avatar',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_use_emergency_code(client):
    """Test case for use_emergency_code

    Using emergency-code
    """
    params = [('emergency_code', 'emergency_code_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/user/account/mfa',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

