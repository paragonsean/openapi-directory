

# Usage

Describes Storage Resource Usage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentValue** | **Integer** | Gets the current count of the allocated resources in the subscription. |  [optional] [readonly] |
|**limit** | **Integer** | Gets the maximum count of the resources that can be allocated in the subscription. |  [optional] [readonly] |
|**name** | [**UsageName**](UsageName.md) |  |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Gets the unit of measurement. |  [optional] [readonly] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| PERCENT | &quot;Percent&quot; |
| COUNTS_PER_SECOND | &quot;CountsPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



