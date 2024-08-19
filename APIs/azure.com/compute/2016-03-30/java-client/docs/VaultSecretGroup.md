

# VaultSecretGroup

Describes a set of certificates which are all in the same Key Vault.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceVault** | [**SubResource**](SubResource.md) |  |  [optional] |
|**vaultCertificates** | [**List&lt;VaultCertificate&gt;**](VaultCertificate.md) | The list of key vault references in SourceVault which contain certificates. |  [optional] |



