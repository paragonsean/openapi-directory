from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_create_recovery_request import AccountCreateRecoveryRequest
from openapi_server.models.account_create_request import AccountCreateRequest
from openapi_server.models.account_create_verification_request import AccountCreateVerificationRequest
from openapi_server.models.account_update_email_request import AccountUpdateEmailRequest
from openapi_server.models.account_update_name_request import AccountUpdateNameRequest
from openapi_server.models.account_update_password_request import AccountUpdatePasswordRequest
from openapi_server.models.account_update_prefs_request import AccountUpdatePrefsRequest
from openapi_server.models.account_update_recovery_request import AccountUpdateRecoveryRequest
from openapi_server.models.account_update_verification_request import AccountUpdateVerificationRequest
from openapi_server.models.jwt import Jwt
from openapi_server.models.log_list import LogList
from openapi_server.models.session import Session
from openapi_server.models.session_list import SessionList
from openapi_server.models.token import Token
from openapi_server.models.user import User
from openapi_server import util


async def account_create(request: web.Request, body=None) -> web.Response:
    """Create Account

    Use this endpoint to allow a new user to register a new account in your project. After the user registration completes successfully, you can use the [/account/verfication](/docs/client/account#accountCreateVerification) route to start verifying the user email address. To allow the new user to login to their new account, you need to create a new [account session](/docs/client/account#accountCreateSession).

    :param body: 
    :type body: dict | bytes

    """
    body = AccountCreateRequest.from_dict(body)
    return web.Response(status=200)


async def account_create_anonymous_session(request: web.Request, ) -> web.Response:
    """Create Anonymous Session

    Use this endpoint to allow a new user to register an anonymous account in your project. This route will also create a new session for the user. To allow the new user to convert an anonymous account to a normal account, you need to update its [email and password](/docs/client/account#accountUpdateEmail) or create an [OAuth2 session](/docs/client/account#accountCreateOAuth2Session).


    """
    return web.Response(status=200)


async def account_create_jwt(request: web.Request, ) -> web.Response:
    """Create Account JWT

    Use this endpoint to create a JSON Web Token. You can use the resulting JWT to authenticate on behalf of the current user when working with the Appwrite server-side API and SDKs. The JWT secret is valid for 15 minutes from its creation and will be invalid if the user will logout in that time frame.


    """
    return web.Response(status=200)


async def account_create_o_auth2_session(request: web.Request, provider, success=None, failure=None, scopes=None) -> web.Response:
    """Create Account Session with OAuth2

    Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2 provider should be enabled from the Appwrite console first. Use the success and failure arguments to provide a redirect URL&#39;s back to your app when login is completed.  If there is already an active session, the new session will be attached to the logged-in account. If there are no active sessions, the server will attempt to look for a user with the same email address as the email received from the OAuth2 provider and attach the new session to the existing user. If no matching user is found - the server will create a new user.. 

    :param provider: OAuth2 Provider. Currently, supported providers are: amazon, apple, bitbucket, bitly, box, discord, dropbox, facebook, github, gitlab, google, linkedin, microsoft, paypal, paypalSandbox, salesforce, slack, spotify, tradeshift, tradeshiftBox, twitch, vk, yahoo, yandex, wordpress.
    :type provider: str
    :param success: URL to redirect back to your app after a successful login attempt.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    :type success: str
    :param failure: URL to redirect back to your app after a failed login attempt.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    :type failure: str
    :param scopes: A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes.
    :type scopes: List[str]

    """
    return web.Response(status=200)


async def account_create_recovery(request: web.Request, body=None) -> web.Response:
    """Create Password Recovery

    Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](/docs/client/account#accountUpdateRecovery) endpoint to complete the process. The verification link sent to the user&#39;s email address is valid for 1 hour.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountCreateRecoveryRequest.from_dict(body)
    return web.Response(status=200)


async def account_create_session(request: web.Request, body=None) -> web.Response:
    """Create Account Session

    Allow the user to login into their account by providing a valid email and password combination. This route will create a new session for the user.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdateEmailRequest.from_dict(body)
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
