

# JobDefinitionFilter

Contains the supported job definition filters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSource** | **String** | The data source associated with the job definition |  [optional] |
|**lastModified** | **OffsetDateTime** | The last modified date time of the data source. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the job definition. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |
| SUPPORTED | &quot;Supported&quot; |



