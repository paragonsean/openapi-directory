

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The amount of the transaction. |  [optional] |
|**bankAccountDetail** | [**BankAccountDetail**](BankAccountDetail.md) | The details of the bank account to where a payout was made. |  [optional] |
|**captureMerchantReference** | **String** | The merchant reference of a related capture. |  [optional] |
|**capturePspReference** | **String** | The psp reference of a related capture. |  [optional] |
|**creationDate** | **OffsetDateTime** | The date on which the transaction was performed. |  [optional] |
|**description** | **String** | A description of the transaction. |  [optional] |
|**destinationAccountCode** | **String** | The code of the account to which funds were credited during an outgoing fund transfer. |  [optional] |
|**disputePspReference** | **String** | The psp reference of the related dispute. |  [optional] |
|**disputeReasonCode** | **String** | The reason code of a dispute. |  [optional] |
|**merchantReference** | **String** | The merchant reference of a transaction. |  [optional] |
|**paymentPspReference** | **String** | The psp reference of the related authorisation or transfer. |  [optional] |
|**payoutPspReference** | **String** | The psp reference of the related payout. |  [optional] |
|**pspReference** | **String** | The psp reference of a transaction. |  [optional] |
|**sourceAccountCode** | **String** | The code of the account from which funds were debited during an incoming fund transfer. |  [optional] |
|**transactionStatus** | [**TransactionStatusEnum**](#TransactionStatusEnum) | The status of the transaction. &gt;Permitted values: &#x60;PendingCredit&#x60;, &#x60;CreditFailed&#x60;, &#x60;CreditClosed&#x60;, &#x60;CreditSuspended&#x60;, &#x60;Credited&#x60;, &#x60;Converted&#x60;, &#x60;PendingDebit&#x60;, &#x60;DebitFailed&#x60;, &#x60;Debited&#x60;, &#x60;DebitReversedReceived&#x60;, &#x60;DebitedReversed&#x60;, &#x60;ChargebackReceived&#x60;, &#x60;Chargeback&#x60;, &#x60;ChargebackReversedReceived&#x60;, &#x60;ChargebackReversed&#x60;, &#x60;Payout&#x60;, &#x60;PayoutReversed&#x60;, &#x60;FundTransfer&#x60;, &#x60;PendingFundTransfer&#x60;, &#x60;ManualCorrected&#x60;. |  [optional] |
|**transferCode** | **String** | The transfer code of the transaction. |  [optional] |



## Enum: TransactionStatusEnum

| Name | Value |
|---- | -----|
| BALANCE_NOT_PAID_OUT_TRANSFER | &quot;BalanceNotPaidOutTransfer&quot; |
| BALANCE_PLATFORM_SWEEP | &quot;BalancePlatformSweep&quot; |
| BALANCE_PLATFORM_SWEEP_RETURNED | &quot;BalancePlatformSweepReturned&quot; |
| CHARGEBACK | &quot;Chargeback&quot; |
| CHARGEBACK_CORRECTION | &quot;ChargebackCorrection&quot; |
| CHARGEBACK_CORRECTION_RECEIVED | &quot;ChargebackCorrectionReceived&quot; |
| CHARGEBACK_RECEIVED | &quot;ChargebackReceived&quot; |
| CHARGEBACK_REVERSED | &quot;ChargebackReversed&quot; |
| CHARGEBACK_REVERSED_CORRECTION | &quot;ChargebackReversedCorrection&quot; |
| CHARGEBACK_REVERSED_CORRECTION_RECEIVED | &quot;ChargebackReversedCorrectionReceived&quot; |
| CHARGEBACK_REVERSED_RECEIVED | &quot;ChargebackReversedReceived&quot; |
| CONVERTED | &quot;Converted&quot; |
| CREDIT_CLOSED | &quot;CreditClosed&quot; |
| CREDIT_FAILED | &quot;CreditFailed&quot; |
| CREDIT_REVERSED | &quot;CreditReversed&quot; |
| CREDIT_REVERSED_RECEIVED | &quot;CreditReversedReceived&quot; |
| CREDIT_SUSPENDED | &quot;CreditSuspended&quot; |
| CREDITED | &quot;Credited&quot; |
| DEBIT_FAILED | &quot;DebitFailed&quot; |
| DEBIT_REVERSED_RECEIVED | &quot;DebitReversedReceived&quot; |
| DEBITED | &quot;Debited&quot; |
| DEBITED_REVERSED | &quot;DebitedReversed&quot; |
| DEPOSIT_CORRECTION_CREDITED | &quot;DepositCorrectionCredited&quot; |
| DEPOSIT_CORRECTION_DEBITED | &quot;DepositCorrectionDebited&quot; |
| FEE | &quot;Fee&quot; |
| FUND_TRANSFER | &quot;FundTransfer&quot; |
| FUND_TRANSFER_REVERSED | &quot;FundTransferReversed&quot; |
| INVOICE_DEDUCTION_CREDITED | &quot;InvoiceDeductionCredited&quot; |
| INVOICE_DEDUCTION_DEBITED | &quot;InvoiceDeductionDebited&quot; |
| MANUAL_CORRECTED | &quot;ManualCorrected&quot; |
| MANUAL_CORRECTION_CREDITED | &quot;ManualCorrectionCredited&quot; |
| MANUAL_CORRECTION_DEBITED | &quot;ManualCorrectionDebited&quot; |
| MERCHANT_PAYIN | &quot;MerchantPayin&quot; |
| MERCHANT_PAYIN_REVERSED | &quot;MerchantPayinReversed&quot; |
| PAYOUT | &quot;Payout&quot; |
| PAYOUT_REVERSED | &quot;PayoutReversed&quot; |
| PENDING_CREDIT | &quot;PendingCredit&quot; |
| PENDING_DEBIT | &quot;PendingDebit&quot; |
| PENDING_FUND_TRANSFER | &quot;PendingFundTransfer&quot; |
| RE_CREDITED | &quot;ReCredited&quot; |
| RE_CREDITED_RECEIVED | &quot;ReCreditedReceived&quot; |
| SECOND_CHARGEBACK | &quot;SecondChargeback&quot; |
| SECOND_CHARGEBACK_CORRECTION | &quot;SecondChargebackCorrection&quot; |
| SECOND_CHARGEBACK_CORRECTION_RECEIVED | &quot;SecondChargebackCorrectionReceived&quot; |
| SECOND_CHARGEBACK_RECEIVED | &quot;SecondChargebackReceived&quot; |



