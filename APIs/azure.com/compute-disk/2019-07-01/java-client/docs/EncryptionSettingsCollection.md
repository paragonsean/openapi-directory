

# EncryptionSettingsCollection

Encryption settings for disk or snapshot

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Set this flag to true and provide DiskEncryptionKey and optional KeyEncryptionKey to enable encryption. Set this flag to false and remove DiskEncryptionKey and KeyEncryptionKey to disable encryption. If EncryptionSettings is null in the request object, the existing settings remain unchanged. |  |
|**encryptionSettings** | [**List&lt;EncryptionSettingsElement&gt;**](EncryptionSettingsElement.md) | A collection of encryption settings, one for each disk volume. |  [optional] |
|**encryptionSettingsVersion** | **String** | Describes what type of encryption is used for the disks. Once this field is set, it cannot be overwritten. &#39;1.0&#39; corresponds to Azure Disk Encryption with AAD app.&#39;1.1&#39; corresponds to Azure Disk Encryption. |  [optional] |



