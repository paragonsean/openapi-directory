# KubernetesEngineApi.NodeManagement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoRepair** | **Boolean** | A flag that specifies whether the node auto-repair is enabled for the node pool. If enabled, the nodes in this node pool will be monitored and, if they fail health checks too many times, an automatic repair action will be triggered. | [optional] 
**autoUpgrade** | **Boolean** | A flag that specifies whether node auto-upgrade is enabled for the node pool. If enabled, node auto-upgrade helps keep the nodes in your node pool up to date with the latest release version of Kubernetes. | [optional] 
**upgradeOptions** | [**AutoUpgradeOptions**](AutoUpgradeOptions.md) |  | [optional] 


