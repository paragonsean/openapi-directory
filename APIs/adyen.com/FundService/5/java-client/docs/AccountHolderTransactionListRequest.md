

# AccountHolderTransactionListRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder that owns the account(s) of which retrieve the transaction list. |  |
|**transactionListsPerAccount** | [**List&lt;TransactionListForAccount&gt;**](TransactionListForAccount.md) | A list of accounts to include in the transaction list. If left blank, the last fifty (50) transactions for all accounts of the account holder will be included. |  [optional] |
|**transactionStatuses** | [**List&lt;TransactionStatusesEnum&gt;**](#List&lt;TransactionStatusesEnum&gt;) | A list of statuses to include in the transaction list. If left blank, all transactions will be included. &gt;Permitted values: &gt;* &#x60;PendingCredit&#x60; - a pending balance credit. &gt;* &#x60;CreditFailed&#x60; - a pending credit failure; the balance will not be credited. &gt;* &#x60;Credited&#x60; - a credited balance. &gt;* &#x60;PendingDebit&#x60; - a pending balance debit (e.g., a refund). &gt;* &#x60;CreditClosed&#x60; - a pending credit closed; the balance will not be credited. &gt;* &#x60;CreditSuspended&#x60; - a pending credit closed; the balance will not be credited. &gt;* &#x60;DebitFailed&#x60; - a pending debit failure; the balance will not be debited. &gt;* &#x60;Debited&#x60; - a debited balance (e.g., a refund). &gt;* &#x60;DebitReversedReceived&#x60; - a pending refund reversal. &gt;* &#x60;DebitedReversed&#x60; - a reversed refund. &gt;* &#x60;ChargebackReceived&#x60; - a received chargeback request. &gt;* &#x60;Chargeback&#x60; - a processed chargeback. &gt;* &#x60;ChargebackReversedReceived&#x60; - a pending chargeback reversal. &gt;* &#x60;ChargebackReversed&#x60; - a reversed chargeback. &gt;* &#x60;Converted&#x60; - converted. &gt;* &#x60;ManualCorrected&#x60; - manual booking/adjustment by Adyen. &gt;* &#x60;Payout&#x60; - a payout. &gt;* &#x60;PayoutReversed&#x60; - a reversed payout. &gt;* &#x60;PendingFundTransfer&#x60; - a pending transfer of funds from one account to another. &gt;* &#x60;FundTransfer&#x60; - a transfer of funds from one account to another. |  [optional] |



## Enum: List&lt;TransactionStatusesEnum&gt;

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



