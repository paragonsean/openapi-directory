# AzureMigrate.AssessedDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gigabytesConsumed** | **Number** | Gigabytes of storage consumed by this disk. | [optional] [readonly] 
**gigabytesForRecommendedDiskSize** | **Number** | Gigabytes of storage provided by the recommended Azure disk size. | [optional] [readonly] 
**gigabytesProvisioned** | **Number** | Gigabytes of storage provisioned for this disk. | [optional] [readonly] 
**megabytesPerSecondOfRead** | **Number** | Disk throughput in MegaBytes per second. | [optional] [readonly] 
**megabytesPerSecondOfReadDataPointsExpected** | **Number** | Expected data points for MegaBytes per second of read. | [optional] [readonly] 
**megabytesPerSecondOfReadDataPointsReceived** | **Number** | Received data points for MegaBytes per second of read. | [optional] [readonly] 
**megabytesPerSecondOfWrite** | **Number** | Disk throughput in MegaBytes per second. | [optional] [readonly] 
**megabytesPerSecondOfWriteDataPointsExpected** | **Number** | Expected data points for MegaBytes per second of write. | [optional] [readonly] 
**megabytesPerSecondOfWriteDataPointsReceived** | **Number** | Received data points for MegaBytes per second of write. | [optional] [readonly] 
**monthlyStorageCost** | **Number** | Estimated aggregate storage cost for a 31-day month for this disk. | [optional] [readonly] 
**name** | **String** | Name of the assessed disk. | [optional] [readonly] 
**numberOfReadOperationsPerSecond** | **Number** | Number of read operations per second for the disk. | [optional] [readonly] 
**numberOfReadOperationsPerSecondDataPointsExpected** | **Number** | Expected number of data points for read operations per second. | [optional] [readonly] 
**numberOfReadOperationsPerSecondDataPointsReceived** | **Number** | Received number of data points for read operations per second. | [optional] [readonly] 
**numberOfWriteOperationsPerSecond** | **Number** | Number of read and write operations per second for the disk. | [optional] [readonly] 
**numberOfWriteOperationsPerSecondDataPointsExpected** | **Number** | Expected number of data points for write operations per second. | [optional] [readonly] 
**numberOfWriteOperationsPerSecondDataPointsReceived** | **Number** | Received number of data points for write operations per second. | [optional] [readonly] 
**recommendedDiskSize** | **String** | Recommended Azure size for the disk, given utilization data and preferences set on Assessment. | [optional] [readonly] 
**recommendedDiskType** | **String** | Storage type selected for this disk. | [optional] [readonly] 
**suitability** | **String** | Whether this disk is suitable for Azure. | [optional] [readonly] 
**suitabilityExplanation** | **String** | If disk is suitable, this explains the reasons and mitigation steps. | [optional] [readonly] 



## Enum: RecommendedDiskSizeEnum


* `Unknown` (value: `"Unknown"`)

* `Standard_S4` (value: `"Standard_S4"`)

* `Standard_S6` (value: `"Standard_S6"`)

* `Standard_S10` (value: `"Standard_S10"`)

* `Standard_S20` (value: `"Standard_S20"`)

* `Standard_S30` (value: `"Standard_S30"`)

* `Standard_S40` (value: `"Standard_S40"`)

* `Standard_S50` (value: `"Standard_S50"`)

* `Premium_P4` (value: `"Premium_P4"`)

* `Premium_P6` (value: `"Premium_P6"`)

* `Premium_P10` (value: `"Premium_P10"`)

* `Premium_P20` (value: `"Premium_P20"`)

* `Premium_P30` (value: `"Premium_P30"`)

* `Premium_P40` (value: `"Premium_P40"`)

* `Premium_P50` (value: `"Premium_P50"`)





## Enum: RecommendedDiskTypeEnum


* `Unknown` (value: `"Unknown"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)





## Enum: SuitabilityEnum


* `Unknown` (value: `"Unknown"`)

* `NotSuitable` (value: `"NotSuitable"`)

* `Suitable` (value: `"Suitable"`)

* `ConditionallySuitable` (value: `"ConditionallySuitable"`)

* `ReadinessUnknown` (value: `"ReadinessUnknown"`)





## Enum: SuitabilityExplanationEnum


* `Unknown` (value: `"Unknown"`)

* `NotApplicable` (value: `"NotApplicable"`)

* `DiskSizeGreaterThanSupported` (value: `"DiskSizeGreaterThanSupported"`)

* `NoSuitableDiskSizeForIops` (value: `"NoSuitableDiskSizeForIops"`)

* `NoSuitableDiskSizeForThroughput` (value: `"NoSuitableDiskSizeForThroughput"`)

* `NoDiskSizeFoundInSelectedLocation` (value: `"NoDiskSizeFoundInSelectedLocation"`)

* `NoDiskSizeFoundForSelectedRedundancy` (value: `"NoDiskSizeFoundForSelectedRedundancy"`)

* `InternalErrorOccurredForDiskEvaluation` (value: `"InternalErrorOccurredForDiskEvaluation"`)




