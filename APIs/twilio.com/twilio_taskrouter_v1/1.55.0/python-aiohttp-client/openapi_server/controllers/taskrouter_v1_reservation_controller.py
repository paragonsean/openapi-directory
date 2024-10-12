from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_task_reservation_response import ListTaskReservationResponse
from openapi_server.models.list_worker_reservation_response import ListWorkerReservationResponse
from openapi_server.models.task_reservation_enum_call_status import TaskReservationEnumCallStatus
from openapi_server.models.task_reservation_enum_conference_event import TaskReservationEnumConferenceEvent
from openapi_server.models.task_reservation_enum_status import TaskReservationEnumStatus
from openapi_server.models.task_reservation_enum_supervisor_mode import TaskReservationEnumSupervisorMode
from openapi_server.models.taskrouter_v1_workspace_task_task_reservation import TaskrouterV1WorkspaceTaskTaskReservation
from openapi_server.models.taskrouter_v1_workspace_worker_worker_reservation import TaskrouterV1WorkspaceWorkerWorkerReservation
from openapi_server.models.worker_reservation_enum_call_status import WorkerReservationEnumCallStatus
from openapi_server.models.worker_reservation_enum_conference_event import WorkerReservationEnumConferenceEvent
from openapi_server.models.worker_reservation_enum_status import WorkerReservationEnumStatus
from openapi_server import util


async def fetch_task_reservation(request: web.Request, workspace_sid, task_sid, sid) -> web.Response:
    """fetch_task_reservation

    

    :param workspace_sid: The SID of the Workspace with the TaskReservation resource to fetch.
    :type workspace_sid: str
    :param task_sid: The SID of the reserved Task resource with the TaskReservation resource to fetch.
    :type task_sid: str
    :param sid: The SID of the TaskReservation resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_worker_reservation(request: web.Request, workspace_sid, worker_sid, sid) -> web.Response:
    """fetch_worker_reservation

    

    :param workspace_sid: The SID of the Workspace with the WorkerReservation resource to fetch.
    :type workspace_sid: str
    :param worker_sid: The SID of the reserved Worker resource with the WorkerReservation resource to fetch.
    :type worker_sid: str
    :param sid: The SID of the WorkerReservation resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_task_reservation(request: web.Request, workspace_sid, task_sid, reservation_status=None, worker_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_task_reservation

    

    :param workspace_sid: The SID of the Workspace with the TaskReservation resources to read.
    :type workspace_sid: str
    :param task_sid: The SID of the reserved Task resource with the TaskReservation resources to read.
    :type task_sid: str
    :param reservation_status: Returns the list of reservations for a task with a specified ReservationStatus.  Can be: &#x60;pending&#x60;, &#x60;accepted&#x60;, &#x60;rejected&#x60;, or &#x60;timeout&#x60;.
    :type reservation_status: str
    :param worker_sid: The SID of the reserved Worker resource to read.
    :type worker_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_worker_reservation(request: web.Request, workspace_sid, worker_sid, reservation_status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_worker_reservation

    

    :param workspace_sid: The SID of the Workspace with the WorkerReservation resources to read.
    :type workspace_sid: str
    :param worker_sid: The SID of the reserved Worker resource with the WorkerReservation resources to read.
    :type worker_sid: str
    :param reservation_status: Returns the list of reservations for a worker with a specified ReservationStatus. Can be: &#x60;pending&#x60;, &#x60;accepted&#x60;, &#x60;rejected&#x60;, &#x60;timeout&#x60;, &#x60;canceled&#x60;, or &#x60;rescinded&#x60;.
    :type reservation_status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_task_reservation(request: web.Request, workspace_sid, task_sid, sid, if_match=None, beep=None, beep_on_customer_entrance=None, call_accept=None, call_from=None, call_record=None, call_status_callback_url=None, call_timeout=None, call_to=None, call_url=None, conference_record=None, conference_recording_status_callback=None, conference_recording_status_callback_method=None, conference_status_callback=None, conference_status_callback_event=None, conference_status_callback_method=None, conference_trim=None, dequeue_from=None, dequeue_post_work_activity_sid=None, dequeue_record=None, dequeue_status_callback_event=None, dequeue_status_callback_url=None, dequeue_timeout=None, dequeue_to=None, early_media=None, end_conference_on_customer_exit=None, end_conference_on_exit=None, _from=None, instruction=None, jitter_buffer_size=None, max_participants=None, muted=None, post_work_activity_sid=None, record=None, recording_channels=None, recording_status_callback=None, recording_status_callback_method=None, redirect_accept=None, redirect_call_sid=None, redirect_url=None, region=None, reservation_status=None, sip_auth_password=None, sip_auth_username=None, start_conference_on_enter=None, status_callback=None, status_callback_event=None, status_callback_method=None, supervisor=None, supervisor_mode=None, timeout=None, to=None, wait_method=None, wait_url=None, worker_activity_sid=None) -> web.Response:
    """update_task_reservation

    

    :param workspace_sid: The SID of the Workspace with the TaskReservation resources to update.
    :type workspace_sid: str
    :param task_sid: The SID of the reserved Task resource with the TaskReservation resources to update.
    :type task_sid: str
    :param sid: The SID of the TaskReservation resource to update.
    :type sid: str
    :param if_match: The If-Match HTTP request header
    :type if_match: str
    :param beep: Whether to play a notification beep when the participant joins or when to play a beep. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;.
    :type beep: str
    :param beep_on_customer_entrance: Whether to play a notification beep when the customer joins.
    :type beep_on_customer_entrance: bool
    :param call_accept: Whether to accept a reservation when executing a Call instruction.
    :type call_accept: bool
    :param call_from: The Caller ID of the outbound call when executing a Call instruction.
    :type call_from: str
    :param call_record: Whether to record both legs of a call when executing a Call instruction or which leg to record.
    :type call_record: str
    :param call_status_callback_url: The URL to call  for the completed call event when executing a Call instruction.
    :type call_status_callback_url: str
    :param call_timeout: Timeout for call when executing a Call instruction.
    :type call_timeout: int
    :param call_to: The Contact URI of the worker when executing a Call instruction.  Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    :type call_to: str
    :param call_url: TwiML URI executed on answering the worker&#39;s leg as a result of the Call instruction.
    :type call_url: str
    :param conference_record: Whether to record the conference the participant is joining or when to record the conference. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;.
    :type conference_record: str
    :param conference_recording_status_callback: The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available.
    :type conference_recording_status_callback: str
    :param conference_recording_status_callback_method: The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type conference_recording_status_callback_method: str
    :param conference_status_callback: The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored.
    :type conference_status_callback: str
    :param conference_status_callback_event: The conference status events that we will send to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;speaker&#x60;.
    :type conference_status_callback_event: list | bytes
    :param conference_status_callback_method: The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type conference_status_callback_method: str
    :param conference_trim: How to trim the leading and trailing silence from your recorded conference audio files. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;.
    :type conference_trim: str
    :param dequeue_from: The Caller ID of the call to the worker when executing a Dequeue instruction.
    :type dequeue_from: str
    :param dequeue_post_work_activity_sid: The SID of the Activity resource to start after executing a Dequeue instruction.
    :type dequeue_post_work_activity_sid: str
    :param dequeue_record: Whether to record both legs of a call when executing a Dequeue instruction or which leg to record.
    :type dequeue_record: str
    :param dequeue_status_callback_event: The Call progress events sent via webhooks as a result of a Dequeue instruction.
    :type dequeue_status_callback_event: List[str]
    :param dequeue_status_callback_url: The Callback URL for completed call event when executing a Dequeue instruction.
    :type dequeue_status_callback_url: str
    :param dequeue_timeout: Timeout for call when executing a Dequeue instruction.
    :type dequeue_timeout: int
    :param dequeue_to: The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    :type dequeue_to: str
    :param early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is &#x60;true&#x60;.
    :type early_media: bool
    :param end_conference_on_customer_exit: Whether to end the conference when the customer leaves.
    :type end_conference_on_customer_exit: bool
    :param end_conference_on_exit: Whether to end the conference when the agent leaves.
    :type end_conference_on_exit: bool
    :param _from: The Caller ID of the call to the worker when executing a Conference instruction.
    :type _from: str
    :param instruction: The assignment instruction for reservation.
    :type instruction: str
    :param jitter_buffer_size: The jitter buffer size for conference. Can be: &#x60;small&#x60;, &#x60;medium&#x60;, &#x60;large&#x60;, &#x60;off&#x60;.
    :type jitter_buffer_size: str
    :param max_participants: The maximum number of participants in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;.
    :type max_participants: int
    :param muted: Whether the agent is muted in the conference. The default is &#x60;false&#x60;.
    :type muted: bool
    :param post_work_activity_sid: The new worker activity SID after executing a Conference instruction.
    :type post_work_activity_sid: str
    :param record: Whether to record the participant and their conferences, including the time between conferences. The default is &#x60;false&#x60;.
    :type record: bool
    :param recording_channels: The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;.
    :type recording_channels: str
    :param recording_status_callback: The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes.
    :type recording_status_callback: str
    :param recording_status_callback_method: The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type recording_status_callback_method: str
    :param redirect_accept: Whether the reservation should be accepted when executing a Redirect instruction.
    :type redirect_accept: bool
    :param redirect_call_sid: The Call SID of the call parked in the queue when executing a Redirect instruction.
    :type redirect_call_sid: str
    :param redirect_url: TwiML URI to redirect the call to when executing the Redirect instruction.
    :type redirect_url: str
    :param region: The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;.
    :type region: str
    :param reservation_status: 
    :type reservation_status: str
    :param sip_auth_password: The SIP password for authentication.
    :type sip_auth_password: str
    :param sip_auth_username: The SIP username used for authentication.
    :type sip_auth_username: str
    :param start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already started. The default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
    :type start_conference_on_enter: bool
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application.
    :type status_callback: str
    :param status_callback_event: The call progress events that we will send to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, or &#x60;completed&#x60;.
    :type status_callback_event: list | bytes
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;.
    :type status_callback_method: str
    :param supervisor: The Supervisor SID/URI when executing the Supervise instruction.
    :type supervisor: str
    :param supervisor_mode: 
    :type supervisor_mode: str
    :param timeout: Timeout for call when executing a Conference instruction.
    :type timeout: int
    :param to: The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    :type to: str
    :param wait_method: The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file.
    :type wait_method: str
    :param wait_url: The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    :type wait_url: str
    :param worker_activity_sid: The new worker activity SID if rejecting a reservation.
    :type worker_activity_sid: str

    """
    conference_status_callback_event = [TaskReservationEnumConferenceEvent.from_dict(d) for d in conference_status_callback_event]
    status_callback_event = [TaskReservationEnumCallStatus.from_dict(d) for d in status_callback_event]
    return web.Response(status=200)


async def update_worker_reservation(request: web.Request, workspace_sid, worker_sid, sid, if_match=None, beep=None, beep_on_customer_entrance=None, call_accept=None, call_from=None, call_record=None, call_status_callback_url=None, call_timeout=None, call_to=None, call_url=None, conference_record=None, conference_recording_status_callback=None, conference_recording_status_callback_method=None, conference_status_callback=None, conference_status_callback_event=None, conference_status_callback_method=None, conference_trim=None, dequeue_from=None, dequeue_post_work_activity_sid=None, dequeue_record=None, dequeue_status_callback_event=None, dequeue_status_callback_url=None, dequeue_timeout=None, dequeue_to=None, early_media=None, end_conference_on_customer_exit=None, end_conference_on_exit=None, _from=None, instruction=None, jitter_buffer_size=None, max_participants=None, muted=None, post_work_activity_sid=None, record=None, recording_channels=None, recording_status_callback=None, recording_status_callback_method=None, redirect_accept=None, redirect_call_sid=None, redirect_url=None, region=None, reservation_status=None, sip_auth_password=None, sip_auth_username=None, start_conference_on_enter=None, status_callback=None, status_callback_event=None, status_callback_method=None, timeout=None, to=None, wait_method=None, wait_url=None, worker_activity_sid=None) -> web.Response:
    """update_worker_reservation

    

    :param workspace_sid: The SID of the Workspace with the WorkerReservation resources to update.
    :type workspace_sid: str
    :param worker_sid: The SID of the reserved Worker resource with the WorkerReservation resources to update.
    :type worker_sid: str
    :param sid: The SID of the WorkerReservation resource to update.
    :type sid: str
    :param if_match: The If-Match HTTP request header
    :type if_match: str
    :param beep: Whether to play a notification beep when the participant joins or when to play a beep. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;.
    :type beep: str
    :param beep_on_customer_entrance: Whether to play a notification beep when the customer joins.
    :type beep_on_customer_entrance: bool
    :param call_accept: Whether to accept a reservation when executing a Call instruction.
    :type call_accept: bool
    :param call_from: The Caller ID of the outbound call when executing a Call instruction.
    :type call_from: str
    :param call_record: Whether to record both legs of a call when executing a Call instruction.
    :type call_record: str
    :param call_status_callback_url: The URL to call for the completed call event when executing a Call instruction.
    :type call_status_callback_url: str
    :param call_timeout: The timeout for a call when executing a Call instruction.
    :type call_timeout: int
    :param call_to: The contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    :type call_to: str
    :param call_url: TwiML URI executed on answering the worker&#39;s leg as a result of the Call instruction.
    :type call_url: str
    :param conference_record: Whether to record the conference the participant is joining or when to record the conference. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;.
    :type conference_record: str
    :param conference_recording_status_callback: The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available.
    :type conference_recording_status_callback: str
    :param conference_recording_status_callback_method: The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type conference_recording_status_callback_method: str
    :param conference_status_callback: The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored.
    :type conference_status_callback: str
    :param conference_status_callback_event: The conference status events that we will send to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;speaker&#x60;.
    :type conference_status_callback_event: list | bytes
    :param conference_status_callback_method: The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type conference_status_callback_method: str
    :param conference_trim: Whether to trim leading and trailing silence from your recorded conference audio files. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;.
    :type conference_trim: str
    :param dequeue_from: The caller ID of the call to the worker when executing a Dequeue instruction.
    :type dequeue_from: str
    :param dequeue_post_work_activity_sid: The SID of the Activity resource to start after executing a Dequeue instruction.
    :type dequeue_post_work_activity_sid: str
    :param dequeue_record: Whether to record both legs of a call when executing a Dequeue instruction or which leg to record.
    :type dequeue_record: str
    :param dequeue_status_callback_event: The call progress events sent via webhooks as a result of a Dequeue instruction.
    :type dequeue_status_callback_event: List[str]
    :param dequeue_status_callback_url: The callback URL for completed call event when executing a Dequeue instruction.
    :type dequeue_status_callback_url: str
    :param dequeue_timeout: The timeout for call when executing a Dequeue instruction.
    :type dequeue_timeout: int
    :param dequeue_to: The contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    :type dequeue_to: str
    :param early_media: Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is &#x60;true&#x60;.
    :type early_media: bool
    :param end_conference_on_customer_exit: Whether to end the conference when the customer leaves.
    :type end_conference_on_customer_exit: bool
    :param end_conference_on_exit: Whether to end the conference when the agent leaves.
    :type end_conference_on_exit: bool
    :param _from: The caller ID of the call to the worker when executing a Conference instruction.
    :type _from: str
    :param instruction: The assignment instruction for the reservation.
    :type instruction: str
    :param jitter_buffer_size: The jitter buffer size for conference. Can be: &#x60;small&#x60;, &#x60;medium&#x60;, &#x60;large&#x60;, &#x60;off&#x60;.
    :type jitter_buffer_size: str
    :param max_participants: The maximum number of participants allowed in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;.
    :type max_participants: int
    :param muted: Whether the agent is muted in the conference. Defaults to &#x60;false&#x60;.
    :type muted: bool
    :param post_work_activity_sid: The new worker activity SID after executing a Conference instruction.
    :type post_work_activity_sid: str
    :param record: Whether to record the participant and their conferences, including the time between conferences. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type record: bool
    :param recording_channels: The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;.
    :type recording_channels: str
    :param recording_status_callback: The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes.
    :type recording_status_callback: str
    :param recording_status_callback_method: The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;.
    :type recording_status_callback_method: str
    :param redirect_accept: Whether the reservation should be accepted when executing a Redirect instruction.
    :type redirect_accept: bool
    :param redirect_call_sid: The Call SID of the call parked in the queue when executing a Redirect instruction.
    :type redirect_call_sid: str
    :param redirect_url: TwiML URI to redirect the call to when executing the Redirect instruction.
    :type redirect_url: str
    :param region: The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;.
    :type region: str
    :param reservation_status: 
    :type reservation_status: str
    :param sip_auth_password: The SIP password for authentication.
    :type sip_auth_password: str
    :param sip_auth_username: The SIP username used for authentication.
    :type sip_auth_username: str
    :param start_conference_on_enter: Whether to start the conference when the participant joins, if it has not already started. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
    :type start_conference_on_enter: bool
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application.
    :type status_callback: str
    :param status_callback_event: The call progress events that we will send to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, or &#x60;completed&#x60;.
    :type status_callback_event: list | bytes
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;.
    :type status_callback_method: str
    :param timeout: The timeout for a call when executing a Conference instruction.
    :type timeout: int
    :param to: The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    :type to: str
    :param wait_method: The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file.
    :type wait_method: str
    :param wait_url: The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    :type wait_url: str
    :param worker_activity_sid: The new worker activity SID if rejecting a reservation.
    :type worker_activity_sid: str

    """
    conference_status_callback_event = [WorkerReservationEnumConferenceEvent.from_dict(d) for d in conference_status_callback_event]
    status_callback_event = [WorkerReservationEnumCallStatus.from_dict(d) for d in status_callback_event]
    return web.Response(status=200)
