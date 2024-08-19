# VertexAiApi.GoogleCloudAiplatformV1beta1Presets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modality** | **String** | The modality of the uploaded model, which automatically configures the distance measurement and feature normalization for the underlying example index and queries. If your model does not precisely fit one of these types, it is okay to choose the closest type. | [optional] 
**query** | **String** | Preset option controlling parameters for speed-precision trade-off when querying for examples. If omitted, defaults to &#x60;PRECISE&#x60;. | [optional] 



## Enum: ModalityEnum


* `MODALITY_UNSPECIFIED` (value: `"MODALITY_UNSPECIFIED"`)

* `IMAGE` (value: `"IMAGE"`)

* `TEXT` (value: `"TEXT"`)

* `TABULAR` (value: `"TABULAR"`)





## Enum: QueryEnum


* `PRECISE` (value: `"PRECISE"`)

* `FAST` (value: `"FAST"`)




