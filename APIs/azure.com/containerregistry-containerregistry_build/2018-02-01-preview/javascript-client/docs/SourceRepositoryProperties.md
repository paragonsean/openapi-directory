# ContainerRegistryManagementClient.SourceRepositoryProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isCommitTriggerEnabled** | **Boolean** | The value of this property indicates whether the source control commit trigger is enabled or not. | [optional] [default to false]
**repositoryUrl** | **String** | The full URL to the source code repository | 
**sourceControlAuthProperties** | [**SourceControlAuthInfo**](SourceControlAuthInfo.md) |  | [optional] 
**sourceControlType** | **String** | The type of source control service. | 



## Enum: SourceControlTypeEnum


* `Github` (value: `"Github"`)

* `VisualStudioTeamService` (value: `"VisualStudioTeamService"`)




