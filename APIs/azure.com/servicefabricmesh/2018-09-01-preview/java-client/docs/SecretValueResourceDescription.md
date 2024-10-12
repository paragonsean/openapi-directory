

# SecretValueResourceDescription

This type describes a value of a secret resource. The name of this resource is the version identifier corresponding to this secret value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**SecretValueResourceProperties**](SecretValueResourceProperties.md) |  |  |
|**location** | **String** | The geo-location where the resource lives |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags. |  [optional] |
|**id** | **String** | Fully qualified identifier for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |  [optional] [readonly] |
|**name** | **String** | The name of the resource |  [optional] [readonly] |
|**type** | **String** | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |  [optional] [readonly] |



