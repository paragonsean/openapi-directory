

# ComputeNodeUser


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiryTime** | **OffsetDateTime** | If omitted, the default is 1 day from the current time. For Linux Compute Nodes, the expiryTime has a precision up to a day. |  [optional] |
|**isAdmin** | **Boolean** | The default value is false. |  [optional] |
|**name** | **String** |  |  |
|**password** | **String** | The password is required for Windows Compute Nodes (those created with &#39;cloudServiceConfiguration&#39;, or created with &#39;virtualMachineConfiguration&#39; using a Windows Image reference). For Linux Compute Nodes, the password can optionally be specified along with the sshPublicKey property. |  [optional] |
|**sshPublicKey** | **String** | The public key should be compatible with OpenSSH encoding and should be base 64 encoded. This property can be specified only for Linux Compute Nodes. If this is specified for a Windows Compute Node, then the Batch service rejects the request; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |



