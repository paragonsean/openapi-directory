# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_auth_uri_response import CreateAuthUriResponse
from openapi_server.models.delete_account_response import DeleteAccountResponse
from openapi_server.models.download_account_response import DownloadAccountResponse
from openapi_server.models.email_link_signin_response import EmailLinkSigninResponse
from openapi_server.models.get_account_info_response import GetAccountInfoResponse
from openapi_server.models.get_oob_confirmation_code_response import GetOobConfirmationCodeResponse
from openapi_server.models.get_recaptcha_param_response import GetRecaptchaParamResponse
from openapi_server.models.identitytoolkit_relyingparty_create_auth_uri_request import IdentitytoolkitRelyingpartyCreateAuthUriRequest
from openapi_server.models.identitytoolkit_relyingparty_delete_account_request import IdentitytoolkitRelyingpartyDeleteAccountRequest
from openapi_server.models.identitytoolkit_relyingparty_download_account_request import IdentitytoolkitRelyingpartyDownloadAccountRequest
from openapi_server.models.identitytoolkit_relyingparty_email_link_signin_request import IdentitytoolkitRelyingpartyEmailLinkSigninRequest
from openapi_server.models.identitytoolkit_relyingparty_get_account_info_request import IdentitytoolkitRelyingpartyGetAccountInfoRequest
from openapi_server.models.identitytoolkit_relyingparty_get_project_config_response import IdentitytoolkitRelyingpartyGetProjectConfigResponse
from openapi_server.models.identitytoolkit_relyingparty_reset_password_request import IdentitytoolkitRelyingpartyResetPasswordRequest
from openapi_server.models.identitytoolkit_relyingparty_send_verification_code_request import IdentitytoolkitRelyingpartySendVerificationCodeRequest
from openapi_server.models.identitytoolkit_relyingparty_send_verification_code_response import IdentitytoolkitRelyingpartySendVerificationCodeResponse
from openapi_server.models.identitytoolkit_relyingparty_set_account_info_request import IdentitytoolkitRelyingpartySetAccountInfoRequest
from openapi_server.models.identitytoolkit_relyingparty_set_project_config_request import IdentitytoolkitRelyingpartySetProjectConfigRequest
from openapi_server.models.identitytoolkit_relyingparty_set_project_config_response import IdentitytoolkitRelyingpartySetProjectConfigResponse
from openapi_server.models.identitytoolkit_relyingparty_sign_out_user_request import IdentitytoolkitRelyingpartySignOutUserRequest
from openapi_server.models.identitytoolkit_relyingparty_sign_out_user_response import IdentitytoolkitRelyingpartySignOutUserResponse
from openapi_server.models.identitytoolkit_relyingparty_signup_new_user_request import IdentitytoolkitRelyingpartySignupNewUserRequest
from openapi_server.models.identitytoolkit_relyingparty_upload_account_request import IdentitytoolkitRelyingpartyUploadAccountRequest
from openapi_server.models.identitytoolkit_relyingparty_verify_assertion_request import IdentitytoolkitRelyingpartyVerifyAssertionRequest
from openapi_server.models.identitytoolkit_relyingparty_verify_custom_token_request import IdentitytoolkitRelyingpartyVerifyCustomTokenRequest
from openapi_server.models.identitytoolkit_relyingparty_verify_password_request import IdentitytoolkitRelyingpartyVerifyPasswordRequest
from openapi_server.models.identitytoolkit_relyingparty_verify_phone_number_request import IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest
from openapi_server.models.identitytoolkit_relyingparty_verify_phone_number_response import IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse
from openapi_server.models.relyingparty import Relyingparty
from openapi_server.models.reset_password_response import ResetPasswordResponse
from openapi_server.models.set_account_info_response import SetAccountInfoResponse
from openapi_server.models.signup_new_user_response import SignupNewUserResponse
from openapi_server.models.upload_account_response import UploadAccountResponse
from openapi_server.models.verify_assertion_response import VerifyAssertionResponse
from openapi_server.models.verify_custom_token_response import VerifyCustomTokenResponse
from openapi_server.models.verify_password_response import VerifyPasswordResponse


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_create_auth_uri(client):
    """Test case for identitytoolkit_relyingparty_create_auth_uri

    
    """
    body = {"identifier":"identifier","clientId":"clientId","oauthScope":"oauthScope","tenantProjectNumber":"tenantProjectNumber","customParameter":{"key":"customParameter"},"authFlowType":"authFlowType","sessionId":"sessionId","providerId":"providerId","appId":"appId","context":"context","hostedDomain":"hostedDomain","tenantId":"tenantId","continueUri":"continueUri","oauthConsumerKey":"oauthConsumerKey","openidRealm":"openidRealm","otaApp":"otaApp"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/createAuthUri',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_delete_account(client):
    """Test case for identitytoolkit_relyingparty_delete_account

    
    """
    body = {"delegatedProjectNumber":"delegatedProjectNumber","idToken":"idToken","localId":"localId"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/deleteAccount',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_download_account(client):
    """Test case for identitytoolkit_relyingparty_download_account

    
    """
    body = {"maxResults":0,"nextPageToken":"nextPageToken","targetProjectId":"targetProjectId","delegatedProjectNumber":"delegatedProjectNumber"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/downloadAccount',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_email_link_signin(client):
    """Test case for identitytoolkit_relyingparty_email_link_signin

    
    """
    body = {"idToken":"idToken","oobCode":"oobCode","email":"email"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/emailLinkSignin',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_get_account_info(client):
    """Test case for identitytoolkit_relyingparty_get_account_info

    
    """
    body = {"phoneNumber":["phoneNumber","phoneNumber"],"delegatedProjectNumber":"delegatedProjectNumber","idToken":"idToken","localId":["localId","localId"],"email":["email","email"]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/getAccountInfo',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_get_oob_confirmation_code(client):
    """Test case for identitytoolkit_relyingparty_get_oob_confirmation_code

    
    """
    body = {"requestType":"requestType","kind":"identitytoolkit#relyingparty","iOSAppStoreId":"iOSAppStoreId","canHandleCodeInApp":True,"continueUrl":"continueUrl","androidInstallApp":True,"androidPackageName":"androidPackageName","captchaResp":"captchaResp","idToken":"idToken","challenge":"challenge","userIp":"userIp","newEmail":"newEmail","iOSBundleId":"iOSBundleId","androidMinimumVersion":"androidMinimumVersion","email":"email"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/getOobConfirmationCode',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_get_project_config(client):
    """Test case for identitytoolkit_relyingparty_get_project_config

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('delegatedProjectNumber', 'delegated_project_number_example'),
                    ('projectNumber', 'project_number_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/identitytoolkit/v3/relyingparty/getProjectConfig',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_get_public_keys(client):
    """Test case for identitytoolkit_relyingparty_get_public_keys

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/identitytoolkit/v3/relyingparty/publicKeys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_get_recaptcha_param(client):
    """Test case for identitytoolkit_relyingparty_get_recaptcha_param

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/identitytoolkit/v3/relyingparty/getRecaptchaParam',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_reset_password(client):
    """Test case for identitytoolkit_relyingparty_reset_password

    
    """
    body = {"oldPassword":"oldPassword","newPassword":"newPassword","oobCode":"oobCode","email":"email"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/resetPassword',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_send_verification_code(client):
    """Test case for identitytoolkit_relyingparty_send_verification_code

    
    """
    body = {"phoneNumber":"phoneNumber","iosReceipt":"iosReceipt","recaptchaToken":"recaptchaToken","iosSecret":"iosSecret"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/sendVerificationCode',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_set_account_info(client):
    """Test case for identitytoolkit_relyingparty_set_account_info

    
    """
    body = {"captchaResponse":"captchaResponse","validSince":"validSince","captchaChallenge":"captchaChallenge","displayName":"displayName","upgradeToFederatedLogin":True,"localId":"localId","oobCode":"oobCode","returnSecureToken":True,"createdAt":"createdAt","emailVerified":True,"photoUrl":"photoUrl","password":"password","instanceId":"instanceId","lastLoginAt":"lastLoginAt","phoneNumber":"phoneNumber","provider":["provider","provider"],"deleteAttribute":["deleteAttribute","deleteAttribute"],"delegatedProjectNumber":"delegatedProjectNumber","idToken":"idToken","disableUser":True,"deleteProvider":["deleteProvider","deleteProvider"],"email":"email","customAttributes":"customAttributes"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/setAccountInfo',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_set_project_config(client):
    """Test case for identitytoolkit_relyingparty_set_project_config

    
    """
    body = {"legacyResetPasswordTemplate":{"subject":"subject","format":"format","replyTo":"replyTo","from":"from","fromDisplayName":"fromDisplayName","body":"body"},"idpConfig":[{"clientId":"clientId","provider":"provider","whitelistedAudiences":["whitelistedAudiences","whitelistedAudiences"],"secret":"secret","experimentPercent":0,"enabled":True},{"clientId":"clientId","provider":"provider","whitelistedAudiences":["whitelistedAudiences","whitelistedAudiences"],"secret":"secret","experimentPercent":0,"enabled":True}],"apiKey":"apiKey","resetPasswordTemplate":{"subject":"subject","format":"format","replyTo":"replyTo","from":"from","fromDisplayName":"fromDisplayName","body":"body"},"delegatedProjectNumber":"delegatedProjectNumber","useEmailSending":True,"enableAnonymousUser":True,"allowPasswordUser":True,"verifyEmailTemplate":{"subject":"subject","format":"format","replyTo":"replyTo","from":"from","fromDisplayName":"fromDisplayName","body":"body"},"authorizedDomains":["authorizedDomains","authorizedDomains"],"changeEmailTemplate":{"subject":"subject","format":"format","replyTo":"replyTo","from":"from","fromDisplayName":"fromDisplayName","body":"body"}}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/setProjectConfig',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_sign_out_user(client):
    """Test case for identitytoolkit_relyingparty_sign_out_user

    
    """
    body = {"instanceId":"instanceId","localId":"localId"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/signOutUser',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_signup_new_user(client):
    """Test case for identitytoolkit_relyingparty_signup_new_user

    
    """
    body = {"captchaResponse":"captchaResponse","captchaChallenge":"captchaChallenge","displayName":"displayName","tenantProjectNumber":"tenantProjectNumber","localId":"localId","emailVerified":True,"photoUrl":"photoUrl","password":"password","instanceId":"instanceId","phoneNumber":"phoneNumber","idToken":"idToken","tenantId":"tenantId","disabled":True,"email":"email"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/signupNewUser',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_upload_account(client):
    """Test case for identitytoolkit_relyingparty_upload_account

    
    """
    body = {"cpuMemCost":6,"signerKey":"signerKey","memoryCost":5,"saltSeparator":"saltSeparator","targetProjectId":"targetProjectId","parallelization":5,"blockSize":0,"users":[{"salt":"salt","validSince":"validSince","providerUserInfo":[{"photoUrl":"photoUrl","phoneNumber":"phoneNumber","displayName":"displayName","federatedId":"federatedId","providerId":"providerId","rawId":"rawId","screenName":"screenName","email":"email"},{"photoUrl":"photoUrl","phoneNumber":"phoneNumber","displayName":"displayName","federatedId":"federatedId","providerId":"providerId","rawId":"rawId","screenName":"screenName","email":"email"}],"displayName":"displayName","customAuth":True,"screenName":"screenName","localId":"localId","version":6,"passwordHash":"passwordHash","createdAt":"createdAt","emailVerified":True,"passwordUpdatedAt":0.8008281904610115,"photoUrl":"photoUrl","lastLoginAt":"lastLoginAt","phoneNumber":"phoneNumber","disabled":True,"rawPassword":"rawPassword","email":"email","customAttributes":"customAttributes"},{"salt":"salt","validSince":"validSince","providerUserInfo":[{"photoUrl":"photoUrl","phoneNumber":"phoneNumber","displayName":"displayName","federatedId":"federatedId","providerId":"providerId","rawId":"rawId","screenName":"screenName","email":"email"},{"photoUrl":"photoUrl","phoneNumber":"phoneNumber","displayName":"displayName","federatedId":"federatedId","providerId":"providerId","rawId":"rawId","screenName":"screenName","email":"email"}],"displayName":"displayName","customAuth":True,"screenName":"screenName","localId":"localId","version":6,"passwordHash":"passwordHash","createdAt":"createdAt","emailVerified":True,"passwordUpdatedAt":0.8008281904610115,"photoUrl":"photoUrl","lastLoginAt":"lastLoginAt","phoneNumber":"phoneNumber","disabled":True,"rawPassword":"rawPassword","email":"email","customAttributes":"customAttributes"}],"delegatedProjectNumber":"delegatedProjectNumber","allowOverwrite":True,"sanityCheck":True,"dkLen":1,"hashAlgorithm":"hashAlgorithm","rounds":2}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/uploadAccount',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_verify_assertion(client):
    """Test case for identitytoolkit_relyingparty_verify_assertion

    
    """
    body = {"pendingIdToken":"pendingIdToken","returnIdpCredential":True,"tenantProjectNumber":"tenantProjectNumber","autoCreate":True,"requestUri":"requestUri","sessionId":"sessionId","returnSecureToken":True,"instanceId":"instanceId","postBody":"postBody","delegatedProjectNumber":"delegatedProjectNumber","returnRefreshToken":True,"idToken":"idToken","tenantId":"tenantId"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/verifyAssertion',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_verify_custom_token(client):
    """Test case for identitytoolkit_relyingparty_verify_custom_token

    
    """
    body = {"instanceId":"instanceId","delegatedProjectNumber":"delegatedProjectNumber","returnSecureToken":True,"token":"token"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/verifyCustomToken',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_verify_password(client):
    """Test case for identitytoolkit_relyingparty_verify_password

    
    """
    body = {"captchaResponse":"captchaResponse","password":"password","instanceId":"instanceId","pendingIdToken":"pendingIdToken","captchaChallenge":"captchaChallenge","delegatedProjectNumber":"delegatedProjectNumber","idToken":"idToken","tenantId":"tenantId","tenantProjectNumber":"tenantProjectNumber","email":"email","returnSecureToken":True}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/verifyPassword',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_relyingparty_verify_phone_number(client):
    """Test case for identitytoolkit_relyingparty_verify_phone_number

    
    """
    body = {"sessionInfo":"sessionInfo","temporaryProof":"temporaryProof","code":"code","phoneNumber":"phoneNumber","verificationProof":"verificationProof","idToken":"idToken","operation":"operation"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/identitytoolkit/v3/relyingparty/verifyPhoneNumber',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

