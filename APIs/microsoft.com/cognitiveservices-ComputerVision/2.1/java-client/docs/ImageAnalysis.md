

# ImageAnalysis

Result of AnalyzeImage operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adult** | [**AdultInfo**](AdultInfo.md) |  |  [optional] |
|**brands** | [**List&lt;DetectedBrand&gt;**](DetectedBrand.md) | Array of brands detected in the image. |  [optional] |
|**categories** | [**List&lt;Category&gt;**](Category.md) | An array indicating identified categories. |  [optional] |
|**color** | [**ColorInfo**](ColorInfo.md) |  |  [optional] |
|**description** | [**ImageDescriptionDetails**](ImageDescriptionDetails.md) |  |  [optional] |
|**faces** | [**List&lt;FaceDescription&gt;**](FaceDescription.md) | An array of possible faces within the image. |  [optional] |
|**imageType** | [**ImageType**](ImageType.md) |  |  [optional] |
|**metadata** | [**ImageMetadata**](ImageMetadata.md) |  |  [optional] |
|**objects** | [**List&lt;DetectedObject&gt;**](DetectedObject.md) | Array of objects describing what was detected in the image. |  [optional] |
|**requestId** | **String** | Id of the REST API request. |  [optional] |
|**tags** | [**List&lt;ImageTag&gt;**](ImageTag.md) | A list of tags with confidence level. |  [optional] |



