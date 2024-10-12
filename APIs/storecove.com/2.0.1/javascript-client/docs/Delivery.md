# StorecoveApi.Delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualDate** | **String** | The actual date of the delivery. Used only for Invoice | [optional] 
**deliveryLocation** | [**DeliveryDeliveryLocation**](DeliveryDeliveryLocation.md) |  | [optional] 
**deliveryParty** | [**DeliveryParty**](DeliveryParty.md) |  | [optional] 
**deliveryPartyName** | **String** | Use deliveryParty. The name of the party that took delivery. Used only for Invoice | [optional] 
**quantity** | **Number** | The quantity of the delivery. Used only for Invoice | [optional] [default to 1]
**requestedDeliveryPeriod** | **String** | The requested delivery period. Used only for DocumentOrder. | [optional] 
**shippingMarks** | **String** | A text that the buyer requests to be printed on the packing labels. Used only for DocumentOrder. | [optional] 


