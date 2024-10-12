# PlacesApiNew.GoogleMapsPlacesV1SearchNearbyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludedPrimaryTypes** | **[String]** | Excluded primary Place type (e.g. \&quot;restaurant\&quot; or \&quot;gas_station\&quot;) from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types &#x3D; [\&quot;restaurant\&quot;], excluded_primary_types &#x3D; [\&quot;restaurant\&quot;]}, the returned places provide \&quot;restaurant\&quot; related services but do not operate primarily as \&quot;restaurants\&quot;. | [optional] 
**excludedTypes** | **[String]** | Excluded Place type (eg, \&quot;restaurant\&quot; or \&quot;gas_station\&quot;) from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If the client provides both included_types (e.g. restaurant) and excluded_types (e.g. cafe), then the response should include places that are restaurant but not cafe. The response includes places that match at least one of the included_types and none of the excluded_types. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types &#x3D; [\&quot;restaurant\&quot;], excluded_primary_types &#x3D; [\&quot;restaurant\&quot;]}, the returned places provide \&quot;restaurant\&quot; related services but do not operate primarily as \&quot;restaurants\&quot;. | [optional] 
**includedPrimaryTypes** | **[String]** | Included primary Place type (e.g. \&quot;restaurant\&quot; or \&quot;gas_station\&quot;) from https://developers.google.com/maps/documentation/places/web-service/place-types. A place can only have a single primary type from the supported types table associated with it. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types &#x3D; [\&quot;restaurant\&quot;], excluded_primary_types &#x3D; [\&quot;restaurant\&quot;]}, the returned places provide \&quot;restaurant\&quot; related services but do not operate primarily as \&quot;restaurants\&quot;. | [optional] 
**includedTypes** | **[String]** | Included Place type (eg, \&quot;restaurant\&quot; or \&quot;gas_station\&quot;) from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types &#x3D; [\&quot;restaurant\&quot;], excluded_primary_types &#x3D; [\&quot;restaurant\&quot;]}, the returned places provide \&quot;restaurant\&quot; related services but do not operate primarily as \&quot;restaurants\&quot;. | [optional] 
**languageCode** | **String** | Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport. | [optional] 
**locationRestriction** | [**GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction**](GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction.md) |  | [optional] 
**maxResultCount** | **Number** | Maximum number of results to return. It must be between 1 and 20 (default), inclusively. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned. | [optional] 
**rankPreference** | **String** | How results will be ranked in the response. | [optional] 
**regionCode** | **String** | The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported. | [optional] 



## Enum: RankPreferenceEnum


* `RANK_PREFERENCE_UNSPECIFIED` (value: `"RANK_PREFERENCE_UNSPECIFIED"`)

* `DISTANCE` (value: `"DISTANCE"`)

* `POPULARITY` (value: `"POPULARITY"`)




