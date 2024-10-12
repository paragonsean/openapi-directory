

# SshPublicKey

Provides information about the public Secure Shell (SSH) key that is associated with a Transfer Family user for the specific file transfer protocol-enabled server (as identified by <code>ServerId</code>). The information returned includes the date the key was imported, the public key contents, and the public key ID. A user can store more than one SSH public key associated with their user name on a specific server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateImported** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**sshPublicKeyBody** | [**String**](String.md) |  |  |
|**sshPublicKeyId** | [**String**](String.md) |  |  |



