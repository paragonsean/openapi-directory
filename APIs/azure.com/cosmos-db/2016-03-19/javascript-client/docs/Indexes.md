# CosmosDb.Indexes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataType** | **String** | The datatype for which the indexing behavior is applied to. | [optional] [default to &#39;String&#39;]
**kind** | **String** | Indicates the type of index. | [optional] [default to &#39;Hash&#39;]
**precision** | **Number** | The precision of the index. -1 is maximum precision. | [optional] 



## Enum: DataTypeEnum


* `String` (value: `"String"`)

* `Number` (value: `"Number"`)

* `Point` (value: `"Point"`)

* `Polygon` (value: `"Polygon"`)

* `LineString` (value: `"LineString"`)

* `MultiPolygon` (value: `"MultiPolygon"`)





## Enum: KindEnum


* `Hash` (value: `"Hash"`)

* `Range` (value: `"Range"`)

* `Spatial` (value: `"Spatial"`)




