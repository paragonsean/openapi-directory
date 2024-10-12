

# StartApplicationUpgrade

The description of the start application upgrade

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md) |  |  [optional] |
|**forceRestart** | **Boolean** |  |  [optional] |
|**monitoringPolicy** | [**MonitoringPolicy**](MonitoringPolicy.md) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**parameters** | [**List&lt;ApplicationParametersInner&gt;**](ApplicationParametersInner.md) |  |  [optional] |
|**rollingUpgradeMode** | **RollingUpgradeMode** |  |  [optional] |
|**targetApplicationTypeVersion** | **String** |  |  [optional] |
|**upgradeKind** | [**UpgradeKindEnum**](#UpgradeKindEnum) |  |  [optional] |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Integer** |  |  [optional] |



## Enum: UpgradeKindEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ROLLING | &quot;Rolling&quot; |



