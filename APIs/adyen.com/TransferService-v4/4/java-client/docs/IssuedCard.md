

# IssuedCard


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorisationType** | **String** | The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation** |  [optional] |
|**panEntryMode** | [**PanEntryModeEnum**](#PanEntryModeEnum) | Indicates the method used for entering the PAN to initiate a transaction.  Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**. |  [optional] |
|**processingType** | [**ProcessingTypeEnum**](#ProcessingTypeEnum) | Contains information about how the payment was processed. For example, **ecommerce** for online or **pos** for in-person payments. |  [optional] |
|**relayedAuthorisationData** | [**RelayedAuthorisationData**](RelayedAuthorisationData.md) | If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server. |  [optional] |
|**schemeTraceId** | **String** | The identifier of the original payment provided by the scheme. The Id could be alphanumeric or numeric depending on the scheme. The schemeTraceID should be referring to an original schemeUniqueTransactionID provided in an earlier payment (not necessarily processed by Adyen). Instances of available schemeTraceId is authAdjustment or recurring payments. |  [optional] |
|**schemeUniqueTransactionId** | **String** | The unique identifier created by the scheme. The ID could be alphanumeric or numeric depending on the scheme. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **issuedCard** |  [optional] |
|**validationFacts** | [**List&lt;TransferNotificationValidationFact&gt;**](TransferNotificationValidationFact.md) | The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information. |  [optional] |



## Enum: PanEntryModeEnum

| Name | Value |
|---- | -----|
| CHIP | &quot;chip&quot; |
| COF | &quot;cof&quot; |
| CONTACTLESS | &quot;contactless&quot; |
| ECOMMERCE | &quot;ecommerce&quot; |
| MAGSTRIPE | &quot;magstripe&quot; |
| MANUAL | &quot;manual&quot; |
| TOKEN | &quot;token&quot; |



## Enum: ProcessingTypeEnum

| Name | Value |
|---- | -----|
| ATM_WITHDRAW | &quot;atmWithdraw&quot; |
| BALANCE_INQUIRY | &quot;balanceInquiry&quot; |
| ECOMMERCE | &quot;ecommerce&quot; |
| MOTO | &quot;moto&quot; |
| POS | &quot;pos&quot; |
| PURCHASE_WITH_CASHBACK | &quot;purchaseWithCashback&quot; |
| RECURRING | &quot;recurring&quot; |
| TOKEN | &quot;token&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ISSUED_CARD | &quot;issuedCard&quot; |



