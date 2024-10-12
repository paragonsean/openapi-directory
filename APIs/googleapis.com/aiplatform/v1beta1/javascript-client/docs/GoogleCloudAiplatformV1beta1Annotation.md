# VertexAiApi.GoogleCloudAiplatformV1beta1Annotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSource** | [**GoogleCloudAiplatformV1beta1UserActionReference**](GoogleCloudAiplatformV1beta1UserActionReference.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp when this Annotation was created. | [optional] [readonly] 
**etag** | **String** | Optional. Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | Optional. The labels with user-defined metadata to organize your Annotations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Annotation(System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. Following system labels exist for each Annotation: * \&quot;aiplatform.googleapis.com/annotation_set_name\&quot;: optional, name of the UI&#39;s annotation set this Annotation belongs to. If not set, the Annotation is not visible in the UI. * \&quot;aiplatform.googleapis.com/payload_schema\&quot;: output only, its value is the payload_schema&#39;s title. | [optional] 
**name** | **String** | Output only. Resource name of the Annotation. | [optional] [readonly] 
**payload** | **Object** | Required. The schema of the payload can be found in payload_schema. | [optional] 
**payloadSchemaUri** | **String** | Required. Google Cloud Storage URI points to a YAML file describing payload. The schema is defined as an [OpenAPI 3.0.2 Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/, note that the chosen schema must be consistent with the parent Dataset&#39;s metadata. | [optional] 
**updateTime** | **String** | Output only. Timestamp when this Annotation was last updated. | [optional] [readonly] 


