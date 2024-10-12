

# RecognizedEntityGroup

Defines a group of previously recognized entities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the group where images of the entity were also found. The following are possible groups. CelebRecognitionAnnotations: Similar to CelebrityAnnotations but provides a higher probability of an accurate match. CelebrityAnnotations: Contains celebrities such as actors, politicians, athletes, and historical figures. |  |
|**recognizedEntityRegions** | [**List&lt;RecognizedEntityRegion&gt;**](RecognizedEntityRegion.md) | The regions of the image that contain entities. |  |



