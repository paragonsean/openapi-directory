# OpenBankingPaymentsInitiationService.PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPayments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditorAccount** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsCreditorAccount**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsCreditorAccount.md) |  | 
**creditorAddress** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsCreditorAddress**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsCreditorAddress.md) |  | [optional] 
**creditorAgent** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsCreditorAgent**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsCreditorAgent.md) |  | 
**creditorName** | **String** | Bank name | 
**debtorAccount** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsDebtorAccount**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsDebtorAccount.md) |  | 
**debtorAddress** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsDebtorAddress**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsDebtorAddress.md) |  | [optional] 
**debtorName** | **String** | Debtor legal name | [optional] 
**endToEndIdentification** | **String** | Payment end to end identification | 
**instructedAmount** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsInstructedAmount**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyPaymentsInstructedAmount.md) |  | 
**instructionIdentification** | **String** | Unique identification as assigned by an instructing party for an instructed party to unambiguously identify the instruction. If API profile of ASPSP is CMA9, then field is mandatory. | [optional] 
**instructionPriority** | **String** | Indicator of the urgency or order of importance | 
**localInstrument** | **String** | User community specific instrument. | 
**remittanceInformationReference** | **String** | Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. (future use) | [optional] 
**remittanceInformationUnstructured** | **String** | Description of the payment | [optional] 
**requestedExecutionDate** | **Date** | Scheduled Payment Date | [optional] 
**transferCharges** | **String** | Charge bearer | [optional] 



## Enum: InstructionPriorityEnum


* `Normal` (value: `"Normal"`)

* `Urgent` (value: `"Urgent"`)





## Enum: LocalInstrumentEnum


* `Swift` (value: `"Swift"`)





## Enum: TransferChargesEnum


* `SEN` (value: `"SEN"`)

* `SHA` (value: `"SHA"`)

* `BEN` (value: `"BEN"`)




