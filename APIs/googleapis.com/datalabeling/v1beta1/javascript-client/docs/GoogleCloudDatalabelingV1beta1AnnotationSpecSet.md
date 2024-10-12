# DataLabelingApi.GoogleCloudDatalabelingV1beta1AnnotationSpecSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSpecs** | [**[GoogleCloudDatalabelingV1beta1AnnotationSpec]**](GoogleCloudDatalabelingV1beta1AnnotationSpec.md) | Required. The array of AnnotationSpecs that you define when you create the AnnotationSpecSet. These are the possible labels for the labeling task. | [optional] 
**blockingResources** | **[String]** | Output only. The names of any related resources that are blocking changes to the annotation spec set. | [optional] 
**description** | **String** | Optional. User-provided description of the annotation specification set. The description can be up to 10,000 characters long. | [optional] 
**displayName** | **String** | Required. The display name for AnnotationSpecSet that you define when you create it. Maximum of 64 characters. | [optional] 
**name** | **String** | Output only. The AnnotationSpecSet resource name in the following format: \&quot;projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}\&quot; | [optional] 


