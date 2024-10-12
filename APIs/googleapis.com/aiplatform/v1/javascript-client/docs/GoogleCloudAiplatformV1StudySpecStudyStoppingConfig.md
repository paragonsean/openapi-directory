# VertexAiApi.GoogleCloudAiplatformV1StudySpecStudyStoppingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxDurationNoProgress** | **String** | If the objective value has not improved for this much time, stop the study. WARNING: Effective only for single-objective studies. | [optional] 
**maxNumTrials** | **Number** | If there are more than this many trials, stop the study. | [optional] 
**maxNumTrialsNoProgress** | **Number** | If the objective value has not improved for this many consecutive trials, stop the study. WARNING: Effective only for single-objective studies. | [optional] 
**maximumRuntimeConstraint** | [**GoogleCloudAiplatformV1StudyTimeConstraint**](GoogleCloudAiplatformV1StudyTimeConstraint.md) |  | [optional] 
**minNumTrials** | **Number** | If there are fewer than this many COMPLETED trials, do not stop the study. | [optional] 
**minimumRuntimeConstraint** | [**GoogleCloudAiplatformV1StudyTimeConstraint**](GoogleCloudAiplatformV1StudyTimeConstraint.md) |  | [optional] 
**shouldStopAsap** | **Boolean** | If true, a Study enters STOPPING_ASAP whenever it would normally enters STOPPING state. The bottom line is: set to true if you want to interrupt on-going evaluations of Trials as soon as the study stopping condition is met. (Please see Study.State documentation for the source of truth). | [optional] 


