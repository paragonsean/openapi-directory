# SwissNextGenBankingApiFramework.PeriodicPaymentInitiationWithStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | 
**creditorAddress** | [**Address**](Address.md) |  | [optional] 
**creditorAgent** | [**CreditorAgent7CH**](CreditorAgent7CH.md) |  | [optional] 
**creditorName** | **String** | Creditor name. | 
**dayOfExecution** | [**DayOfExecution**](DayOfExecution.md) |  | [optional] 
**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | 
**endDate** | **Date** | The last applicable day of execution. If not given, it is an infinite standing order.  | [optional] 
**endToEndIdentification** | **String** |  | [optional] 
**executionRule** | [**ExecutionRule**](ExecutionRule.md) |  | [optional] 
**frequency** | [**FrequencyCode**](FrequencyCode.md) |  | 
**instructedAmount** | [**Amount**](Amount.md) |  | 
**purposeCode** | [**PurposeCode**](PurposeCode.md) |  | [optional] 
**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 
**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  | [optional] 
**remittanceInformationUnstructuredArray** | **[String]** | Array of unstructured remittance information.  | [optional] 
**requestedExecutionDate** | **Date** |  | [optional] 
**requestedExecutionTime** | **Date** |  | [optional] 
**startDate** | **Date** | The first applicable day of execution starting from this date is the first payment.  | 
**transactionStatus** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**ultimateCreditor** | **String** | Ultimate creditor. | [optional] 
**ultimateDebtor** | **String** | Ultimate debtor. | [optional] 


