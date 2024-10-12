# PaymentWebhooksDeprecated.IncomingTransferNotificationData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolder** | [**ResourceReference**](ResourceReference.md) | Contains information about the account holder. | [optional] 
**amount** | [**Amount**](Amount.md) | The amount converted to the balance account&#39;s currency, in case the original transaction currency is different.  * A _positive_ value means the amount is added to the balance account.   * A _negative_ value means the amount is deducted from the balance account.  | [optional] 
**balanceAccount** | [**ResourceReference**](ResourceReference.md) | Contains information about the balance account. | [optional] 
**balancePlatform** | **String** | The unique identifier of the balance platform. | [optional] 
**counterparty** | [**Counterparty**](Counterparty.md) | Contains information about the other party in the transaction. | [optional] 
**creationDate** | **Date** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. | [optional] 
**description** | **String** | Your description for the transfer. If you send a description longer than 140 characters, the text is truncated. | [optional] 
**id** | **String** | The ID of the resource. | [optional] 
**modification** | [**NotificationModificationData**](NotificationModificationData.md) | Contains the amount and type of modification that triggered the notification. For example, this object contains the amount of a partial cancellation or partial expired authorisation. | [optional] 
**originalAmount** | [**Amount**](Amount.md) | The amount in the original currency of the transaction.  * A _positive_ value means the amount is added to the balance account.   * A _negative_ value means the amount is deducted from the balance account.  | [optional] 
**paymentId** | **String** | The ID of the original payment authorisation, refund, or funds transfer request. Use this to trace the original request from the &#x60;balancePlatform.payment.created&#x60; webhook. | [optional] 
**paymentInstrument** | [**ResourceReference**](ResourceReference.md) | Contains information about the payment instrument. | [optional] 
**platformPayment** | [**PlatformPayment**](PlatformPayment.md) | Contains information about the related platform payment. | [optional] 
**reference** | **String** | An Adyen-generated unique reference for the transfer. | [optional] 
**referenceForBeneficiary** | **String** | The reference sent to or received from the counterparty.  * For outgoing funds, this is the [&#x60;referenceForBeneficiary&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary) from the  [&#x60;/transfers&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers) request.   * For incoming funds, this is the reference from the sender. | [optional] 
**status** | **String** | The event status. The possible values depend on the &#x60;type&#x60;.  * **Authorised**, **Refused**, or **Error** for type &#x60;balancePlatform.payment.created&#x60;   * **Expired** or **Cancelled** or **AuthAdjustmentAuthorised** or **AuthAdjustmentRefused** for type &#x60;balancePlatform.payment.updated&#x60;  * **PendingIncomingTransfer** for type &#x60;balancePlatform.incomingTransfer.created&#x60;   * **Refunded** or **IncomingTransfer** for type &#x60;balancePlatform.incomingTransfer.updated&#x60;   * **Captured** or **OutgoingTransfer** for type &#x60;balancePlatform.outgoingTransfer.created&#x60;  * **TransferConfirmed**, **TransferSentOut**, or **TransferFailed** for type &#x60;balancePlatform.outgoingTransfer.updated&#x60;     | [optional] 
**valueDate** | **Date** | Indicates the expected settlement date of this transaction, in ISO 8601 extended format. For example, **2021-08-17T15:34:37+02:00**. | [optional] 


