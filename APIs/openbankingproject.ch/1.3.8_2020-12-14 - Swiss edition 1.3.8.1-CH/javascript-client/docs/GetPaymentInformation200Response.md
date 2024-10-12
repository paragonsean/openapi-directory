# SwissNextGenBankingApiFramework.GetPaymentInformation200Response

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
**dayOfExecution** | [**DayOfExecution**](DayOfExecution.md) |  | [optional] 
**endDate** | **Date** | The last applicable day of execution. If not given, it is an infinite standing order.  | [optional] 
**executionRule** | [**ExecutionRule**](ExecutionRule.md) |  | [optional] 
**frequency** | [**FrequencyCode**](FrequencyCode.md) |  | 
**startDate** | **Date** | The first applicable day of execution starting from this date is the first payment.  | 
**acceptorTransactionDateTime** | **Date** |  | [optional] 
**batchBookingPreferred** | **Boolean** | If this element equals &#39;true&#39;, the PSU prefers only one booking entry. If this element equals &#39;false&#39;, the PSU prefers individual booking of all contained individual transactions.  The ASPSP will follow this preference according to contracts agreed on with the PSU.  | [optional] 
**paymentInformationId** | **String** |  | [optional] 
**payments** | [**[PaymentInitiationBulkElementJson]**](PaymentInitiationBulkElementJson.md) | A list of generic JSON bodies payment initations for bulk payments via JSON.  Note: Some fields from single payments do not occcur in a bulk payment element  | 


