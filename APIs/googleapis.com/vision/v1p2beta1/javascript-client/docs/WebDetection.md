# CloudVisionApi.WebDetection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bestGuessLabels** | [**[WebLabel]**](WebLabel.md) | The service&#39;s best guess as to the topic of the request image. Inferred from similar images on the open web. | [optional] 
**fullMatchingImages** | [**[WebImage]**](WebImage.md) | Fully matching images from the Internet. Can include resized copies of the query image. | [optional] 
**pagesWithMatchingImages** | [**[WebPage]**](WebPage.md) | Web pages containing the matching images from the Internet. | [optional] 
**partialMatchingImages** | [**[WebImage]**](WebImage.md) | Partial matching images from the Internet. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops. | [optional] 
**visuallySimilarImages** | [**[WebImage]**](WebImage.md) | The visually similar image results. | [optional] 
**webEntities** | [**[WebEntity]**](WebEntity.md) | Deduced entities from similar images on the Internet. | [optional] 


