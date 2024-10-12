

# GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction

Prediction results for a Place Autocomplete prediction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**distanceMeters** | **Integer** | The length of the geodesic in meters from &#x60;origin&#x60; if &#x60;origin&#x60; is specified. Certain predictions such as routes may not populate this field. |  [optional] |
|**place** | **String** | The resource name of the suggested Place. This name can be used in other APIs that accept Place names. |  [optional] |
|**placeId** | **String** | The unique identifier of the suggested Place. This identifier can be used in other APIs that accept Place IDs. |  [optional] |
|**structuredFormat** | [**GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat**](GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat.md) |  |  [optional] |
|**text** | [**GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText**](GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText.md) |  |  [optional] |
|**types** | **List&lt;String&gt;** | List of types that apply to this Place from Table A or Table B in https://developers.google.com/maps/documentation/places/web-service/place-types. A type is a categorization of a Place. Places with shared types will share similar characteristics. |  [optional] |



