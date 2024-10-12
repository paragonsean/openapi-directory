# RebillyRestApi.PriceBasedShippingRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | 
**maxOrderSubtotal** | **Number** | Maximum order subtotal for which this shipping rate is applicable (NULL if no maximum). | [optional] 
**minOrderSubtotal** | **Number** | Minimum order subtotal for which this shipping rate is applicable, defaults to 0.00. | [optional] [default to 0]
**name** | **String** | The shipping rate name. | 
**price** | **Number** | The shipping price - 0 is a valid value (for free). | 


