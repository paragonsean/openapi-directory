# SearchAds360ReportingApi.GoogleAdsSearchads360V0CommonUnifiedLocationAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**businessProfileLocations** | [**[GoogleAdsSearchads360V0CommonBusinessProfileLocation]**](GoogleAdsSearchads360V0CommonBusinessProfileLocation.md) | The list of business locations for the customer. This will only be returned if the Location Asset is syncing from the Business Profile account. It is possible to have multiple Business Profile listings under the same account that point to the same Place ID. | [optional] 
**locationOwnershipType** | **String** | The type of location ownership. If the type is BUSINESS_OWNER, it will be served as a location extension. If the type is AFFILIATE, it will be served as an affiliate location. | [optional] 
**placeId** | **String** | Place IDs uniquely identify a place in the Google Places database and on Google Maps. This field is unique for a given customer ID and asset type. See https://developers.google.com/places/web-service/place-id to learn more about Place ID. | [optional] 



## Enum: LocationOwnershipTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `BUSINESS_OWNER` (value: `"BUSINESS_OWNER"`)

* `AFFILIATE` (value: `"AFFILIATE"`)




