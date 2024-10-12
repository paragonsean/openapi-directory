

# AssessedDisk

A disk assessed for an assessment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | User friendly name of the assessed disk. |  [optional] [readonly] |
|**gigabytesForRecommendedDiskSize** | **Integer** | Gigabytes of storage provided by the recommended Azure disk size. |  [optional] [readonly] |
|**gigabytesProvisioned** | **Double** | Gigabytes of storage provisioned for this disk. |  [optional] [readonly] |
|**megabytesPerSecondOfRead** | **Double** | Disk throughput in MegaBytes per second. |  [optional] [readonly] |
|**megabytesPerSecondOfWrite** | **Double** | Disk throughput in MegaBytes per second. |  [optional] [readonly] |
|**monthlyStorageCost** | **Double** | Estimated aggregate storage cost for a 31-day month for this disk. |  [optional] [readonly] |
|**name** | **String** | Name of the assessed disk. |  [optional] [readonly] |
|**numberOfReadOperationsPerSecond** | **Double** | Number of read operations per second for the disk. |  [optional] [readonly] |
|**numberOfWriteOperationsPerSecond** | **Double** | Number of read and write operations per second for the disk. |  [optional] [readonly] |
|**recommendedDiskSize** | [**RecommendedDiskSizeEnum**](#RecommendedDiskSizeEnum) | Recommended Azure size for the disk, given utilization data and preferences set on Assessment. |  [optional] [readonly] |
|**recommendedDiskType** | [**RecommendedDiskTypeEnum**](#RecommendedDiskTypeEnum) | Storage type selected for this disk. |  [optional] [readonly] |
|**suitability** | [**SuitabilityEnum**](#SuitabilityEnum) | Whether this disk is suitable for Azure. |  [optional] [readonly] |
|**suitabilityDetail** | [**SuitabilityDetailEnum**](#SuitabilityDetailEnum) | If disk is suitable to be migrate but some conditions/checks were not considered while calculating suitability, this explains the details. |  [optional] [readonly] |
|**suitabilityExplanation** | [**SuitabilityExplanationEnum**](#SuitabilityExplanationEnum) | If disk is not suitable to be migrated, this explains the reasons and mitigation steps. |  [optional] [readonly] |



## Enum: RecommendedDiskSizeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| STANDARD_S4 | &quot;Standard_S4&quot; |
| STANDARD_S6 | &quot;Standard_S6&quot; |
| STANDARD_S10 | &quot;Standard_S10&quot; |
| STANDARD_S15 | &quot;Standard_S15&quot; |
| STANDARD_S20 | &quot;Standard_S20&quot; |
| STANDARD_S30 | &quot;Standard_S30&quot; |
| STANDARD_S40 | &quot;Standard_S40&quot; |
| STANDARD_S50 | &quot;Standard_S50&quot; |
| PREMIUM_P4 | &quot;Premium_P4&quot; |
| PREMIUM_P6 | &quot;Premium_P6&quot; |
| PREMIUM_P10 | &quot;Premium_P10&quot; |
| PREMIUM_P15 | &quot;Premium_P15&quot; |
| PREMIUM_P20 | &quot;Premium_P20&quot; |
| PREMIUM_P30 | &quot;Premium_P30&quot; |
| PREMIUM_P40 | &quot;Premium_P40&quot; |
| PREMIUM_P50 | &quot;Premium_P50&quot; |
| STANDARD_S60 | &quot;Standard_S60&quot; |
| STANDARD_S70 | &quot;Standard_S70&quot; |
| STANDARD_S80 | &quot;Standard_S80&quot; |
| PREMIUM_P60 | &quot;Premium_P60&quot; |
| PREMIUM_P70 | &quot;Premium_P70&quot; |
| PREMIUM_P80 | &quot;Premium_P80&quot; |
| STANDARD_SSD_E10 | &quot;StandardSSD_E10&quot; |
| STANDARD_SSD_E15 | &quot;StandardSSD_E15&quot; |
| STANDARD_SSD_E20 | &quot;StandardSSD_E20&quot; |
| STANDARD_SSD_E30 | &quot;StandardSSD_E30&quot; |
| STANDARD_SSD_E40 | &quot;StandardSSD_E40&quot; |
| STANDARD_SSD_E50 | &quot;StandardSSD_E50&quot; |
| STANDARD_SSD_E60 | &quot;StandardSSD_E60&quot; |
| STANDARD_SSD_E70 | &quot;StandardSSD_E70&quot; |
| STANDARD_SSD_E80 | &quot;StandardSSD_E80&quot; |
| STANDARD_SSD_E4 | &quot;StandardSSD_E4&quot; |
| STANDARD_SSD_E6 | &quot;StandardSSD_E6&quot; |



## Enum: RecommendedDiskTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| STANDARD_SSD | &quot;StandardSSD&quot; |
| STANDARD_OR_PREMIUM | &quot;StandardOrPremium&quot; |



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
| NUMBER_OF_READ_OPERATIONS_PER_SECOND_MISSING | &quot;NumberOfReadOperationsPerSecondMissing&quot; |
| NUMBER_OF_WRITE_OPERATIONS_PER_SECOND_MISSING | &quot;NumberOfWriteOperationsPerSecondMissing&quot; |
| MEGABYTES_PER_SECOND_OF_READ_MISSING | &quot;MegabytesPerSecondOfReadMissing&quot; |
| MEGABYTES_PER_SECOND_OF_WRITE_MISSING | &quot;MegabytesPerSecondOfWriteMissing&quot; |
| DISK_GIGABYTES_CONSUMED_MISSING | &quot;DiskGigabytesConsumedMissing&quot; |
| DISK_GIGABYTES_PROVISIONED_MISSING | &quot;DiskGigabytesProvisionedMissing&quot; |
| NUMBER_OF_READ_OPERATIONS_PER_SECOND_OUT_OF_RANGE | &quot;NumberOfReadOperationsPerSecondOutOfRange&quot; |
| NUMBER_OF_WRITE_OPERATIONS_PER_SECOND_OUT_OF_RANGE | &quot;NumberOfWriteOperationsPerSecondOutOfRange&quot; |
| MEGABYTES_PER_SECOND_OF_READ_OUT_OF_RANGE | &quot;MegabytesPerSecondOfReadOutOfRange&quot; |
| MEGABYTES_PER_SECOND_OF_WRITE_OUT_OF_RANGE | &quot;MegabytesPerSecondOfWriteOutOfRange&quot; |
| DISK_GIGABYTES_CONSUMED_OUT_OF_RANGE | &quot;DiskGigabytesConsumedOutOfRange&quot; |
| DISK_GIGABYTES_PROVISIONED_OUT_OF_RANGE | &quot;DiskGigabytesProvisionedOutOfRange&quot; |



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
| NO_EA_PRICE_FOUND_FOR_DISK_SIZE | &quot;NoEaPriceFoundForDiskSize&quot; |



