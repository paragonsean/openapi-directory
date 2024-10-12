

# AsyncBatchAnnotateImagesRequest

Request for async image annotation for a list of images.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. |  [optional] |
|**outputConfig** | [**OutputConfig**](OutputConfig.md) |  |  [optional] |
|**parent** | **String** | Optional. Target project and location to make a call. Format: &#x60;projects/{project-id}/locations/{location-id}&#x60;. If no parent is specified, a region will be chosen automatically. Supported location-ids: &#x60;us&#x60;: USA country only, &#x60;asia&#x60;: East asia areas, like Japan, Taiwan, &#x60;eu&#x60;: The European Union. Example: &#x60;projects/project-A/locations/eu&#x60;. |  [optional] |
|**requests** | [**List&lt;AnnotateImageRequest&gt;**](AnnotateImageRequest.md) | Required. Individual image annotation requests for this batch. |  [optional] |



