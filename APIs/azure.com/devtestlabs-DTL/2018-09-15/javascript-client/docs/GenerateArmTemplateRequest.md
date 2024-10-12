# DevTestLabsClient.GenerateArmTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileUploadOptions** | **String** | Options for uploading the files for the artifact. UploadFilesAndGenerateSasTokens is the default value. | [optional] 
**location** | **String** | The location of the virtual machine. | [optional] 
**parameters** | [**[ParameterInfo]**](ParameterInfo.md) | The parameters of the ARM template. | [optional] 
**virtualMachineName** | **String** | The resource name of the virtual machine. | [optional] 



## Enum: FileUploadOptionsEnum


* `UploadFilesAndGenerateSasTokens` (value: `"UploadFilesAndGenerateSasTokens"`)

* `None` (value: `"None"`)




