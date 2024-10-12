

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderId** | **String** | Unique identifier of the account holder. |  |
|**amount** | [**Amount**](Amount.md) | Contains information about the amount of the transaction. |  |
|**balanceAccountId** | **String** | Unique identifier of the balance account. |  |
|**balancePlatform** | **String** | The unique identifier of the balance platform. |  |
|**bookingDate** | **OffsetDateTime** | The date the transaction was booked into the balance account. |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the transaction indicating the type of activity.   Possible values:  * **platformPayment**: The transaction is a payment or payment modification made with an Adyen merchant account.  * **internal**: The transaction resulted from an internal adjustment such as a deposit correction or invoice deduction.  * **bank**: The transaction is a bank-related activity, such as sending a payout or receiving funds.  * **issuedCard**: The transaction is a card-related activity, such as using an Adyen-issued card to pay online.   |  [optional] |
|**counterparty** | [**CounterpartyV3**](CounterpartyV3.md) | Contains information about the other party in the transaction. |  |
|**createdAt** | **OffsetDateTime** | The date the transaction was created. |  |
|**creationDate** | **OffsetDateTime** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |  [optional] |
|**description** | **String** | The &#x60;description&#x60; from the &#x60;/transfers&#x60; request. |  [optional] |
|**eventId** | **String** | The PSP reference of the transaction in the journal. |  [optional] |
|**id** | **String** | The unique identifier of the transaction. |  |
|**instructedAmount** | [**Amount**](Amount.md) | The amount that the sender instructed their bank to send. This can be higher than &#x60;amount.value&#x60; when their bank deducts costs for the transfer. |  [optional] |
|**paymentInstrumentId** | **String** | The unique identifier of the payment instrument that was used for the transaction. |  [optional] |
|**reference** | **String** | The [&#x60;reference&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the &#x60;/transfers&#x60; request. If you haven&#39;t provided any, Adyen generates a unique reference. |  |
|**referenceForBeneficiary** | **String** | The reference sent to or received from the counterparty.  * For outgoing funds, this is the [&#x60;referenceForBeneficiary&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary) from the  [&#x60;/transfers&#x60;](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_referenceForBeneficiary) request.   * For incoming funds, this is the reference from the sender. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the transaction.   Possible values:  * **pending**: The transaction is still pending.  * **booked**: The transaction has been booked to the balance account.   |  |
|**transferId** | **String** | Unique identifier of the related transfer. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the transaction.   Possible values: **payment**, **capture**, **captureReversal**, **refund** **refundReversal**, **chargeback**, **chargebackReversal**, **secondChargeback**, **atmWithdrawal**, **atmWithdrawalReversal**, **internalTransfer**, **manualCorrection**, **invoiceDeduction**, **depositCorrection**, **bankTransfer**, **miscCost**, **paymentCost**, **fee** |  [optional] |
|**valueDate** | **OffsetDateTime** | The date the transfer amount becomes available in the balance account. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| CARD | &quot;card&quot; |
| GRANTS | &quot;grants&quot; |
| INTERNAL | &quot;internal&quot; |
| ISSUED_CARD | &quot;issuedCard&quot; |
| MIGRATION | &quot;migration&quot; |
| PLATFORM_PAYMENT | &quot;platformPayment&quot; |
| TOP_UP | &quot;topUp&quot; |
| UPGRADE | &quot;upgrade&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| BOOKED | &quot;booked&quot; |
| PENDING | &quot;pending&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ATM_WITHDRAWAL | &quot;atmWithdrawal&quot; |
| ATM_WITHDRAWAL_REVERSAL | &quot;atmWithdrawalReversal&quot; |
| BALANCE_ADJUSTMENT | &quot;balanceAdjustment&quot; |
| BALANCE_MIGRATION | &quot;balanceMigration&quot; |
| BALANCE_ROLLOVER | &quot;balanceRollover&quot; |
| BANK_TRANSFER | &quot;bankTransfer&quot; |
| CAPTURE | &quot;capture&quot; |
| CAPTURE_REVERSAL | &quot;captureReversal&quot; |
| CARD_TRANSFER | &quot;cardTransfer&quot; |
| CASH_OUT_FEE | &quot;cashOutFee&quot; |
| CASH_OUT_FUNDING | &quot;cashOutFunding&quot; |
| CASH_OUT_INSTRUCTION | &quot;cashOutInstruction&quot; |
| CHARGEBACK | &quot;chargeback&quot; |
| CHARGEBACK_CORRECTION | &quot;chargebackCorrection&quot; |
| CHARGEBACK_REVERSAL | &quot;chargebackReversal&quot; |
| CHARGEBACK_REVERSAL_CORRECTION | &quot;chargebackReversalCorrection&quot; |
| DEPOSIT_CORRECTION | &quot;depositCorrection&quot; |
| FEE | &quot;fee&quot; |
| GRANT | &quot;grant&quot; |
| INSTALLMENT | &quot;installment&quot; |
| INSTALLMENT_REVERSAL | &quot;installmentReversal&quot; |
| INTERNAL_TRANSFER | &quot;internalTransfer&quot; |
| INVOICE_DEDUCTION | &quot;invoiceDeduction&quot; |
| LEFTOVER | &quot;leftover&quot; |
| MANUAL_CORRECTION | &quot;manualCorrection&quot; |
| MISC_COST | &quot;miscCost&quot; |
| PAYMENT | &quot;payment&quot; |
| PAYMENT_COST | &quot;paymentCost&quot; |
| REFUND | &quot;refund&quot; |
| REFUND_REVERSAL | &quot;refundReversal&quot; |
| REPAYMENT | &quot;repayment&quot; |
| RESERVE_ADJUSTMENT | &quot;reserveAdjustment&quot; |
| SECOND_CHARGEBACK | &quot;secondChargeback&quot; |
| SECOND_CHARGEBACK_CORRECTION | &quot;secondChargebackCorrection&quot; |



