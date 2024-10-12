# ContentApiForShopping.OrdersCustomBatchRequestEntryRejectReturnLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lineItemId** | **String** | The ID of the line item to return. Either lineItemId or productId is required. | [optional] 
**productId** | **String** | The ID of the product to return. This is the REST ID used in the products service. Either lineItemId or productId is required. | [optional] 
**quantity** | **Number** | The quantity to return and refund. | [optional] 
**reason** | **String** | The reason for the return. Acceptable values are: - \&quot;&#x60;damagedOrUsed&#x60;\&quot; - \&quot;&#x60;missingComponent&#x60;\&quot; - \&quot;&#x60;notEligible&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot; - \&quot;&#x60;outOfReturnWindow&#x60;\&quot;  | [optional] 
**reasonText** | **String** | The explanation of the reason. | [optional] 


