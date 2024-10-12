from typing import List, Dict
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
from openapi_server import util


async def identitytoolkit_relyingparty_create_auth_uri(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_create_auth_uri

    Creates the URI used by the IdP to authenticate the user.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyCreateAuthUriRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_delete_account(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_delete_account

    Delete user account.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyDeleteAccountRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_download_account(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_download_account

    Batch download user accounts.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyDownloadAccountRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_email_link_signin(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_email_link_signin

    Reset password for a user.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyEmailLinkSigninRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_get_account_info(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_get_account_info

    Returns the account info.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyGetAccountInfoRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_get_oob_confirmation_code(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_get_oob_confirmation_code

    Get a code for user action confirmation.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Relyingparty.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_get_project_config(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, delegated_project_number=None, project_number=None) -> web.Response:
    """identitytoolkit_relyingparty_get_project_config

    Get project configuration.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param delegated_project_number: Delegated GCP project number of the request.
    :type delegated_project_number: str
    :param project_number: GCP project number of the request.
    :type project_number: str

    """
    return web.Response(status=200)


async def identitytoolkit_relyingparty_get_public_keys(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """identitytoolkit_relyingparty_get_public_keys

    Get token signing public key.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def identitytoolkit_relyingparty_get_recaptcha_param(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """identitytoolkit_relyingparty_get_recaptcha_param

    Get recaptcha secure param.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def identitytoolkit_relyingparty_reset_password(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_reset_password

    Reset password for a user.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyResetPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_send_verification_code(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_send_verification_code

    Send SMS verification code.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartySendVerificationCodeRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_set_account_info(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_set_account_info

    Set account info for a user.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartySetAccountInfoRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_set_project_config(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_set_project_config

    Set project configuration.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartySetProjectConfigRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_sign_out_user(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_sign_out_user

    Sign out user.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartySignOutUserRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_signup_new_user(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_signup_new_user

    Signup new user.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartySignupNewUserRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_upload_account(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_upload_account

    Batch upload existing user accounts.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyUploadAccountRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_verify_assertion(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_verify_assertion

    Verifies the assertion returned by the IdP.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyVerifyAssertionRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_verify_custom_token(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_verify_custom_token

    Verifies the developer asserted ID token.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyVerifyCustomTokenRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_verify_password(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_verify_password

    Verifies the user entered password.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyVerifyPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def identitytoolkit_relyingparty_verify_phone_number(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """identitytoolkit_relyingparty_verify_phone_number

    Verifies ownership of a phone number and creates/updates the user account accordingly.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest.from_dict(body)
    return web.Response(status=200)
