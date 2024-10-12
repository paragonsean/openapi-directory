

# Usage

Describes Storage Resource Usage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentValue** | **Integer** | The current count of the allocated resources in the subscription. |  |
|**limit** | **Integer** | The maximum count of the resources that can be allocated in the subscription. |  |
|**name** | [**UsageName**](UsageName.md) |  |  |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit of measurement. |  |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| PERCENT | &quot;Percent&quot; |
| COUNTS_PER_SECOND | &quot;CountsPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



