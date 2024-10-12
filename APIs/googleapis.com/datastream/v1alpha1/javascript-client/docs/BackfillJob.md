# DatastreamApi.BackfillJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | Output only. Errors which caused the backfill job to fail. | [optional] [readonly] 
**lastEndTime** | **String** | Output only. Backfill job&#39;s end time. | [optional] [readonly] 
**lastStartTime** | **String** | Output only. Backfill job&#39;s start time. | [optional] [readonly] 
**state** | **String** | Backfill job state. | [optional] 
**trigger** | **String** | Backfill job&#39;s triggering reason. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `STOPPED` (value: `"STOPPED"`)

* `FAILED` (value: `"FAILED"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `UNSUPPORTED` (value: `"UNSUPPORTED"`)





## Enum: TriggerEnum


* `TRIGGER_UNSPECIFIED` (value: `"TRIGGER_UNSPECIFIED"`)

* `AUTOMATIC` (value: `"AUTOMATIC"`)

* `MANUAL` (value: `"MANUAL"`)




