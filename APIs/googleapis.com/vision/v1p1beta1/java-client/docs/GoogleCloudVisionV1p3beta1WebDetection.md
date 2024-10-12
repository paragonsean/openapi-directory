

# GoogleCloudVisionV1p3beta1WebDetection

Relevant information for the image from the Internet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bestGuessLabels** | [**List&lt;GoogleCloudVisionV1p3beta1WebDetectionWebLabel&gt;**](GoogleCloudVisionV1p3beta1WebDetectionWebLabel.md) | The service&#39;s best guess as to the topic of the request image. Inferred from similar images on the open web. |  [optional] |
|**fullMatchingImages** | [**List&lt;GoogleCloudVisionV1p3beta1WebDetectionWebImage&gt;**](GoogleCloudVisionV1p3beta1WebDetectionWebImage.md) | Fully matching images from the Internet. Can include resized copies of the query image. |  [optional] |
|**pagesWithMatchingImages** | [**List&lt;GoogleCloudVisionV1p3beta1WebDetectionWebPage&gt;**](GoogleCloudVisionV1p3beta1WebDetectionWebPage.md) | Web pages containing the matching images from the Internet. |  [optional] |
|**partialMatchingImages** | [**List&lt;GoogleCloudVisionV1p3beta1WebDetectionWebImage&gt;**](GoogleCloudVisionV1p3beta1WebDetectionWebImage.md) | Partial matching images from the Internet. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops. |  [optional] |
|**visuallySimilarImages** | [**List&lt;GoogleCloudVisionV1p3beta1WebDetectionWebImage&gt;**](GoogleCloudVisionV1p3beta1WebDetectionWebImage.md) | The visually similar image results. |  [optional] |
|**webEntities** | [**List&lt;GoogleCloudVisionV1p3beta1WebDetectionWebEntity&gt;**](GoogleCloudVisionV1p3beta1WebDetectionWebEntity.md) | Deduced entities from similar images on the Internet. |  [optional] |



