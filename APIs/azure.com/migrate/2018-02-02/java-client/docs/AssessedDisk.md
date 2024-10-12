

# AssessedDisk

A disk assessed for an assessment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gigabytesConsumed** | **Double** | Gigabytes of storage consumed by this disk. |  [optional] [readonly] |
|**gigabytesForRecommendedDiskSize** | **Integer** | Gigabytes of storage provided by the recommended Azure disk size. |  [optional] [readonly] |
|**gigabytesProvisioned** | **Double** | Gigabytes of storage provisioned for this disk. |  [optional] [readonly] |
|**megabytesPerSecondOfRead** | **Double** | Disk throughput in MegaBytes per second. |  [optional] [readonly] |
|**megabytesPerSecondOfReadDataPointsExpected** | **Integer** | Expected data points for MegaBytes per second of read. |  [optional] [readonly] |
|**megabytesPerSecondOfReadDataPointsReceived** | **Integer** | Received data points for MegaBytes per second of read. |  [optional] [readonly] |
|**megabytesPerSecondOfWrite** | **Double** | Disk throughput in MegaBytes per second. |  [optional] [readonly] |
|**megabytesPerSecondOfWriteDataPointsExpected** | **Integer** | Expected data points for MegaBytes per second of write. |  [optional] [readonly] |
|**megabytesPerSecondOfWriteDataPointsReceived** | **Integer** | Received data points for MegaBytes per second of write. |  [optional] [readonly] |
|**monthlyStorageCost** | **Double** | Estimated aggregate storage cost for a 31-day month for this disk. |  [optional] [readonly] |
|**name** | **String** | Name of the assessed disk. |  [optional] [readonly] |
|**numberOfReadOperationsPerSecond** | **Double** | Number of read operations per second for the disk. |  [optional] [readonly] |
|**numberOfReadOperationsPerSecondDataPointsExpected** | **Integer** | Expected number of data points for read operations per second. |  [optional] [readonly] |
|**numberOfReadOperationsPerSecondDataPointsReceived** | **Integer** | Received number of data points for read operations per second. |  [optional] [readonly] |
|**numberOfWriteOperationsPerSecond** | **Double** | Number of read and write operations per second for the disk. |  [optional] [readonly] |
|**numberOfWriteOperationsPerSecondDataPointsExpected** | **Integer** | Expected number of data points for write operations per second. |  [optional] [readonly] |
|**numberOfWriteOperationsPerSecondDataPointsReceived** | **Integer** | Received number of data points for write operations per second. |  [optional] [readonly] |
|**recommendedDiskSize** | [**RecommendedDiskSizeEnum**](#RecommendedDiskSizeEnum) | Recommended Azure size for the disk, given utilization data and preferences set on Assessment. |  [optional] [readonly] |
|**recommendedDiskType** | [**RecommendedDiskTypeEnum**](#RecommendedDiskTypeEnum) | Storage type selected for this disk. |  [optional] [readonly] |
|**suitability** | [**SuitabilityEnum**](#SuitabilityEnum) | Whether this disk is suitable for Azure. |  [optional] [readonly] |
|**suitabilityExplanation** | [**SuitabilityExplanationEnum**](#SuitabilityExplanationEnum) | If disk is suitable, this explains the reasons and mitigation steps. |  [optional] [readonly] |



## Enum: RecommendedDiskSizeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| STANDARD_S4 | &quot;Standard_S4&quot; |
| STANDARD_S6 | &quot;Standard_S6&quot; |
| STANDARD_S10 | &quot;Standard_S10&quot; |
| STANDARD_S20 | &quot;Standard_S20&quot; |
| STANDARD_S30 | &quot;Standard_S30&quot; |
| STANDARD_S40 | &quot;Standard_S40&quot; |
| STANDARD_S50 | &quot;Standard_S50&quot; |
| PREMIUM_P4 | &quot;Premium_P4&quot; |
| PREMIUM_P6 | &quot;Premium_P6&quot; |
| PREMIUM_P10 | &quot;Premium_P10&quot; |
| PREMIUM_P20 | &quot;Premium_P20&quot; |
| PREMIUM_P30 | &quot;Premium_P30&quot; |
| PREMIUM_P40 | &quot;Premium_P40&quot; |
| PREMIUM_P50 | &quot;Premium_P50&quot; |



## Enum: RecommendedDiskTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



## Enum: SuitabilityEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NOT_SUITABLE | &quot;NotSuitable&quot; |
| SUITABLE | &quot;Suitable&quot; |
| CONDITIONALLY_SUITABLE | &quot;ConditionallySuitable&quot; |
| READINESS_UNKNOWN | &quot;ReadinessUnknown&quot; |



## Enum: SuitabilityExplanationEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NOT_APPLICABLE | &quot;NotApplicable&quot; |
| DISK_SIZE_GREATER_THAN_SUPPORTED | &quot;DiskSizeGreaterThanSupported&quot; |
| NO_SUITABLE_DISK_SIZE_FOR_IOPS | &quot;NoSuitableDiskSizeForIops&quot; |
| NO_SUITABLE_DISK_SIZE_FOR_THROUGHPUT | &quot;NoSuitableDiskSizeForThroughput&quot; |
| NO_DISK_SIZE_FOUND_IN_SELECTED_LOCATION | &quot;NoDiskSizeFoundInSelectedLocation&quot; |
| NO_DISK_SIZE_FOUND_FOR_SELECTED_REDUNDANCY | &quot;NoDiskSizeFoundForSelectedRedundancy&quot; |
| INTERNAL_ERROR_OCCURRED_FOR_DISK_EVALUATION | &quot;InternalErrorOccurredForDiskEvaluation&quot; |



