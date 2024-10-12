# KubernetesEngineApi.DatabaseEncryption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyName** | **String** | Name of CloudKMS key to use for the encryption of secrets in etcd. Ex. projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key | [optional] 
**state** | **String** | The desired state of etcd encryption. | [optional] 



## Enum: StateEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENCRYPTED` (value: `"ENCRYPTED"`)

* `DECRYPTED` (value: `"DECRYPTED"`)




