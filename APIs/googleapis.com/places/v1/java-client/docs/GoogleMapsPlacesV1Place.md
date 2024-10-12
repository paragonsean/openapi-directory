

# GoogleMapsPlacesV1Place

All the information representing a Place.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessibilityOptions** | [**GoogleMapsPlacesV1PlaceAccessibilityOptions**](GoogleMapsPlacesV1PlaceAccessibilityOptions.md) |  |  [optional] |
|**addressComponents** | [**List&lt;GoogleMapsPlacesV1PlaceAddressComponent&gt;**](GoogleMapsPlacesV1PlaceAddressComponent.md) | Repeated components for each locality level. Note the following facts about the address_components[] array: - The array of address components may contain more components than the formatted_address. - The array does not necessarily include all the political entities that contain an address, apart from those included in the formatted_address. To retrieve all the political entities that contain a specific address, you should use reverse geocoding, passing the latitude/longitude of the address as a parameter to the request. - The format of the response is not guaranteed to remain the same between requests. In particular, the number of address_components varies based on the address requested and can change over time for the same address. A component can change position in the array. The type of the component can change. A particular component may be missing in a later response. |  [optional] |
|**adrFormatAddress** | **String** | The place&#39;s address in adr microformat: http://microformats.org/wiki/adr. |  [optional] |
|**allowsDogs** | **Boolean** | Place allows dogs. |  [optional] |
|**attributions** | [**List&lt;GoogleMapsPlacesV1PlaceAttribution&gt;**](GoogleMapsPlacesV1PlaceAttribution.md) | A set of data provider that must be shown with this result. |  [optional] |
|**businessStatus** | [**BusinessStatusEnum**](#BusinessStatusEnum) | The business status for the place. |  [optional] |
|**curbsidePickup** | **Boolean** | Specifies if the business supports curbside pickup. |  [optional] |
|**currentOpeningHours** | [**GoogleMapsPlacesV1PlaceOpeningHours**](GoogleMapsPlacesV1PlaceOpeningHours.md) |  |  [optional] |
|**currentSecondaryOpeningHours** | [**List&lt;GoogleMapsPlacesV1PlaceOpeningHours&gt;**](GoogleMapsPlacesV1PlaceOpeningHours.md) | Contains an array of entries for the next seven days including information about secondary hours of a business. Secondary hours are different from a business&#39;s main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place. This field includes the special_days subfield of all hours, set for dates that have exceptional hours. |  [optional] |
|**delivery** | **Boolean** | Specifies if the business supports delivery. |  [optional] |
|**dineIn** | **Boolean** | Specifies if the business supports indoor or outdoor seating options. |  [optional] |
|**displayName** | [**GoogleTypeLocalizedText**](GoogleTypeLocalizedText.md) |  |  [optional] |
|**editorialSummary** | [**GoogleTypeLocalizedText**](GoogleTypeLocalizedText.md) |  |  [optional] |
|**evChargeOptions** | [**GoogleMapsPlacesV1EVChargeOptions**](GoogleMapsPlacesV1EVChargeOptions.md) |  |  [optional] |
|**formattedAddress** | **String** | A full, human-readable address for this place. |  [optional] |
|**fuelOptions** | [**GoogleMapsPlacesV1FuelOptions**](GoogleMapsPlacesV1FuelOptions.md) |  |  [optional] |
|**goodForChildren** | **Boolean** | Place is good for children. |  [optional] |
|**goodForGroups** | **Boolean** | Place accommodates groups. |  [optional] |
|**goodForWatchingSports** | **Boolean** | Place is suitable for watching sports. |  [optional] |
|**googleMapsUri** | **String** | A URL providing more information about this place. |  [optional] |
|**iconBackgroundColor** | **String** | Background color for icon_mask in hex format, e.g. #909CE1. |  [optional] |
|**iconMaskBaseUri** | **String** | A truncated URL to an icon mask. User can access different icon type by appending type suffix to the end (eg, \&quot;.svg\&quot; or \&quot;.png\&quot;). |  [optional] |
|**id** | **String** | The unique identifier of a place. |  [optional] |
|**internationalPhoneNumber** | **String** | A human-readable phone number for the place, in international format. |  [optional] |
|**liveMusic** | **Boolean** | Place provides live music. |  [optional] |
|**location** | [**GoogleTypeLatLng**](GoogleTypeLatLng.md) |  |  [optional] |
|**menuForChildren** | **Boolean** | Place has a children&#39;s menu. |  [optional] |
|**name** | **String** | This Place&#39;s resource name, in &#x60;places/{place_id}&#x60; format. Can be used to look up the Place. |  [optional] |
|**nationalPhoneNumber** | **String** | A human-readable phone number for the place, in national format. |  [optional] |
|**outdoorSeating** | **Boolean** | Place provides outdoor seating. |  [optional] |
|**parkingOptions** | [**GoogleMapsPlacesV1PlaceParkingOptions**](GoogleMapsPlacesV1PlaceParkingOptions.md) |  |  [optional] |
|**paymentOptions** | [**GoogleMapsPlacesV1PlacePaymentOptions**](GoogleMapsPlacesV1PlacePaymentOptions.md) |  |  [optional] |
|**photos** | [**List&lt;GoogleMapsPlacesV1Photo&gt;**](GoogleMapsPlacesV1Photo.md) | Information (including references) about photos of this place. A maximum of 10 photos can be returned. |  [optional] |
|**plusCode** | [**GoogleMapsPlacesV1PlacePlusCode**](GoogleMapsPlacesV1PlacePlusCode.md) |  |  [optional] |
|**priceLevel** | [**PriceLevelEnum**](#PriceLevelEnum) | Price level of the place. |  [optional] |
|**primaryType** | **String** | The primary type of the given result. This type must one of the Places API supported types. For example, \&quot;restaurant\&quot;, \&quot;cafe\&quot;, \&quot;airport\&quot;, etc. A place can only have a single primary type. For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types |  [optional] |
|**primaryTypeDisplayName** | [**GoogleTypeLocalizedText**](GoogleTypeLocalizedText.md) |  |  [optional] |
|**rating** | **Double** | A rating between 1.0 and 5.0, based on user reviews of this place. |  [optional] |
|**regularOpeningHours** | [**GoogleMapsPlacesV1PlaceOpeningHours**](GoogleMapsPlacesV1PlaceOpeningHours.md) |  |  [optional] |
|**regularSecondaryOpeningHours** | [**List&lt;GoogleMapsPlacesV1PlaceOpeningHours&gt;**](GoogleMapsPlacesV1PlaceOpeningHours.md) | Contains an array of entries for information about regular secondary hours of a business. Secondary hours are different from a business&#39;s main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place. |  [optional] |
|**reservable** | **Boolean** | Specifies if the place supports reservations. |  [optional] |
|**restroom** | **Boolean** | Place has restroom. |  [optional] |
|**reviews** | [**List&lt;GoogleMapsPlacesV1Review&gt;**](GoogleMapsPlacesV1Review.md) | List of reviews about this place, sorted by relevance. A maximum of 5 reviews can be returned. |  [optional] |
|**servesBeer** | **Boolean** | Specifies if the place serves beer. |  [optional] |
|**servesBreakfast** | **Boolean** | Specifies if the place serves breakfast. |  [optional] |
|**servesBrunch** | **Boolean** | Specifies if the place serves brunch. |  [optional] |
|**servesCocktails** | **Boolean** | Place serves cocktails. |  [optional] |
|**servesCoffee** | **Boolean** | Place serves coffee. |  [optional] |
|**servesDessert** | **Boolean** | Place serves dessert. |  [optional] |
|**servesDinner** | **Boolean** | Specifies if the place serves dinner. |  [optional] |
|**servesLunch** | **Boolean** | Specifies if the place serves lunch. |  [optional] |
|**servesVegetarianFood** | **Boolean** | Specifies if the place serves vegetarian food. |  [optional] |
|**servesWine** | **Boolean** | Specifies if the place serves wine. |  [optional] |
|**shortFormattedAddress** | **String** | A short, human-readable address for this place. |  [optional] |
|**subDestinations** | [**List&lt;GoogleMapsPlacesV1PlaceSubDestination&gt;**](GoogleMapsPlacesV1PlaceSubDestination.md) | A list of sub destinations related to the place. |  [optional] |
|**takeout** | **Boolean** | Specifies if the business supports takeout. |  [optional] |
|**types** | **List&lt;String&gt;** | A set of type tags for this result. For example, \&quot;political\&quot; and \&quot;locality\&quot;. For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types |  [optional] |
|**userRatingCount** | **Integer** | The total number of reviews (with or without text) for this place. |  [optional] |
|**utcOffsetMinutes** | **Integer** | Number of minutes this place&#39;s timezone is currently offset from UTC. This is expressed in minutes to support timezones that are offset by fractions of an hour, e.g. X hours and 15 minutes. |  [optional] |
|**viewport** | [**GoogleGeoTypeViewport**](GoogleGeoTypeViewport.md) |  |  [optional] |
|**websiteUri** | **String** | The authoritative website for this place, e.g. a business&#39; homepage. Note that for places that are part of a chain (e.g. an IKEA store), this will usually be the website for the individual store, not the overall chain. |  [optional] |



## Enum: BusinessStatusEnum

| Name | Value |
|---- | -----|
| BUSINESS_STATUS_UNSPECIFIED | &quot;BUSINESS_STATUS_UNSPECIFIED&quot; |
| OPERATIONAL | &quot;OPERATIONAL&quot; |
| CLOSED_TEMPORARILY | &quot;CLOSED_TEMPORARILY&quot; |
| CLOSED_PERMANENTLY | &quot;CLOSED_PERMANENTLY&quot; |



## Enum: PriceLevelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRICE_LEVEL_UNSPECIFIED&quot; |
| FREE | &quot;PRICE_LEVEL_FREE&quot; |
| INEXPENSIVE | &quot;PRICE_LEVEL_INEXPENSIVE&quot; |
| MODERATE | &quot;PRICE_LEVEL_MODERATE&quot; |
| EXPENSIVE | &quot;PRICE_LEVEL_EXPENSIVE&quot; |
| VERY_EXPENSIVE | &quot;PRICE_LEVEL_VERY_EXPENSIVE&quot; |



