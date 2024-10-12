

# BulkUpdateLineItemsResponse

Response message for LineItemService.BulkUpdateLineItems.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Status&gt;**](Status.md) | Errors returned by line items that failed to update. |  [optional] |
|**failedLineItemIds** | **List&lt;String&gt;** | The IDs of line items that failed to update. |  [optional] |
|**skippedLineItemIds** | **List&lt;String&gt;** | The IDs of line items that are skipped for updates. For example, unnecessary mutates that will result in effectively no changes to line items will be skipped and corresponding line item IDs can be tracked here. |  [optional] |
|**updatedLineItemIds** | **List&lt;String&gt;** | The IDs of successfully updated line items. |  [optional] |



