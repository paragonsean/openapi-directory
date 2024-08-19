

# SearchServiceProperties

Defines properties of an Azure Search service that can be modified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**partitionCount** | **Integer** | The number of partitions in the Search service; if specified, it can be 1, 2, 3, 4, 6, or 12. |  [optional] |
|**replicaCount** | **Integer** | The number of replicas in the Search service. If specified, it must be a value between 1 and 6 inclusive. |  [optional] |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |



