# StorecoveApi.DocumentSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) | DEPRECATED. Use the attachments array inside the &#39;document&#39; property. An array of attachments. You may provide up to 10 attchments, but the total size must not exceed 10MB after Base64 encoding. | [optional] 
**createPrimaryImage** | **Boolean** | DEPRECATED. In the future we will no longer support creating PDF invoices. Whether or not to create a primary image (PDF) if one is not provided. For customers who started from April 1st 2023, the default is false. For customers who started before that, the default is true. | [optional] 
**document** | [**SendableDocument**](SendableDocument.md) |  | [optional] 
**idempotencyGuid** | **String** | A guid that you generated for this DocumentSubmission to achieve idempotency. If you submit multiple documents with the same idempotencyGuid, only the first one will be processed and any subsequent ones will trigger an HTTP 422 Unprocessable Entity response. | [optional] 
**legalEntityId** | **Number** | The id of the LegalEntity this document should be sent on behalf of. Either legalEntityId or receiveGuid is mandatory. | [optional] 
**receiveGuid** | **String** | The GUID that was in the received_document webhook. Either legalEntityId or receiveGuid is mandatory. This field is used for sending response documents, such as InvoiceReponse and OrderResponse. | [optional] 
**routing** | [**Routing**](Routing.md) |  | [optional] 


