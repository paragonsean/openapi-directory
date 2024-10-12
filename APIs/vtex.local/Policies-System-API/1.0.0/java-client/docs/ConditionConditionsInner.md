

# ConditionConditionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditions** | **List&lt;String&gt;** | These are the conditions the actions can have. The possible values are &#x60;[]&#x60;, &#x60;stringEquals&#x60;, and &#x60;numericGreaterThan&#x60; |  [optional] |
|**key** | **String** | The element that will define what the policy will influence. This field has the possible values &#x60;skuId&#x60;, &#x60;brandId&#x60;, &#x60;discountPercentage&#x60; |  [optional] |
|**operation** | **String** | The action of the condition. This operation possible values are &#x60;None&#x60;, &#x60;stringEquals&#x60;, &#x60;stringEqualsIgnoreCase&#x60;, &#x60;numericEquals&#x60;, &#x60;numericLessThan&#x60;, &#x60;numericLessThanEquals&#x60;,   &#x60;numericGreaterThan&#x60;, &#x60;numericGreaterThanEquals&#x60;, &#x60;bool&#x60;, &#x60;not&#x60;, &#x60;or&#x60;, &#x60;and&#x60;, &#x60;dateTimeUtcGreaterThan&#x60;, &#x60;dateTimeUtcLessThan&#x60;, and &#x60;between&#x60; |  [optional] |
|**values** | **List&lt;String&gt;** | Value of the key |  [optional] |



