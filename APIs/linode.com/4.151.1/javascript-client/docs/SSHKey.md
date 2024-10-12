# LinodeApi.SSHKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | The date this key was added.  | [optional] [readonly] 
**id** | **Number** | The unique identifier of an SSH Key object.  | [optional] [readonly] 
**label** | **String** | A label for the SSH Key.  | [optional] 
**sshKey** | **String** | The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.  Accepted formats: * ssh-dss * ssh-rsa * ecdsa-sha2-nistp * ssh-ed25519 * sk-ecdsa-sha2-nistp256 (Akamai-specific)  | [optional] 


