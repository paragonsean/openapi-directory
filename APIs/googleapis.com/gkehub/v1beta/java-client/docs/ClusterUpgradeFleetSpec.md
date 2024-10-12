

# ClusterUpgradeFleetSpec

**ClusterUpgrade**: The configuration for the fleet-level ClusterUpgrade feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gkeUpgradeOverrides** | [**List&lt;ClusterUpgradeGKEUpgradeOverride&gt;**](ClusterUpgradeGKEUpgradeOverride.md) | Allow users to override some properties of each GKE upgrade. |  [optional] |
|**postConditions** | [**ClusterUpgradePostConditions**](ClusterUpgradePostConditions.md) |  |  [optional] |
|**upstreamFleets** | **List&lt;String&gt;** | This fleet consumes upgrades that have COMPLETE status code in the upstream fleets. See UpgradeStatus.Code for code definitions. The fleet name should be either fleet project number or id. This is defined as repeated for future proof reasons. Initial implementation will enforce at most one upstream fleet. |  [optional] |



