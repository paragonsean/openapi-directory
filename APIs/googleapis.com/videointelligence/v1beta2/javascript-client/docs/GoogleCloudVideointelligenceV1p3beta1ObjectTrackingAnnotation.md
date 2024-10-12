# CloudVideoIntelligenceApi.GoogleCloudVideointelligenceV1p3beta1ObjectTrackingAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | Object category&#39;s labeling confidence of this track. | [optional] 
**entity** | [**GoogleCloudVideointelligenceV1p3beta1Entity**](GoogleCloudVideointelligenceV1p3beta1Entity.md) |  | [optional] 
**frames** | [**[GoogleCloudVideointelligenceV1p3beta1ObjectTrackingFrame]**](GoogleCloudVideointelligenceV1p3beta1ObjectTrackingFrame.md) | Information corresponding to all frames where this object track appears. Non-streaming batch mode: it may be one or multiple ObjectTrackingFrame messages in frames. Streaming mode: it can only be one ObjectTrackingFrame message in frames. | [optional] 
**segment** | [**GoogleCloudVideointelligenceV1p3beta1VideoSegment**](GoogleCloudVideointelligenceV1p3beta1VideoSegment.md) |  | [optional] 
**trackId** | **String** | Streaming mode ONLY. In streaming mode, we do not know the end time of a tracked object before it is completed. Hence, there is no VideoSegment info returned. Instead, we provide a unique identifiable integer track_id so that the customers can correlate the results of the ongoing ObjectTrackAnnotation of the same track_id over time. | [optional] 
**version** | **String** | Feature version. | [optional] 


