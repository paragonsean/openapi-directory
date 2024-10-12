

# TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource. |  [optional] |
|**activityDurations** | **List&lt;Object&gt;** | The minimum, average, maximum, and total time (in seconds) that Workers spent in each Activity. |  [optional] |
|**endTime** | **OffsetDateTime** | The end of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**reservationsAccepted** | **Integer** | The total number of Reservations that were accepted. |  [optional] |
|**reservationsCanceled** | **Integer** | The total number of Reservations that were canceled. |  [optional] |
|**reservationsCreated** | **Integer** | The total number of Reservations that were created. |  [optional] |
|**reservationsRejected** | **Integer** | The total number of Reservations that were rejected. |  [optional] |
|**reservationsRescinded** | **Integer** | The total number of Reservations that were rescinded. |  [optional] |
|**reservationsTimedOut** | **Integer** | The total number of Reservations that were timed out. |  [optional] |
|**startTime** | **OffsetDateTime** | The beginning of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**url** | **URI** | The absolute URL of the Workers statistics resource. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace that contains the Workers. |  [optional] |



