

# MatchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchType** | **String** | Define the action you want to apply to each SKU. Values include:   1. &#x60;newproduct&#x60;: match the SKU as a new product.   2. &#x60;itemMatch&#x60;: associate the received SKU to an existing SKU.   3. &#x60;productMatch&#x60;: associate the received SKU to an existing product.   4. &#x60;deny&#x60;: deny the received SKU.   5. &#x60;pending&#x60;: the received SKU requires attention.   6. &#x60;incomplete&#x60;: the received SKU is lacking information to be matched.   7. &#x60;insufficientScore&#x60;: the score given by the Matcher to this received SKU doesn&#39;t qualify it to be matched.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score. |  |
|**matcherId** | **String** | Identifies the matching entity. It can be either VTEX&#39;s matcher, or an external matcher developed by partners, for example. The &#x60;matcherId&#x60;&#39;s value can be obtained through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint. |  |
|**product** | [**Product**](Product.md) |  |  [optional] |
|**productRef** | **String** | In &#x60;productMatch&#x60; actions, fill in this field on your request to match the item to an existing product in the marketplace. |  [optional] |
|**score** | **String** | Matcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been:   &#x60;Approved&#x60;: score equal to or greater than 80 points.   &#x60;Pending&#x60;: from 31 to 79 points.  &#x60;Denied&#x60;: from 0 to 30 points.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score. |  |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**skuRef** | **String** | In &#x60;itemMatch&#x60; actions, fill in this field on your request to match the item to an existing SKU in the marketplace. |  [optional] |



