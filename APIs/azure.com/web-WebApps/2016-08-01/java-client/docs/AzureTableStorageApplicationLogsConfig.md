

# AzureTableStorageApplicationLogsConfig

Application logs to Azure table storage configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | [**LevelEnum**](#LevelEnum) | Log level. |  [optional] |
|**sasUrl** | **String** | SAS URL to an Azure table with add/query/delete permissions. |  |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| OFF | &quot;Off&quot; |
| VERBOSE | &quot;Verbose&quot; |
| INFORMATION | &quot;Information&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |



