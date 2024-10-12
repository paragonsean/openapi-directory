# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.event_type import EventType
from openapi_server.models.history_event_activity_task_cancel_requested_event_attributes import HistoryEventActivityTaskCancelRequestedEventAttributes
from openapi_server.models.history_event_activity_task_canceled_event_attributes import HistoryEventActivityTaskCanceledEventAttributes
from openapi_server.models.history_event_activity_task_completed_event_attributes import HistoryEventActivityTaskCompletedEventAttributes
from openapi_server.models.history_event_activity_task_failed_event_attributes import HistoryEventActivityTaskFailedEventAttributes
from openapi_server.models.history_event_activity_task_scheduled_event_attributes import HistoryEventActivityTaskScheduledEventAttributes
from openapi_server.models.history_event_activity_task_started_event_attributes import HistoryEventActivityTaskStartedEventAttributes
from openapi_server.models.history_event_activity_task_timed_out_event_attributes import HistoryEventActivityTaskTimedOutEventAttributes
from openapi_server.models.history_event_cancel_timer_failed_event_attributes import HistoryEventCancelTimerFailedEventAttributes
from openapi_server.models.history_event_cancel_workflow_execution_failed_event_attributes import HistoryEventCancelWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_child_workflow_execution_canceled_event_attributes import HistoryEventChildWorkflowExecutionCanceledEventAttributes
from openapi_server.models.history_event_child_workflow_execution_completed_event_attributes import HistoryEventChildWorkflowExecutionCompletedEventAttributes
from openapi_server.models.history_event_child_workflow_execution_failed_event_attributes import HistoryEventChildWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_child_workflow_execution_started_event_attributes import HistoryEventChildWorkflowExecutionStartedEventAttributes
from openapi_server.models.history_event_child_workflow_execution_terminated_event_attributes import HistoryEventChildWorkflowExecutionTerminatedEventAttributes
from openapi_server.models.history_event_child_workflow_execution_timed_out_event_attributes import HistoryEventChildWorkflowExecutionTimedOutEventAttributes
from openapi_server.models.history_event_complete_workflow_execution_failed_event_attributes import HistoryEventCompleteWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_continue_as_new_workflow_execution_failed_event_attributes import HistoryEventContinueAsNewWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_decision_task_completed_event_attributes import HistoryEventDecisionTaskCompletedEventAttributes
from openapi_server.models.history_event_decision_task_scheduled_event_attributes import HistoryEventDecisionTaskScheduledEventAttributes
from openapi_server.models.history_event_decision_task_started_event_attributes import HistoryEventDecisionTaskStartedEventAttributes
from openapi_server.models.history_event_decision_task_timed_out_event_attributes import HistoryEventDecisionTaskTimedOutEventAttributes
from openapi_server.models.history_event_external_workflow_execution_cancel_requested_event_attributes import HistoryEventExternalWorkflowExecutionCancelRequestedEventAttributes
from openapi_server.models.history_event_external_workflow_execution_signaled_event_attributes import HistoryEventExternalWorkflowExecutionSignaledEventAttributes
from openapi_server.models.history_event_fail_workflow_execution_failed_event_attributes import HistoryEventFailWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_lambda_function_completed_event_attributes import HistoryEventLambdaFunctionCompletedEventAttributes
from openapi_server.models.history_event_lambda_function_failed_event_attributes import HistoryEventLambdaFunctionFailedEventAttributes
from openapi_server.models.history_event_lambda_function_scheduled_event_attributes import HistoryEventLambdaFunctionScheduledEventAttributes
from openapi_server.models.history_event_lambda_function_started_event_attributes import HistoryEventLambdaFunctionStartedEventAttributes
from openapi_server.models.history_event_lambda_function_timed_out_event_attributes import HistoryEventLambdaFunctionTimedOutEventAttributes
from openapi_server.models.history_event_marker_recorded_event_attributes import HistoryEventMarkerRecordedEventAttributes
from openapi_server.models.history_event_record_marker_failed_event_attributes import HistoryEventRecordMarkerFailedEventAttributes
from openapi_server.models.history_event_request_cancel_activity_task_failed_event_attributes import HistoryEventRequestCancelActivityTaskFailedEventAttributes
from openapi_server.models.history_event_request_cancel_external_workflow_execution_failed_event_attributes import HistoryEventRequestCancelExternalWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_request_cancel_external_workflow_execution_initiated_event_attributes import HistoryEventRequestCancelExternalWorkflowExecutionInitiatedEventAttributes
from openapi_server.models.history_event_schedule_activity_task_failed_event_attributes import HistoryEventScheduleActivityTaskFailedEventAttributes
from openapi_server.models.history_event_schedule_lambda_function_failed_event_attributes import HistoryEventScheduleLambdaFunctionFailedEventAttributes
from openapi_server.models.history_event_signal_external_workflow_execution_failed_event_attributes import HistoryEventSignalExternalWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_signal_external_workflow_execution_initiated_event_attributes import HistoryEventSignalExternalWorkflowExecutionInitiatedEventAttributes
from openapi_server.models.history_event_start_child_workflow_execution_failed_event_attributes import HistoryEventStartChildWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_start_child_workflow_execution_initiated_event_attributes import HistoryEventStartChildWorkflowExecutionInitiatedEventAttributes
from openapi_server.models.history_event_start_lambda_function_failed_event_attributes import HistoryEventStartLambdaFunctionFailedEventAttributes
from openapi_server.models.history_event_start_timer_failed_event_attributes import HistoryEventStartTimerFailedEventAttributes
from openapi_server.models.history_event_timer_canceled_event_attributes import HistoryEventTimerCanceledEventAttributes
from openapi_server.models.history_event_timer_fired_event_attributes import HistoryEventTimerFiredEventAttributes
from openapi_server.models.history_event_timer_started_event_attributes import HistoryEventTimerStartedEventAttributes
from openapi_server.models.history_event_workflow_execution_cancel_requested_event_attributes import HistoryEventWorkflowExecutionCancelRequestedEventAttributes
from openapi_server.models.history_event_workflow_execution_canceled_event_attributes import HistoryEventWorkflowExecutionCanceledEventAttributes
from openapi_server.models.history_event_workflow_execution_completed_event_attributes import HistoryEventWorkflowExecutionCompletedEventAttributes
from openapi_server.models.history_event_workflow_execution_continued_as_new_event_attributes import HistoryEventWorkflowExecutionContinuedAsNewEventAttributes
from openapi_server.models.history_event_workflow_execution_failed_event_attributes import HistoryEventWorkflowExecutionFailedEventAttributes
from openapi_server.models.history_event_workflow_execution_signaled_event_attributes import HistoryEventWorkflowExecutionSignaledEventAttributes
from openapi_server.models.history_event_workflow_execution_started_event_attributes import HistoryEventWorkflowExecutionStartedEventAttributes
from openapi_server.models.history_event_workflow_execution_terminated_event_attributes import HistoryEventWorkflowExecutionTerminatedEventAttributes
from openapi_server.models.history_event_workflow_execution_timed_out_event_attributes import HistoryEventWorkflowExecutionTimedOutEventAttributes
from openapi_server import util


class HistoryEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event_timestamp: datetime=None, event_type: EventType=None, event_id: int=None, workflow_execution_started_event_attributes: HistoryEventWorkflowExecutionStartedEventAttributes=None, workflow_execution_completed_event_attributes: HistoryEventWorkflowExecutionCompletedEventAttributes=None, complete_workflow_execution_failed_event_attributes: HistoryEventCompleteWorkflowExecutionFailedEventAttributes=None, workflow_execution_failed_event_attributes: HistoryEventWorkflowExecutionFailedEventAttributes=None, fail_workflow_execution_failed_event_attributes: HistoryEventFailWorkflowExecutionFailedEventAttributes=None, workflow_execution_timed_out_event_attributes: HistoryEventWorkflowExecutionTimedOutEventAttributes=None, workflow_execution_canceled_event_attributes: HistoryEventWorkflowExecutionCanceledEventAttributes=None, cancel_workflow_execution_failed_event_attributes: HistoryEventCancelWorkflowExecutionFailedEventAttributes=None, workflow_execution_continued_as_new_event_attributes: HistoryEventWorkflowExecutionContinuedAsNewEventAttributes=None, continue_as_new_workflow_execution_failed_event_attributes: HistoryEventContinueAsNewWorkflowExecutionFailedEventAttributes=None, workflow_execution_terminated_event_attributes: HistoryEventWorkflowExecutionTerminatedEventAttributes=None, workflow_execution_cancel_requested_event_attributes: HistoryEventWorkflowExecutionCancelRequestedEventAttributes=None, decision_task_scheduled_event_attributes: HistoryEventDecisionTaskScheduledEventAttributes=None, decision_task_started_event_attributes: HistoryEventDecisionTaskStartedEventAttributes=None, decision_task_completed_event_attributes: HistoryEventDecisionTaskCompletedEventAttributes=None, decision_task_timed_out_event_attributes: HistoryEventDecisionTaskTimedOutEventAttributes=None, activity_task_scheduled_event_attributes: HistoryEventActivityTaskScheduledEventAttributes=None, activity_task_started_event_attributes: HistoryEventActivityTaskStartedEventAttributes=None, activity_task_completed_event_attributes: HistoryEventActivityTaskCompletedEventAttributes=None, activity_task_failed_event_attributes: HistoryEventActivityTaskFailedEventAttributes=None, activity_task_timed_out_event_attributes: HistoryEventActivityTaskTimedOutEventAttributes=None, activity_task_canceled_event_attributes: HistoryEventActivityTaskCanceledEventAttributes=None, activity_task_cancel_requested_event_attributes: HistoryEventActivityTaskCancelRequestedEventAttributes=None, workflow_execution_signaled_event_attributes: HistoryEventWorkflowExecutionSignaledEventAttributes=None, marker_recorded_event_attributes: HistoryEventMarkerRecordedEventAttributes=None, record_marker_failed_event_attributes: HistoryEventRecordMarkerFailedEventAttributes=None, timer_started_event_attributes: HistoryEventTimerStartedEventAttributes=None, timer_fired_event_attributes: HistoryEventTimerFiredEventAttributes=None, timer_canceled_event_attributes: HistoryEventTimerCanceledEventAttributes=None, start_child_workflow_execution_initiated_event_attributes: HistoryEventStartChildWorkflowExecutionInitiatedEventAttributes=None, child_workflow_execution_started_event_attributes: HistoryEventChildWorkflowExecutionStartedEventAttributes=None, child_workflow_execution_completed_event_attributes: HistoryEventChildWorkflowExecutionCompletedEventAttributes=None, child_workflow_execution_failed_event_attributes: HistoryEventChildWorkflowExecutionFailedEventAttributes=None, child_workflow_execution_timed_out_event_attributes: HistoryEventChildWorkflowExecutionTimedOutEventAttributes=None, child_workflow_execution_canceled_event_attributes: HistoryEventChildWorkflowExecutionCanceledEventAttributes=None, child_workflow_execution_terminated_event_attributes: HistoryEventChildWorkflowExecutionTerminatedEventAttributes=None, signal_external_workflow_execution_initiated_event_attributes: HistoryEventSignalExternalWorkflowExecutionInitiatedEventAttributes=None, external_workflow_execution_signaled_event_attributes: HistoryEventExternalWorkflowExecutionSignaledEventAttributes=None, signal_external_workflow_execution_failed_event_attributes: HistoryEventSignalExternalWorkflowExecutionFailedEventAttributes=None, external_workflow_execution_cancel_requested_event_attributes: HistoryEventExternalWorkflowExecutionCancelRequestedEventAttributes=None, request_cancel_external_workflow_execution_initiated_event_attributes: HistoryEventRequestCancelExternalWorkflowExecutionInitiatedEventAttributes=None, request_cancel_external_workflow_execution_failed_event_attributes: HistoryEventRequestCancelExternalWorkflowExecutionFailedEventAttributes=None, schedule_activity_task_failed_event_attributes: HistoryEventScheduleActivityTaskFailedEventAttributes=None, request_cancel_activity_task_failed_event_attributes: HistoryEventRequestCancelActivityTaskFailedEventAttributes=None, start_timer_failed_event_attributes: HistoryEventStartTimerFailedEventAttributes=None, cancel_timer_failed_event_attributes: HistoryEventCancelTimerFailedEventAttributes=None, start_child_workflow_execution_failed_event_attributes: HistoryEventStartChildWorkflowExecutionFailedEventAttributes=None, lambda_function_scheduled_event_attributes: HistoryEventLambdaFunctionScheduledEventAttributes=None, lambda_function_started_event_attributes: HistoryEventLambdaFunctionStartedEventAttributes=None, lambda_function_completed_event_attributes: HistoryEventLambdaFunctionCompletedEventAttributes=None, lambda_function_failed_event_attributes: HistoryEventLambdaFunctionFailedEventAttributes=None, lambda_function_timed_out_event_attributes: HistoryEventLambdaFunctionTimedOutEventAttributes=None, schedule_lambda_function_failed_event_attributes: HistoryEventScheduleLambdaFunctionFailedEventAttributes=None, start_lambda_function_failed_event_attributes: HistoryEventStartLambdaFunctionFailedEventAttributes=None):
        """HistoryEvent - a model defined in OpenAPI

        :param event_timestamp: The event_timestamp of this HistoryEvent.
        :param event_type: The event_type of this HistoryEvent.
        :param event_id: The event_id of this HistoryEvent.
        :param workflow_execution_started_event_attributes: The workflow_execution_started_event_attributes of this HistoryEvent.
        :param workflow_execution_completed_event_attributes: The workflow_execution_completed_event_attributes of this HistoryEvent.
        :param complete_workflow_execution_failed_event_attributes: The complete_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param workflow_execution_failed_event_attributes: The workflow_execution_failed_event_attributes of this HistoryEvent.
        :param fail_workflow_execution_failed_event_attributes: The fail_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param workflow_execution_timed_out_event_attributes: The workflow_execution_timed_out_event_attributes of this HistoryEvent.
        :param workflow_execution_canceled_event_attributes: The workflow_execution_canceled_event_attributes of this HistoryEvent.
        :param cancel_workflow_execution_failed_event_attributes: The cancel_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param workflow_execution_continued_as_new_event_attributes: The workflow_execution_continued_as_new_event_attributes of this HistoryEvent.
        :param continue_as_new_workflow_execution_failed_event_attributes: The continue_as_new_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param workflow_execution_terminated_event_attributes: The workflow_execution_terminated_event_attributes of this HistoryEvent.
        :param workflow_execution_cancel_requested_event_attributes: The workflow_execution_cancel_requested_event_attributes of this HistoryEvent.
        :param decision_task_scheduled_event_attributes: The decision_task_scheduled_event_attributes of this HistoryEvent.
        :param decision_task_started_event_attributes: The decision_task_started_event_attributes of this HistoryEvent.
        :param decision_task_completed_event_attributes: The decision_task_completed_event_attributes of this HistoryEvent.
        :param decision_task_timed_out_event_attributes: The decision_task_timed_out_event_attributes of this HistoryEvent.
        :param activity_task_scheduled_event_attributes: The activity_task_scheduled_event_attributes of this HistoryEvent.
        :param activity_task_started_event_attributes: The activity_task_started_event_attributes of this HistoryEvent.
        :param activity_task_completed_event_attributes: The activity_task_completed_event_attributes of this HistoryEvent.
        :param activity_task_failed_event_attributes: The activity_task_failed_event_attributes of this HistoryEvent.
        :param activity_task_timed_out_event_attributes: The activity_task_timed_out_event_attributes of this HistoryEvent.
        :param activity_task_canceled_event_attributes: The activity_task_canceled_event_attributes of this HistoryEvent.
        :param activity_task_cancel_requested_event_attributes: The activity_task_cancel_requested_event_attributes of this HistoryEvent.
        :param workflow_execution_signaled_event_attributes: The workflow_execution_signaled_event_attributes of this HistoryEvent.
        :param marker_recorded_event_attributes: The marker_recorded_event_attributes of this HistoryEvent.
        :param record_marker_failed_event_attributes: The record_marker_failed_event_attributes of this HistoryEvent.
        :param timer_started_event_attributes: The timer_started_event_attributes of this HistoryEvent.
        :param timer_fired_event_attributes: The timer_fired_event_attributes of this HistoryEvent.
        :param timer_canceled_event_attributes: The timer_canceled_event_attributes of this HistoryEvent.
        :param start_child_workflow_execution_initiated_event_attributes: The start_child_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :param child_workflow_execution_started_event_attributes: The child_workflow_execution_started_event_attributes of this HistoryEvent.
        :param child_workflow_execution_completed_event_attributes: The child_workflow_execution_completed_event_attributes of this HistoryEvent.
        :param child_workflow_execution_failed_event_attributes: The child_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param child_workflow_execution_timed_out_event_attributes: The child_workflow_execution_timed_out_event_attributes of this HistoryEvent.
        :param child_workflow_execution_canceled_event_attributes: The child_workflow_execution_canceled_event_attributes of this HistoryEvent.
        :param child_workflow_execution_terminated_event_attributes: The child_workflow_execution_terminated_event_attributes of this HistoryEvent.
        :param signal_external_workflow_execution_initiated_event_attributes: The signal_external_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :param external_workflow_execution_signaled_event_attributes: The external_workflow_execution_signaled_event_attributes of this HistoryEvent.
        :param signal_external_workflow_execution_failed_event_attributes: The signal_external_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param external_workflow_execution_cancel_requested_event_attributes: The external_workflow_execution_cancel_requested_event_attributes of this HistoryEvent.
        :param request_cancel_external_workflow_execution_initiated_event_attributes: The request_cancel_external_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :param request_cancel_external_workflow_execution_failed_event_attributes: The request_cancel_external_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param schedule_activity_task_failed_event_attributes: The schedule_activity_task_failed_event_attributes of this HistoryEvent.
        :param request_cancel_activity_task_failed_event_attributes: The request_cancel_activity_task_failed_event_attributes of this HistoryEvent.
        :param start_timer_failed_event_attributes: The start_timer_failed_event_attributes of this HistoryEvent.
        :param cancel_timer_failed_event_attributes: The cancel_timer_failed_event_attributes of this HistoryEvent.
        :param start_child_workflow_execution_failed_event_attributes: The start_child_workflow_execution_failed_event_attributes of this HistoryEvent.
        :param lambda_function_scheduled_event_attributes: The lambda_function_scheduled_event_attributes of this HistoryEvent.
        :param lambda_function_started_event_attributes: The lambda_function_started_event_attributes of this HistoryEvent.
        :param lambda_function_completed_event_attributes: The lambda_function_completed_event_attributes of this HistoryEvent.
        :param lambda_function_failed_event_attributes: The lambda_function_failed_event_attributes of this HistoryEvent.
        :param lambda_function_timed_out_event_attributes: The lambda_function_timed_out_event_attributes of this HistoryEvent.
        :param schedule_lambda_function_failed_event_attributes: The schedule_lambda_function_failed_event_attributes of this HistoryEvent.
        :param start_lambda_function_failed_event_attributes: The start_lambda_function_failed_event_attributes of this HistoryEvent.
        """
        self.openapi_types = {
            'event_timestamp': datetime,
            'event_type': EventType,
            'event_id': int,
            'workflow_execution_started_event_attributes': HistoryEventWorkflowExecutionStartedEventAttributes,
            'workflow_execution_completed_event_attributes': HistoryEventWorkflowExecutionCompletedEventAttributes,
            'complete_workflow_execution_failed_event_attributes': HistoryEventCompleteWorkflowExecutionFailedEventAttributes,
            'workflow_execution_failed_event_attributes': HistoryEventWorkflowExecutionFailedEventAttributes,
            'fail_workflow_execution_failed_event_attributes': HistoryEventFailWorkflowExecutionFailedEventAttributes,
            'workflow_execution_timed_out_event_attributes': HistoryEventWorkflowExecutionTimedOutEventAttributes,
            'workflow_execution_canceled_event_attributes': HistoryEventWorkflowExecutionCanceledEventAttributes,
            'cancel_workflow_execution_failed_event_attributes': HistoryEventCancelWorkflowExecutionFailedEventAttributes,
            'workflow_execution_continued_as_new_event_attributes': HistoryEventWorkflowExecutionContinuedAsNewEventAttributes,
            'continue_as_new_workflow_execution_failed_event_attributes': HistoryEventContinueAsNewWorkflowExecutionFailedEventAttributes,
            'workflow_execution_terminated_event_attributes': HistoryEventWorkflowExecutionTerminatedEventAttributes,
            'workflow_execution_cancel_requested_event_attributes': HistoryEventWorkflowExecutionCancelRequestedEventAttributes,
            'decision_task_scheduled_event_attributes': HistoryEventDecisionTaskScheduledEventAttributes,
            'decision_task_started_event_attributes': HistoryEventDecisionTaskStartedEventAttributes,
            'decision_task_completed_event_attributes': HistoryEventDecisionTaskCompletedEventAttributes,
            'decision_task_timed_out_event_attributes': HistoryEventDecisionTaskTimedOutEventAttributes,
            'activity_task_scheduled_event_attributes': HistoryEventActivityTaskScheduledEventAttributes,
            'activity_task_started_event_attributes': HistoryEventActivityTaskStartedEventAttributes,
            'activity_task_completed_event_attributes': HistoryEventActivityTaskCompletedEventAttributes,
            'activity_task_failed_event_attributes': HistoryEventActivityTaskFailedEventAttributes,
            'activity_task_timed_out_event_attributes': HistoryEventActivityTaskTimedOutEventAttributes,
            'activity_task_canceled_event_attributes': HistoryEventActivityTaskCanceledEventAttributes,
            'activity_task_cancel_requested_event_attributes': HistoryEventActivityTaskCancelRequestedEventAttributes,
            'workflow_execution_signaled_event_attributes': HistoryEventWorkflowExecutionSignaledEventAttributes,
            'marker_recorded_event_attributes': HistoryEventMarkerRecordedEventAttributes,
            'record_marker_failed_event_attributes': HistoryEventRecordMarkerFailedEventAttributes,
            'timer_started_event_attributes': HistoryEventTimerStartedEventAttributes,
            'timer_fired_event_attributes': HistoryEventTimerFiredEventAttributes,
            'timer_canceled_event_attributes': HistoryEventTimerCanceledEventAttributes,
            'start_child_workflow_execution_initiated_event_attributes': HistoryEventStartChildWorkflowExecutionInitiatedEventAttributes,
            'child_workflow_execution_started_event_attributes': HistoryEventChildWorkflowExecutionStartedEventAttributes,
            'child_workflow_execution_completed_event_attributes': HistoryEventChildWorkflowExecutionCompletedEventAttributes,
            'child_workflow_execution_failed_event_attributes': HistoryEventChildWorkflowExecutionFailedEventAttributes,
            'child_workflow_execution_timed_out_event_attributes': HistoryEventChildWorkflowExecutionTimedOutEventAttributes,
            'child_workflow_execution_canceled_event_attributes': HistoryEventChildWorkflowExecutionCanceledEventAttributes,
            'child_workflow_execution_terminated_event_attributes': HistoryEventChildWorkflowExecutionTerminatedEventAttributes,
            'signal_external_workflow_execution_initiated_event_attributes': HistoryEventSignalExternalWorkflowExecutionInitiatedEventAttributes,
            'external_workflow_execution_signaled_event_attributes': HistoryEventExternalWorkflowExecutionSignaledEventAttributes,
            'signal_external_workflow_execution_failed_event_attributes': HistoryEventSignalExternalWorkflowExecutionFailedEventAttributes,
            'external_workflow_execution_cancel_requested_event_attributes': HistoryEventExternalWorkflowExecutionCancelRequestedEventAttributes,
            'request_cancel_external_workflow_execution_initiated_event_attributes': HistoryEventRequestCancelExternalWorkflowExecutionInitiatedEventAttributes,
            'request_cancel_external_workflow_execution_failed_event_attributes': HistoryEventRequestCancelExternalWorkflowExecutionFailedEventAttributes,
            'schedule_activity_task_failed_event_attributes': HistoryEventScheduleActivityTaskFailedEventAttributes,
            'request_cancel_activity_task_failed_event_attributes': HistoryEventRequestCancelActivityTaskFailedEventAttributes,
            'start_timer_failed_event_attributes': HistoryEventStartTimerFailedEventAttributes,
            'cancel_timer_failed_event_attributes': HistoryEventCancelTimerFailedEventAttributes,
            'start_child_workflow_execution_failed_event_attributes': HistoryEventStartChildWorkflowExecutionFailedEventAttributes,
            'lambda_function_scheduled_event_attributes': HistoryEventLambdaFunctionScheduledEventAttributes,
            'lambda_function_started_event_attributes': HistoryEventLambdaFunctionStartedEventAttributes,
            'lambda_function_completed_event_attributes': HistoryEventLambdaFunctionCompletedEventAttributes,
            'lambda_function_failed_event_attributes': HistoryEventLambdaFunctionFailedEventAttributes,
            'lambda_function_timed_out_event_attributes': HistoryEventLambdaFunctionTimedOutEventAttributes,
            'schedule_lambda_function_failed_event_attributes': HistoryEventScheduleLambdaFunctionFailedEventAttributes,
            'start_lambda_function_failed_event_attributes': HistoryEventStartLambdaFunctionFailedEventAttributes
        }

        self.attribute_map = {
            'event_timestamp': 'eventTimestamp',
            'event_type': 'eventType',
            'event_id': 'eventId',
            'workflow_execution_started_event_attributes': 'workflowExecutionStartedEventAttributes',
            'workflow_execution_completed_event_attributes': 'workflowExecutionCompletedEventAttributes',
            'complete_workflow_execution_failed_event_attributes': 'completeWorkflowExecutionFailedEventAttributes',
            'workflow_execution_failed_event_attributes': 'workflowExecutionFailedEventAttributes',
            'fail_workflow_execution_failed_event_attributes': 'failWorkflowExecutionFailedEventAttributes',
            'workflow_execution_timed_out_event_attributes': 'workflowExecutionTimedOutEventAttributes',
            'workflow_execution_canceled_event_attributes': 'workflowExecutionCanceledEventAttributes',
            'cancel_workflow_execution_failed_event_attributes': 'cancelWorkflowExecutionFailedEventAttributes',
            'workflow_execution_continued_as_new_event_attributes': 'workflowExecutionContinuedAsNewEventAttributes',
            'continue_as_new_workflow_execution_failed_event_attributes': 'continueAsNewWorkflowExecutionFailedEventAttributes',
            'workflow_execution_terminated_event_attributes': 'workflowExecutionTerminatedEventAttributes',
            'workflow_execution_cancel_requested_event_attributes': 'workflowExecutionCancelRequestedEventAttributes',
            'decision_task_scheduled_event_attributes': 'decisionTaskScheduledEventAttributes',
            'decision_task_started_event_attributes': 'decisionTaskStartedEventAttributes',
            'decision_task_completed_event_attributes': 'decisionTaskCompletedEventAttributes',
            'decision_task_timed_out_event_attributes': 'decisionTaskTimedOutEventAttributes',
            'activity_task_scheduled_event_attributes': 'activityTaskScheduledEventAttributes',
            'activity_task_started_event_attributes': 'activityTaskStartedEventAttributes',
            'activity_task_completed_event_attributes': 'activityTaskCompletedEventAttributes',
            'activity_task_failed_event_attributes': 'activityTaskFailedEventAttributes',
            'activity_task_timed_out_event_attributes': 'activityTaskTimedOutEventAttributes',
            'activity_task_canceled_event_attributes': 'activityTaskCanceledEventAttributes',
            'activity_task_cancel_requested_event_attributes': 'activityTaskCancelRequestedEventAttributes',
            'workflow_execution_signaled_event_attributes': 'workflowExecutionSignaledEventAttributes',
            'marker_recorded_event_attributes': 'markerRecordedEventAttributes',
            'record_marker_failed_event_attributes': 'recordMarkerFailedEventAttributes',
            'timer_started_event_attributes': 'timerStartedEventAttributes',
            'timer_fired_event_attributes': 'timerFiredEventAttributes',
            'timer_canceled_event_attributes': 'timerCanceledEventAttributes',
            'start_child_workflow_execution_initiated_event_attributes': 'startChildWorkflowExecutionInitiatedEventAttributes',
            'child_workflow_execution_started_event_attributes': 'childWorkflowExecutionStartedEventAttributes',
            'child_workflow_execution_completed_event_attributes': 'childWorkflowExecutionCompletedEventAttributes',
            'child_workflow_execution_failed_event_attributes': 'childWorkflowExecutionFailedEventAttributes',
            'child_workflow_execution_timed_out_event_attributes': 'childWorkflowExecutionTimedOutEventAttributes',
            'child_workflow_execution_canceled_event_attributes': 'childWorkflowExecutionCanceledEventAttributes',
            'child_workflow_execution_terminated_event_attributes': 'childWorkflowExecutionTerminatedEventAttributes',
            'signal_external_workflow_execution_initiated_event_attributes': 'signalExternalWorkflowExecutionInitiatedEventAttributes',
            'external_workflow_execution_signaled_event_attributes': 'externalWorkflowExecutionSignaledEventAttributes',
            'signal_external_workflow_execution_failed_event_attributes': 'signalExternalWorkflowExecutionFailedEventAttributes',
            'external_workflow_execution_cancel_requested_event_attributes': 'externalWorkflowExecutionCancelRequestedEventAttributes',
            'request_cancel_external_workflow_execution_initiated_event_attributes': 'requestCancelExternalWorkflowExecutionInitiatedEventAttributes',
            'request_cancel_external_workflow_execution_failed_event_attributes': 'requestCancelExternalWorkflowExecutionFailedEventAttributes',
            'schedule_activity_task_failed_event_attributes': 'scheduleActivityTaskFailedEventAttributes',
            'request_cancel_activity_task_failed_event_attributes': 'requestCancelActivityTaskFailedEventAttributes',
            'start_timer_failed_event_attributes': 'startTimerFailedEventAttributes',
            'cancel_timer_failed_event_attributes': 'cancelTimerFailedEventAttributes',
            'start_child_workflow_execution_failed_event_attributes': 'startChildWorkflowExecutionFailedEventAttributes',
            'lambda_function_scheduled_event_attributes': 'lambdaFunctionScheduledEventAttributes',
            'lambda_function_started_event_attributes': 'lambdaFunctionStartedEventAttributes',
            'lambda_function_completed_event_attributes': 'lambdaFunctionCompletedEventAttributes',
            'lambda_function_failed_event_attributes': 'lambdaFunctionFailedEventAttributes',
            'lambda_function_timed_out_event_attributes': 'lambdaFunctionTimedOutEventAttributes',
            'schedule_lambda_function_failed_event_attributes': 'scheduleLambdaFunctionFailedEventAttributes',
            'start_lambda_function_failed_event_attributes': 'startLambdaFunctionFailedEventAttributes'
        }

        self._event_timestamp = event_timestamp
        self._event_type = event_type
        self._event_id = event_id
        self._workflow_execution_started_event_attributes = workflow_execution_started_event_attributes
        self._workflow_execution_completed_event_attributes = workflow_execution_completed_event_attributes
        self._complete_workflow_execution_failed_event_attributes = complete_workflow_execution_failed_event_attributes
        self._workflow_execution_failed_event_attributes = workflow_execution_failed_event_attributes
        self._fail_workflow_execution_failed_event_attributes = fail_workflow_execution_failed_event_attributes
        self._workflow_execution_timed_out_event_attributes = workflow_execution_timed_out_event_attributes
        self._workflow_execution_canceled_event_attributes = workflow_execution_canceled_event_attributes
        self._cancel_workflow_execution_failed_event_attributes = cancel_workflow_execution_failed_event_attributes
        self._workflow_execution_continued_as_new_event_attributes = workflow_execution_continued_as_new_event_attributes
        self._continue_as_new_workflow_execution_failed_event_attributes = continue_as_new_workflow_execution_failed_event_attributes
        self._workflow_execution_terminated_event_attributes = workflow_execution_terminated_event_attributes
        self._workflow_execution_cancel_requested_event_attributes = workflow_execution_cancel_requested_event_attributes
        self._decision_task_scheduled_event_attributes = decision_task_scheduled_event_attributes
        self._decision_task_started_event_attributes = decision_task_started_event_attributes
        self._decision_task_completed_event_attributes = decision_task_completed_event_attributes
        self._decision_task_timed_out_event_attributes = decision_task_timed_out_event_attributes
        self._activity_task_scheduled_event_attributes = activity_task_scheduled_event_attributes
        self._activity_task_started_event_attributes = activity_task_started_event_attributes
        self._activity_task_completed_event_attributes = activity_task_completed_event_attributes
        self._activity_task_failed_event_attributes = activity_task_failed_event_attributes
        self._activity_task_timed_out_event_attributes = activity_task_timed_out_event_attributes
        self._activity_task_canceled_event_attributes = activity_task_canceled_event_attributes
        self._activity_task_cancel_requested_event_attributes = activity_task_cancel_requested_event_attributes
        self._workflow_execution_signaled_event_attributes = workflow_execution_signaled_event_attributes
        self._marker_recorded_event_attributes = marker_recorded_event_attributes
        self._record_marker_failed_event_attributes = record_marker_failed_event_attributes
        self._timer_started_event_attributes = timer_started_event_attributes
        self._timer_fired_event_attributes = timer_fired_event_attributes
        self._timer_canceled_event_attributes = timer_canceled_event_attributes
        self._start_child_workflow_execution_initiated_event_attributes = start_child_workflow_execution_initiated_event_attributes
        self._child_workflow_execution_started_event_attributes = child_workflow_execution_started_event_attributes
        self._child_workflow_execution_completed_event_attributes = child_workflow_execution_completed_event_attributes
        self._child_workflow_execution_failed_event_attributes = child_workflow_execution_failed_event_attributes
        self._child_workflow_execution_timed_out_event_attributes = child_workflow_execution_timed_out_event_attributes
        self._child_workflow_execution_canceled_event_attributes = child_workflow_execution_canceled_event_attributes
        self._child_workflow_execution_terminated_event_attributes = child_workflow_execution_terminated_event_attributes
        self._signal_external_workflow_execution_initiated_event_attributes = signal_external_workflow_execution_initiated_event_attributes
        self._external_workflow_execution_signaled_event_attributes = external_workflow_execution_signaled_event_attributes
        self._signal_external_workflow_execution_failed_event_attributes = signal_external_workflow_execution_failed_event_attributes
        self._external_workflow_execution_cancel_requested_event_attributes = external_workflow_execution_cancel_requested_event_attributes
        self._request_cancel_external_workflow_execution_initiated_event_attributes = request_cancel_external_workflow_execution_initiated_event_attributes
        self._request_cancel_external_workflow_execution_failed_event_attributes = request_cancel_external_workflow_execution_failed_event_attributes
        self._schedule_activity_task_failed_event_attributes = schedule_activity_task_failed_event_attributes
        self._request_cancel_activity_task_failed_event_attributes = request_cancel_activity_task_failed_event_attributes
        self._start_timer_failed_event_attributes = start_timer_failed_event_attributes
        self._cancel_timer_failed_event_attributes = cancel_timer_failed_event_attributes
        self._start_child_workflow_execution_failed_event_attributes = start_child_workflow_execution_failed_event_attributes
        self._lambda_function_scheduled_event_attributes = lambda_function_scheduled_event_attributes
        self._lambda_function_started_event_attributes = lambda_function_started_event_attributes
        self._lambda_function_completed_event_attributes = lambda_function_completed_event_attributes
        self._lambda_function_failed_event_attributes = lambda_function_failed_event_attributes
        self._lambda_function_timed_out_event_attributes = lambda_function_timed_out_event_attributes
        self._schedule_lambda_function_failed_event_attributes = schedule_lambda_function_failed_event_attributes
        self._start_lambda_function_failed_event_attributes = start_lambda_function_failed_event_attributes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HistoryEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HistoryEvent of this HistoryEvent.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_timestamp(self):
        """Gets the event_timestamp of this HistoryEvent.


        :return: The event_timestamp of this HistoryEvent.
        :rtype: datetime
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        """Sets the event_timestamp of this HistoryEvent.


        :param event_timestamp: The event_timestamp of this HistoryEvent.
        :type event_timestamp: datetime
        """
        if event_timestamp is None:
            raise ValueError("Invalid value for `event_timestamp`, must not be `None`")

        self._event_timestamp = event_timestamp

    @property
    def event_type(self):
        """Gets the event_type of this HistoryEvent.


        :return: The event_type of this HistoryEvent.
        :rtype: EventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this HistoryEvent.


        :param event_type: The event_type of this HistoryEvent.
        :type event_type: EventType
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")

        self._event_type = event_type

    @property
    def event_id(self):
        """Gets the event_id of this HistoryEvent.


        :return: The event_id of this HistoryEvent.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this HistoryEvent.


        :param event_id: The event_id of this HistoryEvent.
        :type event_id: int
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")

        self._event_id = event_id

    @property
    def workflow_execution_started_event_attributes(self):
        """Gets the workflow_execution_started_event_attributes of this HistoryEvent.


        :return: The workflow_execution_started_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionStartedEventAttributes
        """
        return self._workflow_execution_started_event_attributes

    @workflow_execution_started_event_attributes.setter
    def workflow_execution_started_event_attributes(self, workflow_execution_started_event_attributes):
        """Sets the workflow_execution_started_event_attributes of this HistoryEvent.


        :param workflow_execution_started_event_attributes: The workflow_execution_started_event_attributes of this HistoryEvent.
        :type workflow_execution_started_event_attributes: HistoryEventWorkflowExecutionStartedEventAttributes
        """

        self._workflow_execution_started_event_attributes = workflow_execution_started_event_attributes

    @property
    def workflow_execution_completed_event_attributes(self):
        """Gets the workflow_execution_completed_event_attributes of this HistoryEvent.


        :return: The workflow_execution_completed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionCompletedEventAttributes
        """
        return self._workflow_execution_completed_event_attributes

    @workflow_execution_completed_event_attributes.setter
    def workflow_execution_completed_event_attributes(self, workflow_execution_completed_event_attributes):
        """Sets the workflow_execution_completed_event_attributes of this HistoryEvent.


        :param workflow_execution_completed_event_attributes: The workflow_execution_completed_event_attributes of this HistoryEvent.
        :type workflow_execution_completed_event_attributes: HistoryEventWorkflowExecutionCompletedEventAttributes
        """

        self._workflow_execution_completed_event_attributes = workflow_execution_completed_event_attributes

    @property
    def complete_workflow_execution_failed_event_attributes(self):
        """Gets the complete_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The complete_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventCompleteWorkflowExecutionFailedEventAttributes
        """
        return self._complete_workflow_execution_failed_event_attributes

    @complete_workflow_execution_failed_event_attributes.setter
    def complete_workflow_execution_failed_event_attributes(self, complete_workflow_execution_failed_event_attributes):
        """Sets the complete_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param complete_workflow_execution_failed_event_attributes: The complete_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type complete_workflow_execution_failed_event_attributes: HistoryEventCompleteWorkflowExecutionFailedEventAttributes
        """

        self._complete_workflow_execution_failed_event_attributes = complete_workflow_execution_failed_event_attributes

    @property
    def workflow_execution_failed_event_attributes(self):
        """Gets the workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionFailedEventAttributes
        """
        return self._workflow_execution_failed_event_attributes

    @workflow_execution_failed_event_attributes.setter
    def workflow_execution_failed_event_attributes(self, workflow_execution_failed_event_attributes):
        """Sets the workflow_execution_failed_event_attributes of this HistoryEvent.


        :param workflow_execution_failed_event_attributes: The workflow_execution_failed_event_attributes of this HistoryEvent.
        :type workflow_execution_failed_event_attributes: HistoryEventWorkflowExecutionFailedEventAttributes
        """

        self._workflow_execution_failed_event_attributes = workflow_execution_failed_event_attributes

    @property
    def fail_workflow_execution_failed_event_attributes(self):
        """Gets the fail_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The fail_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventFailWorkflowExecutionFailedEventAttributes
        """
        return self._fail_workflow_execution_failed_event_attributes

    @fail_workflow_execution_failed_event_attributes.setter
    def fail_workflow_execution_failed_event_attributes(self, fail_workflow_execution_failed_event_attributes):
        """Sets the fail_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param fail_workflow_execution_failed_event_attributes: The fail_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type fail_workflow_execution_failed_event_attributes: HistoryEventFailWorkflowExecutionFailedEventAttributes
        """

        self._fail_workflow_execution_failed_event_attributes = fail_workflow_execution_failed_event_attributes

    @property
    def workflow_execution_timed_out_event_attributes(self):
        """Gets the workflow_execution_timed_out_event_attributes of this HistoryEvent.


        :return: The workflow_execution_timed_out_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionTimedOutEventAttributes
        """
        return self._workflow_execution_timed_out_event_attributes

    @workflow_execution_timed_out_event_attributes.setter
    def workflow_execution_timed_out_event_attributes(self, workflow_execution_timed_out_event_attributes):
        """Sets the workflow_execution_timed_out_event_attributes of this HistoryEvent.


        :param workflow_execution_timed_out_event_attributes: The workflow_execution_timed_out_event_attributes of this HistoryEvent.
        :type workflow_execution_timed_out_event_attributes: HistoryEventWorkflowExecutionTimedOutEventAttributes
        """

        self._workflow_execution_timed_out_event_attributes = workflow_execution_timed_out_event_attributes

    @property
    def workflow_execution_canceled_event_attributes(self):
        """Gets the workflow_execution_canceled_event_attributes of this HistoryEvent.


        :return: The workflow_execution_canceled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionCanceledEventAttributes
        """
        return self._workflow_execution_canceled_event_attributes

    @workflow_execution_canceled_event_attributes.setter
    def workflow_execution_canceled_event_attributes(self, workflow_execution_canceled_event_attributes):
        """Sets the workflow_execution_canceled_event_attributes of this HistoryEvent.


        :param workflow_execution_canceled_event_attributes: The workflow_execution_canceled_event_attributes of this HistoryEvent.
        :type workflow_execution_canceled_event_attributes: HistoryEventWorkflowExecutionCanceledEventAttributes
        """

        self._workflow_execution_canceled_event_attributes = workflow_execution_canceled_event_attributes

    @property
    def cancel_workflow_execution_failed_event_attributes(self):
        """Gets the cancel_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The cancel_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventCancelWorkflowExecutionFailedEventAttributes
        """
        return self._cancel_workflow_execution_failed_event_attributes

    @cancel_workflow_execution_failed_event_attributes.setter
    def cancel_workflow_execution_failed_event_attributes(self, cancel_workflow_execution_failed_event_attributes):
        """Sets the cancel_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param cancel_workflow_execution_failed_event_attributes: The cancel_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type cancel_workflow_execution_failed_event_attributes: HistoryEventCancelWorkflowExecutionFailedEventAttributes
        """

        self._cancel_workflow_execution_failed_event_attributes = cancel_workflow_execution_failed_event_attributes

    @property
    def workflow_execution_continued_as_new_event_attributes(self):
        """Gets the workflow_execution_continued_as_new_event_attributes of this HistoryEvent.


        :return: The workflow_execution_continued_as_new_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionContinuedAsNewEventAttributes
        """
        return self._workflow_execution_continued_as_new_event_attributes

    @workflow_execution_continued_as_new_event_attributes.setter
    def workflow_execution_continued_as_new_event_attributes(self, workflow_execution_continued_as_new_event_attributes):
        """Sets the workflow_execution_continued_as_new_event_attributes of this HistoryEvent.


        :param workflow_execution_continued_as_new_event_attributes: The workflow_execution_continued_as_new_event_attributes of this HistoryEvent.
        :type workflow_execution_continued_as_new_event_attributes: HistoryEventWorkflowExecutionContinuedAsNewEventAttributes
        """

        self._workflow_execution_continued_as_new_event_attributes = workflow_execution_continued_as_new_event_attributes

    @property
    def continue_as_new_workflow_execution_failed_event_attributes(self):
        """Gets the continue_as_new_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The continue_as_new_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventContinueAsNewWorkflowExecutionFailedEventAttributes
        """
        return self._continue_as_new_workflow_execution_failed_event_attributes

    @continue_as_new_workflow_execution_failed_event_attributes.setter
    def continue_as_new_workflow_execution_failed_event_attributes(self, continue_as_new_workflow_execution_failed_event_attributes):
        """Sets the continue_as_new_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param continue_as_new_workflow_execution_failed_event_attributes: The continue_as_new_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type continue_as_new_workflow_execution_failed_event_attributes: HistoryEventContinueAsNewWorkflowExecutionFailedEventAttributes
        """

        self._continue_as_new_workflow_execution_failed_event_attributes = continue_as_new_workflow_execution_failed_event_attributes

    @property
    def workflow_execution_terminated_event_attributes(self):
        """Gets the workflow_execution_terminated_event_attributes of this HistoryEvent.


        :return: The workflow_execution_terminated_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionTerminatedEventAttributes
        """
        return self._workflow_execution_terminated_event_attributes

    @workflow_execution_terminated_event_attributes.setter
    def workflow_execution_terminated_event_attributes(self, workflow_execution_terminated_event_attributes):
        """Sets the workflow_execution_terminated_event_attributes of this HistoryEvent.


        :param workflow_execution_terminated_event_attributes: The workflow_execution_terminated_event_attributes of this HistoryEvent.
        :type workflow_execution_terminated_event_attributes: HistoryEventWorkflowExecutionTerminatedEventAttributes
        """

        self._workflow_execution_terminated_event_attributes = workflow_execution_terminated_event_attributes

    @property
    def workflow_execution_cancel_requested_event_attributes(self):
        """Gets the workflow_execution_cancel_requested_event_attributes of this HistoryEvent.


        :return: The workflow_execution_cancel_requested_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionCancelRequestedEventAttributes
        """
        return self._workflow_execution_cancel_requested_event_attributes

    @workflow_execution_cancel_requested_event_attributes.setter
    def workflow_execution_cancel_requested_event_attributes(self, workflow_execution_cancel_requested_event_attributes):
        """Sets the workflow_execution_cancel_requested_event_attributes of this HistoryEvent.


        :param workflow_execution_cancel_requested_event_attributes: The workflow_execution_cancel_requested_event_attributes of this HistoryEvent.
        :type workflow_execution_cancel_requested_event_attributes: HistoryEventWorkflowExecutionCancelRequestedEventAttributes
        """

        self._workflow_execution_cancel_requested_event_attributes = workflow_execution_cancel_requested_event_attributes

    @property
    def decision_task_scheduled_event_attributes(self):
        """Gets the decision_task_scheduled_event_attributes of this HistoryEvent.


        :return: The decision_task_scheduled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventDecisionTaskScheduledEventAttributes
        """
        return self._decision_task_scheduled_event_attributes

    @decision_task_scheduled_event_attributes.setter
    def decision_task_scheduled_event_attributes(self, decision_task_scheduled_event_attributes):
        """Sets the decision_task_scheduled_event_attributes of this HistoryEvent.


        :param decision_task_scheduled_event_attributes: The decision_task_scheduled_event_attributes of this HistoryEvent.
        :type decision_task_scheduled_event_attributes: HistoryEventDecisionTaskScheduledEventAttributes
        """

        self._decision_task_scheduled_event_attributes = decision_task_scheduled_event_attributes

    @property
    def decision_task_started_event_attributes(self):
        """Gets the decision_task_started_event_attributes of this HistoryEvent.


        :return: The decision_task_started_event_attributes of this HistoryEvent.
        :rtype: HistoryEventDecisionTaskStartedEventAttributes
        """
        return self._decision_task_started_event_attributes

    @decision_task_started_event_attributes.setter
    def decision_task_started_event_attributes(self, decision_task_started_event_attributes):
        """Sets the decision_task_started_event_attributes of this HistoryEvent.


        :param decision_task_started_event_attributes: The decision_task_started_event_attributes of this HistoryEvent.
        :type decision_task_started_event_attributes: HistoryEventDecisionTaskStartedEventAttributes
        """

        self._decision_task_started_event_attributes = decision_task_started_event_attributes

    @property
    def decision_task_completed_event_attributes(self):
        """Gets the decision_task_completed_event_attributes of this HistoryEvent.


        :return: The decision_task_completed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventDecisionTaskCompletedEventAttributes
        """
        return self._decision_task_completed_event_attributes

    @decision_task_completed_event_attributes.setter
    def decision_task_completed_event_attributes(self, decision_task_completed_event_attributes):
        """Sets the decision_task_completed_event_attributes of this HistoryEvent.


        :param decision_task_completed_event_attributes: The decision_task_completed_event_attributes of this HistoryEvent.
        :type decision_task_completed_event_attributes: HistoryEventDecisionTaskCompletedEventAttributes
        """

        self._decision_task_completed_event_attributes = decision_task_completed_event_attributes

    @property
    def decision_task_timed_out_event_attributes(self):
        """Gets the decision_task_timed_out_event_attributes of this HistoryEvent.


        :return: The decision_task_timed_out_event_attributes of this HistoryEvent.
        :rtype: HistoryEventDecisionTaskTimedOutEventAttributes
        """
        return self._decision_task_timed_out_event_attributes

    @decision_task_timed_out_event_attributes.setter
    def decision_task_timed_out_event_attributes(self, decision_task_timed_out_event_attributes):
        """Sets the decision_task_timed_out_event_attributes of this HistoryEvent.


        :param decision_task_timed_out_event_attributes: The decision_task_timed_out_event_attributes of this HistoryEvent.
        :type decision_task_timed_out_event_attributes: HistoryEventDecisionTaskTimedOutEventAttributes
        """

        self._decision_task_timed_out_event_attributes = decision_task_timed_out_event_attributes

    @property
    def activity_task_scheduled_event_attributes(self):
        """Gets the activity_task_scheduled_event_attributes of this HistoryEvent.


        :return: The activity_task_scheduled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventActivityTaskScheduledEventAttributes
        """
        return self._activity_task_scheduled_event_attributes

    @activity_task_scheduled_event_attributes.setter
    def activity_task_scheduled_event_attributes(self, activity_task_scheduled_event_attributes):
        """Sets the activity_task_scheduled_event_attributes of this HistoryEvent.


        :param activity_task_scheduled_event_attributes: The activity_task_scheduled_event_attributes of this HistoryEvent.
        :type activity_task_scheduled_event_attributes: HistoryEventActivityTaskScheduledEventAttributes
        """

        self._activity_task_scheduled_event_attributes = activity_task_scheduled_event_attributes

    @property
    def activity_task_started_event_attributes(self):
        """Gets the activity_task_started_event_attributes of this HistoryEvent.


        :return: The activity_task_started_event_attributes of this HistoryEvent.
        :rtype: HistoryEventActivityTaskStartedEventAttributes
        """
        return self._activity_task_started_event_attributes

    @activity_task_started_event_attributes.setter
    def activity_task_started_event_attributes(self, activity_task_started_event_attributes):
        """Sets the activity_task_started_event_attributes of this HistoryEvent.


        :param activity_task_started_event_attributes: The activity_task_started_event_attributes of this HistoryEvent.
        :type activity_task_started_event_attributes: HistoryEventActivityTaskStartedEventAttributes
        """

        self._activity_task_started_event_attributes = activity_task_started_event_attributes

    @property
    def activity_task_completed_event_attributes(self):
        """Gets the activity_task_completed_event_attributes of this HistoryEvent.


        :return: The activity_task_completed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventActivityTaskCompletedEventAttributes
        """
        return self._activity_task_completed_event_attributes

    @activity_task_completed_event_attributes.setter
    def activity_task_completed_event_attributes(self, activity_task_completed_event_attributes):
        """Sets the activity_task_completed_event_attributes of this HistoryEvent.


        :param activity_task_completed_event_attributes: The activity_task_completed_event_attributes of this HistoryEvent.
        :type activity_task_completed_event_attributes: HistoryEventActivityTaskCompletedEventAttributes
        """

        self._activity_task_completed_event_attributes = activity_task_completed_event_attributes

    @property
    def activity_task_failed_event_attributes(self):
        """Gets the activity_task_failed_event_attributes of this HistoryEvent.


        :return: The activity_task_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventActivityTaskFailedEventAttributes
        """
        return self._activity_task_failed_event_attributes

    @activity_task_failed_event_attributes.setter
    def activity_task_failed_event_attributes(self, activity_task_failed_event_attributes):
        """Sets the activity_task_failed_event_attributes of this HistoryEvent.


        :param activity_task_failed_event_attributes: The activity_task_failed_event_attributes of this HistoryEvent.
        :type activity_task_failed_event_attributes: HistoryEventActivityTaskFailedEventAttributes
        """

        self._activity_task_failed_event_attributes = activity_task_failed_event_attributes

    @property
    def activity_task_timed_out_event_attributes(self):
        """Gets the activity_task_timed_out_event_attributes of this HistoryEvent.


        :return: The activity_task_timed_out_event_attributes of this HistoryEvent.
        :rtype: HistoryEventActivityTaskTimedOutEventAttributes
        """
        return self._activity_task_timed_out_event_attributes

    @activity_task_timed_out_event_attributes.setter
    def activity_task_timed_out_event_attributes(self, activity_task_timed_out_event_attributes):
        """Sets the activity_task_timed_out_event_attributes of this HistoryEvent.


        :param activity_task_timed_out_event_attributes: The activity_task_timed_out_event_attributes of this HistoryEvent.
        :type activity_task_timed_out_event_attributes: HistoryEventActivityTaskTimedOutEventAttributes
        """

        self._activity_task_timed_out_event_attributes = activity_task_timed_out_event_attributes

    @property
    def activity_task_canceled_event_attributes(self):
        """Gets the activity_task_canceled_event_attributes of this HistoryEvent.


        :return: The activity_task_canceled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventActivityTaskCanceledEventAttributes
        """
        return self._activity_task_canceled_event_attributes

    @activity_task_canceled_event_attributes.setter
    def activity_task_canceled_event_attributes(self, activity_task_canceled_event_attributes):
        """Sets the activity_task_canceled_event_attributes of this HistoryEvent.


        :param activity_task_canceled_event_attributes: The activity_task_canceled_event_attributes of this HistoryEvent.
        :type activity_task_canceled_event_attributes: HistoryEventActivityTaskCanceledEventAttributes
        """

        self._activity_task_canceled_event_attributes = activity_task_canceled_event_attributes

    @property
    def activity_task_cancel_requested_event_attributes(self):
        """Gets the activity_task_cancel_requested_event_attributes of this HistoryEvent.


        :return: The activity_task_cancel_requested_event_attributes of this HistoryEvent.
        :rtype: HistoryEventActivityTaskCancelRequestedEventAttributes
        """
        return self._activity_task_cancel_requested_event_attributes

    @activity_task_cancel_requested_event_attributes.setter
    def activity_task_cancel_requested_event_attributes(self, activity_task_cancel_requested_event_attributes):
        """Sets the activity_task_cancel_requested_event_attributes of this HistoryEvent.


        :param activity_task_cancel_requested_event_attributes: The activity_task_cancel_requested_event_attributes of this HistoryEvent.
        :type activity_task_cancel_requested_event_attributes: HistoryEventActivityTaskCancelRequestedEventAttributes
        """

        self._activity_task_cancel_requested_event_attributes = activity_task_cancel_requested_event_attributes

    @property
    def workflow_execution_signaled_event_attributes(self):
        """Gets the workflow_execution_signaled_event_attributes of this HistoryEvent.


        :return: The workflow_execution_signaled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventWorkflowExecutionSignaledEventAttributes
        """
        return self._workflow_execution_signaled_event_attributes

    @workflow_execution_signaled_event_attributes.setter
    def workflow_execution_signaled_event_attributes(self, workflow_execution_signaled_event_attributes):
        """Sets the workflow_execution_signaled_event_attributes of this HistoryEvent.


        :param workflow_execution_signaled_event_attributes: The workflow_execution_signaled_event_attributes of this HistoryEvent.
        :type workflow_execution_signaled_event_attributes: HistoryEventWorkflowExecutionSignaledEventAttributes
        """

        self._workflow_execution_signaled_event_attributes = workflow_execution_signaled_event_attributes

    @property
    def marker_recorded_event_attributes(self):
        """Gets the marker_recorded_event_attributes of this HistoryEvent.


        :return: The marker_recorded_event_attributes of this HistoryEvent.
        :rtype: HistoryEventMarkerRecordedEventAttributes
        """
        return self._marker_recorded_event_attributes

    @marker_recorded_event_attributes.setter
    def marker_recorded_event_attributes(self, marker_recorded_event_attributes):
        """Sets the marker_recorded_event_attributes of this HistoryEvent.


        :param marker_recorded_event_attributes: The marker_recorded_event_attributes of this HistoryEvent.
        :type marker_recorded_event_attributes: HistoryEventMarkerRecordedEventAttributes
        """

        self._marker_recorded_event_attributes = marker_recorded_event_attributes

    @property
    def record_marker_failed_event_attributes(self):
        """Gets the record_marker_failed_event_attributes of this HistoryEvent.


        :return: The record_marker_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventRecordMarkerFailedEventAttributes
        """
        return self._record_marker_failed_event_attributes

    @record_marker_failed_event_attributes.setter
    def record_marker_failed_event_attributes(self, record_marker_failed_event_attributes):
        """Sets the record_marker_failed_event_attributes of this HistoryEvent.


        :param record_marker_failed_event_attributes: The record_marker_failed_event_attributes of this HistoryEvent.
        :type record_marker_failed_event_attributes: HistoryEventRecordMarkerFailedEventAttributes
        """

        self._record_marker_failed_event_attributes = record_marker_failed_event_attributes

    @property
    def timer_started_event_attributes(self):
        """Gets the timer_started_event_attributes of this HistoryEvent.


        :return: The timer_started_event_attributes of this HistoryEvent.
        :rtype: HistoryEventTimerStartedEventAttributes
        """
        return self._timer_started_event_attributes

    @timer_started_event_attributes.setter
    def timer_started_event_attributes(self, timer_started_event_attributes):
        """Sets the timer_started_event_attributes of this HistoryEvent.


        :param timer_started_event_attributes: The timer_started_event_attributes of this HistoryEvent.
        :type timer_started_event_attributes: HistoryEventTimerStartedEventAttributes
        """

        self._timer_started_event_attributes = timer_started_event_attributes

    @property
    def timer_fired_event_attributes(self):
        """Gets the timer_fired_event_attributes of this HistoryEvent.


        :return: The timer_fired_event_attributes of this HistoryEvent.
        :rtype: HistoryEventTimerFiredEventAttributes
        """
        return self._timer_fired_event_attributes

    @timer_fired_event_attributes.setter
    def timer_fired_event_attributes(self, timer_fired_event_attributes):
        """Sets the timer_fired_event_attributes of this HistoryEvent.


        :param timer_fired_event_attributes: The timer_fired_event_attributes of this HistoryEvent.
        :type timer_fired_event_attributes: HistoryEventTimerFiredEventAttributes
        """

        self._timer_fired_event_attributes = timer_fired_event_attributes

    @property
    def timer_canceled_event_attributes(self):
        """Gets the timer_canceled_event_attributes of this HistoryEvent.


        :return: The timer_canceled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventTimerCanceledEventAttributes
        """
        return self._timer_canceled_event_attributes

    @timer_canceled_event_attributes.setter
    def timer_canceled_event_attributes(self, timer_canceled_event_attributes):
        """Sets the timer_canceled_event_attributes of this HistoryEvent.


        :param timer_canceled_event_attributes: The timer_canceled_event_attributes of this HistoryEvent.
        :type timer_canceled_event_attributes: HistoryEventTimerCanceledEventAttributes
        """

        self._timer_canceled_event_attributes = timer_canceled_event_attributes

    @property
    def start_child_workflow_execution_initiated_event_attributes(self):
        """Gets the start_child_workflow_execution_initiated_event_attributes of this HistoryEvent.


        :return: The start_child_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :rtype: HistoryEventStartChildWorkflowExecutionInitiatedEventAttributes
        """
        return self._start_child_workflow_execution_initiated_event_attributes

    @start_child_workflow_execution_initiated_event_attributes.setter
    def start_child_workflow_execution_initiated_event_attributes(self, start_child_workflow_execution_initiated_event_attributes):
        """Sets the start_child_workflow_execution_initiated_event_attributes of this HistoryEvent.


        :param start_child_workflow_execution_initiated_event_attributes: The start_child_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :type start_child_workflow_execution_initiated_event_attributes: HistoryEventStartChildWorkflowExecutionInitiatedEventAttributes
        """

        self._start_child_workflow_execution_initiated_event_attributes = start_child_workflow_execution_initiated_event_attributes

    @property
    def child_workflow_execution_started_event_attributes(self):
        """Gets the child_workflow_execution_started_event_attributes of this HistoryEvent.


        :return: The child_workflow_execution_started_event_attributes of this HistoryEvent.
        :rtype: HistoryEventChildWorkflowExecutionStartedEventAttributes
        """
        return self._child_workflow_execution_started_event_attributes

    @child_workflow_execution_started_event_attributes.setter
    def child_workflow_execution_started_event_attributes(self, child_workflow_execution_started_event_attributes):
        """Sets the child_workflow_execution_started_event_attributes of this HistoryEvent.


        :param child_workflow_execution_started_event_attributes: The child_workflow_execution_started_event_attributes of this HistoryEvent.
        :type child_workflow_execution_started_event_attributes: HistoryEventChildWorkflowExecutionStartedEventAttributes
        """

        self._child_workflow_execution_started_event_attributes = child_workflow_execution_started_event_attributes

    @property
    def child_workflow_execution_completed_event_attributes(self):
        """Gets the child_workflow_execution_completed_event_attributes of this HistoryEvent.


        :return: The child_workflow_execution_completed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventChildWorkflowExecutionCompletedEventAttributes
        """
        return self._child_workflow_execution_completed_event_attributes

    @child_workflow_execution_completed_event_attributes.setter
    def child_workflow_execution_completed_event_attributes(self, child_workflow_execution_completed_event_attributes):
        """Sets the child_workflow_execution_completed_event_attributes of this HistoryEvent.


        :param child_workflow_execution_completed_event_attributes: The child_workflow_execution_completed_event_attributes of this HistoryEvent.
        :type child_workflow_execution_completed_event_attributes: HistoryEventChildWorkflowExecutionCompletedEventAttributes
        """

        self._child_workflow_execution_completed_event_attributes = child_workflow_execution_completed_event_attributes

    @property
    def child_workflow_execution_failed_event_attributes(self):
        """Gets the child_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The child_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventChildWorkflowExecutionFailedEventAttributes
        """
        return self._child_workflow_execution_failed_event_attributes

    @child_workflow_execution_failed_event_attributes.setter
    def child_workflow_execution_failed_event_attributes(self, child_workflow_execution_failed_event_attributes):
        """Sets the child_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param child_workflow_execution_failed_event_attributes: The child_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type child_workflow_execution_failed_event_attributes: HistoryEventChildWorkflowExecutionFailedEventAttributes
        """

        self._child_workflow_execution_failed_event_attributes = child_workflow_execution_failed_event_attributes

    @property
    def child_workflow_execution_timed_out_event_attributes(self):
        """Gets the child_workflow_execution_timed_out_event_attributes of this HistoryEvent.


        :return: The child_workflow_execution_timed_out_event_attributes of this HistoryEvent.
        :rtype: HistoryEventChildWorkflowExecutionTimedOutEventAttributes
        """
        return self._child_workflow_execution_timed_out_event_attributes

    @child_workflow_execution_timed_out_event_attributes.setter
    def child_workflow_execution_timed_out_event_attributes(self, child_workflow_execution_timed_out_event_attributes):
        """Sets the child_workflow_execution_timed_out_event_attributes of this HistoryEvent.


        :param child_workflow_execution_timed_out_event_attributes: The child_workflow_execution_timed_out_event_attributes of this HistoryEvent.
        :type child_workflow_execution_timed_out_event_attributes: HistoryEventChildWorkflowExecutionTimedOutEventAttributes
        """

        self._child_workflow_execution_timed_out_event_attributes = child_workflow_execution_timed_out_event_attributes

    @property
    def child_workflow_execution_canceled_event_attributes(self):
        """Gets the child_workflow_execution_canceled_event_attributes of this HistoryEvent.


        :return: The child_workflow_execution_canceled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventChildWorkflowExecutionCanceledEventAttributes
        """
        return self._child_workflow_execution_canceled_event_attributes

    @child_workflow_execution_canceled_event_attributes.setter
    def child_workflow_execution_canceled_event_attributes(self, child_workflow_execution_canceled_event_attributes):
        """Sets the child_workflow_execution_canceled_event_attributes of this HistoryEvent.


        :param child_workflow_execution_canceled_event_attributes: The child_workflow_execution_canceled_event_attributes of this HistoryEvent.
        :type child_workflow_execution_canceled_event_attributes: HistoryEventChildWorkflowExecutionCanceledEventAttributes
        """

        self._child_workflow_execution_canceled_event_attributes = child_workflow_execution_canceled_event_attributes

    @property
    def child_workflow_execution_terminated_event_attributes(self):
        """Gets the child_workflow_execution_terminated_event_attributes of this HistoryEvent.


        :return: The child_workflow_execution_terminated_event_attributes of this HistoryEvent.
        :rtype: HistoryEventChildWorkflowExecutionTerminatedEventAttributes
        """
        return self._child_workflow_execution_terminated_event_attributes

    @child_workflow_execution_terminated_event_attributes.setter
    def child_workflow_execution_terminated_event_attributes(self, child_workflow_execution_terminated_event_attributes):
        """Sets the child_workflow_execution_terminated_event_attributes of this HistoryEvent.


        :param child_workflow_execution_terminated_event_attributes: The child_workflow_execution_terminated_event_attributes of this HistoryEvent.
        :type child_workflow_execution_terminated_event_attributes: HistoryEventChildWorkflowExecutionTerminatedEventAttributes
        """

        self._child_workflow_execution_terminated_event_attributes = child_workflow_execution_terminated_event_attributes

    @property
    def signal_external_workflow_execution_initiated_event_attributes(self):
        """Gets the signal_external_workflow_execution_initiated_event_attributes of this HistoryEvent.


        :return: The signal_external_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :rtype: HistoryEventSignalExternalWorkflowExecutionInitiatedEventAttributes
        """
        return self._signal_external_workflow_execution_initiated_event_attributes

    @signal_external_workflow_execution_initiated_event_attributes.setter
    def signal_external_workflow_execution_initiated_event_attributes(self, signal_external_workflow_execution_initiated_event_attributes):
        """Sets the signal_external_workflow_execution_initiated_event_attributes of this HistoryEvent.


        :param signal_external_workflow_execution_initiated_event_attributes: The signal_external_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :type signal_external_workflow_execution_initiated_event_attributes: HistoryEventSignalExternalWorkflowExecutionInitiatedEventAttributes
        """

        self._signal_external_workflow_execution_initiated_event_attributes = signal_external_workflow_execution_initiated_event_attributes

    @property
    def external_workflow_execution_signaled_event_attributes(self):
        """Gets the external_workflow_execution_signaled_event_attributes of this HistoryEvent.


        :return: The external_workflow_execution_signaled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventExternalWorkflowExecutionSignaledEventAttributes
        """
        return self._external_workflow_execution_signaled_event_attributes

    @external_workflow_execution_signaled_event_attributes.setter
    def external_workflow_execution_signaled_event_attributes(self, external_workflow_execution_signaled_event_attributes):
        """Sets the external_workflow_execution_signaled_event_attributes of this HistoryEvent.


        :param external_workflow_execution_signaled_event_attributes: The external_workflow_execution_signaled_event_attributes of this HistoryEvent.
        :type external_workflow_execution_signaled_event_attributes: HistoryEventExternalWorkflowExecutionSignaledEventAttributes
        """

        self._external_workflow_execution_signaled_event_attributes = external_workflow_execution_signaled_event_attributes

    @property
    def signal_external_workflow_execution_failed_event_attributes(self):
        """Gets the signal_external_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The signal_external_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventSignalExternalWorkflowExecutionFailedEventAttributes
        """
        return self._signal_external_workflow_execution_failed_event_attributes

    @signal_external_workflow_execution_failed_event_attributes.setter
    def signal_external_workflow_execution_failed_event_attributes(self, signal_external_workflow_execution_failed_event_attributes):
        """Sets the signal_external_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param signal_external_workflow_execution_failed_event_attributes: The signal_external_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type signal_external_workflow_execution_failed_event_attributes: HistoryEventSignalExternalWorkflowExecutionFailedEventAttributes
        """

        self._signal_external_workflow_execution_failed_event_attributes = signal_external_workflow_execution_failed_event_attributes

    @property
    def external_workflow_execution_cancel_requested_event_attributes(self):
        """Gets the external_workflow_execution_cancel_requested_event_attributes of this HistoryEvent.


        :return: The external_workflow_execution_cancel_requested_event_attributes of this HistoryEvent.
        :rtype: HistoryEventExternalWorkflowExecutionCancelRequestedEventAttributes
        """
        return self._external_workflow_execution_cancel_requested_event_attributes

    @external_workflow_execution_cancel_requested_event_attributes.setter
    def external_workflow_execution_cancel_requested_event_attributes(self, external_workflow_execution_cancel_requested_event_attributes):
        """Sets the external_workflow_execution_cancel_requested_event_attributes of this HistoryEvent.


        :param external_workflow_execution_cancel_requested_event_attributes: The external_workflow_execution_cancel_requested_event_attributes of this HistoryEvent.
        :type external_workflow_execution_cancel_requested_event_attributes: HistoryEventExternalWorkflowExecutionCancelRequestedEventAttributes
        """

        self._external_workflow_execution_cancel_requested_event_attributes = external_workflow_execution_cancel_requested_event_attributes

    @property
    def request_cancel_external_workflow_execution_initiated_event_attributes(self):
        """Gets the request_cancel_external_workflow_execution_initiated_event_attributes of this HistoryEvent.


        :return: The request_cancel_external_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :rtype: HistoryEventRequestCancelExternalWorkflowExecutionInitiatedEventAttributes
        """
        return self._request_cancel_external_workflow_execution_initiated_event_attributes

    @request_cancel_external_workflow_execution_initiated_event_attributes.setter
    def request_cancel_external_workflow_execution_initiated_event_attributes(self, request_cancel_external_workflow_execution_initiated_event_attributes):
        """Sets the request_cancel_external_workflow_execution_initiated_event_attributes of this HistoryEvent.


        :param request_cancel_external_workflow_execution_initiated_event_attributes: The request_cancel_external_workflow_execution_initiated_event_attributes of this HistoryEvent.
        :type request_cancel_external_workflow_execution_initiated_event_attributes: HistoryEventRequestCancelExternalWorkflowExecutionInitiatedEventAttributes
        """

        self._request_cancel_external_workflow_execution_initiated_event_attributes = request_cancel_external_workflow_execution_initiated_event_attributes

    @property
    def request_cancel_external_workflow_execution_failed_event_attributes(self):
        """Gets the request_cancel_external_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The request_cancel_external_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventRequestCancelExternalWorkflowExecutionFailedEventAttributes
        """
        return self._request_cancel_external_workflow_execution_failed_event_attributes

    @request_cancel_external_workflow_execution_failed_event_attributes.setter
    def request_cancel_external_workflow_execution_failed_event_attributes(self, request_cancel_external_workflow_execution_failed_event_attributes):
        """Sets the request_cancel_external_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param request_cancel_external_workflow_execution_failed_event_attributes: The request_cancel_external_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type request_cancel_external_workflow_execution_failed_event_attributes: HistoryEventRequestCancelExternalWorkflowExecutionFailedEventAttributes
        """

        self._request_cancel_external_workflow_execution_failed_event_attributes = request_cancel_external_workflow_execution_failed_event_attributes

    @property
    def schedule_activity_task_failed_event_attributes(self):
        """Gets the schedule_activity_task_failed_event_attributes of this HistoryEvent.


        :return: The schedule_activity_task_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventScheduleActivityTaskFailedEventAttributes
        """
        return self._schedule_activity_task_failed_event_attributes

    @schedule_activity_task_failed_event_attributes.setter
    def schedule_activity_task_failed_event_attributes(self, schedule_activity_task_failed_event_attributes):
        """Sets the schedule_activity_task_failed_event_attributes of this HistoryEvent.


        :param schedule_activity_task_failed_event_attributes: The schedule_activity_task_failed_event_attributes of this HistoryEvent.
        :type schedule_activity_task_failed_event_attributes: HistoryEventScheduleActivityTaskFailedEventAttributes
        """

        self._schedule_activity_task_failed_event_attributes = schedule_activity_task_failed_event_attributes

    @property
    def request_cancel_activity_task_failed_event_attributes(self):
        """Gets the request_cancel_activity_task_failed_event_attributes of this HistoryEvent.


        :return: The request_cancel_activity_task_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventRequestCancelActivityTaskFailedEventAttributes
        """
        return self._request_cancel_activity_task_failed_event_attributes

    @request_cancel_activity_task_failed_event_attributes.setter
    def request_cancel_activity_task_failed_event_attributes(self, request_cancel_activity_task_failed_event_attributes):
        """Sets the request_cancel_activity_task_failed_event_attributes of this HistoryEvent.


        :param request_cancel_activity_task_failed_event_attributes: The request_cancel_activity_task_failed_event_attributes of this HistoryEvent.
        :type request_cancel_activity_task_failed_event_attributes: HistoryEventRequestCancelActivityTaskFailedEventAttributes
        """

        self._request_cancel_activity_task_failed_event_attributes = request_cancel_activity_task_failed_event_attributes

    @property
    def start_timer_failed_event_attributes(self):
        """Gets the start_timer_failed_event_attributes of this HistoryEvent.


        :return: The start_timer_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventStartTimerFailedEventAttributes
        """
        return self._start_timer_failed_event_attributes

    @start_timer_failed_event_attributes.setter
    def start_timer_failed_event_attributes(self, start_timer_failed_event_attributes):
        """Sets the start_timer_failed_event_attributes of this HistoryEvent.


        :param start_timer_failed_event_attributes: The start_timer_failed_event_attributes of this HistoryEvent.
        :type start_timer_failed_event_attributes: HistoryEventStartTimerFailedEventAttributes
        """

        self._start_timer_failed_event_attributes = start_timer_failed_event_attributes

    @property
    def cancel_timer_failed_event_attributes(self):
        """Gets the cancel_timer_failed_event_attributes of this HistoryEvent.


        :return: The cancel_timer_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventCancelTimerFailedEventAttributes
        """
        return self._cancel_timer_failed_event_attributes

    @cancel_timer_failed_event_attributes.setter
    def cancel_timer_failed_event_attributes(self, cancel_timer_failed_event_attributes):
        """Sets the cancel_timer_failed_event_attributes of this HistoryEvent.


        :param cancel_timer_failed_event_attributes: The cancel_timer_failed_event_attributes of this HistoryEvent.
        :type cancel_timer_failed_event_attributes: HistoryEventCancelTimerFailedEventAttributes
        """

        self._cancel_timer_failed_event_attributes = cancel_timer_failed_event_attributes

    @property
    def start_child_workflow_execution_failed_event_attributes(self):
        """Gets the start_child_workflow_execution_failed_event_attributes of this HistoryEvent.


        :return: The start_child_workflow_execution_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventStartChildWorkflowExecutionFailedEventAttributes
        """
        return self._start_child_workflow_execution_failed_event_attributes

    @start_child_workflow_execution_failed_event_attributes.setter
    def start_child_workflow_execution_failed_event_attributes(self, start_child_workflow_execution_failed_event_attributes):
        """Sets the start_child_workflow_execution_failed_event_attributes of this HistoryEvent.


        :param start_child_workflow_execution_failed_event_attributes: The start_child_workflow_execution_failed_event_attributes of this HistoryEvent.
        :type start_child_workflow_execution_failed_event_attributes: HistoryEventStartChildWorkflowExecutionFailedEventAttributes
        """

        self._start_child_workflow_execution_failed_event_attributes = start_child_workflow_execution_failed_event_attributes

    @property
    def lambda_function_scheduled_event_attributes(self):
        """Gets the lambda_function_scheduled_event_attributes of this HistoryEvent.


        :return: The lambda_function_scheduled_event_attributes of this HistoryEvent.
        :rtype: HistoryEventLambdaFunctionScheduledEventAttributes
        """
        return self._lambda_function_scheduled_event_attributes

    @lambda_function_scheduled_event_attributes.setter
    def lambda_function_scheduled_event_attributes(self, lambda_function_scheduled_event_attributes):
        """Sets the lambda_function_scheduled_event_attributes of this HistoryEvent.


        :param lambda_function_scheduled_event_attributes: The lambda_function_scheduled_event_attributes of this HistoryEvent.
        :type lambda_function_scheduled_event_attributes: HistoryEventLambdaFunctionScheduledEventAttributes
        """

        self._lambda_function_scheduled_event_attributes = lambda_function_scheduled_event_attributes

    @property
    def lambda_function_started_event_attributes(self):
        """Gets the lambda_function_started_event_attributes of this HistoryEvent.


        :return: The lambda_function_started_event_attributes of this HistoryEvent.
        :rtype: HistoryEventLambdaFunctionStartedEventAttributes
        """
        return self._lambda_function_started_event_attributes

    @lambda_function_started_event_attributes.setter
    def lambda_function_started_event_attributes(self, lambda_function_started_event_attributes):
        """Sets the lambda_function_started_event_attributes of this HistoryEvent.


        :param lambda_function_started_event_attributes: The lambda_function_started_event_attributes of this HistoryEvent.
        :type lambda_function_started_event_attributes: HistoryEventLambdaFunctionStartedEventAttributes
        """

        self._lambda_function_started_event_attributes = lambda_function_started_event_attributes

    @property
    def lambda_function_completed_event_attributes(self):
        """Gets the lambda_function_completed_event_attributes of this HistoryEvent.


        :return: The lambda_function_completed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventLambdaFunctionCompletedEventAttributes
        """
        return self._lambda_function_completed_event_attributes

    @lambda_function_completed_event_attributes.setter
    def lambda_function_completed_event_attributes(self, lambda_function_completed_event_attributes):
        """Sets the lambda_function_completed_event_attributes of this HistoryEvent.


        :param lambda_function_completed_event_attributes: The lambda_function_completed_event_attributes of this HistoryEvent.
        :type lambda_function_completed_event_attributes: HistoryEventLambdaFunctionCompletedEventAttributes
        """

        self._lambda_function_completed_event_attributes = lambda_function_completed_event_attributes

    @property
    def lambda_function_failed_event_attributes(self):
        """Gets the lambda_function_failed_event_attributes of this HistoryEvent.


        :return: The lambda_function_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventLambdaFunctionFailedEventAttributes
        """
        return self._lambda_function_failed_event_attributes

    @lambda_function_failed_event_attributes.setter
    def lambda_function_failed_event_attributes(self, lambda_function_failed_event_attributes):
        """Sets the lambda_function_failed_event_attributes of this HistoryEvent.


        :param lambda_function_failed_event_attributes: The lambda_function_failed_event_attributes of this HistoryEvent.
        :type lambda_function_failed_event_attributes: HistoryEventLambdaFunctionFailedEventAttributes
        """

        self._lambda_function_failed_event_attributes = lambda_function_failed_event_attributes

    @property
    def lambda_function_timed_out_event_attributes(self):
        """Gets the lambda_function_timed_out_event_attributes of this HistoryEvent.


        :return: The lambda_function_timed_out_event_attributes of this HistoryEvent.
        :rtype: HistoryEventLambdaFunctionTimedOutEventAttributes
        """
        return self._lambda_function_timed_out_event_attributes

    @lambda_function_timed_out_event_attributes.setter
    def lambda_function_timed_out_event_attributes(self, lambda_function_timed_out_event_attributes):
        """Sets the lambda_function_timed_out_event_attributes of this HistoryEvent.


        :param lambda_function_timed_out_event_attributes: The lambda_function_timed_out_event_attributes of this HistoryEvent.
        :type lambda_function_timed_out_event_attributes: HistoryEventLambdaFunctionTimedOutEventAttributes
        """

        self._lambda_function_timed_out_event_attributes = lambda_function_timed_out_event_attributes

    @property
    def schedule_lambda_function_failed_event_attributes(self):
        """Gets the schedule_lambda_function_failed_event_attributes of this HistoryEvent.


        :return: The schedule_lambda_function_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventScheduleLambdaFunctionFailedEventAttributes
        """
        return self._schedule_lambda_function_failed_event_attributes

    @schedule_lambda_function_failed_event_attributes.setter
    def schedule_lambda_function_failed_event_attributes(self, schedule_lambda_function_failed_event_attributes):
        """Sets the schedule_lambda_function_failed_event_attributes of this HistoryEvent.


        :param schedule_lambda_function_failed_event_attributes: The schedule_lambda_function_failed_event_attributes of this HistoryEvent.
        :type schedule_lambda_function_failed_event_attributes: HistoryEventScheduleLambdaFunctionFailedEventAttributes
        """

        self._schedule_lambda_function_failed_event_attributes = schedule_lambda_function_failed_event_attributes

    @property
    def start_lambda_function_failed_event_attributes(self):
        """Gets the start_lambda_function_failed_event_attributes of this HistoryEvent.


        :return: The start_lambda_function_failed_event_attributes of this HistoryEvent.
        :rtype: HistoryEventStartLambdaFunctionFailedEventAttributes
        """
        return self._start_lambda_function_failed_event_attributes

    @start_lambda_function_failed_event_attributes.setter
    def start_lambda_function_failed_event_attributes(self, start_lambda_function_failed_event_attributes):
        """Sets the start_lambda_function_failed_event_attributes of this HistoryEvent.


        :param start_lambda_function_failed_event_attributes: The start_lambda_function_failed_event_attributes of this HistoryEvent.
        :type start_lambda_function_failed_event_attributes: HistoryEventStartLambdaFunctionFailedEventAttributes
        """

        self._start_lambda_function_failed_event_attributes = start_lambda_function_failed_event_attributes
