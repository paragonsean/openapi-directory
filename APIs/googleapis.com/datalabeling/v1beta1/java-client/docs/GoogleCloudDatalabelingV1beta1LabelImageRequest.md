

# GoogleCloudDatalabelingV1beta1LabelImageRequest

Request message for starting an image labeling task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicConfig** | [**GoogleCloudDatalabelingV1beta1HumanAnnotationConfig**](GoogleCloudDatalabelingV1beta1HumanAnnotationConfig.md) |  |  [optional] |
|**boundingPolyConfig** | [**GoogleCloudDatalabelingV1beta1BoundingPolyConfig**](GoogleCloudDatalabelingV1beta1BoundingPolyConfig.md) |  |  [optional] |
|**feature** | [**FeatureEnum**](#FeatureEnum) | Required. The type of image labeling task. |  [optional] |
|**imageClassificationConfig** | [**GoogleCloudDatalabelingV1beta1ImageClassificationConfig**](GoogleCloudDatalabelingV1beta1ImageClassificationConfig.md) |  |  [optional] |
|**polylineConfig** | [**GoogleCloudDatalabelingV1beta1PolylineConfig**](GoogleCloudDatalabelingV1beta1PolylineConfig.md) |  |  [optional] |
|**segmentationConfig** | [**GoogleCloudDatalabelingV1beta1SegmentationConfig**](GoogleCloudDatalabelingV1beta1SegmentationConfig.md) |  |  [optional] |



## Enum: FeatureEnum

| Name | Value |
|---- | -----|
| FEATURE_UNSPECIFIED | &quot;FEATURE_UNSPECIFIED&quot; |
| CLASSIFICATION | &quot;CLASSIFICATION&quot; |
| BOUNDING_BOX | &quot;BOUNDING_BOX&quot; |
| ORIENTED_BOUNDING_BOX | &quot;ORIENTED_BOUNDING_BOX&quot; |
| BOUNDING_POLY | &quot;BOUNDING_POLY&quot; |
| POLYLINE | &quot;POLYLINE&quot; |
| SEGMENTATION | &quot;SEGMENTATION&quot; |



