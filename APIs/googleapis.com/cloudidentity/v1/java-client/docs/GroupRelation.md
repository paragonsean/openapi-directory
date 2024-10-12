

# GroupRelation

Message representing a transitive group of a user or a group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Display name for this group. |  [optional] |
|**group** | **String** | Resource name for this group. |  [optional] |
|**groupKey** | [**EntityKey**](EntityKey.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels for Group resource. |  [optional] |
|**relationType** | [**RelationTypeEnum**](#RelationTypeEnum) | The relation between the member and the transitive group. |  [optional] |
|**roles** | [**List&lt;TransitiveMembershipRole&gt;**](TransitiveMembershipRole.md) | Membership roles of the member for the group. |  [optional] |



## Enum: RelationTypeEnum

| Name | Value |
|---- | -----|
| RELATION_TYPE_UNSPECIFIED | &quot;RELATION_TYPE_UNSPECIFIED&quot; |
| DIRECT | &quot;DIRECT&quot; |
| INDIRECT | &quot;INDIRECT&quot; |
| DIRECT_AND_INDIRECT | &quot;DIRECT_AND_INDIRECT&quot; |



