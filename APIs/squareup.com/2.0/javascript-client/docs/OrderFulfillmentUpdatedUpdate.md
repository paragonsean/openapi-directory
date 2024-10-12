# SquareConnectApi.OrderFulfillmentUpdatedUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillmentUid** | **String** | A unique ID that identifies the fulfillment only within this order. | [optional] 
**newState** | **String** | The state of the fulfillment after the change. The state might be equal to &#x60;old_state&#x60; if a non-state field was changed on the fulfillment (such as the tracking number). | [optional] 
**oldState** | **String** | The state of the fulfillment before the change. The state is not populated if the fulfillment is created with this new &#x60;Order&#x60; version. | [optional] 


