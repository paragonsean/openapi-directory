

# KeyAndSecretDetails

BEK is bitlocker key.  KEK is encryption key for BEK  If the VM was encrypted then we will store following details :  1. Secret(BEK) - Url + Backup Data + vaultId.  2. Key(KEK) - Url + Backup Data + vaultId.  3. EncryptionMechanism  BEK and KEK can potentially have different vault ids.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bekDetails** | [**BEKDetails**](BEKDetails.md) |  |  [optional] |
|**encryptionMechanism** | **String** | Encryption mechanism: None/ SinglePass/ DoublePass |  [optional] |
|**kekDetails** | [**KEKDetails**](KEKDetails.md) |  |  [optional] |



