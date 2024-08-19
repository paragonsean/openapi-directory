# VertexAiApi.GoogleCloudAiplatformV1beta1Tensor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolVal** | **[Boolean]** | Type specific representations that make it easy to create tensor protos in all languages. Only the representation corresponding to \&quot;dtype\&quot; can be set. The values hold the flattened representation of the tensor in row major order. BOOL | [optional] 
**bytesVal** | **[Blob]** | STRING | [optional] 
**doubleVal** | **[Number]** | DOUBLE | [optional] 
**dtype** | **String** | The data type of tensor. | [optional] 
**floatVal** | **[Number]** | FLOAT | [optional] 
**int64Val** | **[String]** | INT64 | [optional] 
**intVal** | **[Number]** | INT_8 INT_16 INT_32 | [optional] 
**listVal** | [**[GoogleCloudAiplatformV1beta1Tensor]**](GoogleCloudAiplatformV1beta1Tensor.md) | A list of tensor values. | [optional] 
**shape** | **[String]** | Shape of the tensor. | [optional] 
**stringVal** | **[String]** | STRING | [optional] 
**structVal** | [**{String: GoogleCloudAiplatformV1beta1Tensor}**](GoogleCloudAiplatformV1beta1Tensor.md) | A map of string to tensor. | [optional] 
**tensorVal** | **Blob** | Serialized raw tensor content. | [optional] 
**uint64Val** | **[String]** | UINT64 | [optional] 
**uintVal** | **[Number]** | UINT8 UINT16 UINT32 | [optional] 



## Enum: DtypeEnum


* `DATA_TYPE_UNSPECIFIED` (value: `"DATA_TYPE_UNSPECIFIED"`)

* `BOOL` (value: `"BOOL"`)

* `STRING` (value: `"STRING"`)

* `FLOAT` (value: `"FLOAT"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `INT8` (value: `"INT8"`)

* `INT16` (value: `"INT16"`)

* `INT32` (value: `"INT32"`)

* `INT64` (value: `"INT64"`)

* `UINT8` (value: `"UINT8"`)

* `UINT16` (value: `"UINT16"`)

* `UINT32` (value: `"UINT32"`)

* `UINT64` (value: `"UINT64"`)




