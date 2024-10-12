

# ClusterUpgradeScopeState

**ClusterUpgrade**: The state for the scope-level ClusterUpgrade feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downstreamScopes** | **List&lt;String&gt;** | This scopes whose upstream_scopes contain the current scope. The scope name should be in the form: &#x60;projects/{p}/locations/gloobal/scopes/{s}&#x60; Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature&#39;s project. |  [optional] |
|**gkeState** | [**ClusterUpgradeGKEUpgradeFeatureState**](ClusterUpgradeGKEUpgradeFeatureState.md) |  |  [optional] |
|**ignored** | [**Map&lt;String, ClusterUpgradeIgnoredMembership&gt;**](ClusterUpgradeIgnoredMembership.md) | A list of memberships ignored by the feature. For example, manually upgraded clusters can be ignored if they are newer than the default versions of its release channel. The membership resource is in the format: &#x60;projects/{p}/locations/{l}/membership/{m}&#x60;. |  [optional] |



