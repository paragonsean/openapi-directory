

# Money

Represents an amount of money with its currency type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | The three-letter currency code defined in ISO 4217. |  [optional] |
|**nanos** | **Integer** | Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If &#x60;units&#x60; is positive, &#x60;nanos&#x60; must be positive or zero. If &#x60;units&#x60; is zero, &#x60;nanos&#x60; can be positive, zero, or negative. If &#x60;units&#x60; is negative, &#x60;nanos&#x60; must be negative or zero. For example $-1.75 is represented as &#x60;units&#x60;&#x3D;-1 and &#x60;nanos&#x60;&#x3D;-750,000,000. |  [optional] |
|**units** | **String** | The whole units of the amount. For example if &#x60;currencyCode&#x60; is &#x60;\&quot;USD\&quot;&#x60;, then 1 unit is one US dollar. |  [optional] |



