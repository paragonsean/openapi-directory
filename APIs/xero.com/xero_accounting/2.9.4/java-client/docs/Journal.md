

# Journal


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDateUTC** | **String** | Created date UTC format |  [optional] [readonly] |
|**journalDate** | **String** | Date the journal was posted |  [optional] |
|**journalID** | **UUID** | Xero identifier |  [optional] |
|**journalLines** | [**List&lt;JournalLine&gt;**](JournalLine.md) | See JournalLines |  [optional] |
|**journalNumber** | **Integer** | Xero generated journal number |  [optional] |
|**reference** | **String** | reference field for additional indetifying information |  [optional] |
|**sourceID** | **UUID** | The identifier for the source transaction (e.g. InvoiceID) |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The journal source type. The type of transaction that created the journal |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| ACCREC | &quot;ACCREC&quot; |
| ACCPAY | &quot;ACCPAY&quot; |
| ACCRECCREDIT | &quot;ACCRECCREDIT&quot; |
| ACCPAYCREDIT | &quot;ACCPAYCREDIT&quot; |
| ACCRECPAYMENT | &quot;ACCRECPAYMENT&quot; |
| ACCPAYPAYMENT | &quot;ACCPAYPAYMENT&quot; |
| ARCREDITPAYMENT | &quot;ARCREDITPAYMENT&quot; |
| APCREDITPAYMENT | &quot;APCREDITPAYMENT&quot; |
| CASHREC | &quot;CASHREC&quot; |
| CASHPAID | &quot;CASHPAID&quot; |
| TRANSFER | &quot;TRANSFER&quot; |
| ARPREPAYMENT | &quot;ARPREPAYMENT&quot; |
| APPREPAYMENT | &quot;APPREPAYMENT&quot; |
| AROVERPAYMENT | &quot;AROVERPAYMENT&quot; |
| APOVERPAYMENT | &quot;APOVERPAYMENT&quot; |
| EXPCLAIM | &quot;EXPCLAIM&quot; |
| EXPPAYMENT | &quot;EXPPAYMENT&quot; |
| MANJOURNAL | &quot;MANJOURNAL&quot; |
| PAYSLIP | &quot;PAYSLIP&quot; |
| WAGEPAYABLE | &quot;WAGEPAYABLE&quot; |
| INTEGRATEDPAYROLLPE | &quot;INTEGRATEDPAYROLLPE&quot; |
| INTEGRATEDPAYROLLPT | &quot;INTEGRATEDPAYROLLPT&quot; |
| EXTERNALSPENDMONEY | &quot;EXTERNALSPENDMONEY&quot; |
| INTEGRATEDPAYROLLPTPAYMENT | &quot;INTEGRATEDPAYROLLPTPAYMENT&quot; |
| INTEGRATEDPAYROLLCN | &quot;INTEGRATEDPAYROLLCN&quot; |



