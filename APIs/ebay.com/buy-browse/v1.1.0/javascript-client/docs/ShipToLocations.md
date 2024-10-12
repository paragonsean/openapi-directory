# BrowseApi.ShipToLocations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regionExcluded** | [**[ShipToRegion]**](ShipToRegion.md) | An array of containers that express the large geographical regions, countries, state/provinces, or special locations within a country where the seller is not willing to ship to. | [optional] 
**regionIncluded** | [**[ShipToRegion]**](ShipToRegion.md) | An array of containers that express the large geographical regions, countries, or state/provinces within a country where the seller is willing to ship to. Prospective buyers must look at the shipping regions under this container, as well as the shipping regions that are under the regionExcluded to see where the seller is willing to ship items. Sellers can specify that they ship &#39;Worldwide&#39;, but then add several large geographical regions (e.g. Asia, Oceania, Middle East) to the exclusion list, or sellers can specify that they ship to Europe and Africa, but then add several individual countries to the exclusion list. | [optional] 


