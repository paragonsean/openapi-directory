# DevTestLabsClient.ArtifactSourcePropertiesFragment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**armTemplateFolderPath** | **String** | The folder containing Azure Resource Manager templates. | [optional] 
**branchRef** | **String** | The artifact source&#39;s branch reference. | [optional] 
**displayName** | **String** | The artifact source&#39;s display name. | [optional] 
**folderPath** | **String** | The folder containing artifacts. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**securityToken** | **String** | The security token to authenticate to the artifact source. | [optional] 
**sourceType** | **String** | The artifact source&#39;s type. | [optional] 
**status** | **String** | Indicates if the artifact source is enabled (values: Enabled, Disabled). | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 
**uri** | **String** | The artifact source&#39;s URI. | [optional] 



## Enum: SourceTypeEnum


* `VsoGit` (value: `"VsoGit"`)

* `GitHub` (value: `"GitHub"`)





## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




