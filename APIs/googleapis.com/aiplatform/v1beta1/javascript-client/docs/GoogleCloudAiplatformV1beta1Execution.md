# VertexAiApi.GoogleCloudAiplatformV1beta1Execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this Execution was created. | [optional] [readonly] 
**description** | **String** | Description of the Execution | [optional] 
**displayName** | **String** | User provided display name of the Execution. May be up to 128 Unicode characters. | [optional] 
**etag** | **String** | An eTag used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize your Executions. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Execution (System labels are excluded). | [optional] 
**metadata** | **{String: Object}** | Properties of the Execution. Top level metadata keys&#39; heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. | [optional] 
**name** | **String** | Output only. The resource name of the Execution. | [optional] [readonly] 
**schemaTitle** | **String** | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. | [optional] 
**schemaVersion** | **String** | The version of the schema in &#x60;schema_title&#x60; to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. | [optional] 
**state** | **String** | The state of this Execution. This is a property of the Execution, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines) and the system does not prescribe or check the validity of state transitions. | [optional] 
**updateTime** | **String** | Output only. Timestamp when this Execution was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NEW` (value: `"NEW"`)

* `RUNNING` (value: `"RUNNING"`)

* `COMPLETE` (value: `"COMPLETE"`)

* `FAILED` (value: `"FAILED"`)

* `CACHED` (value: `"CACHED"`)

* `CANCELLED` (value: `"CANCELLED"`)




