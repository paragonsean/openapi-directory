# VertexAiApi.GoogleCloudAiplatformV1Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **String** | Required. The relative resource name of the Artifact in the Event. | [optional] 
**eventTime** | **String** | Output only. Time the Event occurred. | [optional] [readonly] 
**execution** | **String** | Output only. The relative resource name of the Execution in the Event. | [optional] [readonly] 
**labels** | **{String: String}** | The labels with user-defined metadata to annotate Events. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Event (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. | [optional] 
**type** | **String** | Required. The type of the Event. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `INPUT` (value: `"INPUT"`)

* `OUTPUT` (value: `"OUTPUT"`)




