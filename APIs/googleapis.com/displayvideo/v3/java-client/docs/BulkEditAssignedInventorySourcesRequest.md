

# BulkEditAssignedInventorySourcesRequest

Request message for AssignedInventorySourceService.BulkEdit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | The ID of the advertiser that owns the parent inventory source group. The parent partner does not have access to these assigned inventory sources. |  [optional] |
|**createdAssignedInventorySources** | [**List&lt;AssignedInventorySource&gt;**](AssignedInventorySource.md) | The assigned inventory sources to create in bulk, specified as a list of AssignedInventorySources. |  [optional] |
|**deletedAssignedInventorySources** | **List&lt;String&gt;** | The IDs of the assigned inventory sources to delete in bulk, specified as a list of assigned_inventory_source_ids. |  [optional] |
|**partnerId** | **String** | The ID of the partner that owns the inventory source group. Only this partner has write access to these assigned inventory sources. |  [optional] |



