

# GoogleCloudAiplatformV1ModelSourceInfo

Detail description of the source information of the model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copy** | **Boolean** | If this Model is copy of another Model. If true then source_type pertains to the original. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Type of the model source. |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| MODEL_SOURCE_TYPE_UNSPECIFIED | &quot;MODEL_SOURCE_TYPE_UNSPECIFIED&quot; |
| AUTOML | &quot;AUTOML&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
| BQML | &quot;BQML&quot; |
| MODEL_GARDEN | &quot;MODEL_GARDEN&quot; |
| GENIE | &quot;GENIE&quot; |
| CUSTOM_TEXT_EMBEDDING | &quot;CUSTOM_TEXT_EMBEDDING&quot; |
| MARKETPLACE | &quot;MARKETPLACE&quot; |



