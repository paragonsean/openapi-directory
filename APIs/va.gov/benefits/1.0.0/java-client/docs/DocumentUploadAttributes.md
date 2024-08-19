

# DocumentUploadAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Unambiguous status code. Only present if status &#x3D; \&quot;error\&quot;  * &#x60;DOC101&#x60; - Invalid multipart payload provided - not a multipart, or missing one or more required parts. * &#x60;DOC102&#x60; - Invalid metadata - not parseable as JSON, incorrect fields, etc. * &#x60;DOC103&#x60; - Invalid content - not parseable as PDF. Detail field will indicate which document or attachment part was affected. * &#x60;DOC104&#x60; - Upload rejected by upstream system. Processing failed and upload must be resubmitted. Detail field will indicate nature of rejection. * &#x60;DOC105&#x60; - Invalid or unknown id * &#x60;DOC106&#x60; - File size limit exceeded. Each document may be a maximum of 100MB. * &#x60;DOC107&#x60; - Empty payload. * &#x60;DOC108&#x60; - Maximum dimensions exceeded. Height and width must be less than 21 in x 21 in. * &#x60;DOC201&#x60; - Upload server error. * &#x60;DOC202&#x60; - Error during processing by upstream system. Processing failed and upload must be resubmitted. Detail field will provide additional details where available.  |  [optional] |
|**detail** | **String** | Human readable error detail. Only present if status &#x3D; \&quot;error\&quot; |  [optional] |
|**guid** | **UUID** | The document upload identifier |  |
|**location** | **URI** | Location to which to PUT document Payload |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Document upload status.  |  |
|**updatedAt** | **OffsetDateTime** | The last time the submission was updated |  [optional] |
|**uploadedPdf** | **Object** | Only populated after submission starts processing |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| UPLOADED | &quot;uploaded&quot; |
| RECEIVED | &quot;received&quot; |
| PROCESSING | &quot;processing&quot; |
| SUCCESS | &quot;success&quot; |
| VBMS | &quot;vbms&quot; |
| ERROR | &quot;error&quot; |



