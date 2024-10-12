

# GoogleCloudVideointelligenceV1beta2LogoRecognitionAnnotation

Annotation corresponding to one detected, tracked and recognized logo class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | [**GoogleCloudVideointelligenceV1beta2Entity**](GoogleCloudVideointelligenceV1beta2Entity.md) |  |  [optional] |
|**segments** | [**List&lt;GoogleCloudVideointelligenceV1beta2VideoSegment&gt;**](GoogleCloudVideointelligenceV1beta2VideoSegment.md) | All video segments where the recognized logo appears. There might be multiple instances of the same logo class appearing in one VideoSegment. |  [optional] |
|**tracks** | [**List&lt;GoogleCloudVideointelligenceV1beta2Track&gt;**](GoogleCloudVideointelligenceV1beta2Track.md) | All logo tracks where the recognized logo appears. Each track corresponds to one logo instance appearing in consecutive frames. |  [optional] |



