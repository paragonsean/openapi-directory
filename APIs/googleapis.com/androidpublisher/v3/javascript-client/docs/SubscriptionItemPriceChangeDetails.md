# GooglePlayAndroidDeveloperApi.SubscriptionItemPriceChangeDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectedNewPriceChargeTime** | **String** | The renewal time at which the price change will become effective for the user. This is subject to change(to a future time) due to cases where the renewal time shifts like pause. This field is only populated if the price change has not taken effect. | [optional] 
**newPrice** | [**Money**](Money.md) |  | [optional] 
**priceChangeMode** | **String** | Price change mode specifies how the subscription item price is changing. | [optional] 
**priceChangeState** | **String** | State the price change is currently in. | [optional] 



## Enum: PriceChangeModeEnum


* `PRICE_CHANGE_MODE_UNSPECIFIED` (value: `"PRICE_CHANGE_MODE_UNSPECIFIED"`)

* `PRICE_DECREASE` (value: `"PRICE_DECREASE"`)

* `PRICE_INCREASE` (value: `"PRICE_INCREASE"`)

* `OPT_OUT_PRICE_INCREASE` (value: `"OPT_OUT_PRICE_INCREASE"`)





## Enum: PriceChangeStateEnum


* `PRICE_CHANGE_STATE_UNSPECIFIED` (value: `"PRICE_CHANGE_STATE_UNSPECIFIED"`)

* `OUTSTANDING` (value: `"OUTSTANDING"`)

* `CONFIRMED` (value: `"CONFIRMED"`)

* `APPLIED` (value: `"APPLIED"`)




