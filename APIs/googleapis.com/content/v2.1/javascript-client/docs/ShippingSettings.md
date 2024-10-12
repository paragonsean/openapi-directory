# ContentApiForShopping.ShippingSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The ID of the account to which these account shipping settings belong. Ignored upon update, always present in get request responses. | [optional] 
**postalCodeGroups** | [**[PostalCodeGroup]**](PostalCodeGroup.md) | A list of postal code groups that can be referred to in &#x60;services&#x60;. Optional. | [optional] 
**services** | [**[Service]**](Service.md) | The target account&#39;s list of services. Optional. | [optional] 
**warehouses** | [**[Warehouse]**](Warehouse.md) | Optional. A list of warehouses which can be referred to in &#x60;services&#x60;. | [optional] 


