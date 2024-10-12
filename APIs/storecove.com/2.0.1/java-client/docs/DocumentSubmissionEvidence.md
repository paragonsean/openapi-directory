

# DocumentSubmissionEvidence


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documents** | [**List&lt;DocumentSubmissionEvidenceDocument&gt;**](DocumentSubmissionEvidenceDocument.md) | An array of documents that were sent. For OpenPeppol, this is always a single document (it may contain a PDF inside). For Email, the number of documents depends on the number of attachments, which in turn depends on the country of the receiver. For email, the raw email in RFC822 format is also included. |  [optional] |
|**evidence** | [**DocumentSubmissionEvidenceEvidence**](DocumentSubmissionEvidenceEvidence.md) |  |  [optional] |
|**network** | [**NetworkEnum**](#NetworkEnum) | The exchange network that was used to send the document |  [optional] |
|**receiver** | **String** | The legal identifier of the receiver, or the tax identifier if there is no legal identifier. |  [optional] |
|**sender** | **String** | The legal identifier of the sender, or the tax identifier if there is no legal identifier. |  [optional] |



## Enum: NetworkEnum

| Name | Value |
|---- | -----|
| AS2 | &quot;as2&quot; |
| EMAIL | &quot;email&quot; |
| PEPPOL | &quot;peppol&quot; |
| SDI | &quot;sdi&quot; |



