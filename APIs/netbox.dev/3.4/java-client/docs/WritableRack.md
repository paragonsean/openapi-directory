

# WritableRack


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTag** | **String** | A unique tag used to identify this rack |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**descUnits** | **Boolean** | Units are numbered top-to-bottom |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceCount** | **Integer** |  |  [optional] [readonly] |
|**display** | **String** |  |  [optional] [readonly] |
|**facilityId** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**location** | **Integer** |  |  [optional] |
|**maxWeight** | **Integer** | Maximum load capacity for the rack |  [optional] |
|**mountingDepth** | **Integer** | Maximum depth of a mounted device, in millimeters. For four-post racks, this is the distance between the front and rear rails. |  [optional] |
|**name** | **String** |  |  |
|**outerDepth** | **Integer** | Outer dimension of rack (depth) |  [optional] |
|**outerUnit** | [**OuterUnitEnum**](#OuterUnitEnum) |  |  [optional] |
|**outerWidth** | **Integer** | Outer dimension of rack (width) |  [optional] |
|**powerfeedCount** | **Integer** |  |  [optional] [readonly] |
|**role** | **Integer** | Functional role |  [optional] |
|**serial** | **String** |  |  [optional] |
|**site** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**uHeight** | **Integer** | Height in rack units |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**weight** | **BigDecimal** |  |  [optional] |
|**weightUnit** | [**WeightUnitEnum**](#WeightUnitEnum) |  |  [optional] |
|**width** | [**WidthEnum**](#WidthEnum) | Rail-to-rail width |  [optional] |



## Enum: OuterUnitEnum

| Name | Value |
|---- | -----|
| MM | &quot;mm&quot; |
| IN | &quot;in&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RESERVED | &quot;reserved&quot; |
| AVAILABLE | &quot;available&quot; |
| PLANNED | &quot;planned&quot; |
| ACTIVE | &quot;active&quot; |
| DEPRECATED | &quot;deprecated&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| _2_POST_FRAME | &quot;2-post-frame&quot; |
| _4_POST_FRAME | &quot;4-post-frame&quot; |
| _4_POST_CABINET | &quot;4-post-cabinet&quot; |
| WALL_FRAME | &quot;wall-frame&quot; |
| WALL_FRAME_VERTICAL | &quot;wall-frame-vertical&quot; |
| WALL_CABINET | &quot;wall-cabinet&quot; |
| WALL_CABINET_VERTICAL | &quot;wall-cabinet-vertical&quot; |



## Enum: WeightUnitEnum

| Name | Value |
|---- | -----|
| KG | &quot;kg&quot; |
| G | &quot;g&quot; |
| LB | &quot;lb&quot; |
| OZ | &quot;oz&quot; |



## Enum: WidthEnum

| Name | Value |
|---- | -----|
| NUMBER_10 | 10 |
| NUMBER_19 | 19 |
| NUMBER_21 | 21 |
| NUMBER_23 | 23 |



