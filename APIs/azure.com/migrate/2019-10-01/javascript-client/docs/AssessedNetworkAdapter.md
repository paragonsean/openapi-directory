# AzureMigrateV2.AssessedNetworkAdapter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | User friendly name of the assessed network adapter. | [optional] [readonly] 
**ipAddresses** | **[String]** | List of IP Addresses on the network adapter. | [optional] [readonly] 
**macAddress** | **String** | MAC Address of the network adapter. | [optional] [readonly] 
**megabytesPerSecondReceived** | **Number** | Adapter throughput for incoming traffic in MegaBytes per second. | [optional] [readonly] 
**megabytesPerSecondTransmitted** | **Number** | Adapter throughput for outgoing traffic in MegaBytes per second. | [optional] [readonly] 
**monthlyBandwidthCosts** | **Number** | Monthly cost estimate for network bandwidth used by this network adapter. | [optional] [readonly] 
**netGigabytesTransmittedPerMonth** | **Number** | Gigabytes transmitted through this adapter each month. | [optional] 
**suitability** | **String** | Whether this adapter is suitable for Azure. | [optional] [readonly] 
**suitabilityDetail** | **String** | If network adapter is not suitable for cloud, this explains the reasons. | [optional] [readonly] 
**suitabilityExplanation** | **String** | If network adapter is suitable, this explains the reasons and mitigation steps. | [optional] [readonly] 



## Enum: SuitabilityEnum


* `Unknown` (value: `"Unknown"`)

* `NotSuitable` (value: `"NotSuitable"`)

* `Suitable` (value: `"Suitable"`)

* `ConditionallySuitable` (value: `"ConditionallySuitable"`)

* `ReadinessUnknown` (value: `"ReadinessUnknown"`)





## Enum: SuitabilityDetailEnum


* `None` (value: `"None"`)

* `MegabytesOfDataTransmittedMissing` (value: `"MegabytesOfDataTransmittedMissing"`)

* `MegabytesOfDataTransmittedOutOfRange` (value: `"MegabytesOfDataTransmittedOutOfRange"`)





## Enum: SuitabilityExplanationEnum


* `Unknown` (value: `"Unknown"`)

* `NotApplicable` (value: `"NotApplicable"`)

* `InternalErrorOccurred` (value: `"InternalErrorOccurred"`)




