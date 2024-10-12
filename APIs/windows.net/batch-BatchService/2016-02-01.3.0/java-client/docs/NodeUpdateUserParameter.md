

# NodeUpdateUserParameter

Parameters for a ComputeNodeOperations.UpdateUser request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiryTime** | **OffsetDateTime** | The time at which the account should expire. If omitted, the default is 1 day from the current time. |  [optional] |
|**password** | **String** | The password of the account. |  [optional] |
|**sshPublicKey** | **String** | The SSH public key that can be used for remote login to the compute node. |  [optional] |



