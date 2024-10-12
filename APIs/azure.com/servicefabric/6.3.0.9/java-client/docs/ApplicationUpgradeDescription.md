

# ApplicationUpgradeDescription

Describes the parameters for an application upgrade. Note that upgrade description replaces the existing application description. This means that if the parameters are not specified, the existing parameters on the applications will be overwritten with the empty parameters list. This would result in the application using the default value of the parameters from the application manifest. If you do not want to change any existing parameter values, please get the application parameters first using the GetApplicationInfo query and then supply those values as Parameters in this ApplicationUpgradeDescription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md) |  |  [optional] |
|**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). |  [optional] |
|**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  |  [optional] |
|**name** | **String** | The name of the target application, including the &#39;fabric:&#39; URI scheme. |  |
|**parameters** | [**List&lt;ApplicationParameter&gt;**](ApplicationParameter.md) | List of application parameters with overridden values from their default values specified in the application manifest. |  |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**targetApplicationTypeVersion** | **String** | The target application type version (found in the application manifest) for the application upgrade. |  |
|**upgradeKind** | **UpgradeKind** |  |  |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Long** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). |  [optional] |



