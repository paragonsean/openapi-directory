

# ManagementGroupProperties

The generic properties of a management group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**children** | [**List&lt;ManagementGroupChildInfo&gt;**](ManagementGroupChildInfo.md) | The list of children. |  [optional] |
|**details** | [**ManagementGroupDetails**](ManagementGroupDetails.md) |  |  [optional] |
|**displayName** | **String** | The friendly name of the management group. |  [optional] |
|**path** | [**List&lt;ManagementGroupPathElement&gt;**](ManagementGroupPathElement.md) | The hierarchial path from the root group to the current group. |  [optional] |
|**roles** | **List&lt;String&gt;** | The role definitions associated with the management group. |  [optional] |
|**tenantId** | **String** | The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000 |  [optional] |



