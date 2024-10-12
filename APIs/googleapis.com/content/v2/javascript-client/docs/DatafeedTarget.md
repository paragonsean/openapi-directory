# ContentApiForShopping.DatafeedTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | The country where the items in the feed will be included in the search index, represented as a CLDR territory code. | [optional] 
**excludedDestinations** | **[String]** | The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center). | [optional] 
**includedDestinations** | **[String]** | The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in &#x60;excludedDestinations&#x60;. List of supported destinations (if available to the account): - DisplayAds - Shopping - ShoppingActions - SurfacesAcrossGoogle  | [optional] 
**language** | **String** | The two-letter ISO 639-1 language of the items in the feed. Must be a valid language for &#x60;targets[].country&#x60;. | [optional] 


