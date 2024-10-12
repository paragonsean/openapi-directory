from typing import List, Dict
from aiohttp import web

from openapi_server.models.local_user_account_lockout_config import LocalUserAccountLockoutConfig
from openapi_server.models.local_user_account_lockout_status import LocalUserAccountLockoutStatus
from openapi_server.models.totp_config_update_request import TotpConfigUpdateRequest
from openapi_server.models.totp_secret import TotpSecret
from openapi_server.models.totp_status import TotpStatus
from openapi_server import util


async def generate_totp_secret(request: web.Request, id) -> web.Response:
    """Generate a TOTP secret key for the given user

    Use this endpoint to generate the time-based one time password (TOTP) secret key for a specified user account. The secret is a key value encoded in Base32 and includes a URI for generating a scannable QR code. 

    :param id: The user account object ID.
    :type id: str

    """
    return web.Response(status=200)


async def get_totp_status(request: web.Request, id) -> web.Response:
    """Get the TOTP status for the given user

    Get the time-based one time password (TOTP) status for a specified user account. The TOTP status specifies whether that account has TOTP enabled and whether TOTP is being enforced for that account. 

    :param id: The user account object ID.
    :type id: str

    """
    return web.Response(status=200)


async def get_user_account_lockout_settings(request: web.Request, ) -> web.Response:
    """Get the local user account lockout settings

    Get the local user account lockout settings which are used to configure whether user accounts will be locked on failed logins, when they will be locked and the duration for which they will stay locked. 


    """
    return web.Response(status=200)


async def manage_user_account_lockout_settings(request: web.Request, body) -> web.Response:
    """Update the local user account lockout settings

    Update the local user account lockout settings which are used to configure whether user accounts will be locked on failed logins, when they will be locked and the duration for which they will stay locked. 

    :param body: Update the local user account lockout settings.
    :type body: dict | bytes

    """
    body = LocalUserAccountLockoutConfig.from_dict(body)
    return web.Response(status=200)


async def reset_totp(request: web.Request, id) -> web.Response:
    """Reset the TOTP for the given user

    Reset the TOTP settings to the default disabled state for the specified user account. 

    :param id: The user account object ID.
    :type id: str

    """
    return web.Response(status=200)


async def setup_totp(request: web.Request, id, body) -> web.Response:
    """Configure the TOTP secret for the given user

    Use this endpoint to configure the time-based one time password (TOTP) secret for a specified user account. The endpoint replaces an existing secret with the new one. The Rubrik cluster checks the secret against a one time password (OTP) to ensure validity. 

    :param id: The user account object ID.
    :type id: str
    :param body: The time-based one time password (TOTP) configuration.
    :type body: dict | bytes

    """
    body = TotpConfigUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def unlock_user(request: web.Request, id) -> web.Response:
    """Unlock a user account

    Unlock a user account that has been locked because of too many failed login attempts.

    :param id: The ID of the user account that has been locked.
    :type id: str

    """
    return web.Response(status=200)
