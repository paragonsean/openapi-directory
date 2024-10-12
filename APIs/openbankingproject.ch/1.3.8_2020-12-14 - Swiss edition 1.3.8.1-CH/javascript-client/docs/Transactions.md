# SwissNextGenBankingApiFramework.Transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksTransactionDetails**](LinksTransactionDetails.md) |  | [optional] 
**additionalInformation** | **String** | Might be used by the ASPSP to transport additional transaction related information to the PSU  | [optional] 
**additionalInformationStructured** | [**AdditionalInformationStructured**](AdditionalInformationStructured.md) |  | [optional] 
**balanceAfterTransaction** | [**Balance**](Balance.md) |  | [optional] 
**bankTransactionCode** | **String** | Bank transaction code as used by the ASPSP and using the sub elements of this structured code defined by ISO 20022.  This code type is concatenating the three ISO20022 Codes   * Domain Code,   * Family Code, and   * SubFamiliy Code by hyphens, resulting in &#39;DomainCode&#39;-&#39;FamilyCode&#39;-&#39;SubFamilyCode&#39;.  | [optional] 
**batchIndicator** | **Boolean** | If this indicator equals true, then the related entry is a batch entry.  | [optional] 
**batchNumberOfTransactions** | **Number** | Shall be used if and only if the batchIndicator is contained and equals true.  | [optional] 
**bookingDate** | **Date** | The date when an entry is posted to an account on the ASPSPs books.  | [optional] 
**checkId** | **String** | Identification of a Cheque. | [optional] 
**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | [optional] 
**creditorAgent** | **String** | BICFI  | [optional] 
**creditorId** | **String** | Identification of Creditors, e.g. a SEPA Creditor ID. | [optional] 
**creditorName** | **String** | Creditor name. | [optional] 
**currencyExchange** | [**[ReportExchangeRate]**](ReportExchangeRate.md) | Array of exchange rates. | [optional] 
**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | [optional] 
**debtorAgent** | **String** | BICFI  | [optional] 
**debtorName** | **String** | Debtor name. | [optional] 
**endToEndId** | **String** | Unique end to end identity. | [optional] 
**entryDetails** | [**[EntryDetailsElement]**](EntryDetailsElement.md) | Might be used by the ASPSP to transport details about transactions within a batch.  | [optional] 
**entryReference** | **String** | Is the identification of the transaction as used e.g. for reference for deltafunction on application level. The same identification as for example used within camt.05x messages.  | [optional] 
**mandateId** | **String** | Identification of Mandates, e.g. a SEPA Mandate ID. | [optional] 
**proprietaryBankTransactionCode** | **String** | Proprietary bank transaction code as used within a community or within an ASPSP e.g. for MT94x based transaction reports.  | [optional] 
**purposeCode** | [**PurposeCode**](PurposeCode.md) |  | [optional] 
**remittanceInformationStructured** | **String** | Structured remittance information Max  | [optional] 
**remittanceInformationStructuredArray** | [**[RemittanceInformationStructured]**](RemittanceInformationStructured.md) | Array of structured remittance information.  | [optional] 
**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  | [optional] 
**remittanceInformationUnstructuredArray** | **[String]** | Array of unstructured remittance information.  | [optional] 
**transactionAmount** | [**Amount**](Amount.md) |  | 
**transactionId** | **String** | This identification is given by the attribute transactionId of the corresponding entry of a transaction list.  | [optional] 
**ultimateCreditor** | **String** | Ultimate creditor. | [optional] 
**ultimateDebtor** | **String** | Ultimate debtor. | [optional] 
**valueDate** | **Date** | The Date at which assets become available to the account owner in case of a credit. | [optional] 


