# TransfersApi.Transfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The amount of the transfer. | 
**balanceAccountId** | **String** | The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id). | [optional] 
**bank** | [**Bank**](Bank.md) | Contains settings for bank transfers. If you are transferring funds to bank accounts and you don&#39;t provide this object, Adyen applies default settings. | [optional] 
**counterparty** | [**Counterparty**](Counterparty.md) | The other party in the transfer. | 
**description** | **String** | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.  Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , &#39; + Space**  Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] &amp; $ % # @** **~ &#x3D; + - _ &#39; \&quot; ! ?** | [optional] 
**direction** | **String** | The direction of the transfer.  Possible values: **incoming**, **outgoing**. | [optional] 
**id** | **String** | The ID of the resource. | [optional] 
**paymentInstrumentId** | **String** | The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id) used in the transfer. | [optional] 
**reason** | **String** | Additional information about the status of the transfer. | [optional] 
**reference** | **String** | Your reference for the transfer, used internally within your platform. If you don&#39;t provide this in the request, Adyen generates a unique reference. | [optional] 
**referenceForBeneficiary** | **String** |  A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.   Supported characters: **a-z**, **A-Z**, **0-9**. Maximum length: 80 characters. | [optional] 
**status** | **String** | The result of the transfer.   For example, **authorised**, **refused**, or **error**. | 



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




