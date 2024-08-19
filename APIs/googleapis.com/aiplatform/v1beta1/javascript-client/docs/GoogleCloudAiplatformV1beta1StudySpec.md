# VertexAiApi.GoogleCloudAiplatformV1beta1StudySpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | The search algorithm specified for the Study. | [optional] 
**convexAutomatedStoppingSpec** | [**GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec**](GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec.md) |  | [optional] 
**convexStopConfig** | [**GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig**](GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig.md) |  | [optional] 
**decayCurveStoppingSpec** | [**GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec**](GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec.md) |  | [optional] 
**measurementSelectionType** | **String** | Describe which measurement selection type will be used | [optional] 
**medianAutomatedStoppingSpec** | [**GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec**](GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec.md) |  | [optional] 
**metrics** | [**[GoogleCloudAiplatformV1beta1StudySpecMetricSpec]**](GoogleCloudAiplatformV1beta1StudySpecMetricSpec.md) | Required. Metric specs for the Study. | [optional] 
**observationNoise** | **String** | The observation noise level of the study. Currently only supported by the Vertex AI Vizier service. Not supported by HyperparameterTuningJob or TrainingPipeline. | [optional] 
**parameters** | [**[GoogleCloudAiplatformV1beta1StudySpecParameterSpec]**](GoogleCloudAiplatformV1beta1StudySpecParameterSpec.md) | Required. The set of parameters to tune. | [optional] 
**studyStoppingConfig** | [**GoogleCloudAiplatformV1beta1StudySpecStudyStoppingConfig**](GoogleCloudAiplatformV1beta1StudySpecStudyStoppingConfig.md) |  | [optional] 
**transferLearningConfig** | [**GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig**](GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig.md) |  | [optional] 



## Enum: AlgorithmEnum


* `ALGORITHM_UNSPECIFIED` (value: `"ALGORITHM_UNSPECIFIED"`)

* `GRID_SEARCH` (value: `"GRID_SEARCH"`)

* `RANDOM_SEARCH` (value: `"RANDOM_SEARCH"`)





## Enum: MeasurementSelectionTypeEnum


* `MEASUREMENT_SELECTION_TYPE_UNSPECIFIED` (value: `"MEASUREMENT_SELECTION_TYPE_UNSPECIFIED"`)

* `LAST_MEASUREMENT` (value: `"LAST_MEASUREMENT"`)

* `BEST_MEASUREMENT` (value: `"BEST_MEASUREMENT"`)





## Enum: ObservationNoiseEnum


* `OBSERVATION_NOISE_UNSPECIFIED` (value: `"OBSERVATION_NOISE_UNSPECIFIED"`)

* `LOW` (value: `"LOW"`)

* `HIGH` (value: `"HIGH"`)




