

# TransactionNotificationData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolder** | [**ResourceReference**](ResourceReference.md) | Contains information about the account holder. |  [optional] |
|**amount** | [**Amount**](Amount.md) | The amount converted to the balance account&#39;s currency, in case the original transaction currency is different.  * A _positive_ value means the amount is added to the balance account.   * A _negative_ value means the amount is deducted from the balance account.  |  [optional] |
|**authCode** | **String** | The authorisation code for the payment. |  [optional] |
|**balanceAccount** | [**ResourceReference**](ResourceReference.md) | Contains information about the balance account. |  [optional] |
|**balancePlatform** | **String** | The unique identifier of the balance platform. |  [optional] |
|**counterparty** | [**Counterparty**](Counterparty.md) | Contains information about the other party in the transaction. |  |
|**creationDate** | **OffsetDateTime** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |  [optional] |
|**description** | **String** | Your description for the transfer. If you send a description longer than 140 characters, the text is truncated. |  [optional] |
|**id** | **String** | The ID of the resource. |  [optional] |
|**merchantData** | [**MerchantData**](MerchantData.md) | Contains information about the merchant that processed the payment. This object is only included for payment authorisation requests and captures. |  [optional] |
|**modification** | [**NotificationModificationData**](NotificationModificationData.md) | Contains the amount and type of modification that triggered the notification. For example, this object contains the amount of a partial cancellation or partial expired authorisation. |  [optional] |
|**originalAmount** | [**Amount**](Amount.md) | The amount in the original currency of the transaction.  * A _positive_ value means the amount is added to the balance account.   * A _negative_ value means the amount is deducted from the balance account.  |  [optional] |
|**paymentId** | **String** | The ID of the original payment authorisation, refund, or funds transfer request. Use this to trace the original request from the &#x60;balancePlatform.payment.created&#x60; webhook. |  [optional] |
|**paymentInstrument** | [**ResourceReference**](ResourceReference.md) | Contains information about the payment instrument. |  [optional] |
|**platformPayment** | [**PlatformPayment**](PlatformPayment.md) | Contains information about the related platform payment. |  [optional] |
|**processingType** | [**ProcessingTypeEnum**](#ProcessingTypeEnum) | Contains information about how the payment was processed. Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **purchaseWithCashback**, **recurring**, **token**, **unknown**. |  [optional] |
|**purposeCode** | **String** | Indicates the purpose of the outgoing transfer. Adyen sets this to:  * **payoutManual** when the transfer was triggered by a one-off payout using the [&#x60;/transfers&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers) endpoint.   * **payoutSweep** when the transfer was triggered by a scheduled payout using [&#x60;sweepConfigurations&#x60;](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_sweepConfigurations). |  [optional] |
|**reference** | **String** | The [&#x60;reference&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the &#x60;/transfers&#x60; request. If you haven&#39;t provided any, Adyen generates a unique reference. |  [optional] |
|**referenceForBeneficiary** | **String** | The reference sent to or received from the counterparty.  * For outgoing funds, this is the [&#x60;referenceForBeneficiary&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary) from the  [&#x60;/transfers&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers) request.   * For incoming funds, this is the reference from the sender. |  [optional] |
|**relayedAuthorisationData** | [**RelayedAuthorisationData**](RelayedAuthorisationData.md) | If you&#39;re using [relayed authorisation](https://docs.adyen.com/issuing/processing-payments-for-cards#relayed-authorisation), this object contains information from the relayed authorisation response from your server. |  [optional] |
|**status** | **String** | The event status. The possible values depend on the &#x60;type&#x60;.  * **Authorised**, **Refused**, or **Error** for type &#x60;balancePlatform.payment.created&#x60;   * **Expired** or **Cancelled** or **AuthAdjustmentAuthorised** or **AuthAdjustmentRefused** for type &#x60;balancePlatform.payment.updated&#x60;  * **PendingIncomingTransfer** for type &#x60;balancePlatform.incomingTransfer.created&#x60;   * **Refunded** or **IncomingTransfer** for type &#x60;balancePlatform.incomingTransfer.updated&#x60;   * **Captured** or **OutgoingTransfer** for type &#x60;balancePlatform.outgoingTransfer.created&#x60;  * **TransferConfirmed**, **TransferSentOut**, or **TransferFailed** for type &#x60;balancePlatform.outgoingTransfer.updated&#x60;     |  [optional] |
|**transactionRulesResult** | [**TransactionRulesResult**](TransactionRulesResult.md) | Contains results from the evaluation of [transaction rules](https://docs.adyen.com/issuing/transaction-rules). |  [optional] |
|**validationResult** | [**List&lt;ValidationResult&gt;**](ValidationResult.md) | Array of checks that Adyen performed to validate the payment and the result of each. |  [optional] |
|**valueDate** | **OffsetDateTime** | Indicates the expected settlement date of this transaction, in ISO 8601 extended format. For example, **2021-08-17T15:34:37+02:00**. |  [optional] |



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
| UNKNOWN | &quot;unknown&quot; |



