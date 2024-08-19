# VisualSearchClient.ImageInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cropArea** | [**CropArea**](CropArea.md) |  | [optional] 
**imageInsightsToken** | **String** | An image insights token. To get the insights token, call one of the Image Search APIs (for example, /images/search). In the search results, the [Image](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#image) object&#39;s [imageInsightsToken](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#image-imageinsightstoken) field contains the token. The imageInsightsToken and url fields mutually exclusive; do not specify both. Do not specify an insights token if the request includes the image form data. | [optional] 
**url** | **String** | The URL of the input image. The imageInsightsToken and url fields are mutually exclusive; do not specify both. Do not specify the URL if the request includes the image form data. | [optional] 


