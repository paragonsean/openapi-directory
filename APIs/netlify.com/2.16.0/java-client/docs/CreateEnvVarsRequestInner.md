

# CreateEnvVarsRequestInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The existing or new name of the key, if you wish to rename it (case-sensitive) |  [optional] |
|**scopes** | [**List&lt;ScopesEnum&gt;**](#List&lt;ScopesEnum&gt;) | The scopes that this environment variable is set to (Pro plans and above) |  [optional] |
|**values** | [**List&lt;EnvVarValue&gt;**](EnvVarValue.md) |  |  [optional] |



## Enum: List&lt;ScopesEnum&gt;

| Name | Value |
|---- | -----|
| BUILDS | &quot;builds&quot; |
| FUNCTIONS | &quot;functions&quot; |
| RUNTIME | &quot;runtime&quot; |
| POST_PROCESSING | &quot;post-processing&quot; |



