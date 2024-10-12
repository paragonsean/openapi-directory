# TransfersApi.Transfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolder** | [**ResourceReference**](ResourceReference.md) | The account holder associated with the balance account used in the transfer. | [optional] 
**amount** | [**Amount**](Amount.md) | The amount of the transfer. | 
**balanceAccount** | [**ResourceReference**](ResourceReference.md) | Contains information about the balance account involved in the transfer. | [optional] 
**category** | **String** | The category of transfer.  Possible values:   - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account.  - **internal**: Transfer to another [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id) within your platform.  - **issuedCard**: Transfer initiated by a Adyen-issued card.  - **platformPayment**: Fund movements related to payments that are acquired for your users. | 
**categoryData** | [**TransferCategoryData**](TransferCategoryData.md) |  | [optional] 
**counterparty** | [**CounterpartyV3**](CounterpartyV3.md) | The other party in the transfer. | 
**creationDate** | **Date** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. | [optional] 
**description** | **String** | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.  Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , &#39; + Space**  Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] &amp; $ % # @** **~ &#x3D; + - _ &#39; \&quot; ! ?** | [optional] 
**direction** | **String** | The direction of the transfer.  Possible values: **incoming**, **outgoing**. | [optional] 
**id** | **String** | The ID of the resource. | [optional] 
**paymentInstrument** | [**PaymentInstrument**](PaymentInstrument.md) | Contains information about the payment instrument used in the transfer. | [optional] 
**reason** | **String** | Additional information about the status of the transfer. | [optional] 
**reference** | **String** | Your reference for the transfer, used internally within your platform. If you don&#39;t provide this in the request, Adyen generates a unique reference. | [optional] 
**referenceForBeneficiary** | **String** |  A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.   Supported characters: **a-z**, **A-Z**, **0-9**. The maximum length depends on the &#x60;category&#x60;.  - **internal**: 80 characters  - **bank**: 35 characters when transferring to an IBAN, 15 characters for others. | [optional] 
**status** | **String** | The result of the transfer.   For example, **authorised**, **refused**, or **error**. | 



## Enum: CategoryEnum


* `bank` (value: `"bank"`)

* `internal` (value: `"internal"`)

* `issuedCard` (value: `"issuedCard"`)

* `platformPayment` (value: `"platformPayment"`)





## Enum: DirectionEnum


* `incoming` (value: `"incoming"`)

* `outgoing` (value: `"outgoing"`)





## Enum: ReasonEnum


* `amountLimitExceeded` (value: `"amountLimitExceeded"`)

* `approved` (value: `"approved"`)

* `balanceAccountTemporarilyBlockedByTransactionRule` (value: `"balanceAccountTemporarilyBlockedByTransactionRule"`)

* `counterpartyAccountBlocked` (value: `"counterpartyAccountBlocked"`)

* `counterpartyAccountClosed` (value: `"counterpartyAccountClosed"`)

* `counterpartyAccountNotFound` (value: `"counterpartyAccountNotFound"`)

* `counterpartyAddressRequired` (value: `"counterpartyAddressRequired"`)

* `counterpartyBankTimedOut` (value: `"counterpartyBankTimedOut"`)

* `counterpartyBankUnavailable` (value: `"counterpartyBankUnavailable"`)

* `declinedByTransactionRule` (value: `"declinedByTransactionRule"`)

* `error` (value: `"error"`)

* `notEnoughBalance` (value: `"notEnoughBalance"`)

* `refusedByCounterpartyBank` (value: `"refusedByCounterpartyBank"`)

* `routeNotFound` (value: `"routeNotFound"`)

* `scaFailed` (value: `"scaFailed"`)

* `unknown` (value: `"unknown"`)





## Enum: StatusEnum


* `approvalPending` (value: `"approvalPending"`)

* `atmWithdrawal` (value: `"atmWithdrawal"`)

* `atmWithdrawalReversalPending` (value: `"atmWithdrawalReversalPending"`)

* `atmWithdrawalReversed` (value: `"atmWithdrawalReversed"`)

* `authAdjustmentAuthorised` (value: `"authAdjustmentAuthorised"`)

* `authAdjustmentError` (value: `"authAdjustmentError"`)

* `authAdjustmentRefused` (value: `"authAdjustmentRefused"`)

* `authorised` (value: `"authorised"`)

* `bankTransfer` (value: `"bankTransfer"`)

* `bankTransferPending` (value: `"bankTransferPending"`)

* `booked` (value: `"booked"`)

* `bookingPending` (value: `"bookingPending"`)

* `cancelled` (value: `"cancelled"`)

* `capturePending` (value: `"capturePending"`)

* `captureReversalPending` (value: `"captureReversalPending"`)

* `captureReversed` (value: `"captureReversed"`)

* `captured` (value: `"captured"`)

* `capturedExternally` (value: `"capturedExternally"`)

* `chargeback` (value: `"chargeback"`)

* `chargebackExternally` (value: `"chargebackExternally"`)

* `chargebackPending` (value: `"chargebackPending"`)

* `chargebackReversalPending` (value: `"chargebackReversalPending"`)

* `chargebackReversed` (value: `"chargebackReversed"`)

* `credited` (value: `"credited"`)

* `depositCorrection` (value: `"depositCorrection"`)

* `depositCorrectionPending` (value: `"depositCorrectionPending"`)

* `dispute` (value: `"dispute"`)

* `disputeClosed` (value: `"disputeClosed"`)

* `disputeExpired` (value: `"disputeExpired"`)

* `disputeNeedsReview` (value: `"disputeNeedsReview"`)

* `error` (value: `"error"`)

* `expired` (value: `"expired"`)

* `failed` (value: `"failed"`)

* `fee` (value: `"fee"`)

* `feePending` (value: `"feePending"`)

* `internalTransfer` (value: `"internalTransfer"`)

* `internalTransferPending` (value: `"internalTransferPending"`)

* `invoiceDeduction` (value: `"invoiceDeduction"`)

* `invoiceDeductionPending` (value: `"invoiceDeductionPending"`)

* `manualCorrectionPending` (value: `"manualCorrectionPending"`)

* `manuallyCorrected` (value: `"manuallyCorrected"`)

* `matchedStatement` (value: `"matchedStatement"`)

* `matchedStatementPending` (value: `"matchedStatementPending"`)

* `merchantPayin` (value: `"merchantPayin"`)

* `merchantPayinPending` (value: `"merchantPayinPending"`)

* `merchantPayinReversed` (value: `"merchantPayinReversed"`)

* `merchantPayinReversedPending` (value: `"merchantPayinReversedPending"`)

* `miscCost` (value: `"miscCost"`)

* `miscCostPending` (value: `"miscCostPending"`)

* `paymentCost` (value: `"paymentCost"`)

* `paymentCostPending` (value: `"paymentCostPending"`)

* `received` (value: `"received"`)

* `refundPending` (value: `"refundPending"`)

* `refundReversalPending` (value: `"refundReversalPending"`)

* `refundReversed` (value: `"refundReversed"`)

* `refunded` (value: `"refunded"`)

* `refundedExternally` (value: `"refundedExternally"`)

* `refused` (value: `"refused"`)

* `reserveAdjustment` (value: `"reserveAdjustment"`)

* `reserveAdjustmentPending` (value: `"reserveAdjustmentPending"`)

* `returned` (value: `"returned"`)

* `secondChargeback` (value: `"secondChargeback"`)

* `secondChargebackPending` (value: `"secondChargebackPending"`)

* `undefined` (value: `"undefined"`)




