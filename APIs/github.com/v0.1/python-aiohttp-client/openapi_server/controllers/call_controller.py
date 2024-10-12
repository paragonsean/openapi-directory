from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_call_response import BulkCallResponse
from openapi_server.models.call_response import CallResponse
from openapi_server.models.cancel_scheduled_hangup_response import CancelScheduledHangupResponse
from openapi_server.models.cancel_scheduled_play_response import CancelScheduledPlayResponse
from openapi_server.models.group_call_response import GroupCallResponse
from openapi_server.models.hangup_all_calls_response import HangupAllCallsResponse
from openapi_server.models.hangup_call_response import HangupCallResponse
from openapi_server.models.play_response import PlayResponse
from openapi_server.models.play_stop_response import PlayStopResponse
from openapi_server.models.record_start_response import RecordStartResponse
from openapi_server.models.record_stop_response import RecordStopResponse
from openapi_server.models.schedule_hangup_response import ScheduleHangupResponse
from openapi_server.models.schedule_play_response import SchedulePlayResponse
from openapi_server.models.send_digits_response import SendDigitsResponse
from openapi_server.models.sound_touch_response import SoundTouchResponse
from openapi_server.models.sound_touch_stop_response import SoundTouchStopResponse
from openapi_server.models.transfer_call_response import TransferCallResponse
from openapi_server import util


async def v01_bulk_call_post(request: web.Request, answer_url, delimiter, _from, gateways, to, caller_name=None, confirm_key=None, confirm_sound=None, core_uuid=None, extra_dial_string=None, gateway_codecs=None, gateway_retries=None, gateway_timeouts=None, hangup_on_ring=None, hangup_url=None, reject_causes=None, ring_url=None, send_digits=None, send_on_preanswer=None, time_limit=None) -> web.Response:
    """/v0.1/BulkCall/

    Initiates multiple concurrent outbound calls

    :param answer_url: Fully qualified URL which will provide the RestXML once the call connects
    :type answer_url: str
    :param delimiter: Any character, except &#x60;/&#x60; and &#x60;,&#x60;, which will be used as a separator within several parameters
    :type delimiter: str
    :param _from: Phone number to be used as Caller ID
    :type _from: str
    :param gateways: Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)
    :type gateways: str
    :param to: Phone number to be called
    :type to: str
    :param caller_name: Caller Name to be set for the call
    :type caller_name: str
    :param confirm_key: DTMF tone the called party must send to accept the call
    :type confirm_key: str
    :param confirm_sound: Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered
    :type confirm_sound: str
    :param core_uuid: Core UUID of the desired FreeSWITCH instance (an Eqivo extension)
    :type core_uuid: str
    :param extra_dial_string: Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.
    :type extra_dial_string: str
    :param gateway_codecs: List of codec(s) to be used for each gateway. Enclose codec groups in single quotes
    :type gateway_codecs: str
    :param gateway_retries: List of maximum retry counts for each gateway
    :type gateway_retries: str
    :param gateway_timeouts: List of maximum timeout amounts (in seconds) for each gateway
    :type gateway_timeouts: str
    :param hangup_on_ring: Schedules the call&#39;s hangup at a given time offset (in seconds) after the destination starts ringing
    :type hangup_on_ring: int
    :param hangup_url: Fully qualified URL to which the call hangup notification will be POSTed. &#x60;HangupCause&#x60; is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)
    :type hangup_url: str
    :param reject_causes: Comma separated reject causes
    :type reject_causes: str
    :param ring_url: Fully qualified URL to which the call ringing notification will be POSTed. &#x60;RequestUUID&#x60; and &#x60;CallUUID&#x60; is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)
    :type ring_url: str
    :param send_digits: DTMF tones to be sent when the call is answered. Each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string
    :type send_digits: str
    :param send_on_preanswer: When set to &#x60;true&#x60;, DTMF tones will be sent as early media rather than when the call is answered
    :type send_on_preanswer: bool
    :param time_limit: Schedules the call&#39;s hangup at a given time offset (in seconds) after the call is answered
    :type time_limit: int

    """
    return web.Response(status=200)


async def v01_call_post(request: web.Request, answer_url, _from, gateways, to, async_amd=None, async_amd_status_callback=None, async_amd_status_callback_method=None, caller_name=None, core_uuid=None, extra_dial_string=None, gateway_codecs=None, gateway_retries=None, gateway_timeouts=None, hangup_on_ring=None, hangup_url=None, machine_detection=None, machine_detection_silence_timeout=None, machine_detection_speech_end_threshold=None, machine_detection_speech_threshold=None, machine_detection_timeout=None, ring_url=None, send_digits=None, send_on_preanswer=None, time_limit=None) -> web.Response:
    """/v0.1/Call/

    Initiates an outbound call

    :param answer_url: Fully qualified URL which will provide the RestXML once the call connects
    :type answer_url: str
    :param _from: Phone number to be used as Caller ID
    :type _from: str
    :param gateways: Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)
    :type gateways: str
    :param to: Phone number to be called
    :type to: str
    :param async_amd: When set to &#x60;true&#x60;, the call flow execution is blocked until answering machine detection is complete (an Eqivo extension)
    :type async_amd: bool
    :param async_amd_status_callback: Fully qualified URL to which the answering machine detection result will be sent. &#x60;AnsweredBy&#x60; and &#x60;MachineDetectionDuration&#x60; are appended to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) (an Eqivo extension)
    :type async_amd_status_callback: str
    :param async_amd_status_callback_method: HTTP method to be used when answering machine detection is completed (an Eqivo extension)
    :type async_amd_status_callback_method: str
    :param caller_name: Caller Name to be set for the call
    :type caller_name: str
    :param core_uuid: Core UUID of the desired FreeSWITCH instance (an Eqivo extension)
    :type core_uuid: str
    :param extra_dial_string: Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.
    :type extra_dial_string: str
    :param gateway_codecs: List of codec(s) to be used for each gateway. Enclose codec groups in single quotes
    :type gateway_codecs: str
    :param gateway_retries: List of maximum retry counts for each gateway
    :type gateway_retries: str
    :param gateway_timeouts: List of maximum timeout amounts (in seconds) for each gateway
    :type gateway_timeouts: str
    :param hangup_on_ring: Schedules the call&#39;s hangup at a given time offset (in seconds) after the destination starts ringing
    :type hangup_on_ring: int
    :param hangup_url: Fully qualified URL to which the call hangup notification will be POSTed. &#x60;HangupCause&#x60; is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)
    :type hangup_url: str
    :param machine_detection: Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension)
    :type machine_detection: str
    :param machine_detection_silence_timeout: Initial silence threshold (in milliseconds, an Eqivo extension)
    :type machine_detection_silence_timeout: int
    :param machine_detection_speech_end_threshold: Silence threshold (in milliseconds, an Eqivo extension)
    :type machine_detection_speech_end_threshold: int
    :param machine_detection_speech_threshold: Speech activity/utterance threshold (in milliseconds, an Eqivo extension)
    :type machine_detection_speech_threshold: int
    :param machine_detection_timeout: Amount of time (in seconds) allotted for answering machine detection assessment (an Eqivo extension)
    :type machine_detection_timeout: int
    :param ring_url: Fully qualified URL to which the call ringing notification will be POSTed. &#x60;RequestUUID&#x60; and &#x60;CallUUID&#x60; is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)
    :type ring_url: str
    :param send_digits: DTMF tones to be sent when the call is answered. Each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string
    :type send_digits: str
    :param send_on_preanswer: When set to &#x60;true&#x60;, DTMF tones will be sent as early media rather than when the call is answered
    :type send_on_preanswer: bool
    :param time_limit: Schedules the call&#39;s hangup at a given time offset (in seconds) after the call is answered
    :type time_limit: int

    """
    return web.Response(status=200)


async def v01_cancel_scheduled_hangup_post(request: web.Request, sched_hangup_id) -> web.Response:
    """/v0.1/CancelScheduledHangup/

    Cancels a scheduled hangup for a call

    :param sched_hangup_id: Unique identifier returned when scheduled hangup was originally requested
    :type sched_hangup_id: str

    """
    return web.Response(status=200)


async def v01_cancel_scheduled_play_post(request: web.Request, sched_play_id) -> web.Response:
    """/v0.1/CancelScheduledPlay/

    Cancels a scheduled playback request

    :param sched_play_id: Unique identifier returned when scheduled playback was originally requested
    :type sched_play_id: str

    """
    return web.Response(status=200)


async def v01_group_call_post(request: web.Request, answer_url, delimiter, _from, gateways, to, caller_name=None, confirm_key=None, confirm_sound=None, core_uuid=None, extra_dial_string=None, gateway_codecs=None, gateway_retries=None, gateway_timeouts=None, hangup_on_ring=None, hangup_url=None, reject_causes=None, ring_url=None, send_digits=None, send_on_preanswer=None, time_limit=None) -> web.Response:
    """/v0.1/GroupCall/

    Initiate multiple racing outbound calls

    :param answer_url: Fully qualified URL which will provide the RestXML once the call connects
    :type answer_url: str
    :param delimiter: Any character, except &#x60;/&#x60; and &#x60;,&#x60;, which will be used as a separator within several parameters
    :type delimiter: str
    :param _from: Phone number to be used as Caller ID
    :type _from: str
    :param gateways: Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)
    :type gateways: str
    :param to: Phone number to be called
    :type to: str
    :param caller_name: Caller Name to be set for the call
    :type caller_name: str
    :param confirm_key: DTMF tone the called party must send to accept the call
    :type confirm_key: str
    :param confirm_sound: Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered
    :type confirm_sound: str
    :param core_uuid: Core UUID of the desired FreeSWITCH instance (an Eqivo extension)
    :type core_uuid: str
    :param extra_dial_string: Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.
    :type extra_dial_string: str
    :param gateway_codecs: List of codec(s) to be used for each gateway. Enclose codec groups in single quotes
    :type gateway_codecs: str
    :param gateway_retries: List of maximum retry counts for each gateway
    :type gateway_retries: str
    :param gateway_timeouts: List of maximum timeout amounts (in seconds) for each gateway
    :type gateway_timeouts: str
    :param hangup_on_ring: Schedules the call&#39;s hangup at a given time offset (in seconds) after the destination starts ringing
    :type hangup_on_ring: int
    :param hangup_url: Fully qualified URL to which the call hangup notification will be POSTed. &#x60;HangupCause&#x60; is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)
    :type hangup_url: str
    :param reject_causes: Comma separated reject causes
    :type reject_causes: str
    :param ring_url: Fully qualified URL to which the call ringing notification will be POSTed. &#x60;RequestUUID&#x60; and &#x60;CallUUID&#x60; is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)
    :type ring_url: str
    :param send_digits: DTMF tones to be sent when the call is answered. Each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string
    :type send_digits: str
    :param send_on_preanswer: When set to &#x60;true&#x60;, DTMF tones will be sent as early media rather than when the call is answered
    :type send_on_preanswer: bool
    :param time_limit: Schedules the call&#39;s hangup at a given time offset (in seconds) after the call is answered
    :type time_limit: int

    """
    return web.Response(status=200)


async def v01_hangup_all_calls_post(request: web.Request, ) -> web.Response:
    """/v0.1/HangupAllCalls/

    Hangs up all established calls


    """
    return web.Response(status=200)


async def v01_hangup_call_post(request: web.Request, call_uuid=None, request_uuid=None) -> web.Response:
    """/v0.1/HangupCall/

    Hangs up a specific call

    :param call_uuid: Unique identifier of the call (when established); this parameter is mutually exclusive with RequestUUID
    :type call_uuid: str
    :param request_uuid: Unique identifier of the API request (when the call is not established yet); this parameter is mutually exclusive with CallUUID
    :type request_uuid: str

    """
    return web.Response(status=200)


async def v01_play_post(request: web.Request, call_uuid, sounds, legs=None, length=None, loop=None, mix=None) -> web.Response:
    """/v0.1/Play/

    Plays media into a live call

    :param call_uuid: Unique identifier of the call to play media into
    :type call_uuid: str
    :param sounds: Comma separated list of file paths/URIs to be played
    :type sounds: str
    :param legs: Call leg(s) for which the media will be played; &#x60;aleg&#x60; refers to the initial call leg, &#x60;bleg&#x60; refers to the bridged call leg, if applicable.
    :type legs: str
    :param length: Maximum amount of time (in seconds) to playback the media
    :type length: int
    :param loop: Loops the media file(s) indefinitely
    :type loop: bool
    :param mix: Whether the media should be mixed with the call&#39;s audio stream
    :type mix: bool

    """
    return web.Response(status=200)


async def v01_play_stop_post(request: web.Request, call_uuid) -> web.Response:
    """/v0.1/PlayStop/

    Interrupts media playback on a given call

    :param call_uuid: Unique identifier of the call
    :type call_uuid: str

    """
    return web.Response(status=200)


async def v01_record_start_post(request: web.Request, call_uuid=None, file_format=None, file_name=None, file_path=None, time_limit=None) -> web.Response:
    """/v0.1/RecordStart/

    Initiates recording of a given call

    :param call_uuid: Unique identifier of the call to be recorded
    :type call_uuid: str
    :param file_format: File format (extension)
    :type file_format: str
    :param file_name: Recording file name (without extension); if empty, a timestamp based file name will be generated
    :type file_name: str
    :param file_path: Directory path/URI where the recording file will be saved
    :type file_path: str
    :param time_limit: Maximum recording length, in seconds
    :type time_limit: int

    """
    return web.Response(status=200)


async def v01_record_stop_post(request: web.Request, call_uuid, record_file) -> web.Response:
    """/v0.1/RecordStop/

    Stops the recording of a given call

    :param call_uuid: Unique identifier of the call
    :type call_uuid: str
    :param record_file: Full path to recording file, as returned by RecordStart; &#x60;all&#x60; shorthand is also available
    :type record_file: str

    """
    return web.Response(status=200)


async def v01_schedule_hangup_post(request: web.Request, call_uuid, time) -> web.Response:
    """/v0.1/ScheduleHangup/

    Schedules a hangup for a specific call

    :param call_uuid: Unique identifier of the call
    :type call_uuid: str
    :param time: Time (in seconds) after which the call in question will be hung up
    :type time: int

    """
    return web.Response(status=200)


async def v01_schedule_play_post(request: web.Request, call_uuid, sounds, time, legs=None, length=None, loop=None, mix=None) -> web.Response:
    """/v0.1/SchedulePlay/

    Schedules media playback for a specific call

    :param call_uuid: Unique identifier of the call to play media into
    :type call_uuid: str
    :param sounds: Comma separated list of file paths/URIs to be played
    :type sounds: str
    :param time: Time (in seconds) after which the media will be playedback
    :type time: int
    :param legs: Call leg(s) for which the media will be played; &#x60;aleg&#x60; refers to the initial call leg, &#x60;bleg&#x60; refers to the bridged call leg, if applicable.
    :type legs: str
    :param length: Maximum amount of time (in seconds) to playback the media
    :type length: int
    :param loop: Loops the media file(s) indefinitely
    :type loop: bool
    :param mix: Whether the media should be mixed with the call&#39;s audio stream
    :type mix: bool

    """
    return web.Response(status=200)


async def v01_send_digits_post(request: web.Request, call_uuid, digits, leg=None) -> web.Response:
    """/v0.1/SendDigits/

    Emits DMTF tones to a call

    :param call_uuid: Unique identifier of the call to send DTMF to
    :type call_uuid: str
    :param digits: DTMF tones to be sent; each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string
    :type digits: str
    :param leg: Call leg(s) to which DTMFs will be sent; &#x60;aleg&#x60; refers to the initial call leg, &#x60;bleg&#x60; refers to the bridged call leg, if applicable.
    :type leg: str

    """
    return web.Response(status=200)


async def v01_sound_touch_post(request: web.Request, call_uuid, audio_direction=None, pitch=None, pitch_octaves=None, pitch_semi_tones=None, rate=None, tempo=None) -> web.Response:
    """/v0.1/SoundTouch/

    Applies SoundTouch effects to a live call

    :param call_uuid: Unique identifier of the call to send DTMF to
    :type call_uuid: str
    :param audio_direction: Media stream to be altered, incoming or outgoing
    :type audio_direction: str
    :param pitch: Adjust the pitch
    :type pitch: float
    :param pitch_octaves: Adjust the pitch in octaves
    :type pitch_octaves: float
    :param pitch_semi_tones: Adjust the pitch in semitones
    :type pitch_semi_tones: float
    :param rate: Adjust the rate
    :type rate: float
    :param tempo: Adjust the tempo
    :type tempo: float

    """
    return web.Response(status=200)


async def v01_sound_touch_stop_post(request: web.Request, call_uuid) -> web.Response:
    """/v0.1/SoundTouchStop/

    Removes SoundTouch effects from a given call

    :param call_uuid: Unique identifier of the call
    :type call_uuid: str

    """
    return web.Response(status=200)


async def v01_transfer_call_post(request: web.Request, call_uuid, url) -> web.Response:
    """/v0.1/TransferCall/

    Replaces the RestXML flow of a live call

    :param call_uuid: Unique identifier of the call
    :type call_uuid: str
    :param url: Absolute URL which will return the updated RestXML flow
    :type url: str

    """
    return web.Response(status=200)
