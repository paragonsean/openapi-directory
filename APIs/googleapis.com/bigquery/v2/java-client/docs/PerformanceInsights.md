

# PerformanceInsights

Performance insights for the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avgPreviousExecutionMs** | **String** | Output only. Average execution ms of previous runs. Indicates the job ran slow compared to previous executions. To find previous executions, use INFORMATION_SCHEMA tables and filter jobs with same query hash. |  [optional] [readonly] |
|**stagePerformanceChangeInsights** | [**List&lt;StagePerformanceChangeInsight&gt;**](StagePerformanceChangeInsight.md) | Output only. Query stage performance insights compared to previous runs, for diagnosing performance regression. |  [optional] [readonly] |
|**stagePerformanceStandaloneInsights** | [**List&lt;StagePerformanceStandaloneInsight&gt;**](StagePerformanceStandaloneInsight.md) | Output only. Standalone query stage performance insights, for exploring potential improvements. |  [optional] [readonly] |



