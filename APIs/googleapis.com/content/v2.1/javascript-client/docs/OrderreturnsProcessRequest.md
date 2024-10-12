# ContentApiForShopping.OrderreturnsProcessRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullChargeReturnShippingCost** | **Boolean** | Option to charge the customer return shipping cost. | [optional] 
**operationId** | **String** | [required] The ID of the operation, unique across all operations for a given order return. | [optional] 
**refundShippingFee** | [**OrderreturnsRefundOperation**](OrderreturnsRefundOperation.md) |  | [optional] 
**returnItems** | [**[OrderreturnsReturnItem]**](OrderreturnsReturnItem.md) | The list of items to return. | [optional] 


