# SwissNextGenBankingApiFramework.PaymentInitiationJson

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
**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | 
**debtorAgent** | [**DebtorAgent7CH**](DebtorAgent7CH.md) |  | [optional] 
**debtorId** | **String** | Debtor Id. | [optional] 
**debtorName** | **String** | Debtor name. | 
**endToEndIdentification** | **String** |  | 
**equivalentAmount** | [**Amount**](Amount.md) |  | [optional] 
**exchangeRateInformation** | [**ExchangeRateInformation1**](ExchangeRateInformation1.md) |  | [optional] 
**instructedAmount** | [**Amount**](Amount.md) |  | [optional] 
**intermediaryAgent** | **String** | BICFI  | [optional] 
**purposeCode** | [**PurposeCode**](PurposeCode.md) |  | [optional] 
**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 
**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  | [optional] 
**requestedExecutionDate** | **Date** |  | 
**serviceLevel** | [**ExternalServiceLevel1Code**](ExternalServiceLevel1Code.md) |  | [optional] 
**transactionCurrency** | **String** | ISO 4217 Alpha 3 currency code.  | [optional] 
**ultimateCreditor** | **String** | Ultimate creditor. | [optional] 
**ultimateDebtor** | **String** | Ultimate debtor. | [optional] 


