

# ApplicationUpgradeDescription

Describes the parameters for an application upgrade. Note that upgrade description replaces the existing application description. This means that if the parameters are not specified, the existing parameters on the applications will be overwritten with the empty parameters list. This would result in the application using the default value of the parameters from the application manifest. If you do not want to change any existing parameter values, please get the application parameters first using the GetApplicationInfo query and then supply those values as Parameters in this ApplicationUpgradeDescription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md) |  |  [optional] |
|**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). |  [optional] |
|**instanceCloseDelayDurationInSeconds** | **Long** | Duration in seconds, to wait before a stateless instance is closed, to allow the active requests to drain gracefully. This would be effective when the instance is closing during the application/cluster upgrade, only for those instances which have a non-zero delay duration configured in the service description. See InstanceCloseDelayDurationSeconds property in $ref: \&quot;#/definitions/StatelessServiceDescription.yaml\&quot; for details. Note, the default value of InstanceCloseDelayDurationInSeconds is 4294967295, which indicates that the behavior will entirely depend on the delay configured in the stateless service description. |  [optional] |
|**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  |  [optional] |
|**name** | **String** | The name of the target application, including the &#39;fabric:&#39; URI scheme. |  |
|**parameters** | [**List&lt;ApplicationParameter&gt;**](ApplicationParameter.md) | List of application parameters with overridden values from their default values specified in the application manifest. |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**sortOrder** | **UpgradeSortOrder** |  |  [optional] |
|**targetApplicationTypeVersion** | **String** | The target application type version (found in the application manifest) for the application upgrade. |  |
|**upgradeKind** | **UpgradeKind** |  |  |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Long** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). |  [optional] |



