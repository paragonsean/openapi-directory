# KubernetesEngineApi.UpgradeSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueGreenSettings** | [**BlueGreenSettings**](BlueGreenSettings.md) |  | [optional] 
**maxSurge** | **Number** | The maximum number of nodes that can be created beyond the current size of the node pool during the upgrade process. | [optional] 
**maxUnavailable** | **Number** | The maximum number of nodes that can be simultaneously unavailable during the upgrade process. A node is considered available if its status is Ready. | [optional] 
**strategy** | **String** | Update strategy of the node pool. | [optional] 



## Enum: StrategyEnum


* `NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED` (value: `"NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED"`)

* `BLUE_GREEN` (value: `"BLUE_GREEN"`)

* `SURGE` (value: `"SURGE"`)




