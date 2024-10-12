# BeanstreamPayments.PaymentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **Number** | Approved &#x3D; 1, declined &#x3D; 0 | [optional] 
**authCode** | **String** | alphanumeric (32) | [optional] 
**card** | [**CardPurchaseResponse**](CardPurchaseResponse.md) |  | [optional] 
**created** | **String** | alphanumeric (32) | [optional] 
**id** | **String** | digits (9) | [optional] 
**links** | [**[Link]**](Link.md) |  | [optional] 
**message** | **String** | alphanumeric (256) | [optional] 
**messageId** | **String** | digits (3) | [optional] 
**orderNumber** | **String** | alphanumeric (32) | [optional] 
**paymentMethod** | **String** | characters (16) | [optional] 
**type** | **String** | characters (16) | [optional] 


