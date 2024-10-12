

# PaymentReversalResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**merchantAccount** | **String** | The merchant account that is used to process the payment. |  |
|**paymentPspReference** | **String** | The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to reverse.  |  |
|**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the reversal request. |  |
|**reference** | **String** | Your reference for the reversal request. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of your request. This will always have the value **received**. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RECEIVED | &quot;received&quot; |



