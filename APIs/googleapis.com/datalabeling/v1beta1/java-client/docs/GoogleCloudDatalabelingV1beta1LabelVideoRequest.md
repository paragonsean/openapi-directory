

# GoogleCloudDatalabelingV1beta1LabelVideoRequest

Request message for LabelVideo.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicConfig** | [**GoogleCloudDatalabelingV1beta1HumanAnnotationConfig**](GoogleCloudDatalabelingV1beta1HumanAnnotationConfig.md) |  |  [optional] |
|**eventConfig** | [**GoogleCloudDatalabelingV1beta1EventConfig**](GoogleCloudDatalabelingV1beta1EventConfig.md) |  |  [optional] |
|**feature** | [**FeatureEnum**](#FeatureEnum) | Required. The type of video labeling task. |  [optional] |
|**objectDetectionConfig** | [**GoogleCloudDatalabelingV1beta1ObjectDetectionConfig**](GoogleCloudDatalabelingV1beta1ObjectDetectionConfig.md) |  |  [optional] |
|**objectTrackingConfig** | [**GoogleCloudDatalabelingV1beta1ObjectTrackingConfig**](GoogleCloudDatalabelingV1beta1ObjectTrackingConfig.md) |  |  [optional] |
|**videoClassificationConfig** | [**GoogleCloudDatalabelingV1beta1VideoClassificationConfig**](GoogleCloudDatalabelingV1beta1VideoClassificationConfig.md) |  |  [optional] |



## Enum: FeatureEnum

| Name | Value |
|---- | -----|
| FEATURE_UNSPECIFIED | &quot;FEATURE_UNSPECIFIED&quot; |
| CLASSIFICATION | &quot;CLASSIFICATION&quot; |
| OBJECT_DETECTION | &quot;OBJECT_DETECTION&quot; |
| OBJECT_TRACKING | &quot;OBJECT_TRACKING&quot; |
| EVENT | &quot;EVENT&quot; |



