

# PlatformPayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | **String** | The account given in the related split. |  [optional] |
|**description** | **String** | The description of the related split. |  [optional] |
|**modificationMerchantReference** | **String** | The merchant reference of the modification. |  [optional] |
|**modificationPspReference** | **String** | The pspReference of the modification. |  [optional] |
|**paymentMerchantReference** | **String** | The merchant reference of the payment. |  [optional] |
|**paymentPspReference** | **String** | The pspReference of the payment. |  [optional] |
|**reference** | **String** | The reference of the related split. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the related split. |  [optional] |



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
| PAYMENT_FEE | &quot;PaymentFee&quot; |
| REMAINDER | &quot;Remainder&quot; |
| SCHEME_FEE | &quot;SchemeFee&quot; |
| TOP_UP | &quot;TopUp&quot; |
| VAT | &quot;VAT&quot; |



