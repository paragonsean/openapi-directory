# VertexAiApi.GoogleCloudAiplatformV1beta1StudySpecMetricSpecSafetyMetricConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desiredMinSafeTrialsFraction** | **Number** | Desired minimum fraction of safe trials (over total number of trials) that should be targeted by the algorithm at any time during the study (best effort). This should be between 0.0 and 1.0 and a value of 0.0 means that there is no minimum and an algorithm proceeds without targeting any specific fraction. A value of 1.0 means that the algorithm attempts to only Suggest safe Trials. | [optional] 
**safetyThreshold** | **Number** | Safety threshold (boundary value between safe and unsafe). NOTE that if you leave SafetyMetricConfig unset, a default value of 0 will be used. | [optional] 


