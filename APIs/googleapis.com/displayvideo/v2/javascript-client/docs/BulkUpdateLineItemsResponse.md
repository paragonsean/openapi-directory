# DisplayVideo360Api.BulkUpdateLineItemsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Status]**](Status.md) | Errors returned by line items that failed to update. | [optional] 
**failedLineItemIds** | **[String]** | The IDs of line items that failed to update. | [optional] 
**skippedLineItemIds** | **[String]** | The IDs of line items that are skipped for updates. For example, unnecessary mutates that will result in effectively no changes to line items will be skipped and corresponding line item IDs can be tracked here. | [optional] 
**updatedLineItemIds** | **[String]** | The IDs of successfully updated line items. | [optional] 


