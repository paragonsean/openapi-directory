

# InlinePayloadInfo

A resource that represents the inline import job payload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | [**FormatEnum**](#FormatEnum) | The import job format. |  [optional] |
|**payload** | [**List&lt;PayloadFile&gt;**](PayloadFile.md) | List of payload files. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPORT_JOB_FORMAT_UNSPECIFIED&quot; |
| CMDB | &quot;IMPORT_JOB_FORMAT_CMDB&quot; |
| RVTOOLS_XLSX | &quot;IMPORT_JOB_FORMAT_RVTOOLS_XLSX&quot; |
| RVTOOLS_CSV | &quot;IMPORT_JOB_FORMAT_RVTOOLS_CSV&quot; |
| EXPORTED_AWS_CSV | &quot;IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV&quot; |
| EXPORTED_AZURE_CSV | &quot;IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV&quot; |
| MANUAL_CSV | &quot;IMPORT_JOB_FORMAT_MANUAL_CSV&quot; |



