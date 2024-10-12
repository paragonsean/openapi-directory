

# InvoiceSubmission

DEPRECATED. The invoice you want Storecove to process, with some meta-data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | An array of attachments. You may provide up to 10 attchments, but the total size must not exceed 10MB after Base64 encoding. |  [optional] |
|**createPrimaryImage** | **Boolean** | DEPRECATED. In the future we will no longer support creating PDF invoices. Whether or not to create a primary image (PDF) if one is not provided. For customers who started from December 1st 2022, the default is false. For customers who started before that, the default is true. |  [optional] |
|**document** | **String** | DEPRECATED. Use attachments. |  [optional] |
|**documentUrl** | **URI** | DEPRECATED. Use attachments. |  [optional] |
|**idempotencyGuid** | **String** | A guid that you generated for this InvoiceSubmission to achieve idempotency. If you submit multiple documents with the same idempotencyGuid, only the first one will be processed. |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  [optional] |
|**invoiceData** | [**InvoiceData**](InvoiceData.md) |  |  [optional] |
|**invoiceRecipient** | [**InvoiceRecipient**](InvoiceRecipient.md) |  |  [optional] |
|**legalEntityId** | **Integer** | The id of the LegalEntity this invoice should be sent for. |  [optional] |
|**legalSupplierId** | **Integer** | DEPRECATED. Use legalEntityId |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | DEPRECATED. |  [optional] |
|**routing** | [**Routing**](Routing.md) |  |  [optional] |
|**supplierId** | **Integer** | DEPRECATED. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| DIRECT | &quot;direct&quot; |



