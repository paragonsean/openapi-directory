

# VolumeResourceDescription

This type describes a volume resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**VolumeResourceProperties**](VolumeResourceProperties.md) |  |  |
|**location** | **String** | The geo-location where the resource lives |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags. |  [optional] |
|**id** | **String** | Fully qualified identifier for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |  [optional] [readonly] |
|**name** | **String** | The name of the resource |  [optional] [readonly] |
|**type** | **String** | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |  [optional] [readonly] |



