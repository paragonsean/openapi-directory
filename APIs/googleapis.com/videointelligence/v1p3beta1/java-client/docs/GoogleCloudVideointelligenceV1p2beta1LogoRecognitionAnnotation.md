

# GoogleCloudVideointelligenceV1p2beta1LogoRecognitionAnnotation

Annotation corresponding to one detected, tracked and recognized logo class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | [**GoogleCloudVideointelligenceV1p2beta1Entity**](GoogleCloudVideointelligenceV1p2beta1Entity.md) |  |  [optional] |
|**segments** | [**List&lt;GoogleCloudVideointelligenceV1p2beta1VideoSegment&gt;**](GoogleCloudVideointelligenceV1p2beta1VideoSegment.md) | All video segments where the recognized logo appears. There might be multiple instances of the same logo class appearing in one VideoSegment. |  [optional] |
|**tracks** | [**List&lt;GoogleCloudVideointelligenceV1p2beta1Track&gt;**](GoogleCloudVideointelligenceV1p2beta1Track.md) | All logo tracks where the recognized logo appears. Each track corresponds to one logo instance appearing in consecutive frames. |  [optional] |



