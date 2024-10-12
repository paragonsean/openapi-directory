

# CseIdentity

The client-side encryption (CSE) configuration for the email address of an authenticated user. Gmail uses CSE configurations to save drafts of client-side encrypted email messages, and to sign and send encrypted email messages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | The email address for the sending identity. The email address must be the primary email address of the authenticated user. |  [optional] |
|**primaryKeyPairId** | **String** | If a key pair is associated, the ID of the key pair, CseKeyPair. |  [optional] |
|**signAndEncryptKeyPairs** | [**SignAndEncryptKeyPairs**](SignAndEncryptKeyPairs.md) |  |  [optional] |



