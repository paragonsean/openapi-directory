

# GoogleCloudVideointelligenceV1p3beta1TimestampedObject

For tracking related features. An object at time_offset with attributes, and located with normalized_bounding_box.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1DetectedAttribute&gt;**](GoogleCloudVideointelligenceV1p3beta1DetectedAttribute.md) | Optional. The attributes of the object in the bounding box. |  [optional] |
|**landmarks** | [**List&lt;GoogleCloudVideointelligenceV1p3beta1DetectedLandmark&gt;**](GoogleCloudVideointelligenceV1p3beta1DetectedLandmark.md) | Optional. The detected landmarks. |  [optional] |
|**normalizedBoundingBox** | [**GoogleCloudVideointelligenceV1p3beta1NormalizedBoundingBox**](GoogleCloudVideointelligenceV1p3beta1NormalizedBoundingBox.md) |  |  [optional] |
|**timeOffset** | **String** | Time-offset, relative to the beginning of the video, corresponding to the video frame for this object. |  [optional] |



