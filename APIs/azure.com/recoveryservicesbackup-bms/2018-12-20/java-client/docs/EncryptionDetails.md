

# EncryptionDetails

Details needed if the VM was encrypted at the time of backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionEnabled** | **Boolean** | Identifies whether this backup copy represents an encrypted VM at the time of backup. |  [optional] |
|**kekUrl** | **String** | Key Url. |  [optional] |
|**kekVaultId** | **String** | ID of Key Vault where KEK is stored. |  [optional] |
|**secretKeyUrl** | **String** | Secret Url. |  [optional] |
|**secretKeyVaultId** | **String** | ID of Key Vault where Secret is stored. |  [optional] |



