

# EntryDetailsElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkId** | **String** | Identification of a Cheque. |  [optional] |
|**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  [optional] |
|**creditorAgent** | **String** | BICFI  |  [optional] |
|**creditorId** | **String** | Identification of Creditors, e.g. a SEPA Creditor ID. |  [optional] |
|**creditorName** | **String** | Creditor name. |  [optional] |
|**currencyExchange** | [**List&lt;ReportExchangeRate&gt;**](ReportExchangeRate.md) | Array of exchange rates. |  [optional] |
|**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  [optional] |
|**debtorAgent** | **String** | BICFI  |  [optional] |
|**debtorName** | **String** | Debtor name. |  [optional] |
|**endToEndId** | **String** | Unique end to end identity. |  [optional] |
|**mandateId** | **String** | Identification of Mandates, e.g. a SEPA Mandate ID. |  [optional] |
|**purposeCode** | **PurposeCode** |  |  [optional] |
|**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  |  [optional] |
|**remittanceInformationStructuredArray** | [**List&lt;RemittanceInformationStructured&gt;**](RemittanceInformationStructured.md) | Array of structured remittance information.  |  [optional] |
|**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  |  [optional] |
|**remittanceInformationUnstructuredArray** | **List&lt;String&gt;** | Array of unstructured remittance information.  |  [optional] |
|**transactionAmount** | [**Amount**](Amount.md) |  |  |
|**ultimateCreditor** | **String** | Ultimate creditor. |  [optional] |
|**ultimateDebtor** | **String** | Ultimate debtor. |  [optional] |



