

# PlatformPayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modificationMerchantReference** | **String** | The capture&#39;s merchant reference included in the transfer. |  [optional] |
|**modificationPspReference** | **String** | The capture reference included in the transfer. |  [optional] |
|**paymentMerchantReference** | **String** | The payment&#39;s merchant reference included in the transfer. |  [optional] |
|**platformPaymentType** | [**PlatformPaymentTypeEnum**](#PlatformPaymentTypeEnum) | The type of the related split. |  [optional] |
|**pspPaymentReference** | **String** | The payment reference included in the transfer. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **platformPayment** |  [optional] |



## Enum: PlatformPaymentTypeEnum

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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PLATFORM_PAYMENT | &quot;platformPayment&quot; |



