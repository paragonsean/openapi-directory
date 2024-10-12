# ServiceFabricClientApis.ApplicationUpgradeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md) |  | [optional] 
**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). | [optional] [default to false]
**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  | [optional] 
**name** | **String** | The name of the target application, including the &#39;fabric:&#39; URI scheme. | 
**parameters** | [**[ApplicationParameter]**](ApplicationParameter.md) | List of application parameters with overridden values from their default values specified in the application manifest. | 
**rollingUpgradeMode** | [**UpgradeMode**](UpgradeMode.md) |  | [optional] 
**targetApplicationTypeVersion** | **String** | The target application type version (found in the application manifest) for the application upgrade. | 
**upgradeKind** | [**UpgradeKind**](UpgradeKind.md) |  | 
**upgradeReplicaSetCheckTimeoutInSeconds** | **Number** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). | [optional] 


