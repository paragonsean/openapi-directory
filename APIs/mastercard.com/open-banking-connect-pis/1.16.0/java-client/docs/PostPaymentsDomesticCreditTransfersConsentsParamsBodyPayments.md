

# PostPaymentsDomesticCreditTransfersConsentsParamsBodyPayments


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creditorAccount** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAccount**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAccount.md) |  |  |
|**creditorAddress** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAddress**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAddress.md) |  |  [optional] |
|**creditorAgent** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAgent**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsCreditorAgent.md) |  |  [optional] |
|**creditorName** | **String** | Bank name |  |
|**debtorAccount** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAccount**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAccount.md) |  |  [optional] |
|**debtorAgent** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAgent**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsDebtorAgent.md) |  |  [optional] |
|**endToEndIdentification** | **String** | Payment end to end identification |  |
|**instructedAmount** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsInstructedAmount**](PostPaymentsDomesticCreditTransfersConsentsParamsBodyPaymentsInstructedAmount.md) |  |  |
|**instructionIdentification** | **String** | Unique identification as assigned by an instructing party for an instructed party to unambiguously identify the instruction. If API profile of ASPSP is CMA9, then field is mandatory. |  [optional] |
|**instructionPriority** | [**InstructionPriorityEnum**](#InstructionPriorityEnum) | Indicator of the urgency or order of importance |  [optional] |
|**localInstrument** | [**LocalInstrumentEnum**](#LocalInstrumentEnum) | User community specific instrument. |  |
|**remittanceInformationReference** | **String** | Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. (future use) |  [optional] |
|**remittanceInformationUnstructured** | **String** | Description of the payment |  [optional] |
|**requestedExecutionDate** | **LocalDate** | Scheduled Payment Date |  [optional] |
|**schedule** | [**RequestPisDomesticSchedule**](RequestPisDomesticSchedule.md) |  |  [optional] |



## Enum: InstructionPriorityEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;Normal&quot; |
| URGENT | &quot;Urgent&quot; |



## Enum: LocalInstrumentEnum

| Name | Value |
|---- | -----|
| UK_FASTER_PAYMENTS | &quot;UK.FasterPayments&quot; |
| PL_ELIXIR | &quot;PL.Elixir&quot; |



