

# RelevantLocation

Information about another location that is related to current one. The relation can be any one of DEPARTMENT_OF or INDEPENDENT_ESTABLISHMENT_OF, and the location specified here can be on either side (parent/child) of the location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**placeId** | **String** | Required. Specify the location that is on the other side of the relation by its placeID. |  [optional] |
|**relationType** | [**RelationTypeEnum**](#RelationTypeEnum) | Required. The type of the relationship. |  [optional] |



## Enum: RelationTypeEnum

| Name | Value |
|---- | -----|
| RELATION_TYPE_UNSPECIFIED | &quot;RELATION_TYPE_UNSPECIFIED&quot; |
| DEPARTMENT_OF | &quot;DEPARTMENT_OF&quot; |
| INDEPENDENT_ESTABLISHMENT_IN | &quot;INDEPENDENT_ESTABLISHMENT_IN&quot; |



