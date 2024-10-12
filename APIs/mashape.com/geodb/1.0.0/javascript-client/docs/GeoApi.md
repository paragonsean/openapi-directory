# GeoDbCitiesApi.GeoApi

All URIs are relative to *https://wft-geo-db.p.rapidapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findAdminDivisionsUsingGET**](GeoApi.md#findAdminDivisionsUsingGET) | **GET** /geo/adminDivisions | Find administrative divisions
[**findCitiesNearAdminDivisionUsingGET**](GeoApi.md#findCitiesNearAdminDivisionUsingGET) | **GET** /geo/adminDivisions/{divisionId}/nearbyCities | Find cities near division
[**findCitiesNearCityUsingGET**](GeoApi.md#findCitiesNearCityUsingGET) | **GET** /geo/cities/{cityId}/nearbyCities | Find cities near city
[**findCitiesNearLocationUsingGET**](GeoApi.md#findCitiesNearLocationUsingGET) | **GET** /geo/locations/{locationId}/nearbyCities | Find cities near location
[**findCitiesUsingGET**](GeoApi.md#findCitiesUsingGET) | **GET** /geo/cities | Find cities
[**findDivisionsNearAdminDivisionUsingGET**](GeoApi.md#findDivisionsNearAdminDivisionUsingGET) | **GET** /geo/adminDivisions/{divisionId}/nearbyDivisions | Find divisions near division
[**findDivisionsNearLocationUsingGET**](GeoApi.md#findDivisionsNearLocationUsingGET) | **GET** /geo/locations/{locationId}/nearbyDivisions | Find divisions near location
[**findRegionCitiesUsingGET**](GeoApi.md#findRegionCitiesUsingGET) | **GET** /geo/countries/{countryId}/regions/{regionCode}/cities | Find country region cities
[**findRegionDivisionsUsingGET**](GeoApi.md#findRegionDivisionsUsingGET) | **GET** /geo/countries/{countryId}/regions/{regionCode}/adminDivisions | Find country region administrative divisions
[**getAdminDivisionUsingGET**](GeoApi.md#getAdminDivisionUsingGET) | **GET** /geo/adminDivisions/{divisionId} | Get administrative division details
[**getCityDateTimeUsingGET**](GeoApi.md#getCityDateTimeUsingGET) | **GET** /geo/cities/{cityId}/dateTime | Get city date-time
[**getCityDistanceUsingGET**](GeoApi.md#getCityDistanceUsingGET) | **GET** /geo/cities/{cityId}/distance | Get city distance
[**getCityLocatedInUsingGET**](GeoApi.md#getCityLocatedInUsingGET) | **GET** /geo/cities/{cityId}/locatedIn | Get city admin region
[**getCityTimeUsingGET**](GeoApi.md#getCityTimeUsingGET) | **GET** /geo/cities/{cityId}/time | Get city time
[**getCityUsingGET**](GeoApi.md#getCityUsingGET) | **GET** /geo/cities/{cityId} | Get city details
[**getCountriesUsingGET**](GeoApi.md#getCountriesUsingGET) | **GET** /geo/countries | Find countries
[**getCountryUsingGET**](GeoApi.md#getCountryUsingGET) | **GET** /geo/countries/{countryId} | Get country details
[**getRegionUsingGET**](GeoApi.md#getRegionUsingGET) | **GET** /geo/countries/{countryId}/regions/{regionCode} | Get region details
[**getRegionsUsingGET**](GeoApi.md#getRegionsUsingGET) | **GET** /geo/countries/{countryId}/regions | Find country regions



## findAdminDivisionsUsingGET

> PopulatedPlacesResponse findAdminDivisionsUsingGET(opts)

Find administrative divisions

Find administrative divisions, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let opts = {
  'location': "location_example", // String | Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
  'radius': 56, // Number | The location radius within which to find places
  'distanceUnit': "'MI'", // String | The unit of distance: MI | KM
  'countryIds': "countryIds_example", // String | Only places in these countries (comma-delimited country codes or WikiData ids)
  'excludedCountryIds': "excludedCountryIds_example", // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findAdminDivisionsUsingGET(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **String**| Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | [optional] 
 **radius** | **Number**| The location radius within which to find places | [optional] 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]
 **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findCitiesNearAdminDivisionUsingGET

> PopulatedPlacesResponse findCitiesNearAdminDivisionUsingGET(divisionId, opts)

Find cities near division

Find cities near the given administrative division, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let divisionId = "divisionId_example"; // String | An admin-division id (either native 'id' or 'wikiDataId')
let opts = {
  'radius': 56, // Number | The location radius within which to find places
  'distanceUnit': "'MI'", // String | The unit of distance: MI | KM
  'countryIds': "countryIds_example", // String | Only places in these countries (comma-delimited country codes or WikiData ids)
  'excludedCountryIds': "excludedCountryIds_example", // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'types': "types_example", // String | Only places for these types (comma-delimited): CITY | ADM2
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findCitiesNearAdminDivisionUsingGET(divisionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divisionId** | **String**| An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 
 **radius** | **Number**| The location radius within which to find places | [optional] 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]
 **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findCitiesNearCityUsingGET

> PopulatedPlacesResponse findCitiesNearCityUsingGET(cityId, opts)

Find cities near city

Find cities near the given origin city, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
let opts = {
  'radius': 56, // Number | The location radius within which to find places
  'distanceUnit': "'MI'", // String | The unit of distance: MI | KM
  'countryIds': "countryIds_example", // String | Only places in these countries (comma-delimited country codes or WikiData ids)
  'excludedCountryIds': "excludedCountryIds_example", // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'types': "types_example", // String | Only places for these types (comma-delimited): CITY | ADM2
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findCitiesNearCityUsingGET(cityId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 
 **radius** | **Number**| The location radius within which to find places | [optional] 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]
 **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findCitiesNearLocationUsingGET

> PopulatedPlacesResponse findCitiesNearLocationUsingGET(locationId, opts)

Find cities near location

Find cities near the given location, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let locationId = "locationId_example"; // String | A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
let opts = {
  'radius': 56, // Number | The location radius within which to find places
  'distanceUnit': "'MI'", // String | The unit of distance: MI | KM
  'countryIds': "countryIds_example", // String | Only places in these countries (comma-delimited country codes or WikiData ids)
  'excludedCountryIds': "excludedCountryIds_example", // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'types': "types_example", // String | Only places for these types (comma-delimited): CITY | ADM2
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findCitiesNearLocationUsingGET(locationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locationId** | **String**| A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | 
 **radius** | **Number**| The location radius within which to find places | [optional] 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]
 **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findCitiesUsingGET

> PopulatedPlacesResponse findCitiesUsingGET(opts)

Find cities

Find cities, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let opts = {
  'location': "location_example", // String | Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
  'radius': 56, // Number | The location radius within which to find places
  'distanceUnit': "'MI'", // String | The unit of distance: MI | KM
  'countryIds': "countryIds_example", // String | Only places in these countries (comma-delimited country codes or WikiData ids)
  'excludedCountryIds': "excludedCountryIds_example", // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'types': "types_example", // String | Only places for these types (comma-delimited): CITY | ADM2
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findCitiesUsingGET(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **String**| Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | [optional] 
 **radius** | **Number**| The location radius within which to find places | [optional] 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]
 **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findDivisionsNearAdminDivisionUsingGET

> PopulatedPlacesResponse findDivisionsNearAdminDivisionUsingGET(divisionId, opts)

Find divisions near division

Find administrative divisions near the given origin division, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let divisionId = "divisionId_example"; // String | An admin-division id (either native 'id' or 'wikiDataId')
let opts = {
  'radius': 56, // Number | The location radius within which to find places
  'distanceUnit': "'MI'", // String | The unit of distance: MI | KM
  'countryIds': "countryIds_example", // String | Only places in these countries (comma-delimited country codes or WikiData ids)
  'excludedCountryIds': "excludedCountryIds_example", // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findDivisionsNearAdminDivisionUsingGET(divisionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divisionId** | **String**| An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 
 **radius** | **Number**| The location radius within which to find places | [optional] 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]
 **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findDivisionsNearLocationUsingGET

> PopulatedPlacesResponse findDivisionsNearLocationUsingGET(locationId, opts)

Find divisions near location

Find administrative divisions near the given location, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let locationId = "locationId_example"; // String | A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
let opts = {
  'radius': 56, // Number | The location radius within which to find places
  'distanceUnit': "'MI'", // String | The unit of distance: MI | KM
  'countryIds': "countryIds_example", // String | Only places in these countries (comma-delimited country codes or WikiData ids)
  'excludedCountryIds': "excludedCountryIds_example", // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findDivisionsNearLocationUsingGET(locationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locationId** | **String**| A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | 
 **radius** | **Number**| The location radius within which to find places | [optional] 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]
 **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findRegionCitiesUsingGET

> PopulatedPlacesResponse findRegionCitiesUsingGET(countryId, regionCode, opts)

Find country region cities

Get the cities in a specific country region. The country and region info is omitted in the response. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
let regionCode = "regionCode_example"; // String | An ISO-3166 or FIPS region code
let opts = {
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'types': "types_example", // String | Only places for these types (comma-delimited): CITY | ADM2
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort place results.  'Format: ±SORT_FIELD,±SORT_FIELD'  where SORT_FIELD = elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findRegionCitiesUsingGET(countryId, regionCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | **String**| An ISO-3166 country code or WikiData id | 
 **regionCode** | **String**| An ISO-3166 or FIPS region code | 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort place results.  &#39;Format: ±SORT_FIELD,±SORT_FIELD&#39;  where SORT_FIELD &#x3D; elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findRegionDivisionsUsingGET

> PopulatedPlacesResponse findRegionDivisionsUsingGET(countryId, regionCode, opts)

Find country region administrative divisions

Get the administrative divisions in a specific country region. The country and region info is omitted in the response. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
let regionCode = "regionCode_example"; // String | An ISO-3166 or FIPS region code
let opts = {
  'minPopulation': 56, // Number | Only places having at least this population
  'maxPopulation': 56, // Number | Only places having no more than this population
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'timeZoneIds': "timeZoneIds_example", // String | Only places in these time-zones (comma-delimited)
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example", // String | How to sort place results.  'Format: ±SORT_FIELD,±SORT_FIELD'  where SORT_FIELD = elevation | name | population 
  'includeDeleted': "'NONE'" // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
};
apiInstance.findRegionDivisionsUsingGET(countryId, regionCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | **String**| An ISO-3166 country code or WikiData id | 
 **regionCode** | **String**| An ISO-3166 or FIPS region code | 
 **minPopulation** | **Number**| Only places having at least this population | [optional] 
 **maxPopulation** | **Number**| Only places having no more than this population | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort place results.  &#39;Format: ±SORT_FIELD,±SORT_FIELD&#39;  where SORT_FIELD &#x3D; elevation | name | population  | [optional] 
 **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to &#39;NONE&#39;]

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAdminDivisionUsingGET

> PopulatedPlaceResponse getAdminDivisionUsingGET(divisionId, opts)

Get administrative division details

Get the details for a specific administrative division, including location coordinates, population, and elevation above sea-level (if available). 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let divisionId = "divisionId_example"; // String | An admin-division id (either native 'id' or 'wikiDataId')
let opts = {
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'languageCode': "languageCode_example" // String | Display results in this language
};
apiInstance.getAdminDivisionUsingGET(divisionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divisionId** | **String**| An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **languageCode** | **String**| Display results in this language | [optional] 

### Return type

[**PopulatedPlaceResponse**](PopulatedPlaceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCityDateTimeUsingGET

> DateTimeResponse getCityDateTimeUsingGET(cityId)

Get city date-time

Get city date-time

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
apiInstance.getCityDateTimeUsingGET(cityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 

### Return type

[**DateTimeResponse**](DateTimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCityDistanceUsingGET

> DistanceResponse getCityDistanceUsingGET(cityId, toCityId, opts)

Get city distance

Get distance from the given city

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
let toCityId = "toCityId_example"; // String | Distance to this city
let opts = {
  'distanceUnit': "'MI'" // String | The unit of distance: MI | KM
};
apiInstance.getCityDistanceUsingGET(cityId, toCityId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 
 **toCityId** | **String**| Distance to this city | 
 **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to &#39;MI&#39;]

### Return type

[**DistanceResponse**](DistanceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCityLocatedInUsingGET

> PopulatedPlaceResponse getCityLocatedInUsingGET(cityId, opts)

Get city admin region

Get the details for the containing populated place (e.g., its county or other administrative division), including location coordinates, population, and elevation above sea-level (if available). 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
let opts = {
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'languageCode': "languageCode_example" // String | Display results in this language
};
apiInstance.getCityLocatedInUsingGET(cityId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **languageCode** | **String**| Display results in this language | [optional] 

### Return type

[**PopulatedPlaceResponse**](PopulatedPlaceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCityTimeUsingGET

> TimeResponse getCityTimeUsingGET(cityId)

Get city time

Get city time

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
apiInstance.getCityTimeUsingGET(cityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 

### Return type

[**TimeResponse**](TimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCityUsingGET

> PopulatedPlaceResponse getCityUsingGET(cityId, opts)

Get city details

Get the details for a specific city, including location coordinates, population, and elevation above sea-level (if available). 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
let opts = {
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'languageCode': "languageCode_example" // String | Display results in this language
};
apiInstance.getCityUsingGET(cityId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **languageCode** | **String**| Display results in this language | [optional] 

### Return type

[**PopulatedPlaceResponse**](PopulatedPlaceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCountriesUsingGET

> CountriesResponse getCountriesUsingGET(opts)

Find countries

Find countries, filtering by optional criteria. If no criteria are set, you will get back all known countries. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let opts = {
  'currencyCode': "currencyCode_example", // String | Only countries supporting this currency
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example" // String | How to sort countries.  Format: ±SORT_FIELD  where SORT_FIELD = code | name
};
apiInstance.getCountriesUsingGET(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencyCode** | **String**| Only countries supporting this currency | [optional] 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort countries.  Format: ±SORT_FIELD  where SORT_FIELD &#x3D; code | name | [optional] 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCountryUsingGET

> CountryResponse getCountryUsingGET(countryId, opts)

Get country details

Get the details for a specific country, including number of regions.

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
let opts = {
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'languageCode': "languageCode_example" // String | Display results in this language
};
apiInstance.getCountryUsingGET(countryId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | **String**| An ISO-3166 country code or WikiData id | 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **languageCode** | **String**| Display results in this language | [optional] 

### Return type

[**CountryResponse**](CountryResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRegionUsingGET

> RegionResponse getRegionUsingGET(countryId, regionCode, opts)

Get region details

Get the details of a specific country region, including number of cities.

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
let regionCode = "regionCode_example"; // String | An ISO-3166 or FIPS region code
let opts = {
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'languageCode': "languageCode_example" // String | Display results in this language
};
apiInstance.getRegionUsingGET(countryId, regionCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | **String**| An ISO-3166 country code or WikiData id | 
 **regionCode** | **String**| An ISO-3166 or FIPS region code | 
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **languageCode** | **String**| Display results in this language | [optional] 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRegionsUsingGET

> RegionsResponse getRegionsUsingGET(countryId, opts)

Find country regions

Get all regions in a specific country. These could be states, provinces, districts, or otherwise major political divisions. 

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.GeoApi();
let countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
let opts = {
  'namePrefix': "namePrefix_example", // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
  'namePrefixDefaultLangResults': true, // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
  'asciiMode': false, // Boolean | Display results using ASCII characters
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'languageCode': "languageCode_example", // String | Display results in this language
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0, // Number | The zero-ary offset index into the results
  'sort': "sort_example" // String | How to sort regions.  Format: ±SORT_FIELD  where SORT_FIELD = fipsCode | isoCode | name
};
apiInstance.getRegionsUsingGET(countryId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | **String**| An ISO-3166 country code or WikiData id | 
 **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] 
 **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true]
 **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false]
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **languageCode** | **String**| Display results in this language | [optional] 
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]
 **sort** | **String**| How to sort regions.  Format: ±SORT_FIELD  where SORT_FIELD &#x3D; fipsCode | isoCode | name | [optional] 

### Return type

[**RegionsResponse**](RegionsResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

