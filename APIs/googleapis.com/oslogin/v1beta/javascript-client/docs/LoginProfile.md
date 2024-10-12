# CloudOsLoginApi.LoginProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Required. A unique user ID. | [optional] 
**posixAccounts** | [**[PosixAccount]**](PosixAccount.md) | The list of POSIX accounts associated with the user. | [optional] 
**securityKeys** | [**[SecurityKey]**](SecurityKey.md) | The registered security key credentials for a user. | [optional] 
**sshPublicKeys** | [**{String: SshPublicKey}**](SshPublicKey.md) | A map from SSH public key fingerprint to the associated key object. | [optional] 


