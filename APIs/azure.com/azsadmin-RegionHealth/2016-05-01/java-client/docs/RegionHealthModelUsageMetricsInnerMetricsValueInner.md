

# RegionHealthModelUsageMetricsInnerMetricsValueInner

Metrics for a source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maCounterName** | **String** | Name of the counter. |  [optional] |
|**name** | **String** | Name of the usage metric. |  [optional] |
|**observedTimestamp** | **OffsetDateTime** | Time counter was observed. |  [optional] |
|**sourceName** | [**SourceNameEnum**](#SourceNameEnum) | The origin of the metric. |  [optional] |
|**sourceType** | **String** | Type of the source. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit of the metric. |  [optional] |
|**value** | **Double** | Name of the usage metric. |  [optional] |



## Enum: SourceNameEnum

| Name | Value |
|---- | -----|
| PHYSICAL_NODE | &quot;PhysicalNode&quot; |
| VIRTUAL_MACHINE | &quot;VirtualMachine&quot; |
| RESOURCE_PROVIDER | &quot;ResourceProvider&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| ONE | &quot;One&quot; |
| PERCENTAGE | &quot;Percentage&quot; |
| B | &quot;B&quot; |
| KB | &quot;KB&quot; |
| MB | &quot;MB&quot; |
| GB | &quot;GB&quot; |
| TB | &quot;TB&quot; |



