# AmazonConnectParticipantService.StartAttachmentUploadRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | Describes the MIME file type of the attachment. For a list of supported file types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html\&quot;&gt;Feature specifications&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. | 
**attachmentSizeInBytes** | **Number** | The size of the attachment in bytes. | 
**attachmentName** | **String** | A case-sensitive name of the attachment being uploaded. | 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. | 


