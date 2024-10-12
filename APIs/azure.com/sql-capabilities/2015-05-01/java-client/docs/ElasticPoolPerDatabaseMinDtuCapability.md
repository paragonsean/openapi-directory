

# ElasticPoolPerDatabaseMinDtuCapability

The minimum per-database DTU capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limit** | **Integer** | The minimum DTUs per database. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



