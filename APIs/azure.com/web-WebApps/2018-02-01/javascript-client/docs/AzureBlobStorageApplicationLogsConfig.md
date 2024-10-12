# WebAppsApiClient.AzureBlobStorageApplicationLogsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **String** | Log level. | [optional] 
**retentionInDays** | **Number** | Retention in days. Remove blobs older than X days. 0 or lower means no retention. | [optional] 
**sasUrl** | **String** | SAS url to a azure blob container with read/write/list/delete permissions. | [optional] 



## Enum: LevelEnum


* `Off` (value: `"Off"`)

* `Verbose` (value: `"Verbose"`)

* `Information` (value: `"Information"`)

* `Warning` (value: `"Warning"`)

* `Error` (value: `"Error"`)




