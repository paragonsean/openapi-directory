

# GoogleCloudAiplatformV1Artifact

Instance of a general artifact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when this Artifact was created. |  [optional] [readonly] |
|**description** | **String** | Description of the Artifact |  [optional] |
|**displayName** | **String** | User provided display name of the Artifact. May be up to 128 Unicode characters. |  [optional] |
|**etag** | **String** | An eTag used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize your Artifacts. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Artifact (System labels are excluded). |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Properties of the Artifact. Top level metadata keys&#39; heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |  [optional] |
|**name** | **String** | Output only. The resource name of the Artifact. |  [optional] [readonly] |
|**schemaTitle** | **String** | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |  [optional] |
|**schemaVersion** | **String** | The version of the schema in schema_name to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of this Artifact. This is a property of the Artifact, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines), and the system does not prescribe or check the validity of state transitions. |  [optional] |
|**updateTime** | **String** | Output only. Timestamp when this Artifact was last updated. |  [optional] [readonly] |
|**uri** | **String** | The uniform resource identifier of the artifact file. May be empty if there is no actual artifact file. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| LIVE | &quot;LIVE&quot; |



