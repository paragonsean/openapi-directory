# GkeHubApi.ClusterUpgradeScopeSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gkeUpgradeOverrides** | [**[ClusterUpgradeGKEUpgradeOverride]**](ClusterUpgradeGKEUpgradeOverride.md) | Allow users to override some properties of each GKE upgrade. | [optional] 
**postConditions** | [**ClusterUpgradePostConditions**](ClusterUpgradePostConditions.md) |  | [optional] 
**upstreamScopes** | **[String]** | This scope consumes upgrades that have COMPLETE status code in the upstream scopes. See UpgradeStatus.Code for code definitions. The scope name should be in the form: &#x60;projects/{p}/locations/global/scopes/{s}&#x60; Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature&#39;s project. This is defined as repeated for future proof reasons. Initial implementation will enforce at most one upstream scope. | [optional] 


