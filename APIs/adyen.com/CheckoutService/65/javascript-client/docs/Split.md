# AdyenCheckoutApi.Split

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | The unique identifier of the account to which the split amount is booked. Required if &#x60;type&#x60; is **MarketPlace** or **BalanceAccount**.  * [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic): The [&#x60;accountCode&#x60;](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount#request-accountCode) of the account to which the split amount is booked. * [Balance Platform](https://docs.adyen.com/marketplaces-and-platforms): The [&#x60;balanceAccountId&#x60;](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/_id_#path-id) of the account to which the split amount is booked. | [optional] 
**amount** | [**SplitAmount**](SplitAmount.md) | The amount of the split item.  * Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic). * Required if &#x60;type&#x60; is **BalanceAccount**, **Commission**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/marketplaces-and-platforms) integration. | [optional] 
**description** | **String** | Your description for the split item. | [optional] 
**reference** | **String** | Your unique reference for the split item.  This is required if &#x60;type&#x60; is **MarketPlace** ([Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic)) or **BalanceAccount** ([Balance Platform](https://docs.adyen.com/marketplaces-and-platforms)).  For the other types, we also recommend providing a **unique** reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. | [optional] 
**type** | **String** | The type of the split item.  Possible values:  * [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic): **Commission**, **Default**, **Marketplace**, **PaymentFee**, **VAT**. * [Balance Platform](https://docs.adyen.com/marketplaces-and-platforms): **BalanceAccount**, **Commission**, **Default**, **PaymentFee**, **Remainder**, **Surcharge**, **Tip**, **VAT**. | 



## Enum: TypeEnum


* `AcquiringFees` (value: `"AcquiringFees"`)

* `AdyenCommission` (value: `"AdyenCommission"`)

* `AdyenFees` (value: `"AdyenFees"`)

* `AdyenMarkup` (value: `"AdyenMarkup"`)

* `BalanceAccount` (value: `"BalanceAccount"`)

* `Commission` (value: `"Commission"`)

* `Default` (value: `"Default"`)

* `Interchange` (value: `"Interchange"`)

* `MarketPlace` (value: `"MarketPlace"`)

* `PaymentFee` (value: `"PaymentFee"`)

* `Remainder` (value: `"Remainder"`)

* `SchemeFee` (value: `"SchemeFee"`)

* `Surcharge` (value: `"Surcharge"`)

* `Tip` (value: `"Tip"`)

* `VAT` (value: `"VAT"`)




