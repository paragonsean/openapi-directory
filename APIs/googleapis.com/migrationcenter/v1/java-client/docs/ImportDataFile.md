

# ImportDataFile

A resource that represents a payload file in an import job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp when the file was created. |  [optional] [readonly] |
|**displayName** | **String** | User-friendly display name. Maximum length is 63 characters. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Required. The payload format. |  [optional] |
|**name** | **String** | Output only. The name of the file. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the import data file. |  [optional] [readonly] |
|**uploadFileInfo** | [**UploadFileInfo**](UploadFileInfo.md) |  |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPORT_JOB_FORMAT_UNSPECIFIED&quot; |
| RVTOOLS_XLSX | &quot;IMPORT_JOB_FORMAT_RVTOOLS_XLSX&quot; |
| RVTOOLS_CSV | &quot;IMPORT_JOB_FORMAT_RVTOOLS_CSV&quot; |
| EXPORTED_AWS_CSV | &quot;IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV&quot; |
| EXPORTED_AZURE_CSV | &quot;IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV&quot; |
| STRATOZONE_CSV | &quot;IMPORT_JOB_FORMAT_STRATOZONE_CSV&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



