from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.verify_v2_service import VerifyV2Service
from openapi_server import util


async def create_service(request: web.Request, friendly_name, code_length=None, custom_code_enabled=None, default_template_sid=None, do_not_share_warning_enabled=None, dtmf_input_required=None, lookup_enabled=None, psd2_enabled=None, push_apn_credential_sid=None, push_fcm_credential_sid=None, push_include_date=None, skip_sms_to_landlines=None, totp_code_length=None, totp_issuer=None, totp_skew=None, totp_time_step=None, tts_name=None, verify_event_subscription_enabled=None) -> web.Response:
    """create_service

    Create a new Verification Service.

    :param friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**
    :type friendly_name: str
    :param code_length: The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
    :type code_length: int
    :param custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
    :type custom_code_enabled: bool
    :param default_template_sid: The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
    :type default_template_sid: str
    :param do_not_share_warning_enabled: Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: &#x60;Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code&#x60;
    :type do_not_share_warning_enabled: bool
    :param dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call.
    :type dtmf_input_required: bool
    :param lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone number.
    :type lookup_enabled: bool
    :param psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
    :type psd2_enabled: bool
    :param push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    :type push_apn_credential_sid: str
    :param push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    :type push_fcm_credential_sid: str
    :param push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge&#39;s response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the one found in &#x60;date_created&#x60;, please use that one instead.
    :type push_include_date: bool
    :param skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires &#x60;lookup_enabled&#x60;.
    :type skip_sms_to_landlines: bool
    :param totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
    :type totp_code_length: int
    :param totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
    :type totp_issuer: str
    :param totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
    :type totp_skew: int
    :param totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
    :type totp_time_step: int
    :param tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
    :type tts_name: str
    :param verify_event_subscription_enabled: Whether to allow verifications from the service to reach the stream-events sinks if configured
    :type verify_event_subscription_enabled: bool

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    Delete a specific Verification Service Instance.

    :param sid: The Twilio-provided string that uniquely identifies the Verification Service resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    Fetch specific Verification Service Instance.

    :param sid: The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    Retrieve a list of all Verification Services for an account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, sid, code_length=None, custom_code_enabled=None, default_template_sid=None, do_not_share_warning_enabled=None, dtmf_input_required=None, friendly_name=None, lookup_enabled=None, psd2_enabled=None, push_apn_credential_sid=None, push_fcm_credential_sid=None, push_include_date=None, skip_sms_to_landlines=None, totp_code_length=None, totp_issuer=None, totp_skew=None, totp_time_step=None, tts_name=None, verify_event_subscription_enabled=None) -> web.Response:
    """update_service

    Update a specific Verification Service.

    :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
    :type sid: str
    :param code_length: The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
    :type code_length: int
    :param custom_code_enabled: Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
    :type custom_code_enabled: bool
    :param default_template_sid: The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
    :type default_template_sid: str
    :param do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.**
    :type do_not_share_warning_enabled: bool
    :param dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call.
    :type dtmf_input_required: bool
    :param friendly_name: A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**
    :type friendly_name: str
    :param lookup_enabled: Whether to perform a lookup with each verification started and return info about the phone number.
    :type lookup_enabled: bool
    :param psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification.
    :type psd2_enabled: bool
    :param push_apn_credential_sid: Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    :type push_apn_credential_sid: str
    :param push_fcm_credential_sid: Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    :type push_fcm_credential_sid: str
    :param push_include_date: Optional configuration for the Push factors. If true, include the date in the Challenge&#39;s response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter.
    :type push_include_date: bool
    :param skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines. Requires &#x60;lookup_enabled&#x60;.
    :type skip_sms_to_landlines: bool
    :param totp_code_length: Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
    :type totp_code_length: int
    :param totp_issuer: Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI.
    :type totp_issuer: str
    :param totp_skew: Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
    :type totp_skew: int
    :param totp_time_step: Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
    :type totp_time_step: int
    :param tts_name: The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
    :type tts_name: str
    :param verify_event_subscription_enabled: Whether to allow verifications from the service to reach the stream-events sinks if configured
    :type verify_event_subscription_enabled: bool

    """
    return web.Response(status=200)
