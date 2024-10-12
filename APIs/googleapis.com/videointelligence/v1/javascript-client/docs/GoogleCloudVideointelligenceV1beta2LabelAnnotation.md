# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1beta2LabelAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryEntities** | [**[GoogleCloudVideointelligenceV1beta2Entity]**](GoogleCloudVideointelligenceV1beta2Entity.md) | Common categories for the detected entity. For example, when the label is &#x60;Terrier&#x60;, the category is likely &#x60;dog&#x60;. And in some cases there might be more than one categories e.g., &#x60;Terrier&#x60; could also be a &#x60;pet&#x60;. | [optional] 
**entity** | [**GoogleCloudVideointelligenceV1beta2Entity**](GoogleCloudVideointelligenceV1beta2Entity.md) |  | [optional] 
**frames** | [**[GoogleCloudVideointelligenceV1beta2LabelFrame]**](GoogleCloudVideointelligenceV1beta2LabelFrame.md) | All video frames where a label was detected. | [optional] 
**segments** | [**[GoogleCloudVideointelligenceV1beta2LabelSegment]**](GoogleCloudVideointelligenceV1beta2LabelSegment.md) | All video segments where a label was detected. | [optional] 
**version** | **String** | Feature version. | [optional] 


