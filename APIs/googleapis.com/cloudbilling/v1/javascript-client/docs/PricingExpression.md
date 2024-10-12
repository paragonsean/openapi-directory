# CloudBillingApi.PricingExpression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseUnit** | **String** | The base unit for the SKU which is the unit used in usage exports. Example: \&quot;By\&quot; | [optional] 
**baseUnitConversionFactor** | **Number** | Conversion factor for converting from price per usage_unit to price per base_unit, and start_usage_amount to start_usage_amount in base_unit. unit_price / base_unit_conversion_factor &#x3D; price per base_unit. start_usage_amount * base_unit_conversion_factor &#x3D; start_usage_amount in base_unit. | [optional] 
**baseUnitDescription** | **String** | The base unit in human readable form. Example: \&quot;byte\&quot;. | [optional] 
**displayQuantity** | **Number** | The recommended quantity of units for displaying pricing info. When displaying pricing info it is recommended to display: (unit_price * display_quantity) per display_quantity usage_unit. This field does not affect the pricing formula and is for display purposes only. Example: If the unit_price is \&quot;0.0001 USD\&quot;, the usage_unit is \&quot;GB\&quot; and the display_quantity is \&quot;1000\&quot; then the recommended way of displaying the pricing info is \&quot;0.10 USD per 1000 GB\&quot; | [optional] 
**tieredRates** | [**[TierRate]**](TierRate.md) | The list of tiered rates for this pricing. The total cost is computed by applying each of the tiered rates on usage. This repeated list is sorted by ascending order of start_usage_amount. | [optional] 
**usageUnit** | **String** | The short hand for unit of usage this pricing is specified in. Example: usage_unit of \&quot;GiBy\&quot; means that usage is specified in \&quot;Gibi Byte\&quot;. | [optional] 
**usageUnitDescription** | **String** | The unit of usage in human readable form. Example: \&quot;gibi byte\&quot;. | [optional] 


