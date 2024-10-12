

# DatabaseEncryption

Configuration of etcd encryption.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyName** | **String** | Name of CloudKMS key to use for the encryption of secrets in etcd. Ex. projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The desired state of etcd encryption. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENCRYPTED | &quot;ENCRYPTED&quot; |
| DECRYPTED | &quot;DECRYPTED&quot; |



