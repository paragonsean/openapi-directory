

# DeploymentEnvironmentWithSettings


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
|**environmentAccessKey** | **String** |  |  [optional] |
|**projects** | [**List&lt;DeploymentEnvironmentProject&gt;**](DeploymentEnvironmentProject.md) | Projects available for selection in UI. Only present in response from getEnvironmentSettings.  |  [optional] |
|**selectedProjects** | **List&lt;Integer&gt;** | Project IDs of selected projects |  [optional] |
|**settings** | [**DeploymentEnvironmentSettings**](DeploymentEnvironmentSettings.md) |  |  [optional] |



