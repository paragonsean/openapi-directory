

# BareMetalParallelUpgradeConfig

BareMetalParallelUpgradeConfig defines the parallel upgrade settings for worker node pools.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**concurrentNodes** | **Integer** | The maximum number of nodes that can be upgraded at once. |  [optional] |
|**minimumAvailableNodes** | **Integer** | The minimum number of nodes that should be healthy and available during an upgrade. If set to the default value of 0, it is possible that none of the nodes will be available during an upgrade. |  [optional] |



