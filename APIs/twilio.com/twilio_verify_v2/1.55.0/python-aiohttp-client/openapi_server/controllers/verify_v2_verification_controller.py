from typing import List, Dict
from aiohttp import web

from openapi_server.models.verification_enum_risk_check import VerificationEnumRiskCheck
from openapi_server.models.verification_enum_status import VerificationEnumStatus
from openapi_server.models.verify_v2_service_verification import VerifyV2ServiceVerification
from openapi_server import util


async def create_verification(request: web.Request, service_sid, channel, to, amount=None, app_hash=None, channel_configuration=None, custom_code=None, custom_friendly_name=None, custom_message=None, device_ip=None, locale=None, payee=None, rate_limits=None, risk_check=None, send_digits=None, tags=None, template_custom_substitutions=None, template_sid=None) -> web.Response:
    """create_verification

    Create a new Verification using a Service

    :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.
    :type service_sid: str
    :param channel: The verification method to use. One of: [&#x60;email&#x60;](https://www.twilio.com/docs/verify/email), &#x60;sms&#x60;, &#x60;whatsapp&#x60;, &#x60;call&#x60;, &#x60;sna&#x60; or &#x60;auto&#x60;.
    :type channel: str
    :param to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    :type to: str
    :param amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :type amount: str
    :param app_hash: Your [App Hash](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string) to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: &#x60;&lt;#&gt; Your AppName verification code is: 1234 He42w354ol9&#x60;.
    :type app_hash: str
    :param channel_configuration: [&#x60;email&#x60;](https://www.twilio.com/docs/verify/email) channel configuration in json format. The fields &#39;from&#39; and &#39;from_name&#39; are optional but if included the &#39;from&#39; field must have a valid email address.
    :type channel_configuration: dict | bytes
    :param custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive.
    :type custom_code: str
    :param custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the verification message
    :type custom_friendly_name: str
    :param custom_message: The text of a custom message to use for the verification.
    :type custom_message: str
    :param device_ip: Strongly encouraged if using the auto channel. The IP address of the client&#39;s device. If provided, it has to be a valid IPv4 or IPv6 address.
    :type device_ip: str
    :param locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](https://www.twilio.com/docs/verify/supported-languages).
    :type locale: str
    :param payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :type payee: str
    :param rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to &#x60;unique_name&#x60; fields defined when [creating your Rate Limit](https://www.twilio.com/docs/verify/api/service-rate-limits). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request.
    :type rate_limits: dict | bytes
    :param risk_check: 
    :type risk_check: str
    :param send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits).
    :type send_digits: str
    :param tags: A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message. The object may contain up to 10 tags. Keys and values can each be up to 128 characters in length.
    :type tags: str
    :param template_custom_substitutions: A stringified JSON object in which the keys are the template&#39;s special variables and the values are the variables substitutions.
    :type template_custom_substitutions: str
    :param template_sid: The message [template](https://www.twilio.com/docs/verify/api/templates). If provided, will override the default template for the Service. SMS and Voice channels only.
    :type template_sid: str

    """
    channel_configuration = object.from_dict(channel_configuration)
    rate_limits = object.from_dict(rate_limits)
    return web.Response(status=200)


async def fetch_verification(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_verification

    Fetch a specific Verification

    :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to fetch the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Verification resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def update_verification(request: web.Request, service_sid, sid, status) -> web.Response:
    """update_verification

    Update a Verification status

    :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to update the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
