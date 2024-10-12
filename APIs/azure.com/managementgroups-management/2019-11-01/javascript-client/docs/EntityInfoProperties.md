# ManagementGroups.EntityInfoProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The friendly name of the management group. | [optional] 
**inheritedPermissions** | [**Permissions**](Permissions.md) |  | [optional] 
**numberOfChildGroups** | **Number** | Number of children is the number of Groups that are exactly one level underneath the current Group. | [optional] 
**numberOfChildren** | **Number** | Number of children is the number of Groups and Subscriptions that are exactly one level underneath the current Group. | [optional] 
**numberOfDescendants** | **Number** |  | [optional] 
**parent** | [**EntityParentGroupInfo**](EntityParentGroupInfo.md) |  | [optional] 
**parentDisplayNameChain** | **[String]** | The parent display name chain from the root group to the immediate parent | [optional] 
**parentNameChain** | **[String]** | The parent name chain from the root group to the immediate parent | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**tenantId** | **String** | The AAD Tenant ID associated with the entity. For example, 00000000-0000-0000-0000-000000000000 | [optional] 


