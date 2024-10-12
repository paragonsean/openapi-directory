

# GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter

A wrapper class which contains the tunable parameters in an AutoML Image training job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkpointName** | **String** | Optional. An unique name of pretrained model checkpoint provided in model garden, it will be mapped to a GCS location internally. |  [optional] |
|**datasetConfig** | **Map&lt;String, String&gt;** | Customizable dataset settings, used in the &#x60;model_garden_trainer&#x60;. |  [optional] |
|**studySpec** | [**GoogleCloudAiplatformV1StudySpec**](GoogleCloudAiplatformV1StudySpec.md) |  |  [optional] |
|**trainerConfig** | **Map&lt;String, String&gt;** | Customizable trainer settings, used in the &#x60;model_garden_trainer&#x60;. |  [optional] |
|**trainerType** | [**TrainerTypeEnum**](#TrainerTypeEnum) |  |  [optional] |



## Enum: TrainerTypeEnum

| Name | Value |
|---- | -----|
| TRAINER_TYPE_UNSPECIFIED | &quot;TRAINER_TYPE_UNSPECIFIED&quot; |
| AUTOML_TRAINER | &quot;AUTOML_TRAINER&quot; |
| MODEL_GARDEN_TRAINER | &quot;MODEL_GARDEN_TRAINER&quot; |



