

# AssessedNetworkAdapter

A network adapter assessed for an assessment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | User friendly name of the assessed network adapter. |  [optional] [readonly] |
|**ipAddresses** | **List&lt;String&gt;** | List of IP Addresses on the network adapter. |  [optional] [readonly] |
|**macAddress** | **String** | MAC Address of the network adapter. |  [optional] [readonly] |
|**megabytesPerSecondReceived** | **Double** | Adapter throughput for incoming traffic in MegaBytes per second. |  [optional] [readonly] |
|**megabytesPerSecondTransmitted** | **Double** | Adapter throughput for outgoing traffic in MegaBytes per second. |  [optional] [readonly] |
|**monthlyBandwidthCosts** | **Double** | Monthly cost estimate for network bandwidth used by this network adapter. |  [optional] [readonly] |
|**netGigabytesTransmittedPerMonth** | **Double** | Gigabytes transmitted through this adapter each month. |  [optional] |
|**suitability** | [**SuitabilityEnum**](#SuitabilityEnum) | Whether this adapter is suitable for Azure. |  [optional] [readonly] |
|**suitabilityDetail** | [**SuitabilityDetailEnum**](#SuitabilityDetailEnum) | If network adapter is not suitable for cloud, this explains the reasons. |  [optional] [readonly] |
|**suitabilityExplanation** | [**SuitabilityExplanationEnum**](#SuitabilityExplanationEnum) | If network adapter is suitable, this explains the reasons and mitigation steps. |  [optional] [readonly] |



## Enum: SuitabilityEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NOT_SUITABLE | &quot;NotSuitable&quot; |
| SUITABLE | &quot;Suitable&quot; |
| CONDITIONALLY_SUITABLE | &quot;ConditionallySuitable&quot; |
| READINESS_UNKNOWN | &quot;ReadinessUnknown&quot; |



## Enum: SuitabilityDetailEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| MEGABYTES_OF_DATA_TRANSMITTED_MISSING | &quot;MegabytesOfDataTransmittedMissing&quot; |
| MEGABYTES_OF_DATA_TRANSMITTED_OUT_OF_RANGE | &quot;MegabytesOfDataTransmittedOutOfRange&quot; |



## Enum: SuitabilityExplanationEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NOT_APPLICABLE | &quot;NotApplicable&quot; |
| INTERNAL_ERROR_OCCURRED | &quot;InternalErrorOccurred&quot; |



