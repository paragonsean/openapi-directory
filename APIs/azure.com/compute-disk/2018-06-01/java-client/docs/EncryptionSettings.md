

# EncryptionSettings

Encryption settings for disk or snapshot

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskEncryptionKey** | [**KeyVaultAndSecretReference**](KeyVaultAndSecretReference.md) |  |  [optional] |
|**enabled** | **Boolean** | Set this flag to true and provide DiskEncryptionKey and optional KeyEncryptionKey to enable encryption. Set this flag to false and remove DiskEncryptionKey and KeyEncryptionKey to disable encryption. If EncryptionSettings is null in the request object, the existing settings remain unchanged. |  [optional] |
|**keyEncryptionKey** | [**KeyVaultAndKeyReference**](KeyVaultAndKeyReference.md) |  |  [optional] |



