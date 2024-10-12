

# ComputeNodeUser

An user account on a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiryTime** | **OffsetDateTime** | The time at which the account should expire. If omitted, the default is 1 day from the current time. |  [optional] |
|**isAdmin** | **Boolean** | Whether the account should be an administrator on the compute node. |  [optional] |
|**name** | **String** | The user name of the account. |  |
|**password** | **String** | The password of the account. |  [optional] |
|**sshPublicKey** | **String** | The SSH public key that can be used for remote login to the compute node. |  [optional] |



