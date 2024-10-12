

# VideoAdSequenceStep

The detail of a single step in a VideoAdSequence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroupId** | **String** | The ID of the corresponding ad group of the step. |  [optional] |
|**interactionType** | [**InteractionTypeEnum**](#InteractionTypeEnum) | The interaction on the previous step that will lead the viewer to this step. The first step does not have interaction_type. |  [optional] |
|**previousStepId** | **String** | The ID of the previous step. The first step does not have previous step. |  [optional] |
|**stepId** | **String** | The ID of the step. |  [optional] |



## Enum: InteractionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INTERACTION_TYPE_UNSPECIFIED&quot; |
| PAID_VIEW | &quot;INTERACTION_TYPE_PAID_VIEW&quot; |
| SKIP | &quot;INTERACTION_TYPE_SKIP&quot; |
| IMPRESSION | &quot;INTERACTION_TYPE_IMPRESSION&quot; |
| ENGAGED_IMPRESSION | &quot;INTERACTION_TYPE_ENGAGED_IMPRESSION&quot; |



