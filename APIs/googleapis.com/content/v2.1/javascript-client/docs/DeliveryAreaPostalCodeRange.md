# ContentApiForShopping.DeliveryAreaPostalCodeRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstPostalCode** | **String** | Required. A postal code or a pattern of the form prefix* denoting the inclusive lower bound of the range defining the area. Examples values: &#x60;\&quot;94108\&quot;&#x60;, &#x60;\&quot;9410*\&quot;&#x60;, &#x60;\&quot;9*\&quot;&#x60;. | [optional] 
**lastPostalCode** | **String** | A postal code or a pattern of the form prefix* denoting the inclusive upper bound of the range defining the area (for example [070* - 078*] results in the range [07000 - 07899]). It must have the same length as &#x60;firstPostalCode&#x60;: if &#x60;firstPostalCode&#x60; is a postal code then &#x60;lastPostalCode&#x60; must be a postal code too; if firstPostalCode is a pattern then &#x60;lastPostalCode&#x60; must be a pattern with the same prefix length. Ignored if not set, then the area is defined as being all the postal codes matching &#x60;firstPostalCode&#x60;. | [optional] 


