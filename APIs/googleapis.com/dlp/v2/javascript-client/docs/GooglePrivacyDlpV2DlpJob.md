# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DlpJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionDetails** | [**[GooglePrivacyDlpV2ActionDetails]**](GooglePrivacyDlpV2ActionDetails.md) | Events that should occur after the job has completed. | [optional] 
**createTime** | **String** | Time when the job was created. | [optional] 
**endTime** | **String** | Time when the job finished. | [optional] 
**errors** | [**[GooglePrivacyDlpV2Error]**](GooglePrivacyDlpV2Error.md) | A stream of errors encountered running the job. | [optional] 
**inspectDetails** | [**GooglePrivacyDlpV2InspectDataSourceDetails**](GooglePrivacyDlpV2InspectDataSourceDetails.md) |  | [optional] 
**jobTriggerName** | **String** | If created by a job trigger, the resource name of the trigger that instantiated the job. | [optional] 
**lastModified** | **String** | Time when the job was last modified by the system. | [optional] 
**name** | **String** | The server-assigned name. | [optional] 
**riskDetails** | [**GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails**](GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails.md) |  | [optional] 
**startTime** | **String** | Time when the job started. | [optional] 
**state** | **String** | State of a job. | [optional] 
**type** | **String** | The type of job. | [optional] 



## Enum: StateEnum


* `JOB_STATE_UNSPECIFIED` (value: `"JOB_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)

* `CANCELED` (value: `"CANCELED"`)

* `FAILED` (value: `"FAILED"`)

* `ACTIVE` (value: `"ACTIVE"`)





## Enum: TypeEnum


* `DLP_JOB_TYPE_UNSPECIFIED` (value: `"DLP_JOB_TYPE_UNSPECIFIED"`)

* `INSPECT_JOB` (value: `"INSPECT_JOB"`)

* `RISK_ANALYSIS_JOB` (value: `"RISK_ANALYSIS_JOB"`)




