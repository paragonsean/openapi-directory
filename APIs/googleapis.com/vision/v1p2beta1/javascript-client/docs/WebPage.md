# CloudVisionApi.WebPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullMatchingImages** | [**[WebImage]**](WebImage.md) | Fully matching images on the page. Can include resized copies of the query image. | [optional] 
**pageTitle** | **String** | Title for the web page, may contain HTML markups. | [optional] 
**partialMatchingImages** | [**[WebImage]**](WebImage.md) | Partial matching images on the page. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops. | [optional] 
**score** | **Number** | (Deprecated) Overall relevancy score for the web page. | [optional] 
**url** | **String** | The result web page URL. | [optional] 


