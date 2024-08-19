# XeroAccountingApi.Journal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDateUTC** | **String** | Created date UTC format | [optional] [readonly] 
**journalDate** | **String** | Date the journal was posted | [optional] 
**journalID** | **String** | Xero identifier | [optional] 
**journalLines** | [**[JournalLine]**](JournalLine.md) | See JournalLines | [optional] 
**journalNumber** | **Number** | Xero generated journal number | [optional] 
**reference** | **String** | reference field for additional indetifying information | [optional] 
**sourceID** | **String** | The identifier for the source transaction (e.g. InvoiceID) | [optional] 
**sourceType** | **String** | The journal source type. The type of transaction that created the journal | [optional] 



## Enum: SourceTypeEnum


* `ACCREC` (value: `"ACCREC"`)

* `ACCPAY` (value: `"ACCPAY"`)

* `ACCRECCREDIT` (value: `"ACCRECCREDIT"`)

* `ACCPAYCREDIT` (value: `"ACCPAYCREDIT"`)

* `ACCRECPAYMENT` (value: `"ACCRECPAYMENT"`)

* `ACCPAYPAYMENT` (value: `"ACCPAYPAYMENT"`)

* `ARCREDITPAYMENT` (value: `"ARCREDITPAYMENT"`)

* `APCREDITPAYMENT` (value: `"APCREDITPAYMENT"`)

* `CASHREC` (value: `"CASHREC"`)

* `CASHPAID` (value: `"CASHPAID"`)

* `TRANSFER` (value: `"TRANSFER"`)

* `ARPREPAYMENT` (value: `"ARPREPAYMENT"`)

* `APPREPAYMENT` (value: `"APPREPAYMENT"`)

* `AROVERPAYMENT` (value: `"AROVERPAYMENT"`)

* `APOVERPAYMENT` (value: `"APOVERPAYMENT"`)

* `EXPCLAIM` (value: `"EXPCLAIM"`)

* `EXPPAYMENT` (value: `"EXPPAYMENT"`)

* `MANJOURNAL` (value: `"MANJOURNAL"`)

* `PAYSLIP` (value: `"PAYSLIP"`)

* `WAGEPAYABLE` (value: `"WAGEPAYABLE"`)

* `INTEGRATEDPAYROLLPE` (value: `"INTEGRATEDPAYROLLPE"`)

* `INTEGRATEDPAYROLLPT` (value: `"INTEGRATEDPAYROLLPT"`)

* `EXTERNALSPENDMONEY` (value: `"EXTERNALSPENDMONEY"`)

* `INTEGRATEDPAYROLLPTPAYMENT` (value: `"INTEGRATEDPAYROLLPTPAYMENT"`)

* `INTEGRATEDPAYROLLCN` (value: `"INTEGRATEDPAYROLLCN"`)




