# BillingManagementClient.InvoiceSummaryProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountDue** | [**Amount**](Amount.md) |  | [optional] 
**billedAmount** | [**Amount**](Amount.md) |  | [optional] 
**billingProfileId** | **String** | The billing profile id this invoice belongs to. | [optional] [readonly] 
**billingProfileName** | **String** | The profile name this invoice belongs to. | [optional] [readonly] 
**documentUrls** | [**[DownloadProperties]**](DownloadProperties.md) | List of document urls available to download including invoice and tax documents. | [optional] [readonly] 
**dueDate** | **Date** | The due date for invoice. | [optional] [readonly] 
**invoiceDate** | **Date** | The date when invoice was created. | [optional] [readonly] 
**invoicePeriodEndDate** | **Date** | The end date of the billing period. | [optional] [readonly] 
**invoicePeriodStartDate** | **Date** | The start date of the billing period. | [optional] [readonly] 
**payments** | [**[PaymentProperties]**](PaymentProperties.md) | List of payments. | [optional] [readonly] 
**purchaseOrderNumber** | **String** | The purchase identifier for the invoice. | [optional] [readonly] 
**status** | **String** | Invoice status. | [optional] [readonly] 



## Enum: StatusEnum


* `PastDue` (value: `"PastDue"`)

* `Due` (value: `"Due"`)

* `Paid` (value: `"Paid"`)

* `Void` (value: `"Void"`)




