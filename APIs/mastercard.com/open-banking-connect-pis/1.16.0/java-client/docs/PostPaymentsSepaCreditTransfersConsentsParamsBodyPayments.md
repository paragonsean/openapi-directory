

# PostPaymentsSepaCreditTransfersConsentsParamsBodyPayments


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryPurpose** | [**CategoryPurposeEnum**](#CategoryPurposeEnum) | Purpose of the payment |  [optional] |
|**creditorAccount** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAccount**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAccount.md) |  |  |
|**creditorAddress** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAddress**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAddress.md) |  |  |
|**creditorAgent** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAgent**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsCreditorAgent.md) |  |  |
|**creditorName** | **String** | Bank name |  |
|**debtorAccount** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAccount**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAccount.md) |  |  [optional] |
|**debtorAddress** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAddress**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAddress.md) |  |  [optional] |
|**debtorAgent** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAgent**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsDebtorAgent.md) |  |  [optional] |
|**debtorName** | **String** | Debtor legal name |  |
|**endToEndIdentification** | **String** | Payment end to end identification |  |
|**instructedAmount** | [**PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsInstructedAmount**](PostPaymentsSepaCreditTransfersConsentsParamsBodyPaymentsInstructedAmount.md) |  |  |
|**instructionPriority** | [**InstructionPriorityEnum**](#InstructionPriorityEnum) | Indicator of the urgency or order of importance |  |
|**localInstrument** | [**LocalInstrumentEnum**](#LocalInstrumentEnum) | User community specific instrument. |  |
|**remittanceInformationReference** | **String** | Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. (future use) |  [optional] |
|**remittanceInformationStructured** | **String** | Description of the payment |  [optional] |
|**remittanceInformationUnstructured** | **String** | Description of the payment |  [optional] |
|**requestedExecutionDate** | **LocalDate** | Scheduled Payment Date |  [optional] |
|**schedule** | [**RequestPisSepaSchedule**](RequestPisSepaSchedule.md) |  |  [optional] |



## Enum: CategoryPurposeEnum

| Name | Value |
|---- | -----|
| CASH | &quot;CASH&quot; |
| CORT | &quot;CORT&quot; |
| DVPM | &quot;DVPM&quot; |
| INTC | &quot;INTC&quot; |
| TREA | &quot;TREA&quot; |



## Enum: InstructionPriorityEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;Normal&quot; |
| URGENT | &quot;Urgent&quot; |



## Enum: LocalInstrumentEnum

| Name | Value |
|---- | -----|
| SEPA | &quot;SEPA&quot; |



