# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpointName** | **String** | Optional. An unique name of pretrained model checkpoint provided in model garden, it will be mapped to a GCS location internally. | [optional] 
**datasetConfig** | **{String: String}** | Customizable dataset settings, used in the &#x60;model_garden_trainer&#x60;. | [optional] 
**studySpec** | [**GoogleCloudAiplatformV1beta1StudySpec**](GoogleCloudAiplatformV1beta1StudySpec.md) |  | [optional] 
**trainerConfig** | **{String: String}** | Customizable trainer settings, used in the &#x60;model_garden_trainer&#x60;. | [optional] 
**trainerType** | **String** |  | [optional] 



## Enum: TrainerTypeEnum


* `TRAINER_TYPE_UNSPECIFIED` (value: `"TRAINER_TYPE_UNSPECIFIED"`)

* `AUTOML_TRAINER` (value: `"AUTOML_TRAINER"`)

* `MODEL_GARDEN_TRAINER` (value: `"MODEL_GARDEN_TRAINER"`)




