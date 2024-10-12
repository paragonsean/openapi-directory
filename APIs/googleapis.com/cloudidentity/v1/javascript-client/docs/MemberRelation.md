# CloudIdentityApi.MemberRelation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **String** | Resource name for this member. | [optional] 
**preferredMemberKey** | [**[EntityKey]**](EntityKey.md) | Entity key has an id and a namespace. In case of discussion forums, the id will be an email address without a namespace. | [optional] 
**relationType** | **String** | The relation between the group and the transitive member. | [optional] 
**roles** | [**[TransitiveMembershipRole]**](TransitiveMembershipRole.md) | The membership role details (i.e name of role and expiry time). | [optional] 



## Enum: RelationTypeEnum


* `RELATION_TYPE_UNSPECIFIED` (value: `"RELATION_TYPE_UNSPECIFIED"`)

* `DIRECT` (value: `"DIRECT"`)

* `INDIRECT` (value: `"INDIRECT"`)

* `DIRECT_AND_INDIRECT` (value: `"DIRECT_AND_INDIRECT"`)




