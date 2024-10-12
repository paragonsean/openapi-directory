# CloudIdentityApi.GroupRelation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Display name for this group. | [optional] 
**group** | **String** | Resource name for this group. | [optional] 
**groupKey** | [**EntityKey**](EntityKey.md) |  | [optional] 
**labels** | **{String: String}** | Labels for Group resource. | [optional] 
**relationType** | **String** | The relation between the member and the transitive group. | [optional] 
**roles** | [**[TransitiveMembershipRole]**](TransitiveMembershipRole.md) | Membership roles of the member for the group. | [optional] 



## Enum: RelationTypeEnum


* `RELATION_TYPE_UNSPECIFIED` (value: `"RELATION_TYPE_UNSPECIFIED"`)

* `DIRECT` (value: `"DIRECT"`)

* `INDIRECT` (value: `"INDIRECT"`)

* `DIRECT_AND_INDIRECT` (value: `"DIRECT_AND_INDIRECT"`)




