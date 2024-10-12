

# UpdateNetworkWirelessBillingRequestPlansInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthLimits** | [**UpdateNetworkWirelessBillingRequestPlansInnerBandwidthLimits**](UpdateNetworkWirelessBillingRequestPlansInnerBandwidthLimits.md) |  |  |
|**id** | **String** | The id of the pricing plan to update. |  [optional] |
|**price** | **Float** | The price of the billing plan. |  |
|**timeLimit** | [**TimeLimitEnum**](#TimeLimitEnum) | The time limit of the pricing plan in minutes. Can be &#39;1 hour&#39;, &#39;1 day&#39;, &#39;1 week&#39;, or &#39;30 days&#39;. |  |



## Enum: TimeLimitEnum

| Name | Value |
|---- | -----|
| _1_DAY | &quot;1 day&quot; |
| _1_HOUR | &quot;1 hour&quot; |
| _1_WEEK | &quot;1 week&quot; |
| _30_DAYS | &quot;30 days&quot; |



