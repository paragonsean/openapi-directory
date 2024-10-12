# VertexAiApi.GoogleCloudAiplatformV1Context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this Context was created. | [optional] [readonly] 
**description** | **String** | Description of the Context | [optional] 
**displayName** | **String** | User provided display name of the Context. May be up to 128 Unicode characters. | [optional] 
**etag** | **String** | An eTag used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize your Contexts. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Context (System labels are excluded). | [optional] 
**metadata** | **{String: Object}** | Properties of the Context. Top level metadata keys&#39; heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. | [optional] 
**name** | **String** | Immutable. The resource name of the Context. | [optional] 
**parentContexts** | **[String]** | Output only. A list of resource names of Contexts that are parents of this Context. A Context may have at most 10 parent_contexts. | [optional] [readonly] 
**schemaTitle** | **String** | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. | [optional] 
**schemaVersion** | **String** | The version of the schema in schema_name to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. | [optional] 
**updateTime** | **String** | Output only. Timestamp when this Context was last updated. | [optional] [readonly] 


