

# InvoiceProperties

The properties of the invoice.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountDue** | [**Amount**](Amount.md) |  |  [optional] |
|**billedAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**billingProfileDisplayName** | **String** | The billing profile display name this invoice belongs to. |  [optional] [readonly] |
|**billingProfileId** | **String** | The billing profile id this invoice belongs to. |  [optional] [readonly] |
|**documents** | [**List&lt;Document&gt;**](Document.md) | List of documents available to download including invoice and tax documents. |  [optional] [readonly] |
|**dueDate** | **OffsetDateTime** | The due date for invoice. |  [optional] [readonly] |
|**invoiceDate** | **OffsetDateTime** | The date when invoice was created. |  [optional] [readonly] |
|**invoicePeriodEndDate** | **OffsetDateTime** | The end date of the billing period. |  [optional] [readonly] |
|**invoicePeriodStartDate** | **OffsetDateTime** | The start date of the billing period. |  [optional] [readonly] |
|**invoiceType** | [**InvoiceTypeEnum**](#InvoiceTypeEnum) | Invoice type. |  [optional] [readonly] |
|**payments** | [**List&lt;PaymentProperties&gt;**](PaymentProperties.md) | List of payments. |  [optional] [readonly] |
|**purchaseOrderNumber** | **String** | The purchase identifier for the invoice. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Invoice status. |  [optional] [readonly] |



## Enum: InvoiceTypeEnum

| Name | Value |
|---- | -----|
| AZURE_SERVICE | &quot;AzureService&quot; |
| AZURE_MARKETPLACE | &quot;AzureMarketplace&quot; |
| AZURE_SUPPORT | &quot;AzureSupport&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PAST_DUE | &quot;PastDue&quot; |
| DUE | &quot;Due&quot; |
| PAID | &quot;Paid&quot; |
| VOID | &quot;Void&quot; |



