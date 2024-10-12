# OsConfigApi.OSPolicyResourceFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowInsecure** | **Boolean** | Defaults to false. When false, files are subject to validations based on the file type: Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified. | [optional] 
**gcs** | [**OSPolicyResourceFileGcs**](OSPolicyResourceFileGcs.md) |  | [optional] 
**localPath** | **String** | A local path within the VM to use. | [optional] 
**remote** | [**OSPolicyResourceFileRemote**](OSPolicyResourceFileRemote.md) |  | [optional] 


