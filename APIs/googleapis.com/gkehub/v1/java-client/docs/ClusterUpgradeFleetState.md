

# ClusterUpgradeFleetState

**ClusterUpgrade**: The state for the fleet-level ClusterUpgrade feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downstreamFleets** | **List&lt;String&gt;** | This fleets whose upstream_fleets contain the current fleet. The fleet name should be either fleet project number or id. |  [optional] |
|**gkeState** | [**ClusterUpgradeGKEUpgradeFeatureState**](ClusterUpgradeGKEUpgradeFeatureState.md) |  |  [optional] |
|**ignored** | [**Map&lt;String, ClusterUpgradeIgnoredMembership&gt;**](ClusterUpgradeIgnoredMembership.md) | A list of memberships ignored by the feature. For example, manually upgraded clusters can be ignored if they are newer than the default versions of its release channel. The membership resource is in the format: &#x60;projects/{p}/locations/{l}/membership/{m}&#x60;. |  [optional] |



