# CloudHealthcareApi.EvaluateAnnotationStoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryDestination** | [**GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination**](GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination.md) |  | [optional] 
**evalInfoTypeMapping** | **{String: String}** | Optional. InfoType mapping for &#x60;eval_store&#x60;. Different resources can map to the same infoType. For example, &#x60;PERSON_NAME&#x60;, &#x60;PERSON&#x60;, &#x60;NAME&#x60;, and &#x60;HUMAN&#x60; are different. To map all of these into a single infoType (such as &#x60;PERSON_NAME&#x60;), specify the following mapping: &#x60;&#x60;&#x60; info_type_mapping[\&quot;PERSON\&quot;] &#x3D; \&quot;PERSON_NAME\&quot; info_type_mapping[\&quot;NAME\&quot;] &#x3D; \&quot;PERSON_NAME\&quot; info_type_mapping[\&quot;HUMAN\&quot;] &#x3D; \&quot;PERSON_NAME\&quot; &#x60;&#x60;&#x60; Unmentioned infoTypes, such as &#x60;DATE&#x60;, are treated as identity mapping. For example: &#x60;&#x60;&#x60; info_type_mapping[\&quot;DATE\&quot;] &#x3D; \&quot;DATE\&quot; &#x60;&#x60;&#x60; InfoTypes are case-insensitive. | [optional] 
**goldenInfoTypeMapping** | **{String: String}** | Optional. Similar to &#x60;eval_info_type_mapping&#x60;, infoType mapping for &#x60;golden_store&#x60;. | [optional] 
**goldenStore** | **String** | Required. The Annotation store to use as ground truth, in the format of &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}&#x60;. | [optional] 
**infoTypeConfig** | [**InfoTypeConfig**](InfoTypeConfig.md) |  | [optional] 


