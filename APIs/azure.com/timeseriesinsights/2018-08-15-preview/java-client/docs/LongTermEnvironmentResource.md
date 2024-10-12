

# LongTermEnvironmentResource

An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource. LongTerm environments do not have set data retention limits.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**LongTermEnvironmentResourceProperties**](LongTermEnvironmentResourceProperties.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | The kind of the environment. |  |
|**sku** | [**Sku**](Sku.md) |  |  |
|**location** | **String** | Resource location |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**name** | **String** | Resource name |  [optional] [readonly] |
|**type** | **String** | Resource type |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| LONG_TERM | &quot;LongTerm&quot; |



