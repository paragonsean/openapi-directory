

# MemberRelation

Message representing a transitive membership of a group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**member** | **String** | Resource name for this member. |  [optional] |
|**preferredMemberKey** | [**List&lt;EntityKey&gt;**](EntityKey.md) | Entity key has an id and a namespace. In case of discussion forums, the id will be an email address without a namespace. |  [optional] |
|**relationType** | [**RelationTypeEnum**](#RelationTypeEnum) | The relation between the group and the transitive membership. |  [optional] |
|**roles** | [**List&lt;TransitiveMembershipRole&gt;**](TransitiveMembershipRole.md) | The membership role details (i.e name of role and expiry time). |  [optional] |



## Enum: RelationTypeEnum

| Name | Value |
|---- | -----|
| RELATION_TYPE_UNSPECIFIED | &quot;RELATION_TYPE_UNSPECIFIED&quot; |
| DIRECT | &quot;DIRECT&quot; |
| INDIRECT | &quot;INDIRECT&quot; |
| DIRECT_AND_INDIRECT | &quot;DIRECT_AND_INDIRECT&quot; |



