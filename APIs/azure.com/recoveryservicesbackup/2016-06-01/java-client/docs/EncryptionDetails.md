

# EncryptionDetails

Details needed if the VM was encrypted at the time of backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionEnabled** | **Boolean** | Identifies whether the backup copy represents an encrypted VM at the time of backup. |  [optional] |
|**kekUrl** | **String** | URL of the Key Encryption Key (KEK). |  [optional] |
|**kekVaultId** | **String** | The ID of Key Vault where the Key Encryption Key (KEK) is stored. |  [optional] |
|**secretKeyUrl** | **String** | URL of the Bitlocker Encryption Key (BEK). |  [optional] |
|**secretKeyVaultId** | **String** | The ID of Key Vault where the Bitlocker Encryption Key (BEK), or Secret, is stored. |  [optional] |



