from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_conference_participant import ApiV2010AccountConferenceParticipant
from openapi_server.models.list_participant_response import ListParticipantResponse
from openapi_server import util


async def create_participant(request: web.Request, account_sid, conference_sid, _from, to, amd_status_callback=None, amd_status_callback_method=None, beep=None, byoc=None, call_reason=None, call_sid_to_coach=None, call_token=None, caller_id=None, coaching=None, conference_record=None, conference_recording_status_callback=None, conference_recording_status_callback_event=None, conference_recording_status_callback_method=None, conference_status_callback=None, conference_status_callback_event=None, conference_status_callback_method=None, conference_trim=None, early_media=None, end_conference_on_exit=None, jitter_buffer_size=None, label=None, machine_detection=None, machine_detection_silence_timeout=None, machine_detection_speech_end_threshold=None, machine_detection_speech_threshold=None, machine_detection_timeout=None, max_participants=None, muted=None, record=None, recording_channels=None, recording_status_callback=None, recording_status_callback_event=None, recording_status_callback_method=None, recording_track=None, region=None, sip_auth_password=None, sip_auth_username=None, start_conference_on_enter=None, status_callback=None, status_callback_event=None, status_callback_method=None, time_limit=None, timeout=None, trim=None, wait_method=None, wait_url=None) -> web.Response:
    """create_participant

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param conference_sid: The SID of the participant&#39;s conference.
    :type conference_sid: str
    :param _from: The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted &#x60;client:name&#x60;. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;from&#x60; must also be a phone number. If &#x60;to&#x60; is sip address, this value of &#x60;from&#x60; should be a username portion to be used to populate the P-Asserted-Identity header that is passed to the SIP endpoint.
    :type _from: str
    :param to: The phone number, SIP address, or Client identifier that received this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). SIP addresses are formatted as &#x60;sip:name@company.com&#x60;. Client identifiers are formatted &#x60;client:name&#x60;. [Custom parameters](https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters) may also be specified.
    :type to: str
    :param amd_status_callback: The URL that we should call using the &#x60;amd_status_callback_method&#x60; to notify customer application whether the call was answered by human, machine or fax.
    :type amd_status_callback: str
    :param amd_status_callback_method: The HTTP method we should use when calling the &#x60;amd_status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;.
    :type amd_status_callback_method: str
    :param beep: Whether to play a notification beep to the conference when the participant joins. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;.
    :type beep: str
    :param byoc: The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that &#x60;byoc&#x60; is only meaningful when &#x60;to&#x60; is a phone number; it will otherwise be ignored. (Beta)
    :type byoc: str
    :param call_reason: The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party&#39;s phone. (Branded Calls Beta)
    :type call_reason: str
    :param call_sid_to_coach: The SID of the participant who is being &#x60;coached&#x60;. The participant being coached is the only participant who can hear the participant who is &#x60;coaching&#x60;.
    :type call_sid_to_coach: str
    :param call_token: A token string needed to invoke a forwarded call. A call_token is generated when an incoming call is received on a Twilio number. Pass an incoming call&#39;s call_token value to a forwarded call via the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the original incoming call.
    :type call_token: str
    :param caller_id: The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted &#x60;client:name&#x60;. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;callerId&#x60; must also be a phone number. If &#x60;to&#x60; is sip address, this value of &#x60;callerId&#x60; should be a username portion to be used to populate the From header that is passed to the SIP endpoint.
    :type caller_id: str
    :param coaching: Whether the participant is coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. If not present, defaults to &#x60;false&#x60; unless &#x60;call_sid_to_coach&#x60; is defined. If &#x60;true&#x60;, &#x60;call_sid_to_coach&#x60; must be defined.
    :type coaching: bool
    :param conference_record: Whether to record the conference the participant is joining. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;.
    :type conference_record: str
    :param conference_recording_status_callback: The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available.
    :type conference_recording_status_callback: str
    :param conference_recording_status_callback_event: The conference recording state changes that generate a call to &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, and &#x60;absent&#x60;. Separate multiple values with a space, ex: &#x60;&#39;in-progress completed failed&#39;&#x60;
    :type conference_recording_status_callback_event: List[str]
    :param conference_recording_status_callback_method: The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type conference_recording_status_callback_method: str
    :param conference_status_callback: The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored.
    :type conference_status_callback: str
    :param conference_status_callback_event: The conference state changes that should generate a call to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;modify&#x60;, &#x60;speaker&#x60;, and &#x60;announcement&#x60;. Separate multiple values with a space. Defaults to &#x60;start end&#x60;.
    :type conference_status_callback_event: List[str]
    :param conference_status_callback_method: The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type conference_status_callback_method: str
    :param conference_trim: Whether to trim leading and trailing silence from the conference recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;.
    :type conference_trim: str
    :param early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;.
    :type early_media: bool
    :param end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;.
    :type end_conference_on_exit: bool
    :param jitter_buffer_size: Jitter buffer size for the connecting participant. Twilio will use this setting to apply Jitter Buffer before participant&#39;s audio is mixed into the conference. Can be: &#x60;off&#x60;, &#x60;small&#x60;, &#x60;medium&#x60;, and &#x60;large&#x60;. Default to &#x60;large&#x60;.
    :type jitter_buffer_size: str
    :param label: A label for this participant. If one is supplied, it may subsequently be used to fetch, update or delete the participant.
    :type label: str
    :param machine_detection: Whether to detect if a human, answering machine, or fax has picked up the call. Can be: &#x60;Enable&#x60; or &#x60;DetectMessageEnd&#x60;. Use &#x60;Enable&#x60; if you would like us to return &#x60;AnsweredBy&#x60; as soon as the called party is identified. Use &#x60;DetectMessageEnd&#x60;, if you would like to leave a message on an answering machine. For more information, see [Answering Machine Detection](https://www.twilio.com/docs/voice/answering-machine-detection).
    :type machine_detection: str
    :param machine_detection_silence_timeout: The number of milliseconds of initial silence after which an &#x60;unknown&#x60; AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
    :type machine_detection_silence_timeout: int
    :param machine_detection_speech_end_threshold: The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
    :type machine_detection_speech_end_threshold: int
    :param machine_detection_speech_threshold: The number of milliseconds that is used as the measuring stick for the length of the speech activity, where durations lower than this value will be interpreted as a human and longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
    :type machine_detection_speech_threshold: int
    :param machine_detection_timeout: The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with &#x60;AnsweredBy&#x60; of &#x60;unknown&#x60;. The default timeout is 30 seconds.
    :type machine_detection_timeout: int
    :param max_participants: The maximum number of participants in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;.
    :type max_participants: int
    :param muted: Whether the agent is muted in the conference. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type muted: bool
    :param record: Whether to record the participant and their conferences, including the time between conferences. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type record: bool
    :param recording_channels: The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;.
    :type recording_channels: str
    :param recording_status_callback: The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes.
    :type recording_status_callback: str
    :param recording_status_callback_event: The recording state changes that should generate a call to &#x60;recording_status_callback&#x60;. Can be: &#x60;started&#x60;, &#x60;in-progress&#x60;, &#x60;paused&#x60;, &#x60;resumed&#x60;, &#x60;stopped&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, and &#x60;absent&#x60;. Separate multiple values with a space, ex: &#x60;&#39;in-progress completed failed&#39;&#x60;.
    :type recording_status_callback_event: List[str]
    :param recording_status_callback_method: The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type recording_status_callback_method: str
    :param recording_track: The audio track to record for the call. Can be: &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. The default is &#x60;both&#x60;. &#x60;inbound&#x60; records the audio that is received by Twilio. &#x60;outbound&#x60; records the audio that is sent from Twilio. &#x60;both&#x60; records the audio that is received and sent by Twilio.
    :type recording_track: str
    :param region: The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;.
    :type region: str
    :param sip_auth_password: The SIP password for authentication.
    :type sip_auth_password: str
    :param sip_auth_username: The SIP username used for authentication.
    :type sip_auth_username: str
    :param start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already started. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
    :type start_conference_on_enter: bool
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application.
    :type status_callback: str
    :param status_callback_event: The conference state changes that should generate a call to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, and &#x60;completed&#x60;. Separate multiple values with a space. The default value is &#x60;completed&#x60;.
    :type status_callback_event: List[str]
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; and &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type status_callback_method: str
    :param time_limit: The maximum duration of the call in seconds. Constraints depend on account and configuration.
    :type time_limit: int
    :param timeout: The number of seconds that we should allow the phone to ring before assuming there is no answer. Can be an integer between &#x60;5&#x60; and &#x60;600&#x60;, inclusive. The default value is &#x60;60&#x60;. We always add a 5-second timeout buffer to outgoing calls, so  value of 10 would result in an actual timeout that was closer to 15 seconds.
    :type timeout: int
    :param trim: Whether to trim any leading and trailing silence from the participant recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and the default is &#x60;trim-silence&#x60;.
    :type trim: str
    :param wait_method: The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file.
    :type wait_method: str
    :param wait_url: The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    :type wait_url: str

    """
    return web.Response(status=200)


async def delete_participant(request: web.Request, account_sid, conference_sid, call_sid) -> web.Response:
    """delete_participant

    Kick a participant from a given conference

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to delete.
    :type account_sid: str
    :param conference_sid: The SID of the conference with the participants to delete.
    :type conference_sid: str
    :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.
    :type call_sid: str

    """
    return web.Response(status=200)


async def fetch_participant(request: web.Request, account_sid, conference_sid, call_sid) -> web.Response:
    """fetch_participant

    Fetch an instance of a participant

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource to fetch.
    :type account_sid: str
    :param conference_sid: The SID of the conference with the participant to fetch.
    :type conference_sid: str
    :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.
    :type call_sid: str

    """
    return web.Response(status=200)


async def list_participant(request: web.Request, account_sid, conference_sid, muted=None, hold=None, coaching=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_participant

    Retrieve a list of participants belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to read.
    :type account_sid: str
    :param conference_sid: The SID of the conference with the participants to read.
    :type conference_sid: str
    :param muted: Whether to return only participants that are muted. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type muted: bool
    :param hold: Whether to return only participants that are on hold. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type hold: bool
    :param coaching: Whether to return only participants who are coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type coaching: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_participant(request: web.Request, account_sid, conference_sid, call_sid, announce_method=None, announce_url=None, beep_on_exit=None, call_sid_to_coach=None, coaching=None, end_conference_on_exit=None, hold=None, hold_method=None, hold_url=None, muted=None, wait_method=None, wait_url=None) -> web.Response:
    """update_participant

    Update the properties of the participant

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to update.
    :type account_sid: str
    :param conference_sid: The SID of the conference with the participant to update.
    :type conference_sid: str
    :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to update. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.
    :type call_sid: str
    :param announce_method: The HTTP method we should use to call &#x60;announce_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type announce_method: str
    :param announce_url: The URL we call using the &#x60;announce_method&#x60; for an announcement to the participant. The URL may return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60;, &#x60;&lt;Pause&gt;&#x60;, or &#x60;&lt;Redirect&gt;&#x60; verbs.
    :type announce_url: str
    :param beep_on_exit: Whether to play a notification beep to the conference when the participant exits. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type beep_on_exit: bool
    :param call_sid_to_coach: The SID of the participant who is being &#x60;coached&#x60;. The participant being coached is the only participant who can hear the participant who is &#x60;coaching&#x60;.
    :type call_sid_to_coach: str
    :param coaching: Whether the participant is coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. If not present, defaults to &#x60;false&#x60; unless &#x60;call_sid_to_coach&#x60; is defined. If &#x60;true&#x60;, &#x60;call_sid_to_coach&#x60; must be defined.
    :type coaching: bool
    :param end_conference_on_exit: Whether to end the conference when the participant leaves. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;.
    :type end_conference_on_exit: bool
    :param hold: Whether the participant should be on hold. Can be: &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; puts the participant on hold, and &#x60;false&#x60; lets them rejoin the conference.
    :type hold: bool
    :param hold_method: The HTTP method we should use to call &#x60;hold_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;GET&#x60;.
    :type hold_method: str
    :param hold_url: The URL we call using the &#x60;hold_method&#x60; for music that plays when the participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60;, &#x60;&lt;Pause&gt;&#x60;, or &#x60;&lt;Redirect&gt;&#x60; verbs.
    :type hold_url: str
    :param muted: Whether the participant should be muted. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; will mute the participant, and &#x60;false&#x60; will un-mute them. Anything value other than &#x60;true&#x60; or &#x60;false&#x60; is interpreted as &#x60;false&#x60;.
    :type muted: bool
    :param wait_method: The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file.
    :type wait_method: str
    :param wait_url: The URL we call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The URL may return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60;, &#x60;&lt;Pause&gt;&#x60;, or &#x60;&lt;Redirect&gt;&#x60; verbs. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    :type wait_url: str

    """
    return web.Response(status=200)
