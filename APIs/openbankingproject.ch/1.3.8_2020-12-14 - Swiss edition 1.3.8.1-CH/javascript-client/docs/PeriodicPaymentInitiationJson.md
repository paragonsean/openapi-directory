# SwissNextGenBankingApiFramework.PeriodicPaymentInitiationJson

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chargeBearer** | [**ChargeBearer**](ChargeBearer.md) |  | [optional] 
**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | 
**creditorAddress** | [**Address**](Address.md) |  | [optional] 
**creditorAgent** | [**CreditorAgent7CH**](CreditorAgent7CH.md) |  | [optional] 
**creditorAgentName** | **String** | Creditor agent name. | [optional] 
**creditorId** | **String** | Identification of Creditors, e.g. a SEPA Creditor ID. | [optional] 
**creditorName** | **String** | Creditor name. | 
**creditorNameAndAddress** | **String** | Creditor Name and Address in a free text field. | [optional] 
**dayOfExecution** | [**DayOfExecution**](DayOfExecution.md) |  | [optional] 
**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | 
**debtorAgent** | [**DebtorAgent7CH**](DebtorAgent7CH.md) |  | [optional] 
**debtorId** | **String** | Debtor Id. | [optional] 
**debtorName** | **String** | Debtor name. | 
**endDate** | **Date** | The last applicable day of execution. If not given, it is an infinite standing order.  | [optional] 
**endToEndIdentification** | **String** |  | 
**equivalentAmount** | [**Amount**](Amount.md) |  | [optional] 
**exchangeRateInformation** | [**ExchangeRateInformation1**](ExchangeRateInformation1.md) |  | [optional] 
**executionRule** | [**ExecutionRule**](ExecutionRule.md) |  | [optional] 
**frequency** | [**FrequencyCode**](FrequencyCode.md) |  | 
**instructedAmount** | [**Amount**](Amount.md) |  | [optional] 
**intermediaryAgent** | **String** | BICFI  | [optional] 
**purposeCode** | [**PurposeCode**](PurposeCode.md) |  | [optional] 
**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 
**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  | [optional] 
**serviceLevel** | [**ExternalServiceLevel1Code**](ExternalServiceLevel1Code.md) |  | [optional] 
**startDate** | **Date** | The first applicable day of execution starting from this date is the first payment.  | 
**transactionCurrency** | **String** | ISO 4217 Alpha 3 currency code.  | [optional] 
**ultimateCreditor** | **String** | Ultimate creditor. | [optional] 
**ultimateDebtor** | **String** | Ultimate debtor. | [optional] 


