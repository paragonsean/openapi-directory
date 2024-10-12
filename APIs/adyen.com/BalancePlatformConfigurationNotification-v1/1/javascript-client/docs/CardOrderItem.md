# ConfigurationWebhooks.CardOrderItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balancePlatform** | **String** | The unique identifier of the balance platform. | [optional] 
**card** | [**CardOrderItemDeliveryStatus**](CardOrderItemDeliveryStatus.md) | The status of the card delivery.  Possible values: **created**, **rejected**, **processing**, **produced**, **shipped**, **delivered**, **notApplicable**, **unknown**.  | [optional] 
**cardOrderItemId** | **String** | The unique identifier of the card order item. | [optional] 
**creationDate** | **Date** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. | [optional] 
**id** | **String** | The ID of the resource. | [optional] 
**paymentInstrumentId** | **String** | The unique identifier of the payment instrument related to the card order item. | [optional] 
**pin** | [**CardOrderItemDeliveryStatus**](CardOrderItemDeliveryStatus.md) | Contains information about the status of the PIN delivery. | [optional] 
**shippingMethod** | **String** | The shipping method used to deliver the card or the PIN. | [optional] 


