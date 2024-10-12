

# NameAndKind

Basic metadata about a counter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Counter aggregation kind. |  [optional] |
|**name** | **String** | Name of the counter. |  [optional] |



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



