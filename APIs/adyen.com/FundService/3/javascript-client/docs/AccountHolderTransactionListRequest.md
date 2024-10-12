# FundApi.AccountHolderTransactionListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the account holder that owns the account(s) of which retrieve the transaction list. | 
**transactionListsPerAccount** | [**[TransactionListForAccountWrapper]**](TransactionListForAccountWrapper.md) | A list of accounts to include in the transaction list. If left blank, the last fifty (50) transactions for all accounts of the account holder will be included. | [optional] 
**transactionStatuses** | **[String]** | A list of statuses to include in the transaction list. If left blank, all transactions will be included. &gt;Permitted values: &gt;* &#x60;PendingCredit&#x60; - a pending balance credit. &gt;* &#x60;CreditFailed&#x60; - a pending credit failure; the balance will not be credited. &gt;* &#x60;Credited&#x60; - a credited balance. &gt;* &#x60;PendingDebit&#x60; - a pending balance debit (e.g., a refund). &gt;* &#x60;CreditClosed&#x60; - a pending credit closed; the balance will not be credited. &gt;* &#x60;CreditSuspended&#x60; - a pending credit closed; the balance will not be credited. &gt;* &#x60;DebitFailed&#x60; - a pending debit failure; the balance will not be debited. &gt;* &#x60;Debited&#x60; - a debited balance (e.g., a refund). &gt;* &#x60;DebitReversedReceived&#x60; - a pending refund reversal. &gt;* &#x60;DebitedReversed&#x60; - a reversed refund. &gt;* &#x60;ChargebackReceived&#x60; - a received chargeback request. &gt;* &#x60;Chargeback&#x60; - a processed chargeback. &gt;* &#x60;ChargebackReversedReceived&#x60; - a pending chargeback reversal. &gt;* &#x60;ChargebackReversed&#x60; - a reversed chargeback. &gt;* &#x60;Converted&#x60; - converted. &gt;* &#x60;ManualCorrected&#x60; - manual booking/adjustment by Adyen. &gt;* &#x60;Payout&#x60; - a payout. &gt;* &#x60;PayoutReversed&#x60; - a reversed payout. &gt;* &#x60;PendingFundTransfer&#x60; - a pending transfer of funds from one account to another. &gt;* &#x60;FundTransfer&#x60; - a transfer of funds from one account to another. | [optional] 



## Enum: [TransactionStatusesEnum]


* `BalanceNotPaidOutTransfer` (value: `"BalanceNotPaidOutTransfer"`)

* `BalancePlatformSweep` (value: `"BalancePlatformSweep"`)

* `BalancePlatformSweepReturned` (value: `"BalancePlatformSweepReturned"`)

* `Chargeback` (value: `"Chargeback"`)

* `ChargebackCorrection` (value: `"ChargebackCorrection"`)

* `ChargebackCorrectionReceived` (value: `"ChargebackCorrectionReceived"`)

* `ChargebackReceived` (value: `"ChargebackReceived"`)

* `ChargebackReversed` (value: `"ChargebackReversed"`)

* `ChargebackReversedCorrection` (value: `"ChargebackReversedCorrection"`)

* `ChargebackReversedCorrectionReceived` (value: `"ChargebackReversedCorrectionReceived"`)

* `ChargebackReversedReceived` (value: `"ChargebackReversedReceived"`)

* `Converted` (value: `"Converted"`)

* `CreditClosed` (value: `"CreditClosed"`)

* `CreditFailed` (value: `"CreditFailed"`)

* `CreditReversed` (value: `"CreditReversed"`)

* `CreditReversedReceived` (value: `"CreditReversedReceived"`)

* `CreditSuspended` (value: `"CreditSuspended"`)

* `Credited` (value: `"Credited"`)

* `DebitFailed` (value: `"DebitFailed"`)

* `DebitReversedReceived` (value: `"DebitReversedReceived"`)

* `Debited` (value: `"Debited"`)

* `DebitedReversed` (value: `"DebitedReversed"`)

* `DepositCorrectionCredited` (value: `"DepositCorrectionCredited"`)

* `DepositCorrectionDebited` (value: `"DepositCorrectionDebited"`)

* `Fee` (value: `"Fee"`)

* `FundTransfer` (value: `"FundTransfer"`)

* `FundTransferReversed` (value: `"FundTransferReversed"`)

* `InvoiceDeductionCredited` (value: `"InvoiceDeductionCredited"`)

* `InvoiceDeductionDebited` (value: `"InvoiceDeductionDebited"`)

* `ManualCorrected` (value: `"ManualCorrected"`)

* `ManualCorrectionCredited` (value: `"ManualCorrectionCredited"`)

* `ManualCorrectionDebited` (value: `"ManualCorrectionDebited"`)

* `MerchantPayin` (value: `"MerchantPayin"`)

* `MerchantPayinReversed` (value: `"MerchantPayinReversed"`)

* `Payout` (value: `"Payout"`)

* `PayoutReversed` (value: `"PayoutReversed"`)

* `PendingCredit` (value: `"PendingCredit"`)

* `PendingDebit` (value: `"PendingDebit"`)

* `PendingFundTransfer` (value: `"PendingFundTransfer"`)

* `ReCredited` (value: `"ReCredited"`)

* `ReCreditedReceived` (value: `"ReCreditedReceived"`)

* `SecondChargeback` (value: `"SecondChargeback"`)

* `SecondChargebackCorrection` (value: `"SecondChargebackCorrection"`)

* `SecondChargebackCorrectionReceived` (value: `"SecondChargebackCorrectionReceived"`)

* `SecondChargebackReceived` (value: `"SecondChargebackReceived"`)




