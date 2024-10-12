

# Split


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | **String** | The unique identifier of the account to which the split amount is booked. Required if &#x60;type&#x60; is **MarketPlace** or **BalanceAccount**.  * [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic): The [&#x60;accountCode&#x60;](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount#request-accountCode) of the account to which the split amount is booked. * [Balance Platform](https://docs.adyen.com/marketplaces-and-platforms): The [&#x60;balanceAccountId&#x60;](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/_id_#path-id) of the account to which the split amount is booked. |  [optional] |
|**amount** | [**SplitAmount**](SplitAmount.md) | The amount of the split item.  * Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic). * Required if &#x60;type&#x60; is **BalanceAccount**, **Commission**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/marketplaces-and-platforms) integration. |  [optional] |
|**description** | **String** | Your description for the split item. |  [optional] |
|**reference** | **String** | Your unique reference for the split item.  This is required if &#x60;type&#x60; is **MarketPlace** ([Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic)) or **BalanceAccount** ([Balance Platform](https://docs.adyen.com/marketplaces-and-platforms)).  For the other types, we also recommend providing a **unique** reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the split item.  Possible values:  * [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic): **Commission**, **Default**, **Marketplace**, **PaymentFee**, **VAT**. * [Balance Platform](https://docs.adyen.com/marketplaces-and-platforms): **BalanceAccount**, **Commission**, **Default**, **PaymentFee**, **Remainder**, **Surcharge**, **Tip**, **VAT**. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACQUIRING_FEES | &quot;AcquiringFees&quot; |
| ADYEN_COMMISSION | &quot;AdyenCommission&quot; |
| ADYEN_FEES | &quot;AdyenFees&quot; |
| ADYEN_MARKUP | &quot;AdyenMarkup&quot; |
| BALANCE_ACCOUNT | &quot;BalanceAccount&quot; |
| COMMISSION | &quot;Commission&quot; |
| DEFAULT | &quot;Default&quot; |
| INTERCHANGE | &quot;Interchange&quot; |
| MARKET_PLACE | &quot;MarketPlace&quot; |
| PAYMENT_FEE | &quot;PaymentFee&quot; |
| REMAINDER | &quot;Remainder&quot; |
| SCHEME_FEE | &quot;SchemeFee&quot; |
| SURCHARGE | &quot;Surcharge&quot; |
| TIP | &quot;Tip&quot; |
| VAT | &quot;VAT&quot; |



