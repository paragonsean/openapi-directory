# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1p3beta1LabelAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryEntities** | [**[GoogleCloudVideointelligenceV1p3beta1Entity]**](GoogleCloudVideointelligenceV1p3beta1Entity.md) | Common categories for the detected entity. For example, when the label is &#x60;Terrier&#x60;, the category is likely &#x60;dog&#x60;. And in some cases there might be more than one categories e.g., &#x60;Terrier&#x60; could also be a &#x60;pet&#x60;. | [optional] 
**entity** | [**GoogleCloudVideointelligenceV1p3beta1Entity**](GoogleCloudVideointelligenceV1p3beta1Entity.md) |  | [optional] 
**frames** | [**[GoogleCloudVideointelligenceV1p3beta1LabelFrame]**](GoogleCloudVideointelligenceV1p3beta1LabelFrame.md) | All video frames where a label was detected. | [optional] 
**segments** | [**[GoogleCloudVideointelligenceV1p3beta1LabelSegment]**](GoogleCloudVideointelligenceV1p3beta1LabelSegment.md) | All video segments where a label was detected. | [optional] 
**version** | **String** | Feature version. | [optional] 


