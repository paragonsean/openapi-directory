

# GoogleCloudVideointelligenceV1beta2Track

A track of an object instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;GoogleCloudVideointelligenceV1beta2DetectedAttribute&gt;**](GoogleCloudVideointelligenceV1beta2DetectedAttribute.md) | Optional. Attributes in the track level. |  [optional] |
|**confidence** | **Float** | Optional. The confidence score of the tracked object. |  [optional] |
|**segment** | [**GoogleCloudVideointelligenceV1beta2VideoSegment**](GoogleCloudVideointelligenceV1beta2VideoSegment.md) |  |  [optional] |
|**timestampedObjects** | [**List&lt;GoogleCloudVideointelligenceV1beta2TimestampedObject&gt;**](GoogleCloudVideointelligenceV1beta2TimestampedObject.md) | The object with timestamp and attributes per frame in the track. |  [optional] |



