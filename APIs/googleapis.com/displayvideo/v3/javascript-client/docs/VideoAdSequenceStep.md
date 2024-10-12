# DisplayVideo360Api.VideoAdSequenceStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroupId** | **String** | The ID of the corresponding ad group of the step. | [optional] 
**interactionType** | **String** | The interaction on the previous step that will lead the viewer to this step. The first step does not have interaction_type. | [optional] 
**previousStepId** | **String** | The ID of the previous step. The first step does not have previous step. | [optional] 
**stepId** | **String** | The ID of the step. | [optional] 



## Enum: InteractionTypeEnum


* `UNSPECIFIED` (value: `"INTERACTION_TYPE_UNSPECIFIED"`)

* `PAID_VIEW` (value: `"INTERACTION_TYPE_PAID_VIEW"`)

* `SKIP` (value: `"INTERACTION_TYPE_SKIP"`)

* `IMPRESSION` (value: `"INTERACTION_TYPE_IMPRESSION"`)

* `ENGAGED_IMPRESSION` (value: `"INTERACTION_TYPE_ENGAGED_IMPRESSION"`)




