

# GoogleCloudChannelV1PricePhase

Specifies the price by the duration of months. For example, a 20% discount for the first six months, then a 10% discount starting on the seventh month.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstPeriod** | **Integer** | Defines first period for the phase. |  [optional] |
|**lastPeriod** | **Integer** | Defines first period for the phase. |  [optional] |
|**periodType** | [**PeriodTypeEnum**](#PeriodTypeEnum) | Defines the phase period type. |  [optional] |
|**price** | [**GoogleCloudChannelV1Price**](GoogleCloudChannelV1Price.md) |  |  [optional] |
|**priceTiers** | [**List&lt;GoogleCloudChannelV1PriceTier&gt;**](GoogleCloudChannelV1PriceTier.md) | Price by the resource tiers. |  [optional] |



## Enum: PeriodTypeEnum

| Name | Value |
|---- | -----|
| PERIOD_TYPE_UNSPECIFIED | &quot;PERIOD_TYPE_UNSPECIFIED&quot; |
| DAY | &quot;DAY&quot; |
| MONTH | &quot;MONTH&quot; |
| YEAR | &quot;YEAR&quot; |



