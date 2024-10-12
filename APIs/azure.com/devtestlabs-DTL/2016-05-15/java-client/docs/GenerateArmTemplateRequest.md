

# GenerateArmTemplateRequest

Parameters for generating an ARM template for deploying artifacts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileUploadOptions** | [**FileUploadOptionsEnum**](#FileUploadOptionsEnum) | Options for uploading the files for the artifact. UploadFilesAndGenerateSasTokens is the default value. |  [optional] |
|**location** | **String** | The location of the virtual machine. |  [optional] |
|**parameters** | [**List&lt;ParameterInfo&gt;**](ParameterInfo.md) | The parameters of the ARM template. |  [optional] |
|**virtualMachineName** | **String** | The resource name of the virtual machine. |  [optional] |



## Enum: FileUploadOptionsEnum

| Name | Value |
|---- | -----|
| UPLOAD_FILES_AND_GENERATE_SAS_TOKENS | &quot;UploadFilesAndGenerateSasTokens&quot; |
| NONE | &quot;None&quot; |



