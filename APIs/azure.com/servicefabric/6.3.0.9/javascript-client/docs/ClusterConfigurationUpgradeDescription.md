# ServiceFabricClientApis.ClusterConfigurationUpgradeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationHealthPolicies** | [**ApplicationHealthPolicies**](ApplicationHealthPolicies.md) |  | [optional] 
**clusterConfig** | **String** | The cluster configuration. | 
**healthCheckRetryTimeout** | **String** | The length of time between attempts to perform a health checks if the application or cluster is not healthy. | [optional] [default to &#39;PT0H0M0S&#39;]
**healthCheckStableDurationInSeconds** | **String** | The length of time that the application or cluster must remain healthy. | [optional] [default to &#39;PT0H0M0S&#39;]
**healthCheckWaitDurationInSeconds** | **String** | The length of time to wait after completing an upgrade domain before starting the health checks process. | [optional] [default to &#39;PT0H0M0S&#39;]
**maxPercentDeltaUnhealthyNodes** | **Number** | The maximum allowed percentage of delta health degradation during the upgrade. Allowed values are integer values from zero to 100. | [optional] 
**maxPercentUnhealthyApplications** | **Number** | The maximum allowed percentage of unhealthy applications during the upgrade. Allowed values are integer values from zero to 100. | [optional] 
**maxPercentUnhealthyNodes** | **Number** | The maximum allowed percentage of unhealthy nodes during the upgrade. Allowed values are integer values from zero to 100. | [optional] 
**maxPercentUpgradeDomainDeltaUnhealthyNodes** | **Number** | The maximum allowed percentage of upgrade domain delta health degradation during the upgrade. Allowed values are integer values from zero to 100. | [optional] 
**upgradeDomainTimeoutInSeconds** | **String** | The timeout for the upgrade domain. | [optional] [default to &#39;PT0H0M0S&#39;]
**upgradeTimeoutInSeconds** | **String** | The upgrade timeout. | [optional] [default to &#39;PT0H0M0S&#39;]


