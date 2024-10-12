

# AzureTableStorageApplicationLogsConfig

Application logs to azure table storage configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | [**LevelEnum**](#LevelEnum) | Log level |  [optional] |
|**sasUrl** | **String** | SAS url to an azure table with add/query/delete permissions |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| OFF | &quot;Off&quot; |
| VERBOSE | &quot;Verbose&quot; |
| INFORMATION | &quot;Information&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |



