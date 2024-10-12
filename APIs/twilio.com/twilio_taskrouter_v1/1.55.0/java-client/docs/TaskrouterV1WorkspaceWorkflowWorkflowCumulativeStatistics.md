

# TaskrouterV1WorkspaceWorkflowWorkflowCumulativeStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workflow resource. |  [optional] |
|**avgTaskAcceptanceTime** | **Integer** | The average time in seconds between Task creation and acceptance. |  [optional] |
|**endTime** | **OffsetDateTime** | The end of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**reservationsAccepted** | **Integer** | The total number of Reservations accepted by Workers. |  [optional] |
|**reservationsCanceled** | **Integer** | The total number of Reservations that were canceled. |  [optional] |
|**reservationsCreated** | **Integer** | The total number of Reservations that were created for Workers. |  [optional] |
|**reservationsRejected** | **Integer** | The total number of Reservations that were rejected. |  [optional] |
|**reservationsRescinded** | **Integer** | The total number of Reservations that were rescinded. |  [optional] |
|**reservationsTimedOut** | **Integer** | The total number of Reservations that were timed out. |  [optional] |
|**splitByWaitTime** | **Object** | A list of objects that describe the number of Tasks canceled and reservations accepted above and below the thresholds specified in seconds. |  [optional] |
|**startTime** | **OffsetDateTime** | The beginning of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**tasksCanceled** | **Integer** | The total number of Tasks that were canceled. |  [optional] |
|**tasksCompleted** | **Integer** | The total number of Tasks that were completed. |  [optional] |
|**tasksDeleted** | **Integer** | The total number of Tasks that were deleted. |  [optional] |
|**tasksEntered** | **Integer** | The total number of Tasks that entered the Workflow. |  [optional] |
|**tasksMoved** | **Integer** | The total number of Tasks that were moved from one queue to another. |  [optional] |
|**tasksTimedOutInWorkflow** | **Integer** | The total number of Tasks that were timed out of their Workflows (and deleted). |  [optional] |
|**url** | **URI** | The absolute URL of the Workflow statistics resource. |  [optional] |
|**waitDurationUntilAccepted** | **Object** | The wait duration statistics (&#x60;avg&#x60;, &#x60;min&#x60;, &#x60;max&#x60;, &#x60;total&#x60;) for Tasks that were accepted. |  [optional] |
|**waitDurationUntilCanceled** | **Object** | The wait duration statistics (&#x60;avg&#x60;, &#x60;min&#x60;, &#x60;max&#x60;, &#x60;total&#x60;) for Tasks that were canceled. |  [optional] |
|**workflowSid** | **String** | Returns the list of Tasks that are being controlled by the Workflow with the specified Sid value. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace that contains the Workflow. |  [optional] |



