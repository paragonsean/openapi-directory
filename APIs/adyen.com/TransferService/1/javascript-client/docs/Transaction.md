# TransfersApi.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderId** | **String** | Unique identifier of the account holder. | 
**amount** | [**Amount**](Amount.md) | Contains information about the amount of the transaction. | 
**balanceAccountId** | **String** | Unique identifier of the balance account. | 
**balancePlatform** | **String** | The unique identifier of the balance platform. | 
**bookingDate** | **Date** | The date the transaction was booked into the balance account. | 
**category** | **String** | The category of the transaction indicating the type of activity.   Possible values:  * **platformPayment**: The transaction is a payment or payment modification made with an Adyen merchant account.  * **internal**: The transaction resulted from an internal adjustment such as a deposit correction or invoice deduction.  * **bank**: The transaction is a bank-related activity, such as sending a payout or receiving funds.  * **issuedCard**: The transaction is a card-related activity, such as using an Adyen-issued card to pay online.   | [optional] 
**counterparty** | [**Counterparty**](Counterparty.md) | Contains information about the other party in the transaction. | 
**createdAt** | **Date** | The date the transaction was created. | 
**creationDate** | **Date** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. | [optional] 
**description** | **String** | The &#x60;description&#x60; from the &#x60;/transfers&#x60; request. | [optional] 
**id** | **String** | The unique identifier of the transaction. | 
**instructedAmount** | [**Amount**](Amount.md) | The amount that the sender instructed their bank to send. This can be higher than &#x60;amount.value&#x60; when their bank deducts costs for the transfer. | [optional] 
**paymentInstrumentId** | **String** | The unique identifier of the payment instrument that was used for the transaction. | [optional] 
**reference** | **String** | The [&#x60;reference&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the &#x60;/transfers&#x60; request. If you haven&#39;t provided any, Adyen generates a unique reference. | 
**referenceForBeneficiary** | **String** | The reference sent to or received from the counterparty.  * For outgoing funds, this is the [&#x60;referenceForBeneficiary&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary) from the  [&#x60;/transfers&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_referenceForBeneficiary) request.   * For incoming funds, this is the reference from the sender. | [optional] 
**status** | **String** | The status of the transaction.   Possible values:  * **pending**: The transaction is still pending.  * **booked**: The transaction has been booked to the balance account.   | 
**transferId** | **String** | Unique identifier of the related transfer. | [optional] 
**type** | **String** | The type of the transaction.   Possible values: **payment**, **capture**, **captureReversal**, **refund** **refundReversal**, **chargeback**, **chargebackReversal**, **secondChargeback**, **atmWithdrawal**, **atmWithdrawalReversal**, **internalTransfer**, **manualCorrection**, **invoiceDeduction**, **depositCorrection**, **bankTransfer**, **miscCost**, **paymentCost**, **fee** | [optional] 
**valueDate** | **Date** | The date the transfer amount becomes available in the balance account. | 



## Enum: CategoryEnum


* `bank` (value: `"bank"`)

* `card` (value: `"card"`)

* `grants` (value: `"grants"`)

* `internal` (value: `"internal"`)

* `issuedCard` (value: `"issuedCard"`)

* `migration` (value: `"migration"`)

* `platformPayment` (value: `"platformPayment"`)

* `topUp` (value: `"topUp"`)

* `upgrade` (value: `"upgrade"`)





## Enum: StatusEnum


* `booked` (value: `"booked"`)

* `pending` (value: `"pending"`)





## Enum: TypeEnum


* `atmWithdrawal` (value: `"atmWithdrawal"`)

* `atmWithdrawalReversal` (value: `"atmWithdrawalReversal"`)

* `balanceAdjustment` (value: `"balanceAdjustment"`)

* `balanceMigration` (value: `"balanceMigration"`)

* `balanceRollover` (value: `"balanceRollover"`)

* `bankTransfer` (value: `"bankTransfer"`)

* `capture` (value: `"capture"`)

* `captureReversal` (value: `"captureReversal"`)

* `cardTransfer` (value: `"cardTransfer"`)

* `cashOutFee` (value: `"cashOutFee"`)

* `cashOutFunding` (value: `"cashOutFunding"`)

* `cashOutInstruction` (value: `"cashOutInstruction"`)

* `chargeback` (value: `"chargeback"`)

* `chargebackCorrection` (value: `"chargebackCorrection"`)

* `chargebackReversal` (value: `"chargebackReversal"`)

* `chargebackReversalCorrection` (value: `"chargebackReversalCorrection"`)

* `depositCorrection` (value: `"depositCorrection"`)

* `fee` (value: `"fee"`)

* `grant` (value: `"grant"`)

* `installment` (value: `"installment"`)

* `installmentReversal` (value: `"installmentReversal"`)

* `internalTransfer` (value: `"internalTransfer"`)

* `invoiceDeduction` (value: `"invoiceDeduction"`)

* `leftover` (value: `"leftover"`)

* `manualCorrection` (value: `"manualCorrection"`)

* `miscCost` (value: `"miscCost"`)

* `payment` (value: `"payment"`)

* `paymentCost` (value: `"paymentCost"`)

* `refund` (value: `"refund"`)

* `refundReversal` (value: `"refundReversal"`)

* `repayment` (value: `"repayment"`)

* `reserveAdjustment` (value: `"reserveAdjustment"`)

* `secondChargeback` (value: `"secondChargeback"`)

* `secondChargebackCorrection` (value: `"secondChargebackCorrection"`)




