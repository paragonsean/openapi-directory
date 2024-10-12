

# GoogleCloudVideointelligenceV1p2beta1Track

A track of an object instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;GoogleCloudVideointelligenceV1p2beta1DetectedAttribute&gt;**](GoogleCloudVideointelligenceV1p2beta1DetectedAttribute.md) | Optional. Attributes in the track level. |  [optional] |
|**confidence** | **Float** | Optional. The confidence score of the tracked object. |  [optional] |
|**segment** | [**GoogleCloudVideointelligenceV1p2beta1VideoSegment**](GoogleCloudVideointelligenceV1p2beta1VideoSegment.md) |  |  [optional] |
|**timestampedObjects** | [**List&lt;GoogleCloudVideointelligenceV1p2beta1TimestampedObject&gt;**](GoogleCloudVideointelligenceV1p2beta1TimestampedObject.md) | The object with timestamp and attributes per frame in the track. |  [optional] |



