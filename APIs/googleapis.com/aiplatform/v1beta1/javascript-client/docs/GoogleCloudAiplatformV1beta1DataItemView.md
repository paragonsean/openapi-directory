# VertexAiApi.GoogleCloudAiplatformV1beta1DataItemView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**[GoogleCloudAiplatformV1beta1Annotation]**](GoogleCloudAiplatformV1beta1Annotation.md) | The Annotations on the DataItem. If too many Annotations should be returned for the DataItem, this field will be truncated per annotations_limit in request. If it was, then the has_truncated_annotations will be set to true. | [optional] 
**dataItem** | [**GoogleCloudAiplatformV1beta1DataItem**](GoogleCloudAiplatformV1beta1DataItem.md) |  | [optional] 
**hasTruncatedAnnotations** | **Boolean** | True if and only if the Annotations field has been truncated. It happens if more Annotations for this DataItem met the request&#39;s annotation_filter than are allowed to be returned by annotations_limit. Note that if Annotations field is not being returned due to field mask, then this field will not be set to true no matter how many Annotations are there. | [optional] 


