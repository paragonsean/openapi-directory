# MigrationCenterApi.ImportDataFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp when the file was created. | [optional] [readonly] 
**displayName** | **String** | User-friendly display name. Maximum length is 63 characters. | [optional] 
**format** | **String** | Required. The payload format. | [optional] 
**name** | **String** | Output only. The name of the file. | [optional] [readonly] 
**state** | **String** | Output only. The state of the import data file. | [optional] [readonly] 
**uploadFileInfo** | [**UploadFileInfo**](UploadFileInfo.md) |  | [optional] 



## Enum: FormatEnum


* `UNSPECIFIED` (value: `"IMPORT_JOB_FORMAT_UNSPECIFIED"`)

* `RVTOOLS_XLSX` (value: `"IMPORT_JOB_FORMAT_RVTOOLS_XLSX"`)

* `RVTOOLS_CSV` (value: `"IMPORT_JOB_FORMAT_RVTOOLS_CSV"`)

* `EXPORTED_AWS_CSV` (value: `"IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV"`)

* `EXPORTED_AZURE_CSV` (value: `"IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV"`)

* `STRATOZONE_CSV` (value: `"IMPORT_JOB_FORMAT_STRATOZONE_CSV"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)




