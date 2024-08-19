

# GoogleCloudAiplatformV1beta1Presets

Preset configuration for example-based explanations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modality** | [**ModalityEnum**](#ModalityEnum) | The modality of the uploaded model, which automatically configures the distance measurement and feature normalization for the underlying example index and queries. If your model does not precisely fit one of these types, it is okay to choose the closest type. |  [optional] |
|**query** | [**QueryEnum**](#QueryEnum) | Preset option controlling parameters for speed-precision trade-off when querying for examples. If omitted, defaults to &#x60;PRECISE&#x60;. |  [optional] |



## Enum: ModalityEnum

| Name | Value |
|---- | -----|
| MODALITY_UNSPECIFIED | &quot;MODALITY_UNSPECIFIED&quot; |
| IMAGE | &quot;IMAGE&quot; |
| TEXT | &quot;TEXT&quot; |
| TABULAR | &quot;TABULAR&quot; |



## Enum: QueryEnum

| Name | Value |
|---- | -----|
| PRECISE | &quot;PRECISE&quot; |
| FAST | &quot;FAST&quot; |



