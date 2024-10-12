

# ElasticPoolPerDatabaseMinPerformanceLevelCapability

The minimum per-database performance level capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limit** | **Double** | The minimum performance level per database. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | Unit type used to measure performance level. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| DTU | &quot;DTU&quot; |
| V_CORES | &quot;VCores&quot; |



