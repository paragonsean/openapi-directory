

# Relation

Represents a relation to another feature in the tile. For example, a building might be occupied by a given POI. The related feature can be retrieved using the related feature index.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**relatedFeatureIndex** | **Integer** | Zero-based index to look up the related feature from the list of features in the tile. |  [optional] |
|**relationType** | [**RelationTypeEnum**](#RelationTypeEnum) | Relation type between the origin feature to the related feature. |  [optional] |



## Enum: RelationTypeEnum

| Name | Value |
|---- | -----|
| RELATION_TYPE_UNSPECIFIED | &quot;RELATION_TYPE_UNSPECIFIED&quot; |
| OCCUPIES | &quot;OCCUPIES&quot; |
| PRIMARILY_OCCUPIED_BY | &quot;PRIMARILY_OCCUPIED_BY&quot; |



