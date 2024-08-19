# VertexAiApi.GoogleCloudAiplatformV1Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. The description of the data. | [optional] 
**_enum** | **[String]** | Optional. Possible values of the element of Type.STRING with enum format. For example we can define an Enum Direction as : {type:STRING, format:enum, enum:[\&quot;EAST\&quot;, NORTH\&quot;, \&quot;SOUTH\&quot;, \&quot;WEST\&quot;]} | [optional] 
**example** | **Object** | Optional. Example of the object. Will only populated when the object is the root. | [optional] 
**format** | **String** | Optional. The format of the data. Supported formats: for NUMBER type: float, double for INTEGER type: int32, int64 | [optional] 
**items** | [**GoogleCloudAiplatformV1Schema**](GoogleCloudAiplatformV1Schema.md) |  | [optional] 
**nullable** | **Boolean** | Optional. Indicates if the value may be null. | [optional] 
**properties** | [**{String: GoogleCloudAiplatformV1Schema}**](GoogleCloudAiplatformV1Schema.md) | Optional. Properties of Type.OBJECT. | [optional] 
**required** | **[String]** | Optional. Required properties of Type.OBJECT. | [optional] 
**type** | **String** | Optional. The type of the data. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `STRING` (value: `"STRING"`)

* `NUMBER` (value: `"NUMBER"`)

* `INTEGER` (value: `"INTEGER"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `ARRAY` (value: `"ARRAY"`)

* `OBJECT` (value: `"OBJECT"`)




