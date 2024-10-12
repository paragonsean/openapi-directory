# CloudComposerApi.Environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**EnvironmentConfig**](EnvironmentConfig.md) |  | [optional] 
**createTime** | **String** | Output only. The time at which this environment was created. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \\p{Ll}\\p{Lo}{0,62} * Values must conform to regexp: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} * Both keys and values are additionally constrained to be &lt;&#x3D; 128 bytes in size. | [optional] 
**name** | **String** | The resource name of the environment, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot; EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. | [optional] 
**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**state** | **String** | The current state of the environment. | [optional] 
**storageConfig** | [**StorageConfig**](StorageConfig.md) |  | [optional] 
**updateTime** | **String** | Output only. The time at which this environment was last modified. | [optional] [readonly] 
**uuid** | **String** | Output only. The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `RUNNING` (value: `"RUNNING"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `ERROR` (value: `"ERROR"`)




