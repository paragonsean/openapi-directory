# BigQueryApi.StagePerformanceStandaloneInsight

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biEngineReasons** | [**[BiEngineReason]**](BiEngineReason.md) | Output only. If present, the stage had the following reasons for being disqualified from BI Engine execution. | [optional] [readonly] 
**highCardinalityJoins** | [**[HighCardinalityJoin]**](HighCardinalityJoin.md) | Output only. High cardinality joins in the stage. | [optional] [readonly] 
**insufficientShuffleQuota** | **Boolean** | Output only. True if the stage has insufficient shuffle quota. | [optional] [readonly] 
**slotContention** | **Boolean** | Output only. True if the stage has a slot contention issue. | [optional] [readonly] 
**stageId** | **String** | Output only. The stage id that the insight mapped to. | [optional] [readonly] 


