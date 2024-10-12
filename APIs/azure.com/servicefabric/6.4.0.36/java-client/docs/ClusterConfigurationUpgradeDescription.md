

# ClusterConfigurationUpgradeDescription

Describes the parameters for a standalone cluster configuration upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicies** | [**ApplicationHealthPolicies**](ApplicationHealthPolicies.md) |  |  [optional] |
|**clusterConfig** | **String** | The cluster configuration as a JSON string. For example, [this file](https://github.com/Azure-Samples/service-fabric-dotnet-standalone-cluster-configuration/blob/master/Samples/ClusterConfig.Unsecure.DevCluster.json) contains JSON describing the [nodes and other properties of the cluster](https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-manifest). |  |
|**healthCheckRetryTimeout** | **String** | The length of time between attempts to perform health checks if the application or cluster is not healthy. |  [optional] |
|**healthCheckStableDurationInSeconds** | **String** | The length of time that the application or cluster must remain healthy before the upgrade proceeds to the next upgrade domain. |  [optional] |
|**healthCheckWaitDurationInSeconds** | **String** | The length of time to wait after completing an upgrade domain before starting the health checks process. |  [optional] |
|**maxPercentDeltaUnhealthyNodes** | **Integer** | The maximum allowed percentage of delta health degradation during the upgrade. Allowed values are integer values from zero to 100. |  [optional] |
|**maxPercentUnhealthyApplications** | **Integer** | The maximum allowed percentage of unhealthy applications during the upgrade. Allowed values are integer values from zero to 100. |  [optional] |
|**maxPercentUnhealthyNodes** | **Integer** | The maximum allowed percentage of unhealthy nodes during the upgrade. Allowed values are integer values from zero to 100. |  [optional] |
|**maxPercentUpgradeDomainDeltaUnhealthyNodes** | **Integer** | The maximum allowed percentage of upgrade domain delta health degradation during the upgrade. Allowed values are integer values from zero to 100. |  [optional] |
|**upgradeDomainTimeoutInSeconds** | **String** | The timeout for the upgrade domain. |  [optional] |
|**upgradeTimeoutInSeconds** | **String** | The upgrade timeout. |  [optional] |



