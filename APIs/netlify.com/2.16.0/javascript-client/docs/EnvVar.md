# NetlifysApiDocumentation.EnvVar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | The environment variable key, like ALGOLIA_ID (case-sensitive) | [optional] 
**scopes** | **[String]** | The scopes that this environment variable is set to | [optional] 
**updatedAt** | **Date** | The timestamp of when the value was last updated | [optional] 
**updatedBy** | [**EnvVarUser**](EnvVarUser.md) |  | [optional] 
**values** | [**[EnvVarValue]**](EnvVarValue.md) | An array of Value objects containing values and metadata | [optional] 



## Enum: [ScopesEnum]


* `builds` (value: `"builds"`)

* `functions` (value: `"functions"`)

* `runtime` (value: `"runtime"`)

* `post-processing` (value: `"post-processing"`)




