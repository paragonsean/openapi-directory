# ClassicPlatformsNotifications.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The amount of the transaction. | [optional] 
**bankAccountDetail** | [**BankAccountDetail**](BankAccountDetail.md) | The details of the bank account to where a payout was made. | [optional] 
**captureMerchantReference** | **String** | The merchant reference of a related capture. | [optional] 
**capturePspReference** | **String** | The psp reference of a related capture. | [optional] 
**creationDate** | **Date** | The date on which the transaction was performed. | [optional] 
**description** | **String** | A description of the transaction. | [optional] 
**destinationAccountCode** | **String** | The code of the account to which funds were credited during an outgoing fund transfer. | [optional] 
**disputePspReference** | **String** | The psp reference of the related dispute. | [optional] 
**disputeReasonCode** | **String** | The reason code of a dispute. | [optional] 
**merchantReference** | **String** | The merchant reference of a transaction. | [optional] 
**paymentPspReference** | **String** | The psp reference of the related authorisation or transfer. | [optional] 
**payoutPspReference** | **String** | The psp reference of the related payout. | [optional] 
**pspReference** | **String** | The psp reference of a transaction. | [optional] 
**sourceAccountCode** | **String** | The code of the account from which funds were debited during an incoming fund transfer. | [optional] 
**transactionStatus** | **String** | The status of the transaction. &gt;Permitted values: &#x60;PendingCredit&#x60;, &#x60;CreditFailed&#x60;, &#x60;CreditClosed&#x60;, &#x60;CreditSuspended&#x60;, &#x60;Credited&#x60;, &#x60;Converted&#x60;, &#x60;PendingDebit&#x60;, &#x60;DebitFailed&#x60;, &#x60;Debited&#x60;, &#x60;DebitReversedReceived&#x60;, &#x60;DebitedReversed&#x60;, &#x60;ChargebackReceived&#x60;, &#x60;Chargeback&#x60;, &#x60;ChargebackReversedReceived&#x60;, &#x60;ChargebackReversed&#x60;, &#x60;Payout&#x60;, &#x60;PayoutReversed&#x60;, &#x60;FundTransfer&#x60;, &#x60;PendingFundTransfer&#x60;, &#x60;ManualCorrected&#x60;. | [optional] 
**transferCode** | **String** | The transfer code of the transaction. | [optional] 



## Enum: TransactionStatusEnum


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




