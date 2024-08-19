# AppVeyorRestApi.DeploymentEnvironmentWithSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploymentEnvironmentId** | **Number** |  | [optional] 
**name** | **String** |  | [optional] 
**provider** | [**DeploymentProviderType**](DeploymentProviderType.md) |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**updated** | **Date** |  | [optional] [readonly] 
**accountId** | **Number** |  | [optional] 
**projectsMode** | [**DeploymentProjectSelectionMode**](DeploymentProjectSelectionMode.md) |  | [optional] 
**securityDescriptor** | [**SecurityDescriptor**](SecurityDescriptor.md) |  | [optional] 
**tags** | **String** | Comma-separated list of environment tags for dynamic grouping. Appears that any input is accepted.  The returned value only contains case-preserving but insensitive unique values where spaces around \&quot;,\&quot; are removed but otherwise preserved.  Empty values and items are allowed. | [optional] 
**environmentAccessKey** | **String** |  | [optional] 
**projects** | [**[DeploymentEnvironmentProject]**](DeploymentEnvironmentProject.md) | Projects available for selection in UI. Only present in response from getEnvironmentSettings.  | [optional] 
**selectedProjects** | **[Number]** | Project IDs of selected projects | [optional] 
**settings** | [**DeploymentEnvironmentSettings**](DeploymentEnvironmentSettings.md) |  | [optional] 


