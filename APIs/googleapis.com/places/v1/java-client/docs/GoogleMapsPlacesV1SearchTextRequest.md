

# GoogleMapsPlacesV1SearchTextRequest

Request proto for SearchText. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includedType** | **String** | The requested place type. Full list of types supported: https://developers.google.com/maps/documentation/places/web-service/place-types. Only support one included type. |  [optional] |
|**languageCode** | **String** | Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport. |  [optional] |
|**locationBias** | [**GoogleMapsPlacesV1SearchTextRequestLocationBias**](GoogleMapsPlacesV1SearchTextRequestLocationBias.md) |  |  [optional] |
|**locationRestriction** | [**GoogleMapsPlacesV1SearchTextRequestLocationRestriction**](GoogleMapsPlacesV1SearchTextRequestLocationRestriction.md) |  |  [optional] |
|**maxResultCount** | **Integer** | Maximum number of results to return. It must be between 1 and 20, inclusively. The default is 20. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned. |  [optional] |
|**minRating** | **Double** | Filter out results whose average user rating is strictly less than this limit. A valid value must be a float between 0 and 5 (inclusively) at a 0.5 cadence i.e. [0, 0.5, 1.0, ... , 5.0] inclusively. The input rating will round up to the nearest 0.5(ceiling). For instance, a rating of 0.6 will eliminate all results with a less than 1.0 rating. |  [optional] |
|**openNow** | **Boolean** | Used to restrict the search to places that are currently open. The default is false. |  [optional] |
|**priceLevels** | [**List&lt;PriceLevelsEnum&gt;**](#List&lt;PriceLevelsEnum&gt;) | Used to restrict the search to places that are marked as certain price levels. Users can choose any combinations of price levels. Default to select all price levels. |  [optional] |
|**rankPreference** | [**RankPreferenceEnum**](#RankPreferenceEnum) | How results will be ranked in the response. |  [optional] |
|**regionCode** | **String** | The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported. |  [optional] |
|**strictTypeFiltering** | **Boolean** | Used to set strict type filtering for included_type. If set to true, only results of the same type will be returned. Default to false. |  [optional] |
|**textQuery** | **String** | Required. The text query for textual search. |  [optional] |



## Enum: List&lt;PriceLevelsEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRICE_LEVEL_UNSPECIFIED&quot; |
| FREE | &quot;PRICE_LEVEL_FREE&quot; |
| INEXPENSIVE | &quot;PRICE_LEVEL_INEXPENSIVE&quot; |
| MODERATE | &quot;PRICE_LEVEL_MODERATE&quot; |
| EXPENSIVE | &quot;PRICE_LEVEL_EXPENSIVE&quot; |
| VERY_EXPENSIVE | &quot;PRICE_LEVEL_VERY_EXPENSIVE&quot; |



## Enum: RankPreferenceEnum

| Name | Value |
|---- | -----|
| RANK_PREFERENCE_UNSPECIFIED | &quot;RANK_PREFERENCE_UNSPECIFIED&quot; |
| DISTANCE | &quot;DISTANCE&quot; |
| RELEVANCE | &quot;RELEVANCE&quot; |



