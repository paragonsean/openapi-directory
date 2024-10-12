

# GoogleCloudVisionV1p2beta1AnnotateFileResponse

Response to a single file annotation request. A file may contain one or more images, which individually have their own responses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**Status**](Status.md) |  |  [optional] |
|**inputConfig** | [**GoogleCloudVisionV1p2beta1InputConfig**](GoogleCloudVisionV1p2beta1InputConfig.md) |  |  [optional] |
|**responses** | [**List&lt;GoogleCloudVisionV1p2beta1AnnotateImageResponse&gt;**](GoogleCloudVisionV1p2beta1AnnotateImageResponse.md) | Individual responses to images found within the file. This field will be empty if the &#x60;error&#x60; field is set. |  [optional] |
|**totalPages** | **Integer** | This field gives the total number of pages in the file. |  [optional] |



