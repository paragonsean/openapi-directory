

# TransferCategoryData

The relevant data according to the transfer category.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**priority** | [**PriorityEnum**](#PriorityEnum) | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with &#x60;category&#x60; **bank**.  Possible values:  * **regular**: For normal, low-value transactions.  * **fast**: Faster way to transfer funds but has higher fees. Recommended for high-priority, low-value transactions.  * **wire**: Fastest way to transfer funds but has the highest fees. Recommended for high-priority, high-value transactions.  * **instant**: Instant way to transfer funds in [SEPA countries](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  * **crossBorder**: High-value transfer to a recipient in a different country.  * **internal**: Transfer to an Adyen-issued business bank account (by bank account number/IBAN). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **bank** |  [optional] |
|**modificationMerchantReference** | **String** | The capture&#39;s merchant reference included in the transfer. |  [optional] |
|**modificationPspReference** | **String** | The capture reference included in the transfer. |  [optional] |
|**authorisationType** | **String** | The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation** |  [optional] |
|**panEntryMode** | [**PanEntryModeEnum**](#PanEntryModeEnum) | Indicates the method used for entering the PAN to initiate a transaction.  Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**. |  [optional] |
|**processingType** | [**ProcessingTypeEnum**](#ProcessingTypeEnum) | Contains information about how the payment was processed. For example, **ecommerce** for online or **pos** for in-person payments. |  [optional] |
|**relayedAuthorisationData** | [**RelayedAuthorisationData**](RelayedAuthorisationData.md) | If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server. |  [optional] |
|**schemeTraceId** | **String** | The identifier of the original payment provided by the scheme. The Id could be alphanumeric or numeric depending on the scheme. The schemeTraceID should be referring to an original schemeUniqueTransactionID provided in an earlier payment (not necessarily processed by Adyen). Instances of available schemeTraceId is authAdjustment or recurring payments. |  [optional] |
|**schemeUniqueTransactionId** | **String** | The unique identifier created by the scheme. The ID could be alphanumeric or numeric depending on the scheme. |  [optional] |
|**validationFacts** | [**List&lt;TransferNotificationValidationFact&gt;**](TransferNotificationValidationFact.md) | The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information. |  [optional] |
|**paymentMerchantReference** | **String** | The payment&#39;s merchant reference included in the transfer. |  [optional] |
|**platformPaymentType** | [**PlatformPaymentTypeEnum**](#PlatformPaymentTypeEnum) | The type of the related split. |  [optional] |
|**pspPaymentReference** | **String** | The payment reference included in the transfer. |  [optional] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| CROSS_BORDER | &quot;crossBorder&quot; |
| FAST | &quot;fast&quot; |
| INSTANT | &quot;instant&quot; |
| INTERNAL | &quot;internal&quot; |
| REGULAR | &quot;regular&quot; |
| WIRE | &quot;wire&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| INTERNAL | &quot;internal&quot; |
| ISSUED_CARD | &quot;issuedCard&quot; |
| PLATFORM_PAYMENT | &quot;platformPayment&quot; |



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



