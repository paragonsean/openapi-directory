

# GoogleCloudAiplatformV1beta1Schema

Schema is used to define the format of input/output data. Represents a select subset of an [OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema). More fields may be added in the future as needed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. The description of the data. |  [optional] |
|**_enum** | **List&lt;String&gt;** | Optional. Possible values of the element of Type.STRING with enum format. For example we can define an Enum Direction as : {type:STRING, format:enum, enum:[\&quot;EAST\&quot;, NORTH\&quot;, \&quot;SOUTH\&quot;, \&quot;WEST\&quot;]} |  [optional] |
|**example** | **Object** | Optional. Example of the object. Will only populated when the object is the root. |  [optional] |
|**format** | **String** | Optional. The format of the data. Supported formats: for NUMBER type: float, double for INTEGER type: int32, int64 |  [optional] |
|**items** | [**GoogleCloudAiplatformV1beta1Schema**](GoogleCloudAiplatformV1beta1Schema.md) |  |  [optional] |
|**nullable** | **Boolean** | Optional. Indicates if the value may be null. |  [optional] |
|**properties** | [**Map&lt;String, GoogleCloudAiplatformV1beta1Schema&gt;**](GoogleCloudAiplatformV1beta1Schema.md) | Optional. Properties of Type.OBJECT. |  [optional] |
|**required** | **List&lt;String&gt;** | Optional. Required properties of Type.OBJECT. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. The type of the data. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| STRING | &quot;STRING&quot; |
| NUMBER | &quot;NUMBER&quot; |
| INTEGER | &quot;INTEGER&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| ARRAY | &quot;ARRAY&quot; |
| OBJECT | &quot;OBJECT&quot; |



