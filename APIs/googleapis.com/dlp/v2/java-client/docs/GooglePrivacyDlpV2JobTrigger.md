

# GooglePrivacyDlpV2JobTrigger

Contains a configuration to make dlp api calls on a repeating basis. See https://cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers to learn more.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The creation timestamp of a triggeredJob. |  [optional] [readonly] |
|**description** | **String** | User provided description (max 256 chars) |  [optional] |
|**displayName** | **String** | Display name (max 100 chars) |  [optional] |
|**errors** | [**List&lt;GooglePrivacyDlpV2Error&gt;**](GooglePrivacyDlpV2Error.md) | Output only. A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared. |  [optional] [readonly] |
|**inspectJob** | [**GooglePrivacyDlpV2InspectJobConfig**](GooglePrivacyDlpV2InspectJobConfig.md) |  |  [optional] |
|**lastRunTime** | **String** | Output only. The timestamp of the last time this trigger executed. |  [optional] [readonly] |
|**name** | **String** | Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example &#x60;projects/dlp-test-project/jobTriggers/53234423&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Required. A status for this trigger. |  [optional] |
|**triggers** | [**List&lt;GooglePrivacyDlpV2Trigger&gt;**](GooglePrivacyDlpV2Trigger.md) | A list of triggers which will be OR&#39;ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object. |  [optional] |
|**updateTime** | **String** | Output only. The last update timestamp of a triggeredJob. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| HEALTHY | &quot;HEALTHY&quot; |
| PAUSED | &quot;PAUSED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



