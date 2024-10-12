# ServiceFabricClientApis.ApplicationResourceUpgradeProgressInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationUpgradeStatusDetails** | **String** | Additional detailed information about the status of the pending upgrade. | [optional] 
**failureTimestampUtc** | **String** | The estimated UTC datetime when the upgrade failed and FailureAction was executed. | [optional] 
**name** | **String** | Name of the Application resource. | [optional] 
**percentCompleted** | **String** | The estimated percent of replicas are completed in the upgrade. | [optional] 
**rollingUpgradeMode** | [**RollingUpgradeMode**](RollingUpgradeMode.md) |  | [optional] 
**serviceUpgradeProgress** | [**[ServiceUpgradeProgress]**](ServiceUpgradeProgress.md) | List of service upgrade progresses. | [optional] 
**startTimestampUtc** | **String** | The estimated UTC datetime when the upgrade started. | [optional] 
**targetApplicationTypeVersion** | **String** | The target application version for the application upgrade. | [optional] 
**upgradeDuration** | **String** | The estimated amount of time that the overall upgrade elapsed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;PT0H2M0S&#39;]
**upgradeReplicaSetCheckTimeoutInSeconds** | **Number** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). | [optional] [default to 42949672925]
**upgradeState** | [**ApplicationResourceUpgradeState**](ApplicationResourceUpgradeState.md) |  | [optional] 


