

# GoogleCloudDocumentaiV1beta2ProcessDocumentRequest

Request to process one document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automlParams** | [**GoogleCloudDocumentaiV1beta2AutoMlParams**](GoogleCloudDocumentaiV1beta2AutoMlParams.md) |  |  [optional] |
|**documentType** | **String** | Specifies a known document type for deeper structure detection. Valid values are currently \&quot;general\&quot; and \&quot;invoice\&quot;. If not provided, \&quot;general\&quot;\\ is used as default. If any other value is given, the request is rejected. |  [optional] |
|**entityExtractionParams** | [**GoogleCloudDocumentaiV1beta2EntityExtractionParams**](GoogleCloudDocumentaiV1beta2EntityExtractionParams.md) |  |  [optional] |
|**formExtractionParams** | [**GoogleCloudDocumentaiV1beta2FormExtractionParams**](GoogleCloudDocumentaiV1beta2FormExtractionParams.md) |  |  [optional] |
|**inputConfig** | [**GoogleCloudDocumentaiV1beta2InputConfig**](GoogleCloudDocumentaiV1beta2InputConfig.md) |  |  [optional] |
|**ocrParams** | [**GoogleCloudDocumentaiV1beta2OcrParams**](GoogleCloudDocumentaiV1beta2OcrParams.md) |  |  [optional] |
|**outputConfig** | [**GoogleCloudDocumentaiV1beta2OutputConfig**](GoogleCloudDocumentaiV1beta2OutputConfig.md) |  |  [optional] |
|**parent** | **String** | Target project and location to make a call. Format: &#x60;projects/{project-id}/locations/{location-id}&#x60;. If no location is specified, a region will be chosen automatically. This field is only populated when used in ProcessDocument method. |  [optional] |
|**tableExtractionParams** | [**GoogleCloudDocumentaiV1beta2TableExtractionParams**](GoogleCloudDocumentaiV1beta2TableExtractionParams.md) |  |  [optional] |



