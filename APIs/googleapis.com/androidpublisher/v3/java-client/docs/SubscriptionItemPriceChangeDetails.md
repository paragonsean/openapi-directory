

# SubscriptionItemPriceChangeDetails

Price change related information of a subscription item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectedNewPriceChargeTime** | **String** | The renewal time at which the price change will become effective for the user. This is subject to change(to a future time) due to cases where the renewal time shifts like pause. This field is only populated if the price change has not taken effect. |  [optional] |
|**newPrice** | [**Money**](Money.md) |  |  [optional] |
|**priceChangeMode** | [**PriceChangeModeEnum**](#PriceChangeModeEnum) | Price change mode specifies how the subscription item price is changing. |  [optional] |
|**priceChangeState** | [**PriceChangeStateEnum**](#PriceChangeStateEnum) | State the price change is currently in. |  [optional] |



## Enum: PriceChangeModeEnum

| Name | Value |
|---- | -----|
| PRICE_CHANGE_MODE_UNSPECIFIED | &quot;PRICE_CHANGE_MODE_UNSPECIFIED&quot; |
| PRICE_DECREASE | &quot;PRICE_DECREASE&quot; |
| PRICE_INCREASE | &quot;PRICE_INCREASE&quot; |
| OPT_OUT_PRICE_INCREASE | &quot;OPT_OUT_PRICE_INCREASE&quot; |



## Enum: PriceChangeStateEnum

| Name | Value |
|---- | -----|
| PRICE_CHANGE_STATE_UNSPECIFIED | &quot;PRICE_CHANGE_STATE_UNSPECIFIED&quot; |
| OUTSTANDING | &quot;OUTSTANDING&quot; |
| CONFIRMED | &quot;CONFIRMED&quot; |
| APPLIED | &quot;APPLIED&quot; |



