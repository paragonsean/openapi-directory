from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_call import ApiV2010AccountCall
from openapi_server.models.call_enum_status import CallEnumStatus
from openapi_server.models.call_enum_update_status import CallEnumUpdateStatus
from openapi_server.models.list_call_response import ListCallResponse
from openapi_server import util


async def create_call(request: web.Request, account_sid, _from, to, application_sid=None, async_amd=None, async_amd_status_callback=None, async_amd_status_callback_method=None, byoc=None, call_reason=None, call_token=None, caller_id=None, fallback_method=None, fallback_url=None, machine_detection=None, machine_detection_silence_timeout=None, machine_detection_speech_end_threshold=None, machine_detection_speech_threshold=None, machine_detection_timeout=None, method=None, record=None, recording_channels=None, recording_status_callback=None, recording_status_callback_event=None, recording_status_callback_method=None, recording_track=None, send_digits=None, sip_auth_password=None, sip_auth_username=None, status_callback=None, status_callback_event=None, status_callback_method=None, time_limit=None, timeout=None, trim=None, twiml=None, url=None) -> web.Response:
    """create_call

    Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client connections

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param _from: The phone number or client identifier to use as the caller id. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;From&#x60; must also be a phone number.
    :type _from: str
    :param to: The phone number, SIP address, or client identifier to call.
    :type to: str
    :param application_sid: The SID of the Application resource that will handle the call, if the call will be handled by an application.
    :type application_sid: str
    :param async_amd: Select whether to perform answering machine detection in the background. Default, blocks the execution of the call until Answering Machine Detection is completed. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type async_amd: str
    :param async_amd_status_callback: The URL that we should call using the &#x60;async_amd_status_callback_method&#x60; to notify customer application whether the call was answered by human, machine or fax.
    :type async_amd_status_callback: str
    :param async_amd_status_callback_method: The HTTP method we should use when calling the &#x60;async_amd_status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;.
    :type async_amd_status_callback_method: str
    :param byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that &#x60;byoc&#x60; is only meaningful when &#x60;to&#x60; is a phone number; it will otherwise be ignored. (Beta)
    :type byoc: str
    :param call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party&#39;s phone. (Branded Calls Beta)
    :type call_reason: str
    :param call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming call is received on a Twilio number. Pass an incoming call&#39;s call_token value to a forwarded call via the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the original incoming call.
    :type call_token: str
    :param caller_id: The phone number, SIP address, or Client identifier that made this call. Phone numbers are in [E.164 format](https://wwnw.twilio.com/docs/glossary/what-e164) (e.g., +16175551212). SIP addresses are formatted as &#x60;name@company.com&#x60;.
    :type caller_id: str
    :param fallback_method: The HTTP method that we should use to request the &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type fallback_method: str
    :param fallback_url: The URL that we call using the &#x60;fallback_method&#x60; if an error occurs when requesting or executing the TwiML at &#x60;url&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type fallback_url: str
    :param machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be: &#x60;Enable&#x60; or &#x60;DetectMessageEnd&#x60;. Use &#x60;Enable&#x60; if you would like us to return &#x60;AnsweredBy&#x60; as soon as the called party is identified. Use &#x60;DetectMessageEnd&#x60;, if you would like to leave a message on an answering machine. If &#x60;send_digits&#x60; is provided, this parameter is ignored. For more information, see [Answering Machine Detection](https://www.twilio.com/docs/voice/answering-machine-detection).
    :type machine_detection: str
    :param machine_detection_silence_timeout: The number of milliseconds of initial silence after which an &#x60;unknown&#x60; AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
    :type machine_detection_silence_timeout: int
    :param machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
    :type machine_detection_speech_end_threshold: int
    :param machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the length of the speech activity, where durations lower than this value will be interpreted as a human and longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
    :type machine_detection_speech_threshold: int
    :param machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with &#x60;AnsweredBy&#x60; of &#x60;unknown&#x60;. The default timeout is 30 seconds.
    :type machine_detection_timeout: int
    :param method: The HTTP method we should use when calling the &#x60;url&#x60; parameter&#39;s value. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type method: str
    :param record: Whether to record the call. Can be &#x60;true&#x60; to record the phone call, or &#x60;false&#x60; to not. The default is &#x60;false&#x60;. The &#x60;recording_url&#x60; is sent to the &#x60;status_callback&#x60; URL.
    :type record: bool
    :param recording_channels: The number of channels in the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60;. The default is &#x60;mono&#x60;. &#x60;mono&#x60; records both legs of the call in a single channel of the recording file. &#x60;dual&#x60; records each leg to a separate channel of the recording file. The first channel of a dual-channel recording contains the parent call and the second channel contains the child call.
    :type recording_channels: str
    :param recording_status_callback: The URL that we call when the recording is available to be accessed.
    :type recording_status_callback: str
    :param recording_status_callback_event: The recording status events that will trigger calls to the URL specified in &#x60;recording_status_callback&#x60;. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60; and &#x60;absent&#x60;. Defaults to &#x60;completed&#x60;. Separate  multiple values with a space.
    :type recording_status_callback_event: List[str]
    :param recording_status_callback_method: The HTTP method we should use when calling the &#x60;recording_status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;.
    :type recording_status_callback_method: str
    :param recording_track: The audio track to record for the call. Can be: &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. The default is &#x60;both&#x60;. &#x60;inbound&#x60; records the audio that is received by Twilio. &#x60;outbound&#x60; records the audio that is generated from Twilio. &#x60;both&#x60; records the audio that is received and generated by Twilio.
    :type recording_track: str
    :param send_digits: A string of keys to dial after connecting to the number, maximum of 32 digits. Valid digits in the string include: any digit (&#x60;0&#x60;-&#x60;9&#x60;), &#39;&#x60;#&#x60;&#39;, &#39;&#x60;*&#x60;&#39; and &#39;&#x60;w&#x60;&#39;, to insert a half second pause. For example, if you connected to a company phone number and wanted to pause for one second, and then dial extension 1234 followed by the pound key, the value of this parameter would be &#x60;ww1234#&#x60;. Remember to URL-encode this string, since the &#39;&#x60;#&#x60;&#39; character has special meaning in a URL. If both &#x60;SendDigits&#x60; and &#x60;MachineDetection&#x60; parameters are provided, then &#x60;MachineDetection&#x60; will be ignored.
    :type send_digits: str
    :param sip_auth_password: The password required to authenticate the user account specified in &#x60;sip_auth_username&#x60;.
    :type sip_auth_password: str
    :param sip_auth_username: The username used to authenticate the caller making a SIP call.
    :type sip_auth_username: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. If no &#x60;status_callback_event&#x60; is specified, we will send the &#x60;completed&#x60; status. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted).
    :type status_callback: str
    :param status_callback_event: The call progress events that we will send to the &#x60;status_callback&#x60; URL. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, and &#x60;completed&#x60;. If no event is specified, we send the &#x60;completed&#x60; status. If you want to receive multiple events, specify each one in a separate &#x60;status_callback_event&#x60; parameter. See the code sample for [monitoring call progress](https://www.twilio.com/docs/voice/api/call-resource?code-sample&#x3D;code-create-a-call-resource-and-specify-a-statuscallbackevent&amp;code-sdk-version&#x3D;json). If an &#x60;application_sid&#x60; is present, this parameter is ignored.
    :type status_callback_event: List[str]
    :param status_callback_method: The HTTP method we should use when calling the &#x60;status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type status_callback_method: str
    :param time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
    :type time_limit: int
    :param timeout: The integer number of seconds that we should allow the phone to ring before assuming there is no answer. The default is &#x60;60&#x60; seconds and the maximum is &#x60;600&#x60; seconds. For some call flows, we will add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as &#x60;15&#x60; seconds, to hang up before reaching an answering machine or voicemail.
    :type timeout: int
    :param trim: Whether to trim any leading and trailing silence from the recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and the default is &#x60;trim-silence&#x60;.
    :type trim: str
    :param twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both &#x60;twiml&#x60; and &#x60;url&#x60; are provided then &#x60;twiml&#x60; parameter will be ignored. Max 4000 characters.
    :type twiml: str
    :param url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the &#x60;method&#x60; when the call connects. For more information, see the [Url Parameter](https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter) section in [Making Calls](https://www.twilio.com/docs/voice/make-calls).
    :type url: str

    """
    return web.Response(status=200)


async def delete_call(request: web.Request, account_sid, sid) -> web.Response:
    """delete_call

    Delete a Call record from your account. Once the record is deleted, it will no longer appear in the API and Account Portal logs.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to delete.
    :type account_sid: str
    :param sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_call(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_call

    Fetch the call specified by the provided Call SID

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to fetch.
    :type account_sid: str
    :param sid: The SID of the Call resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_call(request: web.Request, account_sid, to=None, _from=None, parent_call_sid=None, status=None, start_time=None, start_time2=None, start_time3=None, end_time=None, end_time2=None, end_time3=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_call

    Retrieves a collection of calls made to and from your account

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to read.
    :type account_sid: str
    :param to: Only show calls made to this phone number, SIP address, Client identifier or SIM SID.
    :type to: str
    :param _from: Only include calls from this phone number, SIP address, Client identifier or SIM SID.
    :type _from: str
    :param parent_call_sid: Only include calls spawned by calls with this SID.
    :type parent_call_sid: str
    :param status: The status of the calls to include. Can be: &#x60;queued&#x60;, &#x60;ringing&#x60;, &#x60;in-progress&#x60;, &#x60;canceled&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, &#x60;busy&#x60;, or &#x60;no-answer&#x60;.
    :type status: str
    :param start_time: Only include calls that started on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that started on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that started on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that started on or after midnight of this date.
    :type start_time: str
    :param start_time2: Only include calls that started on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that started on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that started on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that started on or after midnight of this date.
    :type start_time2: str
    :param start_time3: Only include calls that started on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that started on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that started on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that started on or after midnight of this date.
    :type start_time3: str
    :param end_time: Only include calls that ended on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that ended on this date. You can also specify an inequality, such as &#x60;EndTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that ended on or before midnight of this date, and &#x60;EndTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that ended on or after midnight of this date.
    :type end_time: str
    :param end_time2: Only include calls that ended on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that ended on this date. You can also specify an inequality, such as &#x60;EndTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that ended on or before midnight of this date, and &#x60;EndTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that ended on or after midnight of this date.
    :type end_time2: str
    :param end_time3: Only include calls that ended on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that ended on this date. You can also specify an inequality, such as &#x60;EndTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that ended on or before midnight of this date, and &#x60;EndTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that ended on or after midnight of this date.
    :type end_time3: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    start_time = util.deserialize_datetime(start_time)
    start_time2 = util.deserialize_datetime(start_time2)
    start_time3 = util.deserialize_datetime(start_time3)
    end_time = util.deserialize_datetime(end_time)
    end_time2 = util.deserialize_datetime(end_time2)
    end_time3 = util.deserialize_datetime(end_time3)
    return web.Response(status=200)


async def update_call(request: web.Request, account_sid, sid, fallback_method=None, fallback_url=None, method=None, status=None, status_callback=None, status_callback_method=None, time_limit=None, twiml=None, url=None) -> web.Response:
    """update_call

    Initiates a call redirect or terminates a call

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Call resource to update
    :type sid: str
    :param fallback_method: The HTTP method that we should use to request the &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type fallback_method: str
    :param fallback_url: The URL that we call using the &#x60;fallback_method&#x60; if an error occurs when requesting or executing the TwiML at &#x60;url&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type fallback_url: str
    :param method: The HTTP method we should use when calling the &#x60;url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type method: str
    :param status: 
    :type status: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. If no &#x60;status_callback_event&#x60; is specified, we will send the &#x60;completed&#x60; status. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted).
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use when requesting the &#x60;status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored.
    :type status_callback_method: str
    :param time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
    :type time_limit: int
    :param twiml: TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url parameters are mutually exclusive
    :type twiml: str
    :param url: The absolute URL that returns the TwiML instructions for the call. We will call this URL using the &#x60;method&#x60; when the call connects. For more information, see the [Url Parameter](https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter) section in [Making Calls](https://www.twilio.com/docs/voice/make-calls).
    :type url: str

    """
    return web.Response(status=200)
