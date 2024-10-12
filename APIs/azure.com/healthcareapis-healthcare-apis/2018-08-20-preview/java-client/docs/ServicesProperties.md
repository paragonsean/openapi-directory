

# ServicesProperties

The properties of a service instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPolicies** | [**List&lt;ServiceAccessPolicyEntry&gt;**](ServiceAccessPolicyEntry.md) | The access policies of the service instance. |  |
|**authenticationConfiguration** | [**ServiceAuthenticationConfigurationInfo**](ServiceAuthenticationConfigurationInfo.md) |  |  [optional] |
|**corsConfiguration** | [**ServiceCorsConfigurationInfo**](ServiceCorsConfigurationInfo.md) |  |  [optional] |
|**cosmosDbConfiguration** | [**ServiceCosmosDbConfigurationInfo**](ServiceCosmosDbConfigurationInfo.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| ACCEPTED | &quot;Accepted&quot; |
| VERIFYING | &quot;Verifying&quot; |
| UPDATING | &quot;Updating&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| DEPROVISIONED | &quot;Deprovisioned&quot; |



