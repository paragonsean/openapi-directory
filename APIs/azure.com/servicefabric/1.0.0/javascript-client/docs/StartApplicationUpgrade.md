# ServiceFabricClient.StartApplicationUpgrade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md) |  | [optional] 
**forceRestart** | **Boolean** |  | [optional] 
**monitoringPolicy** | [**MonitoringPolicy**](MonitoringPolicy.md) |  | [optional] 
**name** | **String** |  | [optional] 
**parameters** | [**[ApplicationParametersInner]**](ApplicationParametersInner.md) |  | [optional] 
**rollingUpgradeMode** | [**RollingUpgradeMode**](RollingUpgradeMode.md) |  | [optional] 
**targetApplicationTypeVersion** | **String** |  | [optional] 
**upgradeKind** | **String** |  | [optional] 
**upgradeReplicaSetCheckTimeoutInSeconds** | **Number** |  | [optional] 



## Enum: UpgradeKindEnum


* `Invalid` (value: `"Invalid"`)

* `Rolling` (value: `"Rolling"`)




