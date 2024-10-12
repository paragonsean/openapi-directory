# DataLabelingApi.GoogleCloudDatalabelingV1beta1AnnotationSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. User-provided description of the annotation specification. The description can be up to 10,000 characters long. | [optional] 
**displayName** | **String** | Required. The display name of the AnnotationSpec. Maximum of 64 characters. | [optional] 
**index** | **Number** | Output only. This is the integer index of the AnnotationSpec. The index for the whole AnnotationSpecSet is sequential starting from 0. For example, an AnnotationSpecSet with classes &#x60;dog&#x60; and &#x60;cat&#x60;, might contain one AnnotationSpec with &#x60;{ display_name: \&quot;dog\&quot;, index: 0 }&#x60; and one AnnotationSpec with &#x60;{ display_name: \&quot;cat\&quot;, index: 1 }&#x60;. This is especially useful for model training as it encodes the string labels into numeric values. | [optional] 


