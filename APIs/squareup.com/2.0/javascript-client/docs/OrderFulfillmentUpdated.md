# SquareConnectApi.OrderFulfillmentUpdated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | The timestamp for when the order was created, in RFC 3339 format. | [optional] 
**fulfillmentUpdate** | [**[OrderFulfillmentUpdatedUpdate]**](OrderFulfillmentUpdatedUpdate.md) | The fulfillments that were updated with this version change. | [optional] 
**locationId** | **String** | The ID of the seller location that this order is associated with. | [optional] 
**orderId** | **String** | The order&#39;s unique ID. | [optional] 
**state** | **String** | The state of the order. | [optional] 
**updatedAt** | **String** | The timestamp for when the order was last updated, in RFC 3339 format. | [optional] 
**version** | **Number** | The version number, which is incremented each time an update is committed to the order. Orders that were not created through the API do not include a version number and therefore cannot be updated.  [Read more about working with versions.](https://developer.squareup.com/docs/orders-api/manage-orders#update-orders) | [optional] 


