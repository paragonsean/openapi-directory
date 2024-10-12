# CloudVisionApi.GoogleCloudVisionV1p2beta1ImageContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cropHintsParams** | [**GoogleCloudVisionV1p2beta1CropHintsParams**](GoogleCloudVisionV1p2beta1CropHintsParams.md) |  | [optional] 
**languageHints** | **[String]** | List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting &#x60;language_hints&#x60; is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages). | [optional] 
**latLongRect** | [**GoogleCloudVisionV1p2beta1LatLongRect**](GoogleCloudVisionV1p2beta1LatLongRect.md) |  | [optional] 
**productSearchParams** | [**GoogleCloudVisionV1p2beta1ProductSearchParams**](GoogleCloudVisionV1p2beta1ProductSearchParams.md) |  | [optional] 
**textDetectionParams** | [**GoogleCloudVisionV1p2beta1TextDetectionParams**](GoogleCloudVisionV1p2beta1TextDetectionParams.md) |  | [optional] 
**webDetectionParams** | [**GoogleCloudVisionV1p2beta1WebDetectionParams**](GoogleCloudVisionV1p2beta1WebDetectionParams.md) |  | [optional] 


