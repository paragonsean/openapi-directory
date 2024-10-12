# DataLabelingApi.GoogleCloudDatalabelingV1beta1LabelVideoRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basicConfig** | [**GoogleCloudDatalabelingV1beta1HumanAnnotationConfig**](GoogleCloudDatalabelingV1beta1HumanAnnotationConfig.md) |  | [optional] 
**eventConfig** | [**GoogleCloudDatalabelingV1beta1EventConfig**](GoogleCloudDatalabelingV1beta1EventConfig.md) |  | [optional] 
**feature** | **String** | Required. The type of video labeling task. | [optional] 
**objectDetectionConfig** | [**GoogleCloudDatalabelingV1beta1ObjectDetectionConfig**](GoogleCloudDatalabelingV1beta1ObjectDetectionConfig.md) |  | [optional] 
**objectTrackingConfig** | [**GoogleCloudDatalabelingV1beta1ObjectTrackingConfig**](GoogleCloudDatalabelingV1beta1ObjectTrackingConfig.md) |  | [optional] 
**videoClassificationConfig** | [**GoogleCloudDatalabelingV1beta1VideoClassificationConfig**](GoogleCloudDatalabelingV1beta1VideoClassificationConfig.md) |  | [optional] 



## Enum: FeatureEnum


* `FEATURE_UNSPECIFIED` (value: `"FEATURE_UNSPECIFIED"`)

* `CLASSIFICATION` (value: `"CLASSIFICATION"`)

* `OBJECT_DETECTION` (value: `"OBJECT_DETECTION"`)

* `OBJECT_TRACKING` (value: `"OBJECT_TRACKING"`)

* `EVENT` (value: `"EVENT"`)




