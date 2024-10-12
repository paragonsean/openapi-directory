

# RegionPostalCodeAreaPostalCodeRange

A range of postal codes that defines the region area.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**begin** | **String** | Required. A postal code or a pattern of the form prefix* denoting the inclusive lower bound of the range defining the area. Examples values: \&quot;94108\&quot;, \&quot;9410*\&quot;, \&quot;9*\&quot;. |  [optional] |
|**end** | **String** | Optional. A postal code or a pattern of the form prefix* denoting the inclusive upper bound of the range defining the area. It must have the same length as postalCodeRangeBegin: if postalCodeRangeBegin is a postal code then postalCodeRangeEnd must be a postal code too; if postalCodeRangeBegin is a pattern then postalCodeRangeEnd must be a pattern with the same prefix length. Optional: if not set, then the area is defined as being all the postal codes matching postalCodeRangeBegin. |  [optional] |



