

# CreateManagementGroupChildInfo

The child information of a management group used during creation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**children** | [**List&lt;CreateManagementGroupChildInfo&gt;**](CreateManagementGroupChildInfo.md) | The list of children. |  [optional] [readonly] |
|**displayName** | **String** | The friendly name of the child resource. |  [optional] [readonly] |
|**id** | **String** | The fully qualified ID for the child resource (management group or subscription).  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 |  [optional] [readonly] |
|**name** | **String** | The name of the child entity. |  [optional] [readonly] |
|**roles** | **List&lt;String&gt;** | The roles definitions associated with the management group. |  [optional] [readonly] |
|**type** | **ManagementGroupChildType** |  |  [optional] |



