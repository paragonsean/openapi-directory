

# EntityInfoProperties

The generic properties of an entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The friendly name of the management group. |  [optional] |
|**inheritedPermissions** | **Permissions** |  |  [optional] |
|**numberOfChildGroups** | **Integer** | Number of child groups is the number of Groups that are exactly one level underneath the current Group. |  [optional] |
|**numberOfChildren** | **Integer** | Number of children is the number of Groups and Subscriptions that are exactly one level underneath the current Group. |  [optional] |
|**numberOfDescendants** | **Integer** |  |  [optional] |
|**parent** | [**EntityParentGroupInfo**](EntityParentGroupInfo.md) |  |  [optional] |
|**parentDisplayNameChain** | **List&lt;String&gt;** | The parent display name chain from the root group to the immediate parent |  [optional] |
|**parentNameChain** | **List&lt;String&gt;** | The parent name chain from the root group to the immediate parent |  [optional] |
|**permissions** | **Permissions** |  |  [optional] |
|**tenantId** | **String** | The AAD Tenant ID associated with the entity. For example, 00000000-0000-0000-0000-000000000000 |  [optional] |



