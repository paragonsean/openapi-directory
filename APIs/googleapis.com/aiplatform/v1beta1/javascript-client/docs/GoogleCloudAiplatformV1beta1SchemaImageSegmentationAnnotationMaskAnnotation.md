# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationMaskAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSpecColors** | [**[GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor]**](GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor.md) | The mapping between color and AnnotationSpec for this Annotation. | [optional] 
**maskGcsUri** | **String** | Google Cloud Storage URI that points to the mask image. The image must be in PNG format. It must have the same size as the DataItem&#39;s image. Each pixel in the image mask represents the AnnotationSpec which the pixel in the image DataItem belong to. Each color is mapped to one AnnotationSpec based on annotation_spec_colors. | [optional] 


