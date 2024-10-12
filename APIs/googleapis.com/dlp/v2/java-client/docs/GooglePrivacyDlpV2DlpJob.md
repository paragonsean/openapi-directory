

# GooglePrivacyDlpV2DlpJob

Combines all of the information about a DLP job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionDetails** | [**List&lt;GooglePrivacyDlpV2ActionDetails&gt;**](GooglePrivacyDlpV2ActionDetails.md) | Events that should occur after the job has completed. |  [optional] |
|**createTime** | **String** | Time when the job was created. |  [optional] |
|**endTime** | **String** | Time when the job finished. |  [optional] |
|**errors** | [**List&lt;GooglePrivacyDlpV2Error&gt;**](GooglePrivacyDlpV2Error.md) | A stream of errors encountered running the job. |  [optional] |
|**inspectDetails** | [**GooglePrivacyDlpV2InspectDataSourceDetails**](GooglePrivacyDlpV2InspectDataSourceDetails.md) |  |  [optional] |
|**jobTriggerName** | **String** | If created by a job trigger, the resource name of the trigger that instantiated the job. |  [optional] |
|**lastModified** | **String** | Time when the job was last modified by the system. |  [optional] |
|**name** | **String** | The server-assigned name. |  [optional] |
|**riskDetails** | [**GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails**](GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails.md) |  |  [optional] |
|**startTime** | **String** | Time when the job started. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of a job. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of job. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| JOB_STATE_UNSPECIFIED | &quot;JOB_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |
| CANCELED | &quot;CANCELED&quot; |
| FAILED | &quot;FAILED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DLP_JOB_TYPE_UNSPECIFIED | &quot;DLP_JOB_TYPE_UNSPECIFIED&quot; |
| INSPECT_JOB | &quot;INSPECT_JOB&quot; |
| RISK_ANALYSIS_JOB | &quot;RISK_ANALYSIS_JOB&quot; |



