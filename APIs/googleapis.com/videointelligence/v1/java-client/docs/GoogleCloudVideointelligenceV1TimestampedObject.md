

# GoogleCloudVideointelligenceV1TimestampedObject

For tracking related features. An object at time_offset with attributes, and located with normalized_bounding_box.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;GoogleCloudVideointelligenceV1DetectedAttribute&gt;**](GoogleCloudVideointelligenceV1DetectedAttribute.md) | Optional. The attributes of the object in the bounding box. |  [optional] |
|**landmarks** | [**List&lt;GoogleCloudVideointelligenceV1DetectedLandmark&gt;**](GoogleCloudVideointelligenceV1DetectedLandmark.md) | Optional. The detected landmarks. |  [optional] |
|**normalizedBoundingBox** | [**GoogleCloudVideointelligenceV1NormalizedBoundingBox**](GoogleCloudVideointelligenceV1NormalizedBoundingBox.md) |  |  [optional] |
|**timeOffset** | **String** | Time-offset, relative to the beginning of the video, corresponding to the video frame for this object. |  [optional] |



