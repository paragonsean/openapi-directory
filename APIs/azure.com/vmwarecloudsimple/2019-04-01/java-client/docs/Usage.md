

# Usage

Usage model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentValue** | **Integer** | The current usage value |  |
|**limit** | **Integer** | limit of a given sku in a region for a subscription. The maximum permitted value for the usage quota. If there is no limit, this value will be -1 |  |
|**name** | [**UsageName**](UsageName.md) |  |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The usages&#39; unit |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| PERCENT | &quot;Percent&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



