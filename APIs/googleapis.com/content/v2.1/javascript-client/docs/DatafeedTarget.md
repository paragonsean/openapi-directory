# ContentApiForShopping.DatafeedTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | Deprecated. Use &#x60;feedLabel&#x60; instead. The country where the items in the feed will be included in the search index, represented as a CLDR territory code. | [optional] 
**excludedDestinations** | **[String]** | The list of destinations to exclude for this target (corresponds to cleared check boxes in Merchant Center). Products that are excluded from all destinations for more than 7 days are automatically deleted. | [optional] 
**feedLabel** | **String** | Feed label for the DatafeedTarget. Either &#x60;country&#x60; or &#x60;feedLabel&#x60; is required. If both &#x60;feedLabel&#x60; and &#x60;country&#x60; is specified, the values must match. Must be less than or equal to 20 uppercase letters (A-Z), numbers (0-9), and dashes (-). | [optional] 
**includedDestinations** | **[String]** | The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in &#x60;excludedDestinations&#x60;. | [optional] 
**language** | **String** | The two-letter ISO 639-1 language of the items in the feed. Must be a valid language for &#x60;targets[].country&#x60;. | [optional] 
**targetCountries** | **[String]** | The countries where the items may be displayed. Represented as a CLDR territory code. Will be ignored for \&quot;product inventory\&quot; feeds. | [optional] 


