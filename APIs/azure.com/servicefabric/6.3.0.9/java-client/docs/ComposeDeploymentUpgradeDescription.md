

# ComposeDeploymentUpgradeDescription

Describes the parameters for a compose deployment upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md) |  |  [optional] |
|**composeFileContent** | **String** | The content of the compose file that describes the deployment to create. |  |
|**deploymentName** | **String** | The name of the deployment. |  |
|**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). |  [optional] |
|**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  |  [optional] |
|**registryCredential** | [**RegistryCredential**](RegistryCredential.md) |  |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**upgradeKind** | **UpgradeKind** |  |  |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Long** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). |  [optional] |



