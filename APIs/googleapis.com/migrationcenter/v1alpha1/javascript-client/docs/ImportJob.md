# MigrationCenterApi.ImportJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetSource** | **String** | Required. Reference to a source. | [optional] 
**completeTime** | **String** | Output only. The timestamp when the import job was completed. | [optional] [readonly] 
**createTime** | **String** | Output only. The timestamp when the import job was created. | [optional] [readonly] 
**displayName** | **String** | User-friendly display name. Maximum length is 63 characters. | [optional] 
**executionReport** | [**ExecutionReport**](ExecutionReport.md) |  | [optional] 
**gcsPayload** | [**GCSPayloadInfo**](GCSPayloadInfo.md) |  | [optional] 
**inlinePayload** | [**InlinePayloadInfo**](InlinePayloadInfo.md) |  | [optional] 
**labels** | **{String: String}** | Labels as key value pairs. | [optional] 
**name** | **String** | Output only. The full name of the import job. | [optional] [readonly] 
**state** | **String** | Output only. The state of the import job. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when the import job was last updated. | [optional] [readonly] 
**validationReport** | [**ValidationReport**](ValidationReport.md) |  | [optional] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"IMPORT_JOB_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"IMPORT_JOB_STATE_PENDING"`)

* `RUNNING` (value: `"IMPORT_JOB_STATE_RUNNING"`)

* `COMPLETED` (value: `"IMPORT_JOB_STATE_COMPLETED"`)

* `FAILED` (value: `"IMPORT_JOB_STATE_FAILED"`)

* `VALIDATING` (value: `"IMPORT_JOB_STATE_VALIDATING"`)

* `FAILED_VALIDATION` (value: `"IMPORT_JOB_STATE_FAILED_VALIDATION"`)

* `READY` (value: `"IMPORT_JOB_STATE_READY"`)




