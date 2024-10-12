

# GoogleCloudVideointelligenceV1p3beta1Track

A track of an object instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1DetectedAttribute&gt;**](GoogleCloudVideointelligenceV1p3beta1DetectedAttribute.md) | Optional. Attributes in the track level. |  [optional] |
|**confidence** | **Float** | Optional. The confidence score of the tracked object. |  [optional] |
|**segment** | [**GoogleCloudVideointelligenceV1p3beta1VideoSegment**](GoogleCloudVideointelligenceV1p3beta1VideoSegment.md) |  |  [optional] |
|**timestampedObjects** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1TimestampedObject&gt;**](GoogleCloudVideointelligenceV1p3beta1TimestampedObject.md) | The object with timestamp and attributes per frame in the track. |  [optional] |



