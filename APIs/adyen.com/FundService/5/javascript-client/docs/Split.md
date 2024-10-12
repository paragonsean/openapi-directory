# FundApi.Split

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | Unique identifier of the account where the split amount should be sent. This is required if &#x60;type&#x60; is **MarketPlace** or **BalanceAccount**.   | [optional] 
**amount** | [**SplitAmount**](SplitAmount.md) | The amount of this split. | 
**description** | **String** | A description of this split. | [optional] 
**reference** | **String** | Your reference for the split, which you can use to link the split to other operations such as captures and refunds.  This is required if &#x60;type&#x60; is **MarketPlace** or **BalanceAccount**. For the other types, we also recommend sending a reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. If the reference is not provided, the split is reported as part of the aggregated [TransferBalance record type](https://docs.adyen.com/reporting/marketpay-payments-accounting-report) in Adyen for Platforms. | [optional] 
**type** | **String** | The type of split. Possible values: **Default**, **PaymentFee**, **VAT**, **Commission**, **MarketPlace**, **BalanceAccount**, **Remainder**, **Surcharge**, **Tip**. | 



## Enum: TypeEnum


* `BalanceAccount` (value: `"BalanceAccount"`)

* `Commission` (value: `"Commission"`)

* `Default` (value: `"Default"`)

* `MarketPlace` (value: `"MarketPlace"`)

* `PaymentFee` (value: `"PaymentFee"`)

* `PaymentFeeAcquiring` (value: `"PaymentFeeAcquiring"`)

* `PaymentFeeAdyen` (value: `"PaymentFeeAdyen"`)

* `PaymentFeeAdyenCommission` (value: `"PaymentFeeAdyenCommission"`)

* `PaymentFeeAdyenMarkup` (value: `"PaymentFeeAdyenMarkup"`)

* `PaymentFeeInterchange` (value: `"PaymentFeeInterchange"`)

* `PaymentFeeSchemeFee` (value: `"PaymentFeeSchemeFee"`)

* `Remainder` (value: `"Remainder"`)

* `Surcharge` (value: `"Surcharge"`)

* `Tip` (value: `"Tip"`)

* `VAT` (value: `"VAT"`)

* `Verification` (value: `"Verification"`)




