

# ImageContext

Image context and/or feature-specific parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cropHintsParams** | [**CropHintsParams**](CropHintsParams.md) |  |  [optional] |
|**languageHints** | **List&lt;String&gt;** | List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting &#x60;language_hints&#x60; is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages). |  [optional] |
|**latLongRect** | [**LatLongRect**](LatLongRect.md) |  |  [optional] |
|**productSearchParams** | [**ProductSearchParams**](ProductSearchParams.md) |  |  [optional] |
|**textDetectionParams** | [**TextDetectionParams**](TextDetectionParams.md) |  |  [optional] |
|**webDetectionParams** | [**WebDetectionParams**](WebDetectionParams.md) |  |  [optional] |



