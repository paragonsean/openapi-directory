# ContentApiForShopping.Value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrierRateName** | **String** | The name of a carrier rate referring to a carrier rate defined in the same rate group. Can only be set if all other fields are not set. | [optional] 
**flatRate** | [**Price**](Price.md) |  | [optional] 
**noShipping** | **Boolean** | If true, then the product can&#39;t ship. Must be true when set, can only be set if all other fields are not set. | [optional] 
**pricePercentage** | **String** | A percentage of the price represented as a number in decimal notation (for example, &#x60;\&quot;5.4\&quot;&#x60;). Can only be set if all other fields are not set. | [optional] 
**subtableName** | **String** | The name of a subtable. Can only be set in table cells (not for single values), and only if all other fields are not set. | [optional] 


