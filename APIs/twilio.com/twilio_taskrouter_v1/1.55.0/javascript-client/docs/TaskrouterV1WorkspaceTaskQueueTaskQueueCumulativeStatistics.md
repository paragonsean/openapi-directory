# TwilioTaskrouter.TaskrouterV1WorkspaceTaskQueueTaskQueueCumulativeStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource. | [optional] 
**avgTaskAcceptanceTime** | **Number** | The average time in seconds between Task creation and acceptance. | [optional] 
**endTime** | **Date** | The end of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**reservationsAccepted** | **Number** | The total number of Reservations accepted for Tasks in the TaskQueue. | [optional] 
**reservationsCanceled** | **Number** | The total number of Reservations canceled for Tasks in the TaskQueue. | [optional] 
**reservationsCreated** | **Number** | The total number of Reservations created for Tasks in the TaskQueue. | [optional] 
**reservationsRejected** | **Number** | The total number of Reservations rejected for Tasks in the TaskQueue. | [optional] 
**reservationsRescinded** | **Number** | The total number of Reservations rescinded. | [optional] 
**reservationsTimedOut** | **Number** | The total number of Reservations that timed out for Tasks in the TaskQueue. | [optional] 
**splitByWaitTime** | **Object** | A list of objects that describe the number of Tasks canceled and reservations accepted above and below the thresholds specified in seconds. | [optional] 
**startTime** | **Date** | The beginning of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**taskQueueSid** | **String** | The SID of the TaskQueue from which these statistics were calculated. | [optional] 
**tasksCanceled** | **Number** | The total number of Tasks canceled in the TaskQueue. | [optional] 
**tasksCompleted** | **Number** | The total number of Tasks completed in the TaskQueue. | [optional] 
**tasksDeleted** | **Number** | The total number of Tasks deleted in the TaskQueue. | [optional] 
**tasksEntered** | **Number** | The total number of Tasks entered into the TaskQueue. | [optional] 
**tasksMoved** | **Number** | The total number of Tasks that were moved from one queue to another. | [optional] 
**url** | **String** | The absolute URL of the TaskQueue statistics resource. | [optional] 
**waitDurationInQueueUntilAccepted** | **Object** | The relative wait duration statistics (&#x60;avg&#x60;, &#x60;min&#x60;, &#x60;max&#x60;, &#x60;total&#x60;) for Tasks accepted while in the TaskQueue. Calculation is based on the time when the Tasks entered the TaskQueue. | [optional] 
**waitDurationUntilAccepted** | **Object** | The wait duration statistics (&#x60;avg&#x60;, &#x60;min&#x60;, &#x60;max&#x60;, &#x60;total&#x60;) for Tasks accepted while in the TaskQueue. Calculation is based on the time when the Tasks were created. For transfers, the wait duration is counted from the moment ***the Task was created***, and not from when the transfer was initiated. | [optional] 
**waitDurationUntilCanceled** | **Object** | The wait duration statistics (&#x60;avg&#x60;, &#x60;min&#x60;, &#x60;max&#x60;, &#x60;total&#x60;) for Tasks canceled while in the TaskQueue. | [optional] 
**workspaceSid** | **String** | The SID of the Workspace that contains the TaskQueue. | [optional] 


