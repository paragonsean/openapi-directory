

# BalanceCheckResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | [**BalanceCheckResponseAdditionalData**](BalanceCheckResponseAdditionalData.md) |  |  [optional] |
|**balance** | [**Amount**](Amount.md) | The balance for the payment method. |  |
|**fraudResult** | [**FraudResult**](FraudResult.md) | The fraud result properties of the payment. |  [optional] |
|**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |  [optional] |
|**refusalReason** | **String** | If the payment&#39;s authorisation is refused or an error occurs during authorisation, this field holds Adyen&#39;s mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes &#x60;resultCode&#x60; and &#x60;refusalReason&#x60; values.  For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |  [optional] |
|**resultCode** | [**ResultCodeEnum**](#ResultCodeEnum) | The result of the cancellation request.  Possible values:  * **Success** – Indicates that the balance check was successful. * **NotEnoughBalance** – Commonly indicates that the card did not have enough balance to pay the amount in the request, or that the currency of the balance on the card did not match the currency of the requested amount. * **Failed** – Indicates that the balance check failed. |  |



## Enum: ResultCodeEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;Success&quot; |
| NOT_ENOUGH_BALANCE | &quot;NotEnoughBalance&quot; |
| FAILED | &quot;Failed&quot; |



