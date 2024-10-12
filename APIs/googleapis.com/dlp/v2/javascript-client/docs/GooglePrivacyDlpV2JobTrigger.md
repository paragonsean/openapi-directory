# SensitiveDataProtectionDlp.GooglePrivacyDlpV2JobTrigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation timestamp of a triggeredJob. | [optional] [readonly] 
**description** | **String** | User provided description (max 256 chars) | [optional] 
**displayName** | **String** | Display name (max 100 chars) | [optional] 
**errors** | [**[GooglePrivacyDlpV2Error]**](GooglePrivacyDlpV2Error.md) | Output only. A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared. | [optional] [readonly] 
**inspectJob** | [**GooglePrivacyDlpV2InspectJobConfig**](GooglePrivacyDlpV2InspectJobConfig.md) |  | [optional] 
**lastRunTime** | **String** | Output only. The timestamp of the last time this trigger executed. | [optional] [readonly] 
**name** | **String** | Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example &#x60;projects/dlp-test-project/jobTriggers/53234423&#x60;. | [optional] 
**status** | **String** | Required. A status for this trigger. | [optional] 
**triggers** | [**[GooglePrivacyDlpV2Trigger]**](GooglePrivacyDlpV2Trigger.md) | A list of triggers which will be OR&#39;ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object. | [optional] 
**updateTime** | **String** | Output only. The last update timestamp of a triggeredJob. | [optional] [readonly] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `HEALTHY` (value: `"HEALTHY"`)

* `PAUSED` (value: `"PAUSED"`)

* `CANCELLED` (value: `"CANCELLED"`)




