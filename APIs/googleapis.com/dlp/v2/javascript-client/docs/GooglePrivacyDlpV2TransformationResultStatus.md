# SensitiveDataProtectionDlp.GooglePrivacyDlpV2TransformationResultStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**resultStatusType** | **String** | Transformation result status type, this will be either SUCCESS, or it will be the reason for why the transformation was not completely successful. | [optional] 



## Enum: ResultStatusTypeEnum


* `STATE_TYPE_UNSPECIFIED` (value: `"STATE_TYPE_UNSPECIFIED"`)

* `INVALID_TRANSFORM` (value: `"INVALID_TRANSFORM"`)

* `BIGQUERY_MAX_ROW_SIZE_EXCEEDED` (value: `"BIGQUERY_MAX_ROW_SIZE_EXCEEDED"`)

* `METADATA_UNRETRIEVABLE` (value: `"METADATA_UNRETRIEVABLE"`)

* `SUCCESS` (value: `"SUCCESS"`)




