

# SendableDocument

The document to send.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentType** | [**DocumentTypeEnum**](#DocumentTypeEnum) | The type of document to be sent. |  |
|**invoice** | [**Invoice**](Invoice.md) |  |  [optional] |
|**invoiceResponse** | [**DocumentInvoiceResponse**](DocumentInvoiceResponse.md) |  |  [optional] |
|**order** | [**DocumentOrder**](DocumentOrder.md) |  |  [optional] |
|**rawDocumentData** | [**RawDocumentData**](RawDocumentData.md) |  |  [optional] |



## Enum: DocumentTypeEnum

| Name | Value |
|---- | -----|
| INVOICE | &quot;invoice&quot; |
| INVOICE_RESPONSE | &quot;invoice_response&quot; |
| ORDER | &quot;order&quot; |



