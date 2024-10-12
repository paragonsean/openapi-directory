

# AssessedMachineProperties

Properties of an assessed machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootType** | [**BootTypeEnum**](#BootTypeEnum) | Boot type of the machine. |  [optional] [readonly] |
|**confidenceRatingInPercentage** | **Double** | Confidence rating of assessed machine. |  [optional] [readonly] |
|**createdTimestamp** | **OffsetDateTime** | Time when this machine was created. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**datacenterMachineArmId** | **String** | ARM ID of the discovered machine. |  [optional] [readonly] |
|**datacenterManagementServerArmId** | **String** | ARM ID of the discovered datacenter. |  [optional] [readonly] |
|**datacenterManagementServerName** | **String** | Name of the server hosting the datacenter management solution. |  [optional] [readonly] |
|**description** | **String** | Description of the machine |  [optional] [readonly] |
|**disks** | [**Map&lt;String, AssessedDisk&gt;**](AssessedDisk.md) | Dictionary of disks attached to the machine. Key is ID of disk. Value is a disk object. |  [optional] [readonly] |
|**displayName** | **String** | User readable name of the machine as defined by the user in their private datacenter. |  [optional] [readonly] |
|**megabytesOfMemory** | **Double** | Memory in Megabytes. |  [optional] [readonly] |
|**megabytesOfMemoryForRecommendedSize** | **Double** | Megabytes of memory in the Recommended Azure VM Size. |  [optional] [readonly] |
|**monthlyBandwidthCost** | **Double** | Monthly network cost estimate for the network adapters that are attached to this machine as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyComputeCostForRecommendedSize** | **Double** | Compute Cost for a 31-day month, if the machine is migrated to Azure with the Recommended Size. |  [optional] [readonly] |
|**monthlyPremiumStorageCost** | **Double** | Monthly premium storage cost estimate for the disks that are attached to this machine as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyStandardSSDStorageCost** | **Double** | Monthly standard SSD storage cost estimate for the disks that are attached to this machine as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyStorageCost** | **Double** | Monthly storage cost estimate for the disks that are attached to this machine as a group, for a 31-day month. |  [optional] [readonly] |
|**networkAdapters** | [**Map&lt;String, AssessedNetworkAdapter&gt;**](AssessedNetworkAdapter.md) | Dictionary of network adapters attached to the machine. Key is name of the adapter. Value is a network adapter object. |  [optional] [readonly] |
|**numberOfCores** | **Integer** | Processor count. |  [optional] [readonly] |
|**numberOfCoresForRecommendedSize** | **Integer** | Number of CPU cores in the Recommended Azure VM Size. |  [optional] [readonly] |
|**operatingSystemName** | **String** | Operating System name of the machine. |  [optional] [readonly] |
|**operatingSystemType** | **String** | Operating System type of the machine. |  [optional] [readonly] |
|**operatingSystemVersion** | **String** | Operating System version of the machine. |  [optional] [readonly] |
|**percentageCoresUtilization** | **Double** | Utilization percentage of the processor core as observed in the private data center, in the Time Range selected on Assessment, reported as the Percentile value based on the percentile number selected in assessment. |  [optional] [readonly] |
|**percentageMemoryUtilization** | **Double** | Utilization percentage of the memory as observed in the private data center, in the Time Range selected on Assessment, reported as the Percentile value based on the percentile number selected in assessment. |  [optional] [readonly] |
|**recommendedSize** | [**RecommendedSizeEnum**](#RecommendedSizeEnum) | Recommended Azure size for this machine. |  [optional] [readonly] |
|**suitability** | [**SuitabilityEnum**](#SuitabilityEnum) | Whether machine is suitable for migration to Azure. |  [optional] [readonly] |
|**suitabilityDetail** | [**SuitabilityDetailEnum**](#SuitabilityDetailEnum) | If machine is not suitable for cloud, this explains the reasons. |  [optional] [readonly] |
|**suitabilityExplanation** | [**SuitabilityExplanationEnum**](#SuitabilityExplanationEnum) | If machine is not ready to be migrated, this explains the reasons and mitigation steps. |  [optional] [readonly] |
|**updatedTimestamp** | **OffsetDateTime** | Time when this machine was last updated. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |



## Enum: BootTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| EFI | &quot;EFI&quot; |
| BIOS | &quot;BIOS&quot; |



## Enum: RecommendedSizeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| BASIC_A0 | &quot;Basic_A0&quot; |
| BASIC_A1 | &quot;Basic_A1&quot; |
| BASIC_A2 | &quot;Basic_A2&quot; |
| BASIC_A3 | &quot;Basic_A3&quot; |
| BASIC_A4 | &quot;Basic_A4&quot; |
| STANDARD_A0 | &quot;Standard_A0&quot; |
| STANDARD_A1 | &quot;Standard_A1&quot; |
| STANDARD_A2 | &quot;Standard_A2&quot; |
| STANDARD_A3 | &quot;Standard_A3&quot; |
| STANDARD_A4 | &quot;Standard_A4&quot; |
| STANDARD_A5 | &quot;Standard_A5&quot; |
| STANDARD_A6 | &quot;Standard_A6&quot; |
| STANDARD_A7 | &quot;Standard_A7&quot; |
| STANDARD_A8 | &quot;Standard_A8&quot; |
| STANDARD_A9 | &quot;Standard_A9&quot; |
| STANDARD_A10 | &quot;Standard_A10&quot; |
| STANDARD_A11 | &quot;Standard_A11&quot; |
| STANDARD_A1_V2 | &quot;Standard_A1_v2&quot; |
| STANDARD_A2_V2 | &quot;Standard_A2_v2&quot; |
| STANDARD_A4_V2 | &quot;Standard_A4_v2&quot; |
| STANDARD_A8_V2 | &quot;Standard_A8_v2&quot; |
| STANDARD_A2M_V2 | &quot;Standard_A2m_v2&quot; |
| STANDARD_A4M_V2 | &quot;Standard_A4m_v2&quot; |
| STANDARD_A8M_V2 | &quot;Standard_A8m_v2&quot; |
| STANDARD_D1 | &quot;Standard_D1&quot; |
| STANDARD_D2 | &quot;Standard_D2&quot; |
| STANDARD_D3 | &quot;Standard_D3&quot; |
| STANDARD_D4 | &quot;Standard_D4&quot; |
| STANDARD_D11 | &quot;Standard_D11&quot; |
| STANDARD_D12 | &quot;Standard_D12&quot; |
| STANDARD_D13 | &quot;Standard_D13&quot; |
| STANDARD_D14 | &quot;Standard_D14&quot; |
| STANDARD_D1_V2 | &quot;Standard_D1_v2&quot; |
| STANDARD_D2_V2 | &quot;Standard_D2_v2&quot; |
| STANDARD_D3_V2 | &quot;Standard_D3_v2&quot; |
| STANDARD_D4_V2 | &quot;Standard_D4_v2&quot; |
| STANDARD_D5_V2 | &quot;Standard_D5_v2&quot; |
| STANDARD_D11_V2 | &quot;Standard_D11_v2&quot; |
| STANDARD_D12_V2 | &quot;Standard_D12_v2&quot; |
| STANDARD_D13_V2 | &quot;Standard_D13_v2&quot; |
| STANDARD_D14_V2 | &quot;Standard_D14_v2&quot; |
| STANDARD_D15_V2 | &quot;Standard_D15_v2&quot; |
| STANDARD_DS1 | &quot;Standard_DS1&quot; |
| STANDARD_DS2 | &quot;Standard_DS2&quot; |
| STANDARD_DS3 | &quot;Standard_DS3&quot; |
| STANDARD_DS4 | &quot;Standard_DS4&quot; |
| STANDARD_DS11 | &quot;Standard_DS11&quot; |
| STANDARD_DS12 | &quot;Standard_DS12&quot; |
| STANDARD_DS13 | &quot;Standard_DS13&quot; |
| STANDARD_DS14 | &quot;Standard_DS14&quot; |
| STANDARD_DS1_V2 | &quot;Standard_DS1_v2&quot; |
| STANDARD_DS2_V2 | &quot;Standard_DS2_v2&quot; |
| STANDARD_DS3_V2 | &quot;Standard_DS3_v2&quot; |
| STANDARD_DS4_V2 | &quot;Standard_DS4_v2&quot; |
| STANDARD_DS5_V2 | &quot;Standard_DS5_v2&quot; |
| STANDARD_DS11_V2 | &quot;Standard_DS11_v2&quot; |
| STANDARD_DS12_V2 | &quot;Standard_DS12_v2&quot; |
| STANDARD_DS13_V2 | &quot;Standard_DS13_v2&quot; |
| STANDARD_DS14_V2 | &quot;Standard_DS14_v2&quot; |
| STANDARD_DS15_V2 | &quot;Standard_DS15_v2&quot; |
| STANDARD_F1 | &quot;Standard_F1&quot; |
| STANDARD_F2 | &quot;Standard_F2&quot; |
| STANDARD_F4 | &quot;Standard_F4&quot; |
| STANDARD_F8 | &quot;Standard_F8&quot; |
| STANDARD_F16 | &quot;Standard_F16&quot; |
| STANDARD_F1S | &quot;Standard_F1s&quot; |
| STANDARD_F2S | &quot;Standard_F2s&quot; |
| STANDARD_F4S | &quot;Standard_F4s&quot; |
| STANDARD_F8S | &quot;Standard_F8s&quot; |
| STANDARD_F16S | &quot;Standard_F16s&quot; |
| STANDARD_G1 | &quot;Standard_G1&quot; |
| STANDARD_G2 | &quot;Standard_G2&quot; |
| STANDARD_G3 | &quot;Standard_G3&quot; |
| STANDARD_G4 | &quot;Standard_G4&quot; |
| STANDARD_G5 | &quot;Standard_G5&quot; |
| STANDARD_GS1 | &quot;Standard_GS1&quot; |
| STANDARD_GS2 | &quot;Standard_GS2&quot; |
| STANDARD_GS3 | &quot;Standard_GS3&quot; |
| STANDARD_GS4 | &quot;Standard_GS4&quot; |
| STANDARD_GS5 | &quot;Standard_GS5&quot; |
| STANDARD_H8 | &quot;Standard_H8&quot; |
| STANDARD_H16 | &quot;Standard_H16&quot; |
| STANDARD_H8M | &quot;Standard_H8m&quot; |
| STANDARD_H16M | &quot;Standard_H16m&quot; |
| STANDARD_H16R | &quot;Standard_H16r&quot; |
| STANDARD_H16MR | &quot;Standard_H16mr&quot; |
| STANDARD_L4S | &quot;Standard_L4s&quot; |
| STANDARD_L8S | &quot;Standard_L8s&quot; |
| STANDARD_L16S | &quot;Standard_L16s&quot; |
| STANDARD_L32S | &quot;Standard_L32s&quot; |
| STANDARD_D2S_V3 | &quot;Standard_D2s_v3&quot; |
| STANDARD_D4S_V3 | &quot;Standard_D4s_v3&quot; |
| STANDARD_D8S_V3 | &quot;Standard_D8s_v3&quot; |
| STANDARD_D16S_V3 | &quot;Standard_D16s_v3&quot; |
| STANDARD_D32S_V3 | &quot;Standard_D32s_v3&quot; |
| STANDARD_D64S_V3 | &quot;Standard_D64s_v3&quot; |
| STANDARD_D2_V3 | &quot;Standard_D2_v3&quot; |
| STANDARD_D4_V3 | &quot;Standard_D4_v3&quot; |
| STANDARD_D8_V3 | &quot;Standard_D8_v3&quot; |
| STANDARD_D16_V3 | &quot;Standard_D16_v3&quot; |
| STANDARD_D32_V3 | &quot;Standard_D32_v3&quot; |
| STANDARD_D64_V3 | &quot;Standard_D64_v3&quot; |
| STANDARD_F2S_V2 | &quot;Standard_F2s_v2&quot; |
| STANDARD_F4S_V2 | &quot;Standard_F4s_v2&quot; |
| STANDARD_F8S_V2 | &quot;Standard_F8s_v2&quot; |
| STANDARD_F16S_V2 | &quot;Standard_F16s_v2&quot; |
| STANDARD_F32S_V2 | &quot;Standard_F32s_v2&quot; |
| STANDARD_F64S_V2 | &quot;Standard_F64s_v2&quot; |
| STANDARD_F72S_V2 | &quot;Standard_F72s_v2&quot; |
| STANDARD_E2_V3 | &quot;Standard_E2_v3&quot; |
| STANDARD_E4_V3 | &quot;Standard_E4_v3&quot; |
| STANDARD_E8_V3 | &quot;Standard_E8_v3&quot; |
| STANDARD_E16_V3 | &quot;Standard_E16_v3&quot; |
| STANDARD_E32_V3 | &quot;Standard_E32_v3&quot; |
| STANDARD_E64_V3 | &quot;Standard_E64_v3&quot; |
| STANDARD_E2S_V3 | &quot;Standard_E2s_v3&quot; |
| STANDARD_E4S_V3 | &quot;Standard_E4s_v3&quot; |
| STANDARD_E8S_V3 | &quot;Standard_E8s_v3&quot; |
| STANDARD_E16S_V3 | &quot;Standard_E16s_v3&quot; |
| STANDARD_E32S_V3 | &quot;Standard_E32s_v3&quot; |
| STANDARD_E64S_V3 | &quot;Standard_E64s_v3&quot; |
| STANDARD_M64S | &quot;Standard_M64s&quot; |
| STANDARD_M64MS | &quot;Standard_M64ms&quot; |
| STANDARD_M128S | &quot;Standard_M128s&quot; |
| STANDARD_M128MS | &quot;Standard_M128ms&quot; |



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
| RECOMMENDED_SIZE_HAS_LESS_NETWORK_ADAPTERS | &quot;RecommendedSizeHasLessNetworkAdapters&quot; |
| CANNOT_REPORT_COMPUTE_COST | &quot;CannotReportComputeCost&quot; |
| CANNOT_REPORT_STORAGE_COST | &quot;CannotReportStorageCost&quot; |
| CANNOT_REPORT_BANDWIDTH_COSTS | &quot;CannotReportBandwidthCosts&quot; |
| PERCENTAGE_OF_CORES_UTILIZED_MISSING | &quot;PercentageOfCoresUtilizedMissing&quot; |
| PERCENTAGE_OF_MEMORY_UTILIZED_MISSING | &quot;PercentageOfMemoryUtilizedMissing&quot; |
| PERCENTAGE_OF_CORES_UTILIZED_OUT_OF_RANGE | &quot;PercentageOfCoresUtilizedOutOfRange&quot; |
| PERCENTAGE_OF_MEMORY_UTILIZED_OUT_OF_RANGE | &quot;PercentageOfMemoryUtilizedOutOfRange&quot; |



## Enum: SuitabilityExplanationEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NOT_APPLICABLE | &quot;NotApplicable&quot; |
| GUEST_OPERATING_SYSTEM_ARCHITECTURE_NOT_SUPPORTED | &quot;GuestOperatingSystemArchitectureNotSupported&quot; |
| GUEST_OPERATING_SYSTEM_NOT_SUPPORTED | &quot;GuestOperatingSystemNotSupported&quot; |
| BOOT_TYPE_NOT_SUPPORTED | &quot;BootTypeNotSupported&quot; |
| MORE_DISKS_THAN_SUPPORTED | &quot;MoreDisksThanSupported&quot; |
| NO_SUITABLE_VM_SIZE_FOUND | &quot;NoSuitableVmSizeFound&quot; |
| ONE_OR_MORE_DISKS_NOT_SUITABLE | &quot;OneOrMoreDisksNotSuitable&quot; |
| ONE_OR_MORE_ADAPTERS_NOT_SUITABLE | &quot;OneOrMoreAdaptersNotSuitable&quot; |
| INTERNAL_ERROR_OCCURRED_DURING_COMPUTE_EVALUATION | &quot;InternalErrorOccurredDuringComputeEvaluation&quot; |
| INTERNAL_ERROR_OCCURRED_DURING_STORAGE_EVALUATION | &quot;InternalErrorOccurredDuringStorageEvaluation&quot; |
| INTERNAL_ERROR_OCCURRED_DURING_NETWORK_EVALUATION | &quot;InternalErrorOccurredDuringNetworkEvaluation&quot; |
| NO_VM_SIZE_SUPPORTS_STORAGE_PERFORMANCE | &quot;NoVmSizeSupportsStoragePerformance&quot; |
| NO_VM_SIZE_SUPPORTS_NETWORK_PERFORMANCE | &quot;NoVmSizeSupportsNetworkPerformance&quot; |
| NO_VM_SIZE_FOR_SELECTED_PRICING_TIER | &quot;NoVmSizeForSelectedPricingTier&quot; |
| NO_VM_SIZE_FOR_SELECTED_AZURE_LOCATION | &quot;NoVmSizeForSelectedAzureLocation&quot; |
| CHECK_RED_HAT_LINUX_VERSION | &quot;CheckRedHatLinuxVersion&quot; |
| CHECK_OPEN_SUSE_LINUX_VERSION | &quot;CheckOpenSuseLinuxVersion&quot; |
| CHECK_WINDOWS_SERVER2008_R2_VERSION | &quot;CheckWindowsServer2008R2Version&quot; |
| CHECK_CENT_OS_VERSION | &quot;CheckCentOsVersion&quot; |
| CHECK_DEBIAN_LINUX_VERSION | &quot;CheckDebianLinuxVersion&quot; |
| CHECK_SUSE_LINUX_VERSION | &quot;CheckSuseLinuxVersion&quot; |
| CHECK_ORACLE_LINUX_VERSION | &quot;CheckOracleLinuxVersion&quot; |
| CHECK_UBUNTU_LINUX_VERSION | &quot;CheckUbuntuLinuxVersion&quot; |
| CHECK_CORE_OS_LINUX_VERSION | &quot;CheckCoreOsLinuxVersion&quot; |
| WINDOWS_SERVER_VERSION_CONDITIONALLY_SUPPORTED | &quot;WindowsServerVersionConditionallySupported&quot; |
| NO_GUEST_OPERATING_SYSTEM_CONDITIONALLY_SUPPORTED | &quot;NoGuestOperatingSystemConditionallySupported&quot; |
| WINDOWS_CLIENT_VERSIONS_CONDITIONALLY_SUPPORTED | &quot;WindowsClientVersionsConditionallySupported&quot; |
| BOOT_TYPE_UNKNOWN | &quot;BootTypeUnknown&quot; |
| GUEST_OPERATING_SYSTEM_UNKNOWN | &quot;GuestOperatingSystemUnknown&quot; |
| WINDOWS_SERVER_VERSIONS_SUPPORTED_WITH_CAVEAT | &quot;WindowsServerVersionsSupportedWithCaveat&quot; |
| WINDOWS_OSNO_LONGER_UNDER_MS_SUPPORT | &quot;WindowsOSNoLongerUnderMSSupport&quot; |
| ENDORSED_WITH_CONDITIONS_LINUX_DISTRIBUTIONS | &quot;EndorsedWithConditionsLinuxDistributions&quot; |
| UNENDORSED_LINUX_DISTRIBUTIONS | &quot;UnendorsedLinuxDistributions&quot; |
| NO_VM_SIZE_FOR_STANDARD_PRICING_TIER | &quot;NoVmSizeForStandardPricingTier&quot; |
| NO_VM_SIZE_FOR_BASIC_PRICING_TIER | &quot;NoVmSizeForBasicPricingTier&quot; |



