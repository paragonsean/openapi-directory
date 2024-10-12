# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1LabelAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryEntities** | [**[GoogleCloudVideointelligenceV1Entity]**](GoogleCloudVideointelligenceV1Entity.md) | Common categories for the detected entity. For example, when the label is &#x60;Terrier&#x60;, the category is likely &#x60;dog&#x60;. And in some cases there might be more than one categories e.g., &#x60;Terrier&#x60; could also be a &#x60;pet&#x60;. | [optional] 
**entity** | [**GoogleCloudVideointelligenceV1Entity**](GoogleCloudVideointelligenceV1Entity.md) |  | [optional] 
**frames** | [**[GoogleCloudVideointelligenceV1LabelFrame]**](GoogleCloudVideointelligenceV1LabelFrame.md) | All video frames where a label was detected. | [optional] 
**segments** | [**[GoogleCloudVideointelligenceV1LabelSegment]**](GoogleCloudVideointelligenceV1LabelSegment.md) | All video segments where a label was detected. | [optional] 
**version** | **String** | Feature version. | [optional] 


