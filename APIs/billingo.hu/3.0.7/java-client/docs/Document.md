

# Document

Document object representing your invoice.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockId** | **Integer** | DocumentBlock&#39;s identifier. |  [optional] |
|**cancelled** | **Boolean** |  |  [optional] |
|**comment** | **String** |  |  [optional] |
|**conversionRate** | **Float** |  |  [optional] |
|**currency** | **Currency** |  |  [optional] |
|**dueDate** | **LocalDate** |  |  [optional] |
|**electronic** | **Boolean** |  |  [optional] |
|**fulfillmentDate** | **LocalDate** |  |  [optional] |
|**grossTotal** | **Float** | The document&#39;s gross total price. |  [optional] |
|**id** | **Integer** | The document&#39;s unique identifier. |  [optional] |
|**invoiceDate** | **LocalDate** |  |  [optional] |
|**invoiceNumber** | **String** | The document&#39;s invoice number. |  [optional] |
|**items** | [**List&lt;DocumentItem&gt;**](DocumentItem.md) |  |  [optional] |
|**language** | **DocumentLanguage** |  |  [optional] |
|**notificationStatus** | **DocumentNotificationStatus** |  |  [optional] |
|**organization** | [**DocumentOrganization**](DocumentOrganization.md) |  |  [optional] |
|**paidDate** | **LocalDate** |  |  [optional] |
|**partner** | [**Partner**](Partner.md) |  |  [optional] |
|**paymentMethod** | **PaymentMethod** |  |  [optional] |
|**paymentStatus** | **PaymentStatus** |  |  [optional] |
|**settings** | [**DocumentSettings**](DocumentSettings.md) |  |  [optional] |
|**summary** | [**DocumentSummary**](DocumentSummary.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**type** | **DocumentType** |  |  [optional] |



