# ContentApiForShopping.OrdersCustomBatchRequestEntryUpdateLineItemShippingDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliverByDate** | **String** | Updated delivery by date, in ISO 8601 format. If not specified only ship by date is updated. Provided date should be within 1 year timeframe and can not be a date in the past. | [optional] 
**lineItemId** | **String** | The ID of the line item to set metadata. Either lineItemId or productId is required. | [optional] 
**productId** | **String** | The ID of the product to set metadata. This is the REST ID used in the products service. Either lineItemId or productId is required. | [optional] 
**shipByDate** | **String** | Updated ship by date, in ISO 8601 format. If not specified only deliver by date is updated. Provided date should be within 1 year timeframe and can not be a date in the past. | [optional] 


