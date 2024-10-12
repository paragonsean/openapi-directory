# ContentApiForShopping.LocalInventory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | **String** | The availability of the product. For accepted attribute values, see the local product inventory feed specification. | [optional] 
**customAttributes** | [**[CustomAttribute]**](CustomAttribute.md) | A list of custom (merchant-provided) attributes. Can also be used to submit any attribute of the feed specification in its generic form, for example, &#x60;{ \&quot;name\&quot;: \&quot;size type\&quot;, \&quot;value\&quot;: \&quot;regular\&quot; }&#x60;. | [optional] 
**instoreProductLocation** | **String** | The in-store product location. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#localInventory&#x60;\&quot; | [optional] 
**pickupMethod** | **String** | The supported pickup method for this offer. Unless the value is \&quot;not supported\&quot;, this field must be submitted together with &#x60;pickupSla&#x60;. For accepted attribute values, see the local product inventory feed specification. | [optional] 
**pickupSla** | **String** | The expected date that an order will be ready for pickup relative to the order date. Must be submitted together with &#x60;pickupMethod&#x60;. For accepted attribute values, see the local product inventory feed specification. | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 
**quantity** | **Number** | The quantity of the product. Must be nonnegative. | [optional] 
**salePrice** | [**Price**](Price.md) |  | [optional] 
**salePriceEffectiveDate** | **String** | A date range represented by a pair of ISO 8601 dates separated by a space, comma, or slash. Both dates may be specified as &#39;null&#39; if undecided. | [optional] 
**storeCode** | **String** | Required. The store code of this local inventory resource. | [optional] 


