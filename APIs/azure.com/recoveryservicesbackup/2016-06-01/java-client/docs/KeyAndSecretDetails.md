

# KeyAndSecretDetails

BEK stands for Bitlocker Encryption Key.   KEK stands for Key Encryption Key. KEK is the encryption key used to protect the Secret for the BEK    If the VM is encrypted, then the service stores the following details :    1. Secret(BEK) - Url + Backup Data + vaultID.              2. Key(KEK) - Url + Backup Data + vaultID.     It is possible for the BEK and KEK to have different vaultIDs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bekDetails** | [**BEKDetails**](BEKDetails.md) |  |  [optional] |
|**kekDetails** | [**KEKDetails**](KEKDetails.md) |  |  [optional] |



