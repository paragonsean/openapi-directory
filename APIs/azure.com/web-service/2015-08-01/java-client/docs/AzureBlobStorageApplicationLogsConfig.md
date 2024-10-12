

# AzureBlobStorageApplicationLogsConfig

Application logs azure blob storage configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | [**LevelEnum**](#LevelEnum) | Log level |  [optional] |
|**retentionInDays** | **Integer** | Retention in days.              Remove blobs older than X days.              0 or lower means no retention. |  [optional] |
|**sasUrl** | **String** | SAS url to a azure blob container with read/write/list/delete permissions |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| OFF | &quot;Off&quot; |
| VERBOSE | &quot;Verbose&quot; |
| INFORMATION | &quot;Information&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |



