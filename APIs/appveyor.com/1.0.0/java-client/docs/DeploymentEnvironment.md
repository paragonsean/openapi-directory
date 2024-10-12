

# DeploymentEnvironment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentEnvironmentId** | **Integer** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**provider** | **DeploymentProviderType** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**accountId** | **Integer** |  |  [optional] |
|**projectsMode** | **DeploymentProjectSelectionMode** |  |  [optional] |
|**securityDescriptor** | [**SecurityDescriptor**](SecurityDescriptor.md) |  |  [optional] |
|**tags** | **String** | Comma-separated list of environment tags for dynamic grouping. Appears that any input is accepted.  The returned value only contains case-preserving but insensitive unique values where spaces around \&quot;,\&quot; are removed but otherwise preserved.  Empty values and items are allowed. |  [optional] |



