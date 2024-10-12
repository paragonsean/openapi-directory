# DataLabelingApi.GoogleCloudDatalabelingV1beta1LabelImageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basicConfig** | [**GoogleCloudDatalabelingV1beta1HumanAnnotationConfig**](GoogleCloudDatalabelingV1beta1HumanAnnotationConfig.md) |  | [optional] 
**boundingPolyConfig** | [**GoogleCloudDatalabelingV1beta1BoundingPolyConfig**](GoogleCloudDatalabelingV1beta1BoundingPolyConfig.md) |  | [optional] 
**feature** | **String** | Required. The type of image labeling task. | [optional] 
**imageClassificationConfig** | [**GoogleCloudDatalabelingV1beta1ImageClassificationConfig**](GoogleCloudDatalabelingV1beta1ImageClassificationConfig.md) |  | [optional] 
**polylineConfig** | [**GoogleCloudDatalabelingV1beta1PolylineConfig**](GoogleCloudDatalabelingV1beta1PolylineConfig.md) |  | [optional] 
**segmentationConfig** | [**GoogleCloudDatalabelingV1beta1SegmentationConfig**](GoogleCloudDatalabelingV1beta1SegmentationConfig.md) |  | [optional] 



## Enum: FeatureEnum


* `FEATURE_UNSPECIFIED` (value: `"FEATURE_UNSPECIFIED"`)

* `CLASSIFICATION` (value: `"CLASSIFICATION"`)

* `BOUNDING_BOX` (value: `"BOUNDING_BOX"`)

* `ORIENTED_BOUNDING_BOX` (value: `"ORIENTED_BOUNDING_BOX"`)

* `BOUNDING_POLY` (value: `"BOUNDING_POLY"`)

* `POLYLINE` (value: `"POLYLINE"`)

* `SEGMENTATION` (value: `"SEGMENTATION"`)




