from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_create_recovery_request import AccountCreateRecoveryRequest
from openapi_server.models.account_create_verification_request import AccountCreateVerificationRequest
from openapi_server.models.account_update_email_request import AccountUpdateEmailRequest
from openapi_server.models.account_update_name_request import AccountUpdateNameRequest
from openapi_server.models.account_update_password_request import AccountUpdatePasswordRequest
from openapi_server.models.account_update_prefs_request import AccountUpdatePrefsRequest
from openapi_server.models.account_update_recovery_request import AccountUpdateRecoveryRequest
from openapi_server.models.account_update_verification_request import AccountUpdateVerificationRequest
from openapi_server.models.log_list import LogList
from openapi_server.models.session import Session
from openapi_server.models.session_list import SessionList
from openapi_server.models.token import Token
from openapi_server.models.user import User
from openapi_server import util


async def account_create_recovery(request: web.Request, body=None) -> web.Response:
    """Create Password Recovery

    Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](/docs/client/account#accountUpdateRecovery) endpoint to complete the process. The verification link sent to the user&#39;s email address is valid for 1 hour.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountCreateRecoveryRequest.from_dict(body)
    return web.Response(status=200)


async def account_create_verification(request: web.Request, body=None) -> web.Response:
    """Create Email Verification

    Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](/docs/client/account#accountUpdateVerification). The verification link sent to the user&#39;s email address is valid for 7 days.  Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface. 

    :param body: 
    :type body: dict | bytes

    """
    body = AccountCreateVerificationRequest.from_dict(body)
    return web.Response(status=200)


async def account_delete(request: web.Request, ) -> web.Response:
    """Delete Account

    Delete a currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. This is done to avoid deleted accounts being overtaken by new users with the same email address. Any user-related resources like documents or storage files should be deleted separately.


    """
    return web.Response(status=200)


async def account_delete_session(request: web.Request, session_id) -> web.Response:
    """Delete Account Session

    Use this endpoint to log out the currently logged in user from all their account sessions across all of their different devices. When using the option id argument, only the session unique ID provider will be deleted.

    :param session_id: Session unique ID. Use the string &#39;current&#39; to delete the current device session.
    :type session_id: str

    """
    return web.Response(status=200)


async def account_delete_sessions(request: web.Request, ) -> web.Response:
    """Delete All Account Sessions

    Delete all sessions from the user account and remove any sessions cookies from the end client.


    """
    return web.Response(status=200)


async def account_get(request: web.Request, ) -> web.Response:
    """Get Account

    Get currently logged in user data as JSON object.


    """
    return web.Response(status=200)


async def account_get_logs(request: web.Request, ) -> web.Response:
    """Get Account Logs

    Get currently logged in user list of latest security activity logs. Each log returns user IP address, location and date and time of log.


    """
    return web.Response(status=200)


async def account_get_prefs(request: web.Request, ) -> web.Response:
    """Get Account Preferences

    Get currently logged in user preferences as a key-value object.


    """
    return web.Response(status=200)


async def account_get_session(request: web.Request, session_id) -> web.Response:
    """Get Session By ID

    Use this endpoint to get a logged in user&#39;s session using a Session ID. Inputting &#39;current&#39; will return the current session being used.

    :param session_id: Session unique ID. Use the string &#39;current&#39; to get the current device session.
    :type session_id: str

    """
    return web.Response(status=200)


async def account_get_sessions(request: web.Request, ) -> web.Response:
    """Get Account Sessions

    Get currently logged in user list of active sessions across different devices.


    """
    return web.Response(status=200)


async def account_update_email(request: web.Request, body=None) -> web.Response:
    """Update Account Email

    Update currently logged in user account email address. After changing user address, user confirmation status is being reset and a new confirmation mail is sent. For security measures, user password is required to complete this request. This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdateEmailRequest.from_dict(body)
    return web.Response(status=200)


async def account_update_name(request: web.Request, body=None) -> web.Response:
    """Update Account Name

    Update currently logged in user account name.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdateNameRequest.from_dict(body)
    return web.Response(status=200)


async def account_update_password(request: web.Request, body=None) -> web.Response:
    """Update Account Password

    Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth and Team Invites, oldPassword is optional.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdatePasswordRequest.from_dict(body)
    return web.Response(status=200)


async def account_update_prefs(request: web.Request, body=None) -> web.Response:
    """Update Account Preferences

    Update currently logged in user account preferences. You can pass only the specific settings you wish to update.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdatePrefsRequest.from_dict(body)
    return web.Response(status=200)


async def account_update_recovery(request: web.Request, body=None) -> web.Response:
    """Complete Password Recovery

    Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](/docs/client/account#accountCreateRecovery) endpoint.  Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdateRecoveryRequest.from_dict(body)
    return web.Response(status=200)


async def account_update_verification(request: web.Request, body=None) -> web.Response:
    """Complete Email Verification

    Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdateVerificationRequest.from_dict(body)
    return web.Response(status=200)
