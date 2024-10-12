# AppCenterClient.BranchConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactVersioning** | [**BranchConfigurationsGet200ResponseAllOfArtifactVersioning**](BranchConfigurationsGet200ResponseAllOfArtifactVersioning.md) |  | [optional] 
**badgeIsEnabled** | **Boolean** |  | [optional] 
**cloneFromBranch** | **String** | A configured branch name to clone from. If provided, all other parameters will be ignored. Only supported in POST requests. | [optional] 
**signed** | **Boolean** |  | [optional] 
**testsEnabled** | **Boolean** |  | [optional] 
**toolsets** | [**BranchConfigurationsGet200ResponseAllOfToolsets**](BranchConfigurationsGet200ResponseAllOfToolsets.md) |  | [optional] 
**trigger** | **String** |  | [optional] 



## Enum: TriggerEnum


* `continous` (value: `"continous"`)

* `continuous` (value: `"continuous"`)

* `manual` (value: `"manual"`)




