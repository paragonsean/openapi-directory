

# CounterMetadata

CounterMetadata includes all static non-name non-value counter attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Human-readable description of the counter semantics. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Counter aggregation kind. |  [optional] |
|**otherUnits** | **String** | A string referring to the unit type. |  [optional] |
|**standardUnits** | [**StandardUnitsEnum**](#StandardUnitsEnum) | System defined Units, see above enum. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;INVALID&quot; |
| SUM | &quot;SUM&quot; |
| MAX | &quot;MAX&quot; |
| MIN | &quot;MIN&quot; |
| MEAN | &quot;MEAN&quot; |
| OR | &quot;OR&quot; |
| AND | &quot;AND&quot; |
| SET | &quot;SET&quot; |
| DISTRIBUTION | &quot;DISTRIBUTION&quot; |
| LATEST_VALUE | &quot;LATEST_VALUE&quot; |



## Enum: StandardUnitsEnum

| Name | Value |
|---- | -----|
| BYTES | &quot;BYTES&quot; |
| BYTES_PER_SEC | &quot;BYTES_PER_SEC&quot; |
| MILLISECONDS | &quot;MILLISECONDS&quot; |
| MICROSECONDS | &quot;MICROSECONDS&quot; |
| NANOSECONDS | &quot;NANOSECONDS&quot; |
| TIMESTAMP_MSEC | &quot;TIMESTAMP_MSEC&quot; |
| TIMESTAMP_USEC | &quot;TIMESTAMP_USEC&quot; |
| TIMESTAMP_NSEC | &quot;TIMESTAMP_NSEC&quot; |



