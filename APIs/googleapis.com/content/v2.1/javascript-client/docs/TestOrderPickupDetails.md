# ContentApiForShopping.TestOrderPickupDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locationCode** | **String** | Required. Code of the location defined by provider or merchant. | [optional] 
**pickupLocationAddress** | [**TestOrderAddress**](TestOrderAddress.md) |  | [optional] 
**pickupLocationType** | **String** | Pickup location type. Acceptable values are: - \&quot;&#x60;locker&#x60;\&quot; - \&quot;&#x60;store&#x60;\&quot; - \&quot;&#x60;curbside&#x60;\&quot;  | [optional] 
**pickupPersons** | [**[TestOrderPickupDetailsPickupPerson]**](TestOrderPickupDetailsPickupPerson.md) | Required. all pickup persons set by users. | [optional] 


