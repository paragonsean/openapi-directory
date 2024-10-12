

# GoogleCloudVisionV1p1beta1ImageContext

Image context and/or feature-specific parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cropHintsParams** | [**GoogleCloudVisionV1p1beta1CropHintsParams**](GoogleCloudVisionV1p1beta1CropHintsParams.md) |  |  [optional] |
|**languageHints** | **List&lt;String&gt;** | List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting &#x60;language_hints&#x60; is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages). |  [optional] |
|**latLongRect** | [**GoogleCloudVisionV1p1beta1LatLongRect**](GoogleCloudVisionV1p1beta1LatLongRect.md) |  |  [optional] |
|**productSearchParams** | [**GoogleCloudVisionV1p1beta1ProductSearchParams**](GoogleCloudVisionV1p1beta1ProductSearchParams.md) |  |  [optional] |
|**textDetectionParams** | [**GoogleCloudVisionV1p1beta1TextDetectionParams**](GoogleCloudVisionV1p1beta1TextDetectionParams.md) |  |  [optional] |
|**webDetectionParams** | [**GoogleCloudVisionV1p1beta1WebDetectionParams**](GoogleCloudVisionV1p1beta1WebDetectionParams.md) |  |  [optional] |



