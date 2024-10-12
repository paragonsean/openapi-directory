# AzureMigrate.AssessedMachineProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootType** | **String** | Boot type of the machine. | [optional] [readonly] 
**createdTimestamp** | **Date** | Time when this machine was created. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**datacenterContainer** | **String** | Container defined in the management solution that this machine is part of in the datacenter. | [optional] [readonly] 
**datacenterMachineId** | **String** | ID of the machine as tracked by the datacenter management solution. | [optional] [readonly] 
**datacenterManagementServer** | **String** | Name of the server hosting the datacenter management solution. | [optional] [readonly] 
**datacenterManagementServerId** | **String** | ID of the server hosting the datacenter management solution. | [optional] [readonly] 
**description** | **String** | Description of the machine | [optional] [readonly] 
**discoveredTimestamp** | **Date** | Time when this machine was discovered by Azure Migrate agent. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**disks** | [**{String: AssessedDisk}**](AssessedDisk.md) | Dictionary of disks attached to the machine. Key is ID of disk. Value is a disk object. | [optional] [readonly] 
**displayName** | **String** | User readable name of the machine as defined by the user in their private datacenter. | [optional] [readonly] 
**groups** | **[String]** | List of references to the groups that the machine is member of. | [optional] [readonly] 
**megabytesOfMemory** | **Number** | Memory in Megabytes. | [optional] [readonly] 
**megabytesOfMemoryForRecommendedSize** | **Number** | Megabytes of memory in the Recommended Azure VM Size. | [optional] [readonly] 
**monthlyBandwidthCost** | **Number** | Monthly network cost estimate for the network adapters that are attached to this machine as a group, for a 31-day month. | [optional] [readonly] 
**monthlyComputeCostForRecommendedSize** | **Number** | Compute Cost for a 31-day month, if the machine is migrated to Azure with the Recommended Size. | [optional] [readonly] 
**monthlyStorageCost** | **Number** | Monthly storage cost estimate for the disks that are attached to this machine as a group, for a 31-day month. | [optional] [readonly] 
**networkAdapters** | [**{String: AssessedNetworkAdapter}**](AssessedNetworkAdapter.md) | Dictionary of network adapters attached to the machine. Key is name of the adapter. Value is a network adapter object. | [optional] [readonly] 
**numberOfCores** | **Number** | Processor count. | [optional] [readonly] 
**numberOfCoresForRecommendedSize** | **Number** | Number of CPU cores in the Recommended Azure VM Size. | [optional] [readonly] 
**operatingSystem** | **String** | Operating System of the machine. | [optional] [readonly] 
**percentageCoresUtilization** | **Number** | Utilization percentage of the processor core as observed in the private data center, in the Time Range selected on Assessment, reported as the Percentile value based on the percentile number selected in assessment. | [optional] [readonly] 
**percentageMemoryUtilization** | **Number** | Utilization percentage of the memory as observed in the private data center, in the Time Range selected on Assessment, reported as the Percentile value based on the percentile number selected in assessment. | [optional] [readonly] 
**recommendedSize** | **String** | Recommended Azure size for this machine. | [optional] [readonly] 
**suitability** | **String** | Whether machine is suitable for migration to Azure. | [optional] [readonly] 
**suitabilityExplanation** | **String** | If machine is not ready to be migrated, this explains the reasons and mitigation steps. | [optional] [readonly] 
**updatedTimestamp** | **Date** | Time when this machine was last updated. Date-Time represented in ISO-8601 format. | [optional] [readonly] 



## Enum: BootTypeEnum


* `Unknown` (value: `"Unknown"`)

* `EFI` (value: `"EFI"`)

* `BIOS` (value: `"BIOS"`)





## Enum: RecommendedSizeEnum


* `Unknown` (value: `"Unknown"`)

* `Basic_A0` (value: `"Basic_A0"`)

* `Basic_A1` (value: `"Basic_A1"`)

* `Basic_A2` (value: `"Basic_A2"`)

* `Basic_A3` (value: `"Basic_A3"`)

* `Basic_A4` (value: `"Basic_A4"`)

* `Standard_A0` (value: `"Standard_A0"`)

* `Standard_A1` (value: `"Standard_A1"`)

* `Standard_A2` (value: `"Standard_A2"`)

* `Standard_A3` (value: `"Standard_A3"`)

* `Standard_A4` (value: `"Standard_A4"`)

* `Standard_A5` (value: `"Standard_A5"`)

* `Standard_A6` (value: `"Standard_A6"`)

* `Standard_A7` (value: `"Standard_A7"`)

* `Standard_A8` (value: `"Standard_A8"`)

* `Standard_A9` (value: `"Standard_A9"`)

* `Standard_A10` (value: `"Standard_A10"`)

* `Standard_A11` (value: `"Standard_A11"`)

* `Standard_A1_v2` (value: `"Standard_A1_v2"`)

* `Standard_A2_v2` (value: `"Standard_A2_v2"`)

* `Standard_A4_v2` (value: `"Standard_A4_v2"`)

* `Standard_A8_v2` (value: `"Standard_A8_v2"`)

* `Standard_A2m_v2` (value: `"Standard_A2m_v2"`)

* `Standard_A4m_v2` (value: `"Standard_A4m_v2"`)

* `Standard_A8m_v2` (value: `"Standard_A8m_v2"`)

* `Standard_D1` (value: `"Standard_D1"`)

* `Standard_D2` (value: `"Standard_D2"`)

* `Standard_D3` (value: `"Standard_D3"`)

* `Standard_D4` (value: `"Standard_D4"`)

* `Standard_D11` (value: `"Standard_D11"`)

* `Standard_D12` (value: `"Standard_D12"`)

* `Standard_D13` (value: `"Standard_D13"`)

* `Standard_D14` (value: `"Standard_D14"`)

* `Standard_D1_v2` (value: `"Standard_D1_v2"`)

* `Standard_D2_v2` (value: `"Standard_D2_v2"`)

* `Standard_D3_v2` (value: `"Standard_D3_v2"`)

* `Standard_D4_v2` (value: `"Standard_D4_v2"`)

* `Standard_D5_v2` (value: `"Standard_D5_v2"`)

* `Standard_D11_v2` (value: `"Standard_D11_v2"`)

* `Standard_D12_v2` (value: `"Standard_D12_v2"`)

* `Standard_D13_v2` (value: `"Standard_D13_v2"`)

* `Standard_D14_v2` (value: `"Standard_D14_v2"`)

* `Standard_D15_v2` (value: `"Standard_D15_v2"`)

* `Standard_DS1` (value: `"Standard_DS1"`)

* `Standard_DS2` (value: `"Standard_DS2"`)

* `Standard_DS3` (value: `"Standard_DS3"`)

* `Standard_DS4` (value: `"Standard_DS4"`)

* `Standard_DS11` (value: `"Standard_DS11"`)

* `Standard_DS12` (value: `"Standard_DS12"`)

* `Standard_DS13` (value: `"Standard_DS13"`)

* `Standard_DS14` (value: `"Standard_DS14"`)

* `Standard_DS1_v2` (value: `"Standard_DS1_v2"`)

* `Standard_DS2_v2` (value: `"Standard_DS2_v2"`)

* `Standard_DS3_v2` (value: `"Standard_DS3_v2"`)

* `Standard_DS4_v2` (value: `"Standard_DS4_v2"`)

* `Standard_DS5_v2` (value: `"Standard_DS5_v2"`)

* `Standard_DS11_v2` (value: `"Standard_DS11_v2"`)

* `Standard_DS12_v2` (value: `"Standard_DS12_v2"`)

* `Standard_DS13_v2` (value: `"Standard_DS13_v2"`)

* `Standard_DS14_v2` (value: `"Standard_DS14_v2"`)

* `Standard_DS15_v2` (value: `"Standard_DS15_v2"`)

* `Standard_F1` (value: `"Standard_F1"`)

* `Standard_F2` (value: `"Standard_F2"`)

* `Standard_F4` (value: `"Standard_F4"`)

* `Standard_F8` (value: `"Standard_F8"`)

* `Standard_F16` (value: `"Standard_F16"`)

* `Standard_F1s` (value: `"Standard_F1s"`)

* `Standard_F2s` (value: `"Standard_F2s"`)

* `Standard_F4s` (value: `"Standard_F4s"`)

* `Standard_F8s` (value: `"Standard_F8s"`)

* `Standard_F16s` (value: `"Standard_F16s"`)

* `Standard_G1` (value: `"Standard_G1"`)

* `Standard_G2` (value: `"Standard_G2"`)

* `Standard_G3` (value: `"Standard_G3"`)

* `Standard_G4` (value: `"Standard_G4"`)

* `Standard_G5` (value: `"Standard_G5"`)

* `Standard_GS1` (value: `"Standard_GS1"`)

* `Standard_GS2` (value: `"Standard_GS2"`)

* `Standard_GS3` (value: `"Standard_GS3"`)

* `Standard_GS4` (value: `"Standard_GS4"`)

* `Standard_GS5` (value: `"Standard_GS5"`)

* `Standard_H8` (value: `"Standard_H8"`)

* `Standard_H16` (value: `"Standard_H16"`)

* `Standard_H8m` (value: `"Standard_H8m"`)

* `Standard_H16m` (value: `"Standard_H16m"`)

* `Standard_H16r` (value: `"Standard_H16r"`)

* `Standard_H16mr` (value: `"Standard_H16mr"`)

* `Standard_L4s` (value: `"Standard_L4s"`)

* `Standard_L8s` (value: `"Standard_L8s"`)

* `Standard_L16s` (value: `"Standard_L16s"`)

* `Standard_L32s` (value: `"Standard_L32s"`)





## Enum: SuitabilityEnum


* `Unknown` (value: `"Unknown"`)

* `NotSuitable` (value: `"NotSuitable"`)

* `Suitable` (value: `"Suitable"`)

* `ConditionallySuitable` (value: `"ConditionallySuitable"`)





## Enum: SuitabilityExplanationEnum


* `Unknown` (value: `"Unknown"`)

* `NotApplicable` (value: `"NotApplicable"`)

* `GuestOperatingSystemArchitectureNotSupported` (value: `"GuestOperatingSystemArchitectureNotSupported"`)

* `GuestOperatingSystemNotSupported` (value: `"GuestOperatingSystemNotSupported"`)

* `BootTypeNotSupported` (value: `"BootTypeNotSupported"`)

* `MoreDisksThanSupported` (value: `"MoreDisksThanSupported"`)

* `NoSuitableVmSizeFound` (value: `"NoSuitableVmSizeFound"`)

* `OneOrMoreDisksNotSuitable` (value: `"OneOrMoreDisksNotSuitable"`)

* `OneOrMoreAdaptersNotSuitable` (value: `"OneOrMoreAdaptersNotSuitable"`)

* `InternalErrorOccuredDuringComputeEvaluation` (value: `"InternalErrorOccuredDuringComputeEvaluation"`)

* `InternalErrorOccuredDuringStorageEvaluation` (value: `"InternalErrorOccuredDuringStorageEvaluation"`)

* `InternalErrorOccuredDuringNetworkEvaluation` (value: `"InternalErrorOccuredDuringNetworkEvaluation"`)

* `NoVmSizeSupportsStoragePerformance` (value: `"NoVmSizeSupportsStoragePerformance"`)

* `NoVmSizeSupportsNetworkPerformance` (value: `"NoVmSizeSupportsNetworkPerformance"`)

* `NoVmSizeForSelectedPricingTier` (value: `"NoVmSizeForSelectedPricingTier"`)

* `NoVmSizeForSelectedAzureLocation` (value: `"NoVmSizeForSelectedAzureLocation"`)

* `CheckRedHatLinuxVersion` (value: `"CheckRedHatLinuxVersion"`)

* `CheckOpenSuseLinuxVersion` (value: `"CheckOpenSuseLinuxVersion"`)

* `CheckWindowsServer2008R2Version` (value: `"CheckWindowsServer2008R2Version"`)

* `CheckCentOsVersion` (value: `"CheckCentOsVersion"`)

* `CheckDebianLinuxVersion` (value: `"CheckDebianLinuxVersion"`)

* `CheckSuseLinuxVersion` (value: `"CheckSuseLinuxVersion"`)

* `CheckOracleLinuxVersion` (value: `"CheckOracleLinuxVersion"`)

* `CheckUbuntuLinuxVersion` (value: `"CheckUbuntuLinuxVersion"`)

* `CheckCoreOsLinuxVersion` (value: `"CheckCoreOsLinuxVersion"`)

* `WindowsServerVersionConditionallySupported` (value: `"WindowsServerVersionConditionallySupported"`)

* `NoGuestOperatingSystemConditionallySupported` (value: `"NoGuestOperatingSystemConditionallySupported"`)

* `WindowsClientVersionsConditionallySupported` (value: `"WindowsClientVersionsConditionallySupported"`)




