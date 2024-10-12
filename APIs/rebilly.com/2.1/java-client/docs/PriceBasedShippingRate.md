

# PriceBasedShippingRate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  |
|**maxOrderSubtotal** | **Double** | Maximum order subtotal for which this shipping rate is applicable (NULL if no maximum). |  [optional] |
|**minOrderSubtotal** | **Double** | Minimum order subtotal for which this shipping rate is applicable, defaults to 0.00. |  [optional] |
|**name** | **String** | The shipping rate name. |  |
|**price** | **Double** | The shipping price - 0 is a valid value (for free). |  |



