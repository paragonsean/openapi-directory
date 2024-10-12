# CloudDataplexApi.GoogleCloudDataplexV1SessionEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventSucceeded** | **Boolean** | The status of the event. | [optional] 
**fastStartupEnabled** | **Boolean** | If the session is associated with an environment with fast startup enabled, and was created before being assigned to a user. | [optional] 
**message** | **String** | The log message. | [optional] 
**query** | [**GoogleCloudDataplexV1SessionEventQueryDetail**](GoogleCloudDataplexV1SessionEventQueryDetail.md) |  | [optional] 
**sessionId** | **String** | Unique identifier for the session. | [optional] 
**type** | **String** | The type of the event. | [optional] 
**unassignedDuration** | **String** | The idle duration of a warm pooled session before it is assigned to user. | [optional] 
**userId** | **String** | The information about the user that created the session. It will be the email address of the user. | [optional] 



## Enum: TypeEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `START` (value: `"START"`)

* `STOP` (value: `"STOP"`)

* `QUERY` (value: `"QUERY"`)

* `CREATE` (value: `"CREATE"`)




