# AutomationManagement.SourceControlCreateOrUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoSync** | **Boolean** | The auto async of the source control. Default is false. | [optional] 
**branch** | **String** | The repo branch of the source control. Include branch as empty string for VsoTfvc. | [optional] 
**description** | **String** | The user description of the source control. | [optional] 
**folderPath** | **String** | The folder path of the source control. Path must be relative. | [optional] 
**publishRunbook** | **Boolean** | The auto publish of the source control. Default is true. | [optional] 
**repoUrl** | **String** | The repo url of the source control. | [optional] 
**securityToken** | [**SourceControlSecurityTokenProperties**](SourceControlSecurityTokenProperties.md) |  | [optional] 
**sourceType** | **String** | The source type. Must be one of VsoGit, VsoTfvc, GitHub, case sensitive. | [optional] 



## Enum: SourceTypeEnum


* `VsoGit` (value: `"VsoGit"`)

* `VsoTfvc` (value: `"VsoTfvc"`)

* `GitHub` (value: `"GitHub"`)




