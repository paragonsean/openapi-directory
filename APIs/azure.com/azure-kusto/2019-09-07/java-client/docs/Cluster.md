

# Cluster

Class representing a Kusto cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identity** | [**Identity**](Identity.md) |  |  [optional] |
|**properties** | [**ClusterProperties**](ClusterProperties.md) |  |  [optional] |
|**sku** | [**AzureSku**](AzureSku.md) |  |  |
|**zones** | **List&lt;String&gt;** | An array represents the availability zones of the cluster. |  [optional] |
|**location** | **String** | The geo-location where the resource lives |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags. |  [optional] |
|**id** | **String** | Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |  [optional] [readonly] |
|**name** | **String** | The name of the resource |  [optional] [readonly] |
|**type** | **String** | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |  [optional] [readonly] |



