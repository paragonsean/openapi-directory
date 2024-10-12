

# ApplicationGatewaySslCertificatePropertiesFormat

Properties of SSL certificates of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **String** | Base-64 encoded pfx certificate. Only applicable in PUT Request. |  [optional] |
|**keyVaultSecretId** | **String** | Secret Id of (base-64 encoded unencrypted pfx) &#39;Secret&#39; or &#39;Certificate&#39; object stored in KeyVault. |  [optional] |
|**password** | **String** | Password for the pfx file specified in data. Only applicable in PUT request. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**publicCertData** | **String** | Base-64 encoded Public cert data corresponding to pfx specified in data. Only applicable in GET request. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



