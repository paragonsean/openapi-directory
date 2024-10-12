

# Split


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | **String** | Unique identifier of the account where the split amount should be sent. This is required if &#x60;type&#x60; is **MarketPlace** or **BalanceAccount**.   |  [optional] |
|**amount** | [**SplitAmount**](SplitAmount.md) | The amount of this split. |  |
|**description** | **String** | A description of this split. |  [optional] |
|**reference** | **String** | Your reference for the split, which you can use to link the split to other operations such as captures and refunds.  This is required if &#x60;type&#x60; is **MarketPlace** or **BalanceAccount**. For the other types, we also recommend sending a reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. If the reference is not provided, the split is reported as part of the aggregated [TransferBalance record type](https://docs.adyen.com/reporting/marketpay-payments-accounting-report) in Adyen for Platforms. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of split. Possible values: **Default**, **PaymentFee**, **VAT**, **Commission**, **MarketPlace**, **BalanceAccount**, **Remainder**, **Surcharge**, **Tip**. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BALANCE_ACCOUNT | &quot;BalanceAccount&quot; |
| COMMISSION | &quot;Commission&quot; |
| DEFAULT | &quot;Default&quot; |
| MARKET_PLACE | &quot;MarketPlace&quot; |
| PAYMENT_FEE | &quot;PaymentFee&quot; |
| PAYMENT_FEE_ACQUIRING | &quot;PaymentFeeAcquiring&quot; |
| PAYMENT_FEE_ADYEN | &quot;PaymentFeeAdyen&quot; |
| PAYMENT_FEE_ADYEN_COMMISSION | &quot;PaymentFeeAdyenCommission&quot; |
| PAYMENT_FEE_ADYEN_MARKUP | &quot;PaymentFeeAdyenMarkup&quot; |
| PAYMENT_FEE_INTERCHANGE | &quot;PaymentFeeInterchange&quot; |
| PAYMENT_FEE_SCHEME_FEE | &quot;PaymentFeeSchemeFee&quot; |
| REMAINDER | &quot;Remainder&quot; |
| SURCHARGE | &quot;Surcharge&quot; |
| TIP | &quot;Tip&quot; |
| VAT | &quot;VAT&quot; |
| VERIFICATION | &quot;Verification&quot; |



