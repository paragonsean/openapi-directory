

# PaymentAmountUpdateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The updated amount. |  |
|**merchantAccount** | **String** | The merchant account that is used to process the payment. |  |
|**paymentPspReference** | **String** | The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to update.  |  |
|**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the amount update request. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason for the amount update. Possible values:  * **DelayedCharge**  * **NoShow** |  [optional] |
|**reference** | **String** | Your reference for the amount update request. Maximum length: 80 characters. |  |
|**splits** | [**List&lt;Split&gt;**](Split.md) | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of your request. This will always have the value **received**. |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| DELAYED_CHARGE | &quot;delayedCharge&quot; |
| NO_SHOW | &quot;noShow&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RECEIVED | &quot;received&quot; |



