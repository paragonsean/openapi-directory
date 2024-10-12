

# GooglePrivacyDlpV2TransformationResultStatus

The outcome of a transformation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**resultStatusType** | [**ResultStatusTypeEnum**](#ResultStatusTypeEnum) | Transformation result status type, this will be either SUCCESS, or it will be the reason for why the transformation was not completely successful. |  [optional] |



## Enum: ResultStatusTypeEnum

| Name | Value |
|---- | -----|
| STATE_TYPE_UNSPECIFIED | &quot;STATE_TYPE_UNSPECIFIED&quot; |
| INVALID_TRANSFORM | &quot;INVALID_TRANSFORM&quot; |
| BIGQUERY_MAX_ROW_SIZE_EXCEEDED | &quot;BIGQUERY_MAX_ROW_SIZE_EXCEEDED&quot; |
| METADATA_UNRETRIEVABLE | &quot;METADATA_UNRETRIEVABLE&quot; |
| SUCCESS | &quot;SUCCESS&quot; |



