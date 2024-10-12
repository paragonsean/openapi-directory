

# ElasticPoolPerDatabaseMaxDtuCapability

The max per-database DTU capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limit** | **Integer** | The maximum DTUs per database. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedPerDatabaseMinDtus** | [**List&lt;ElasticPoolPerDatabaseMinDtuCapability&gt;**](ElasticPoolPerDatabaseMinDtuCapability.md) | The list of supported min database DTUs. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



