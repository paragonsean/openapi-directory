

# GoogleCloudDocumentaiV1ProcessRequest

Request message for the ProcessDocument method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldMask** | **String** | Specifies which fields to include in the ProcessResponse.document output. Only supports top-level document and pages field, so it must be in the form of &#x60;{document_field_name}&#x60; or &#x60;pages.{page_field_name}&#x60;. |  [optional] |
|**gcsDocument** | [**GoogleCloudDocumentaiV1GcsDocument**](GoogleCloudDocumentaiV1GcsDocument.md) |  |  [optional] |
|**inlineDocument** | [**GoogleCloudDocumentaiV1Document**](GoogleCloudDocumentaiV1Document.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. |  [optional] |
|**processOptions** | [**GoogleCloudDocumentaiV1ProcessOptions**](GoogleCloudDocumentaiV1ProcessOptions.md) |  |  [optional] |
|**rawDocument** | [**GoogleCloudDocumentaiV1RawDocument**](GoogleCloudDocumentaiV1RawDocument.md) |  |  [optional] |
|**skipHumanReview** | **Boolean** | Whether human review should be skipped for this request. Default to &#x60;false&#x60;. |  [optional] |



