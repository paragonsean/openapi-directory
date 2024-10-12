# CloudVisionApi.GoogleCloudVisionV1p1beta1WebDetection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bestGuessLabels** | [**[GoogleCloudVisionV1p1beta1WebDetectionWebLabel]**](GoogleCloudVisionV1p1beta1WebDetectionWebLabel.md) | The service&#39;s best guess as to the topic of the request image. Inferred from similar images on the open web. | [optional] 
**fullMatchingImages** | [**[GoogleCloudVisionV1p1beta1WebDetectionWebImage]**](GoogleCloudVisionV1p1beta1WebDetectionWebImage.md) | Fully matching images from the Internet. Can include resized copies of the query image. | [optional] 
**pagesWithMatchingImages** | [**[GoogleCloudVisionV1p1beta1WebDetectionWebPage]**](GoogleCloudVisionV1p1beta1WebDetectionWebPage.md) | Web pages containing the matching images from the Internet. | [optional] 
**partialMatchingImages** | [**[GoogleCloudVisionV1p1beta1WebDetectionWebImage]**](GoogleCloudVisionV1p1beta1WebDetectionWebImage.md) | Partial matching images from the Internet. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops. | [optional] 
**visuallySimilarImages** | [**[GoogleCloudVisionV1p1beta1WebDetectionWebImage]**](GoogleCloudVisionV1p1beta1WebDetectionWebImage.md) | The visually similar image results. | [optional] 
**webEntities** | [**[GoogleCloudVisionV1p1beta1WebDetectionWebEntity]**](GoogleCloudVisionV1p1beta1WebDetectionWebEntity.md) | Deduced entities from similar images on the Internet. | [optional] 


