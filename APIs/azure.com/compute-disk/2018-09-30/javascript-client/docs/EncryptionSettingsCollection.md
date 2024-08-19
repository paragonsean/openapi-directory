# DiskResourceProviderClient.EncryptionSettingsCollection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Set this flag to true and provide DiskEncryptionKey and optional KeyEncryptionKey to enable encryption. Set this flag to false and remove DiskEncryptionKey and KeyEncryptionKey to disable encryption. If EncryptionSettings is null in the request object, the existing settings remain unchanged. | 
**encryptionSettings** | [**[EncryptionSettingsElement]**](EncryptionSettingsElement.md) | A collection of encryption settings, one for each disk volume. | [optional] 


