

# StandalonePaymentCancelResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**merchantAccount** | **String** | The merchant account that is used to process the payment. |  |
|**paymentReference** | **String** | The [&#x60;reference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference) of the payment to cancel. |  |
|**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the cancel request. |  |
|**reference** | **String** | Your reference for the cancel request. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of your request. This will always have the value **received**. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RECEIVED | &quot;received&quot; |



