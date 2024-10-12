# GkeHubApi.ClusterUpgradeScopeState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downstreamScopes** | **[String]** | This scopes whose upstream_scopes contain the current scope. The scope name should be in the form: &#x60;projects/{p}/locations/gloobal/scopes/{s}&#x60; Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature&#39;s project. | [optional] 
**gkeState** | [**ClusterUpgradeGKEUpgradeFeatureState**](ClusterUpgradeGKEUpgradeFeatureState.md) |  | [optional] 
**ignored** | [**{String: ClusterUpgradeIgnoredMembership}**](ClusterUpgradeIgnoredMembership.md) | A list of memberships ignored by the feature. For example, manually upgraded clusters can be ignored if they are newer than the default versions of its release channel. The membership resource is in the format: &#x60;projects/{p}/locations/{l}/membership/{m}&#x60;. | [optional] 


