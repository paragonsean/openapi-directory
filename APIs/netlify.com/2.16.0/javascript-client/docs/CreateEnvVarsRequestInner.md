# NetlifysApiDocumentation.CreateEnvVarsRequestInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | The existing or new name of the key, if you wish to rename it (case-sensitive) | [optional] 
**scopes** | **[String]** | The scopes that this environment variable is set to (Pro plans and above) | [optional] 
**values** | [**[EnvVarValue]**](EnvVarValue.md) |  | [optional] 



## Enum: [ScopesEnum]


* `builds` (value: `"builds"`)

* `functions` (value: `"functions"`)

* `runtime` (value: `"runtime"`)

* `post-processing` (value: `"post-processing"`)




