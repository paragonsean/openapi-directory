

# GoogleCloudVideointelligenceV1p2beta1LabelDetectionConfig

Config for LABEL_DETECTION.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frameConfidenceThreshold** | **Float** | The confidence threshold we perform filtering on the labels from frame-level detection. If not set, it is set to 0.4 by default. The valid range for this threshold is [0.1, 0.9]. Any value set outside of this range will be clipped. Note: For best results, follow the default threshold. We will update the default threshold everytime when we release a new model. |  [optional] |
|**labelDetectionMode** | [**LabelDetectionModeEnum**](#LabelDetectionModeEnum) | What labels should be detected with LABEL_DETECTION, in addition to video-level labels or segment-level labels. If unspecified, defaults to &#x60;SHOT_MODE&#x60;. |  [optional] |
|**model** | **String** | Model to use for label detection. Supported values: \&quot;builtin/stable\&quot; (the default if unset) and \&quot;builtin/latest\&quot;. |  [optional] |
|**stationaryCamera** | **Boolean** | Whether the video has been shot from a stationary (i.e., non-moving) camera. When set to true, might improve detection accuracy for moving objects. Should be used with &#x60;SHOT_AND_FRAME_MODE&#x60; enabled. |  [optional] |
|**videoConfidenceThreshold** | **Float** | The confidence threshold we perform filtering on the labels from video-level and shot-level detections. If not set, it&#39;s set to 0.3 by default. The valid range for this threshold is [0.1, 0.9]. Any value set outside of this range will be clipped. Note: For best results, follow the default threshold. We will update the default threshold everytime when we release a new model. |  [optional] |



## Enum: LabelDetectionModeEnum

| Name | Value |
|---- | -----|
| LABEL_DETECTION_MODE_UNSPECIFIED | &quot;LABEL_DETECTION_MODE_UNSPECIFIED&quot; |
| SHOT_MODE | &quot;SHOT_MODE&quot; |
| FRAME_MODE | &quot;FRAME_MODE&quot; |
| SHOT_AND_FRAME_MODE | &quot;SHOT_AND_FRAME_MODE&quot; |



