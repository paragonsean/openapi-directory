

# GoogleCloudAiplatformV1StudySpec

Represents specification of a Study.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | The search algorithm specified for the Study. |  [optional] |
|**convexAutomatedStoppingSpec** | [**GoogleCloudAiplatformV1StudySpecConvexAutomatedStoppingSpec**](GoogleCloudAiplatformV1StudySpecConvexAutomatedStoppingSpec.md) |  |  [optional] |
|**decayCurveStoppingSpec** | [**GoogleCloudAiplatformV1StudySpecDecayCurveAutomatedStoppingSpec**](GoogleCloudAiplatformV1StudySpecDecayCurveAutomatedStoppingSpec.md) |  |  [optional] |
|**measurementSelectionType** | [**MeasurementSelectionTypeEnum**](#MeasurementSelectionTypeEnum) | Describe which measurement selection type will be used |  [optional] |
|**medianAutomatedStoppingSpec** | [**GoogleCloudAiplatformV1StudySpecMedianAutomatedStoppingSpec**](GoogleCloudAiplatformV1StudySpecMedianAutomatedStoppingSpec.md) |  |  [optional] |
|**metrics** | [**List&lt;GoogleCloudAiplatformV1StudySpecMetricSpec&gt;**](GoogleCloudAiplatformV1StudySpecMetricSpec.md) | Required. Metric specs for the Study. |  [optional] |
|**observationNoise** | [**ObservationNoiseEnum**](#ObservationNoiseEnum) | The observation noise level of the study. Currently only supported by the Vertex AI Vizier service. Not supported by HyperparameterTuningJob or TrainingPipeline. |  [optional] |
|**parameters** | [**List&lt;GoogleCloudAiplatformV1StudySpecParameterSpec&gt;**](GoogleCloudAiplatformV1StudySpecParameterSpec.md) | Required. The set of parameters to tune. |  [optional] |
|**studyStoppingConfig** | [**GoogleCloudAiplatformV1StudySpecStudyStoppingConfig**](GoogleCloudAiplatformV1StudySpecStudyStoppingConfig.md) |  |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| ALGORITHM_UNSPECIFIED | &quot;ALGORITHM_UNSPECIFIED&quot; |
| GRID_SEARCH | &quot;GRID_SEARCH&quot; |
| RANDOM_SEARCH | &quot;RANDOM_SEARCH&quot; |



## Enum: MeasurementSelectionTypeEnum

| Name | Value |
|---- | -----|
| MEASUREMENT_SELECTION_TYPE_UNSPECIFIED | &quot;MEASUREMENT_SELECTION_TYPE_UNSPECIFIED&quot; |
| LAST_MEASUREMENT | &quot;LAST_MEASUREMENT&quot; |
| BEST_MEASUREMENT | &quot;BEST_MEASUREMENT&quot; |



## Enum: ObservationNoiseEnum

| Name | Value |
|---- | -----|
| OBSERVATION_NOISE_UNSPECIFIED | &quot;OBSERVATION_NOISE_UNSPECIFIED&quot; |
| LOW | &quot;LOW&quot; |
| HIGH | &quot;HIGH&quot; |



