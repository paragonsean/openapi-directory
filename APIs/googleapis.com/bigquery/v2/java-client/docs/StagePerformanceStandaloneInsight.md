

# StagePerformanceStandaloneInsight

Standalone performance insights for a specific stage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**biEngineReasons** | [**List&lt;BiEngineReason&gt;**](BiEngineReason.md) | Output only. If present, the stage had the following reasons for being disqualified from BI Engine execution. |  [optional] [readonly] |
|**highCardinalityJoins** | [**List&lt;HighCardinalityJoin&gt;**](HighCardinalityJoin.md) | Output only. High cardinality joins in the stage. |  [optional] [readonly] |
|**insufficientShuffleQuota** | **Boolean** | Output only. True if the stage has insufficient shuffle quota. |  [optional] [readonly] |
|**slotContention** | **Boolean** | Output only. True if the stage has a slot contention issue. |  [optional] [readonly] |
|**stageId** | **String** | Output only. The stage id that the insight mapped to. |  [optional] [readonly] |



