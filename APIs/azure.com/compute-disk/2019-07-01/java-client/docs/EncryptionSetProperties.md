

# EncryptionSetProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeKey** | [**KeyVaultAndKeyReference**](KeyVaultAndKeyReference.md) |  |  [optional] |
|**previousKeys** | [**List&lt;KeyVaultAndKeyReference&gt;**](KeyVaultAndKeyReference.md) | A readonly collection of key vault keys previously used by this disk encryption set while a key rotation is in progress. It will be empty if there is no ongoing key rotation. |  [optional] [readonly] |
|**provisioningState** | **String** | The disk encryption set provisioning state. |  [optional] [readonly] |



