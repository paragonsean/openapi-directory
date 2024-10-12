

# GoogleCloudAiplatformV1Tensor

A tensor value type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolVal** | **List&lt;Boolean&gt;** | Type specific representations that make it easy to create tensor protos in all languages. Only the representation corresponding to \&quot;dtype\&quot; can be set. The values hold the flattened representation of the tensor in row major order. BOOL |  [optional] |
|**bytesVal** | **List&lt;byte[]&gt;** | STRING |  [optional] |
|**doubleVal** | **List&lt;Double&gt;** | DOUBLE |  [optional] |
|**dtype** | [**DtypeEnum**](#DtypeEnum) | The data type of tensor. |  [optional] |
|**floatVal** | **List&lt;Float&gt;** | FLOAT |  [optional] |
|**int64Val** | **List&lt;String&gt;** | INT64 |  [optional] |
|**intVal** | **List&lt;Integer&gt;** | INT_8 INT_16 INT_32 |  [optional] |
|**listVal** | [**List&lt;GoogleCloudAiplatformV1Tensor&gt;**](GoogleCloudAiplatformV1Tensor.md) | A list of tensor values. |  [optional] |
|**shape** | **List&lt;String&gt;** | Shape of the tensor. |  [optional] |
|**stringVal** | **List&lt;String&gt;** | STRING |  [optional] |
|**structVal** | [**Map&lt;String, GoogleCloudAiplatformV1Tensor&gt;**](GoogleCloudAiplatformV1Tensor.md) | A map of string to tensor. |  [optional] |
|**tensorVal** | **byte[]** | Serialized raw tensor content. |  [optional] |
|**uint64Val** | **List&lt;String&gt;** | UINT64 |  [optional] |
|**uintVal** | **List&lt;Integer&gt;** | UINT8 UINT16 UINT32 |  [optional] |



## Enum: DtypeEnum

| Name | Value |
|---- | -----|
| DATA_TYPE_UNSPECIFIED | &quot;DATA_TYPE_UNSPECIFIED&quot; |
| BOOL | &quot;BOOL&quot; |
| STRING | &quot;STRING&quot; |
| FLOAT | &quot;FLOAT&quot; |
| DOUBLE | &quot;DOUBLE&quot; |
| INT8 | &quot;INT8&quot; |
| INT16 | &quot;INT16&quot; |
| INT32 | &quot;INT32&quot; |
| INT64 | &quot;INT64&quot; |
| UINT8 | &quot;UINT8&quot; |
| UINT16 | &quot;UINT16&quot; |
| UINT32 | &quot;UINT32&quot; |
| UINT64 | &quot;UINT64&quot; |



