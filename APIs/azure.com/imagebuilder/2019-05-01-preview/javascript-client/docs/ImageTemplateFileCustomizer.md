# VirtualMachineImageTemplate.ImageTemplateFileCustomizer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **String** | The absolute path to a file (with nested directory structures already created) where the file (from sourceUri) will be uploaded to in the VM | [optional] 
**sha256Checksum** | **String** | SHA256 checksum of the file provided in the sourceUri field above | [optional] 
**sourceUri** | **String** | The URI of the file to be uploaded for customizing the VM. It can be a github link, SAS URI for Azure Storage, etc | [optional] 


