

# EnvVar

Environment variable model definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The environment variable key, like ALGOLIA_ID (case-sensitive) |  [optional] |
|**scopes** | [**List&lt;ScopesEnum&gt;**](#List&lt;ScopesEnum&gt;) | The scopes that this environment variable is set to |  [optional] |
|**updatedAt** | **OffsetDateTime** | The timestamp of when the value was last updated |  [optional] |
|**updatedBy** | [**EnvVarUser**](EnvVarUser.md) |  |  [optional] |
|**values** | [**List&lt;EnvVarValue&gt;**](EnvVarValue.md) | An array of Value objects containing values and metadata |  [optional] |



## Enum: List&lt;ScopesEnum&gt;

| Name | Value |
|---- | -----|
| BUILDS | &quot;builds&quot; |
| FUNCTIONS | &quot;functions&quot; |
| RUNTIME | &quot;runtime&quot; |
| POST_PROCESSING | &quot;post-processing&quot; |



