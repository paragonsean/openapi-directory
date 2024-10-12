# BillingManagementClient.InvoiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountDue** | [**Amount**](Amount.md) |  | [optional] 
**billedAmount** | [**Amount**](Amount.md) |  | [optional] 
**billingProfileDisplayName** | **String** | The billing profile display name this invoice belongs to. | [optional] [readonly] 
**billingProfileId** | **String** | The billing profile id this invoice belongs to. | [optional] [readonly] 
**documents** | [**[Document]**](Document.md) | List of documents available to download including invoice and tax documents. | [optional] [readonly] 
**dueDate** | **Date** | The due date for invoice. | [optional] [readonly] 
**invoiceDate** | **Date** | The date when invoice was created. | [optional] [readonly] 
**invoicePeriodEndDate** | **Date** | The end date of the billing period. | [optional] [readonly] 
**invoicePeriodStartDate** | **Date** | The start date of the billing period. | [optional] [readonly] 
**invoiceType** | **String** | Invoice type. | [optional] [readonly] 
**payments** | [**[PaymentProperties]**](PaymentProperties.md) | List of payments. | [optional] [readonly] 
**purchaseOrderNumber** | **String** | The purchase identifier for the invoice. | [optional] [readonly] 
**status** | **String** | Invoice status. | [optional] [readonly] 



## Enum: InvoiceTypeEnum


* `AzureService` (value: `"AzureService"`)

* `AzureMarketplace` (value: `"AzureMarketplace"`)

* `AzureSupport` (value: `"AzureSupport"`)





## Enum: StatusEnum


* `PastDue` (value: `"PastDue"`)

* `Due` (value: `"Due"`)

* `Paid` (value: `"Paid"`)

* `Void` (value: `"Void"`)




