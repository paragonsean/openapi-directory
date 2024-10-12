# OpenBankingPaymentsInitiationService.PostPaymentsSepaCreditTransfersConsentsParamsBodyPayments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryPurpose** | **String** | Purpose of the payment | [optional] 
**creditorAccount** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAccount**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAccount.md) |  | 
**creditorAddress** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAddress**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAddress.md) |  | 
**creditorAgent** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAgent**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAgent.md) |  | 
**creditorName** | **String** | Bank name | 
**debtorAccount** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAccount**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAccount.md) |  | [optional] 
**debtorAddress** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAddress**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAddress.md) |  | [optional] 
**debtorAgent** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAgent**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAgent.md) |  | [optional] 
**debtorName** | **String** | Debtor legal name | 
**endToEndIdentification** | **String** | Payment end to end identification | 
**instructedAmount** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsInstructedAmount**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsInstructedAmount.md) |  | 
**instructionPriority** | **String** | Indicator of the urgency or order of importance | 
**localInstrument** | **String** | User community specific instrument. | 
**remittanceInformationReference** | **String** | Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. (future use) | [optional] 
**remittanceInformationStructured** | **String** | Description of the payment | [optional] 
**remittanceInformationUnstructured** | **String** | Description of the payment | [optional] 
**requestedExecutionDate** | **Date** | Scheduled Payment Date | [optional] 
**schedule** | [**RequestPisSepaSchedule**](RequestPisSepaSchedule.md) |  | [optional] 



## Enum: CategoryPurposeEnum


* `CASH` (value: `"CASH"`)

* `CORT` (value: `"CORT"`)

* `DVPM` (value: `"DVPM"`)

* `INTC` (value: `"INTC"`)

* `TREA` (value: `"TREA"`)





## Enum: InstructionPriorityEnum


* `Normal` (value: `"Normal"`)

* `Urgent` (value: `"Urgent"`)





## Enum: LocalInstrumentEnum


* `SEPA` (value: `"SEPA"`)




