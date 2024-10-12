# CloudDataprocApi.YarnApplication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Required. The application name. | [optional] 
**progress** | **Number** | Required. The numerical progress of the application, from 1 to 100. | [optional] 
**state** | **String** | Required. The application state. | [optional] 
**trackingUrl** | **String** | Optional. The HTTP URL of the ApplicationMaster, HistoryServer, or TimelineServer that provides application-specific information. The URL uses the internal hostname, and requires a proxy server for resolution and, possibly, access. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NEW` (value: `"NEW"`)

* `NEW_SAVING` (value: `"NEW_SAVING"`)

* `SUBMITTED` (value: `"SUBMITTED"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `RUNNING` (value: `"RUNNING"`)

* `FINISHED` (value: `"FINISHED"`)

* `FAILED` (value: `"FAILED"`)

* `KILLED` (value: `"KILLED"`)




