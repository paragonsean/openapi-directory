

# PostalCodeRange


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postalCodeRangeBegin** | **String** | A postal code or a pattern of the form &#x60;prefix*&#x60; denoting the inclusive lower bound of the range defining the area. Examples values: &#x60;\&quot;94108\&quot;&#x60;, &#x60;\&quot;9410*\&quot;&#x60;, &#x60;\&quot;9*\&quot;&#x60;. Required. |  [optional] |
|**postalCodeRangeEnd** | **String** | A postal code or a pattern of the form &#x60;prefix*&#x60; denoting the inclusive upper bound of the range defining the area. It must have the same length as &#x60;postalCodeRangeBegin&#x60;: if &#x60;postalCodeRangeBegin&#x60; is a postal code then &#x60;postalCodeRangeEnd&#x60; must be a postal code too; if &#x60;postalCodeRangeBegin&#x60; is a pattern then &#x60;postalCodeRangeEnd&#x60; must be a pattern with the same prefix length. Optional: if not set, then the area is defined as being all the postal codes matching &#x60;postalCodeRangeBegin&#x60;. |  [optional] |



