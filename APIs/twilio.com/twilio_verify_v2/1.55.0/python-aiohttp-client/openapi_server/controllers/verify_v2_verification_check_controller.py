from typing import List, Dict
from aiohttp import web

from openapi_server.models.verify_v2_service_verification_check import VerifyV2ServiceVerificationCheck
from openapi_server import util


async def create_verification_check(request: web.Request, service_sid, amount=None, code=None, payee=None, to=None, verification_sid=None) -> web.Response:
    """create_verification_check

    challenge a specific Verification Check.

    :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.
    :type service_sid: str
    :param amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :type amount: str
    :param code: The 4-10 character string being verified.
    :type code: str
    :param payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :type payee: str
    :param to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the &#x60;verification_sid&#x60; must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    :type to: str
    :param verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the &#x60;to&#x60; phone number/[email](https://www.twilio.com/docs/verify/email) must be specified.
    :type verification_sid: str

    """
    return web.Response(status=200)
