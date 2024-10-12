

# ClusterUpgradeMembershipState

Per-membership state for this feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignored** | [**ClusterUpgradeIgnoredMembership**](ClusterUpgradeIgnoredMembership.md) |  |  [optional] |
|**scopes** | **List&lt;String&gt;** | Fully qualified scope names that this clusters is bound to which also have rollout sequencing enabled. |  [optional] |
|**upgrades** | [**List&lt;ClusterUpgradeMembershipGKEUpgradeState&gt;**](ClusterUpgradeMembershipGKEUpgradeState.md) | Actual upgrade state against desired. |  [optional] |



