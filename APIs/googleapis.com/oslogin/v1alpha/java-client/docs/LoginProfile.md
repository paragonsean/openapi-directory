

# LoginProfile

The user profile information used for logging in to a virtual machine on Google Compute Engine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. A unique user ID. |  [optional] |
|**posixAccounts** | [**List&lt;PosixAccount&gt;**](PosixAccount.md) | The list of POSIX accounts associated with the user. |  [optional] |
|**securityKeys** | [**List&lt;SecurityKey&gt;**](SecurityKey.md) | The registered security key credentials for a user. |  [optional] |
|**sshPublicKeys** | [**Map&lt;String, SshPublicKey&gt;**](SshPublicKey.md) | A map from SSH public key fingerprint to the associated key object. |  [optional] |



