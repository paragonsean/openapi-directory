

# BranchConfiguration

The branch build configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactVersioning** | [**BranchConfigurationsGet200ResponseAllOfArtifactVersioning**](BranchConfigurationsGet200ResponseAllOfArtifactVersioning.md) |  |  [optional] |
|**badgeIsEnabled** | **Boolean** |  |  [optional] |
|**cloneFromBranch** | **String** | A configured branch name to clone from. If provided, all other parameters will be ignored. Only supported in POST requests. |  [optional] |
|**signed** | **Boolean** |  |  [optional] |
|**testsEnabled** | **Boolean** |  |  [optional] |
|**toolsets** | [**BranchConfigurationsGet200ResponseAllOfToolsets**](BranchConfigurationsGet200ResponseAllOfToolsets.md) |  |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) |  |  [optional] |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| CONTINOUS | &quot;continous&quot; |
| CONTINUOUS | &quot;continuous&quot; |
| MANUAL | &quot;manual&quot; |



