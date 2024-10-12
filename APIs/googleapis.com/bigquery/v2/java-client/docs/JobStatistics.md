

# JobStatistics

Statistics for a single job execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completionRatio** | **Double** | Output only. [TrustedTester] Job progress (0.0 -&gt; 1.0) for LOAD and EXTRACT jobs. |  [optional] [readonly] |
|**copy** | [**JobStatistics5**](JobStatistics5.md) |  |  [optional] |
|**creationTime** | **String** | Output only. Creation time of this job, in milliseconds since the epoch. This field will be present on all jobs. |  [optional] [readonly] |
|**dataMaskingStatistics** | [**DataMaskingStatistics**](DataMaskingStatistics.md) |  |  [optional] |
|**endTime** | **String** | Output only. End time of this job, in milliseconds since the epoch. This field will be present whenever a job is in the DONE state. |  [optional] [readonly] |
|**extract** | [**JobStatistics4**](JobStatistics4.md) |  |  [optional] |
|**finalExecutionDurationMs** | **String** | Output only. The duration in milliseconds of the execution of the final attempt of this job, as BigQuery may internally re-attempt to execute the job. |  [optional] [readonly] |
|**load** | [**JobStatistics3**](JobStatistics3.md) |  |  [optional] |
|**numChildJobs** | **String** | Output only. Number of child jobs executed. |  [optional] [readonly] |
|**parentJobId** | **String** | Output only. If this is a child job, specifies the job ID of the parent. |  [optional] [readonly] |
|**query** | [**JobStatistics2**](JobStatistics2.md) |  |  [optional] |
|**quotaDeferments** | **List&lt;String&gt;** | Output only. Quotas which delayed this job&#39;s start time. |  [optional] [readonly] |
|**reservationUsage** | [**List&lt;JobStatisticsReservationUsageInner&gt;**](JobStatisticsReservationUsageInner.md) | Output only. Job resource usage breakdown by reservation. This field reported misleading information and will no longer be populated. |  [optional] [readonly] |
|**reservationId** | **String** | Output only. Name of the primary reservation assigned to this job. Note that this could be different than reservations reported in the reservation usage field if parent reservations were used to execute this job. |  [optional] [readonly] |
|**rowLevelSecurityStatistics** | [**RowLevelSecurityStatistics**](RowLevelSecurityStatistics.md) |  |  [optional] |
|**scriptStatistics** | [**ScriptStatistics**](ScriptStatistics.md) |  |  [optional] |
|**sessionInfo** | [**SessionInfo**](SessionInfo.md) |  |  [optional] |
|**startTime** | **String** | Output only. Start time of this job, in milliseconds since the epoch. This field will be present when the job transitions from the PENDING state to either RUNNING or DONE. |  [optional] [readonly] |
|**totalBytesProcessed** | **String** | Output only. Total bytes processed for the job. |  [optional] [readonly] |
|**totalSlotMs** | **String** | Output only. Slot-milliseconds for the job. |  [optional] [readonly] |
|**transactionInfo** | [**TransactionInfo**](TransactionInfo.md) |  |  [optional] |



