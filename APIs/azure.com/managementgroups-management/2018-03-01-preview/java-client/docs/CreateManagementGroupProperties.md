

# CreateManagementGroupProperties

The generic properties of a management group used during creation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**children** | [**List&lt;CreateManagementGroupChildInfo&gt;**](CreateManagementGroupChildInfo.md) | The list of children. |  [optional] [readonly] |
|**details** | [**CreateManagementGroupDetails**](CreateManagementGroupDetails.md) |  |  [optional] |
|**displayName** | **String** | The friendly name of the management group. If no value is passed then this  field will be set to the groupId. |  [optional] |
|**roles** | **List&lt;String&gt;** | The roles definitions associated with the management group. |  [optional] [readonly] |
|**tenantId** | **String** | The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000 |  [optional] [readonly] |



