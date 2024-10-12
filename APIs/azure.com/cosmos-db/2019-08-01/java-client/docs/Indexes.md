

# Indexes

The indexes for the path.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | The datatype for which the indexing behavior is applied to. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Indicates the type of index. |  [optional] |
|**precision** | **Integer** | The precision of the index. -1 is maximum precision. |  [optional] |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;String&quot; |
| NUMBER | &quot;Number&quot; |
| POINT | &quot;Point&quot; |
| POLYGON | &quot;Polygon&quot; |
| LINE_STRING | &quot;LineString&quot; |
| MULTI_POLYGON | &quot;MultiPolygon&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| HASH | &quot;Hash&quot; |
| RANGE | &quot;Range&quot; |
| SPATIAL | &quot;Spatial&quot; |



