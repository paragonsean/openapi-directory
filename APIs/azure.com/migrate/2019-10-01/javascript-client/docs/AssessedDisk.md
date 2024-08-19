# AzureMigrateV2.AssessedDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | User friendly name of the assessed disk. | [optional] [readonly] 
**gigabytesForRecommendedDiskSize** | **Number** | Gigabytes of storage provided by the recommended Azure disk size. | [optional] [readonly] 
**gigabytesProvisioned** | **Number** | Gigabytes of storage provisioned for this disk. | [optional] [readonly] 
**megabytesPerSecondOfRead** | **Number** | Disk throughput in MegaBytes per second. | [optional] [readonly] 
**megabytesPerSecondOfWrite** | **Number** | Disk throughput in MegaBytes per second. | [optional] [readonly] 
**monthlyStorageCost** | **Number** | Estimated aggregate storage cost for a 31-day month for this disk. | [optional] [readonly] 
**name** | **String** | Name of the assessed disk. | [optional] [readonly] 
**numberOfReadOperationsPerSecond** | **Number** | Number of read operations per second for the disk. | [optional] [readonly] 
**numberOfWriteOperationsPerSecond** | **Number** | Number of read and write operations per second for the disk. | [optional] [readonly] 
**recommendedDiskSize** | **String** | Recommended Azure size for the disk, given utilization data and preferences set on Assessment. | [optional] [readonly] 
**recommendedDiskType** | **String** | Storage type selected for this disk. | [optional] [readonly] 
**suitability** | **String** | Whether this disk is suitable for Azure. | [optional] [readonly] 
**suitabilityDetail** | **String** | If disk is suitable to be migrate but some conditions/checks were not considered while calculating suitability, this explains the details. | [optional] [readonly] 
**suitabilityExplanation** | **String** | If disk is not suitable to be migrated, this explains the reasons and mitigation steps. | [optional] [readonly] 



## Enum: RecommendedDiskSizeEnum


* `Unknown` (value: `"Unknown"`)

* `Standard_S4` (value: `"Standard_S4"`)

* `Standard_S6` (value: `"Standard_S6"`)

* `Standard_S10` (value: `"Standard_S10"`)

* `Standard_S15` (value: `"Standard_S15"`)

* `Standard_S20` (value: `"Standard_S20"`)

* `Standard_S30` (value: `"Standard_S30"`)

* `Standard_S40` (value: `"Standard_S40"`)

* `Standard_S50` (value: `"Standard_S50"`)

* `Premium_P4` (value: `"Premium_P4"`)

* `Premium_P6` (value: `"Premium_P6"`)

* `Premium_P10` (value: `"Premium_P10"`)

* `Premium_P15` (value: `"Premium_P15"`)

* `Premium_P20` (value: `"Premium_P20"`)

* `Premium_P30` (value: `"Premium_P30"`)

* `Premium_P40` (value: `"Premium_P40"`)

* `Premium_P50` (value: `"Premium_P50"`)

* `Standard_S60` (value: `"Standard_S60"`)

* `Standard_S70` (value: `"Standard_S70"`)

* `Standard_S80` (value: `"Standard_S80"`)

* `Premium_P60` (value: `"Premium_P60"`)

* `Premium_P70` (value: `"Premium_P70"`)

* `Premium_P80` (value: `"Premium_P80"`)

* `StandardSSD_E10` (value: `"StandardSSD_E10"`)

* `StandardSSD_E15` (value: `"StandardSSD_E15"`)

* `StandardSSD_E20` (value: `"StandardSSD_E20"`)

* `StandardSSD_E30` (value: `"StandardSSD_E30"`)

* `StandardSSD_E40` (value: `"StandardSSD_E40"`)

* `StandardSSD_E50` (value: `"StandardSSD_E50"`)

* `StandardSSD_E60` (value: `"StandardSSD_E60"`)

* `StandardSSD_E70` (value: `"StandardSSD_E70"`)

* `StandardSSD_E80` (value: `"StandardSSD_E80"`)

* `StandardSSD_E4` (value: `"StandardSSD_E4"`)

* `StandardSSD_E6` (value: `"StandardSSD_E6"`)





## Enum: RecommendedDiskTypeEnum


* `Unknown` (value: `"Unknown"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `StandardSSD` (value: `"StandardSSD"`)

* `StandardOrPremium` (value: `"StandardOrPremium"`)





## Enum: SuitabilityEnum


* `Unknown` (value: `"Unknown"`)

* `NotSuitable` (value: `"NotSuitable"`)

* `Suitable` (value: `"Suitable"`)

* `ConditionallySuitable` (value: `"ConditionallySuitable"`)

* `ReadinessUnknown` (value: `"ReadinessUnknown"`)





## Enum: SuitabilityDetailEnum


* `None` (value: `"None"`)

* `NumberOfReadOperationsPerSecondMissing` (value: `"NumberOfReadOperationsPerSecondMissing"`)

* `NumberOfWriteOperationsPerSecondMissing` (value: `"NumberOfWriteOperationsPerSecondMissing"`)

* `MegabytesPerSecondOfReadMissing` (value: `"MegabytesPerSecondOfReadMissing"`)

* `MegabytesPerSecondOfWriteMissing` (value: `"MegabytesPerSecondOfWriteMissing"`)

* `DiskGigabytesConsumedMissing` (value: `"DiskGigabytesConsumedMissing"`)

* `DiskGigabytesProvisionedMissing` (value: `"DiskGigabytesProvisionedMissing"`)

* `NumberOfReadOperationsPerSecondOutOfRange` (value: `"NumberOfReadOperationsPerSecondOutOfRange"`)

* `NumberOfWriteOperationsPerSecondOutOfRange` (value: `"NumberOfWriteOperationsPerSecondOutOfRange"`)

* `MegabytesPerSecondOfReadOutOfRange` (value: `"MegabytesPerSecondOfReadOutOfRange"`)

* `MegabytesPerSecondOfWriteOutOfRange` (value: `"MegabytesPerSecondOfWriteOutOfRange"`)

* `DiskGigabytesConsumedOutOfRange` (value: `"DiskGigabytesConsumedOutOfRange"`)

* `DiskGigabytesProvisionedOutOfRange` (value: `"DiskGigabytesProvisionedOutOfRange"`)





## Enum: SuitabilityExplanationEnum


* `Unknown` (value: `"Unknown"`)

* `NotApplicable` (value: `"NotApplicable"`)

* `DiskSizeGreaterThanSupported` (value: `"DiskSizeGreaterThanSupported"`)

* `NoSuitableDiskSizeForIops` (value: `"NoSuitableDiskSizeForIops"`)

* `NoSuitableDiskSizeForThroughput` (value: `"NoSuitableDiskSizeForThroughput"`)

* `NoDiskSizeFoundInSelectedLocation` (value: `"NoDiskSizeFoundInSelectedLocation"`)

* `NoDiskSizeFoundForSelectedRedundancy` (value: `"NoDiskSizeFoundForSelectedRedundancy"`)

* `InternalErrorOccurredForDiskEvaluation` (value: `"InternalErrorOccurredForDiskEvaluation"`)

* `NoEaPriceFoundForDiskSize` (value: `"NoEaPriceFoundForDiskSize"`)




