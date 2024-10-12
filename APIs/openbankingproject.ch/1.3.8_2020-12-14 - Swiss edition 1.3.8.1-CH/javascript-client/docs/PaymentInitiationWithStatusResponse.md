# SwissNextGenBankingApiFramework.PaymentInitiationWithStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | 
**creditorAddress** | [**Address**](Address.md) |  | [optional] 
**creditorAgent** | [**CreditorAgent7CH**](CreditorAgent7CH.md) |  | [optional] 
**creditorName** | **String** | Creditor name. | 
**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | 
**endToEndIdentification** | **String** |  | [optional] 
**instructedAmount** | [**Amount**](Amount.md) |  | 
**purposeCode** | [**PurposeCode**](PurposeCode.md) |  | [optional] 
**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 
**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  | [optional] 
**remittanceInformationUnstructuredArray** | **[String]** | Array of unstructured remittance information.  | [optional] 
**requestedExecutionDate** | **Date** |  | [optional] 
**requestedExecutionTime** | **Date** |  | [optional] 
**transactionStatus** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**ultimateCreditor** | **String** | Ultimate creditor. | [optional] 
**ultimateDebtor** | **String** | Ultimate debtor. | [optional] 


