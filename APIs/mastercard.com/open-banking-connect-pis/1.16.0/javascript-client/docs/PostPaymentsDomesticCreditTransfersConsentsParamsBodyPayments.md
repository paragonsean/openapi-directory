# OpenBankingPaymentsInitiationService.PostPaymentsDomesticCreditTransfersConsentsParamsBodyPayments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditorAccount** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAccount**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAccount.md) |  | 
**creditorAddress** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAddress**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAddress.md) |  | [optional] 
**creditorAgent** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAgent**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAgent.md) |  | [optional] 
**creditorName** | **String** | Bank name | 
**debtorAccount** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAccount**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAccount.md) |  | [optional] 
**debtorAgent** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAgent**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAgent.md) |  | [optional] 
**endToEndIdentification** | **String** | Payment end to end identification | 
**instructedAmount** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsInstructedAmount**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsInstructedAmount.md) |  | 
**instructionIdentification** | **String** | Unique identification as assigned by an instructing party for an instructed party to unambiguously identify the instruction. If API profile of ASPSP is CMA9, then field is mandatory. | [optional] 
**instructionPriority** | **String** | Indicator of the urgency or order of importance | [optional] 
**localInstrument** | **String** | User community specific instrument. | 
**remittanceInformationReference** | **String** | Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. (future use) | [optional] 
**remittanceInformationUnstructured** | **String** | Description of the payment | [optional] 
**requestedExecutionDate** | **Date** | Scheduled Payment Date | [optional] 
**schedule** | [**RequestPisDomesticSchedule**](RequestPisDomesticSchedule.md) |  | [optional] 



## Enum: InstructionPriorityEnum


* `Normal` (value: `"Normal"`)

* `Urgent` (value: `"Urgent"`)





## Enum: LocalInstrumentEnum


* `UK.FasterPayments` (value: `"UK.FasterPayments"`)

* `PL.Elixir` (value: `"PL.Elixir"`)




