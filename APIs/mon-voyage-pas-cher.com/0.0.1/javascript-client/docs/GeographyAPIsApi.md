# MonVoyagePasCherComPublicApi.GeographyAPIsApi

All URIs are relative to *https://api.mon-voyage-pas-cher.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAirport**](GeographyAPIsApi.md#getAirport) | **GET** /airports | Search airports by country / Search nearby airports / Search an airport
[**getAutocomplete**](GeographyAPIsApi.md#getAutocomplete) | **GET** /cities/findcitiesfromtext | Retrieve cities informations from a string / build an autocomplete
[**getCities**](GeographyAPIsApi.md#getCities) | **GET** /cities/findcitiesfromlatlong | Search all cities from lat/long or countrycode
[**getContinents**](GeographyAPIsApi.md#getContinents) | **GET** /continents | Search all continents or one specific continent
[**getCountries**](GeographyAPIsApi.md#getCountries) | **GET** /countries | Search all countries or one specific country
[**getSignificantCities**](GeographyAPIsApi.md#getSignificantCities) | **GET** /cities/significant | Search significant cities from lat/long or countrycode



## getAirport

> AirportsSearchResponse getAirport(language, opts)

Search airports by country / Search nearby airports / Search an airport

This webservice is providing you the ability to retrieve a list of airports matching your search criterias.&lt;br /&gt;The 3 mains search criterias are&lt;br /&gt;- by country code, this will list all airports for a given country.&lt;br /&gt;- by latitude/longitude with a radius in km. You can actually combine those 2 criterias, and search for example the closest airport in the USA of Vancoucer, Canada.&lt;br /&gt;- The last way to use the API is by searching directly with a IATA CODE in the location parameter, this will only return one result in the array of data results

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.GeographyAPIsApi();
let language = "language_example"; // String | the language code of the language you want the content to be returned
let opts = {
  'location': "location_example", // String | The location you want to search for. Either a latitude/longitude point or a letter airport IATA CODE ( ex. LHR ) if you want the detail for only one single airport.
  'radius': 100, // Number | Radius in km for a lat/long search, will be ignore if a IATA is passed in location parameter code is passed
  'countrycode': "countrycode_example", // String | Filter - The country ISO code 2 letters, provided by the GET /countries. If passed the results will be filtered to this country only, regardless if you passed a lat/long and a large radius
  'topAirports': true // Boolean | Filter the results to only the top and large airports airports.
};
apiInstance.getAirport(language, opts, (error, data, response) => {
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
 **language** | **String**| the language code of the language you want the content to be returned | 
 **location** | **String**| The location you want to search for. Either a latitude/longitude point or a letter airport IATA CODE ( ex. LHR ) if you want the detail for only one single airport. | [optional] 
 **radius** | **Number**| Radius in km for a lat/long search, will be ignore if a IATA is passed in location parameter code is passed | [optional] [default to 100]
 **countrycode** | **String**| Filter - The country ISO code 2 letters, provided by the GET /countries. If passed the results will be filtered to this country only, regardless if you passed a lat/long and a large radius | [optional] 
 **topAirports** | **Boolean**| Filter the results to only the top and large airports airports. | [optional] 

### Return type

[**AirportsSearchResponse**](AirportsSearchResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAutocomplete

> CitiesResponse getAutocomplete(q, language, sort, opts)

Retrieve cities informations from a string / build an autocomplete

Search cities from a string parameters.

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.GeographyAPIsApi();
let q = "q_example"; // String | the string you want to search
let language = "language_example"; // String | the language code of the language you want the content to be returned
let sort = "'population,desc'"; // String | The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
let opts = {
  'countrycode': "countrycode_example" // String | if you want to limit the result to one country
};
apiInstance.getAutocomplete(q, language, sort, opts, (error, data, response) => {
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
 **q** | **String**| the string you want to search | 
 **language** | **String**| the language code of the language you want the content to be returned | 
 **sort** | **String**| The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point | [default to &#39;population,desc&#39;]
 **countrycode** | **String**| if you want to limit the result to one country | [optional] 

### Return type

[**CitiesResponse**](CitiesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCities

> CitiesResponse getCities(language, sort, opts)

Search all cities from lat/long or countrycode

Search cities according to given criterias. Either lat/long + radius or country code. A limit can be given but cannot exceed 50 results.&lt;br /&gt; A significant city will be defined according to the pourcent of population within a country.

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.GeographyAPIsApi();
let language = "language_example"; // String | the language code of the language you want the content to be returned
let sort = "'distance,asc'"; // String | The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
let opts = {
  'countrycode': "countrycode_example", // String | if you want to limit the result to one country
  'location': "location_example", // String | The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456)
  'radius': 20, // Number | Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed
  'limit': 20, // Number | Limit of the result. Default is 20 rows, and maximum is 50.
  'offset': 0 // Number | offset of the result set
};
apiInstance.getCities(language, sort, opts, (error, data, response) => {
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
 **language** | **String**| the language code of the language you want the content to be returned | 
 **sort** | **String**| The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point | [default to &#39;distance,asc&#39;]
 **countrycode** | **String**| if you want to limit the result to one country | [optional] 
 **location** | **String**| The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456) | [optional] 
 **radius** | **Number**| Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed | [optional] [default to 20]
 **limit** | **Number**| Limit of the result. Default is 20 rows, and maximum is 50. | [optional] [default to 20]
 **offset** | **Number**| offset of the result set | [optional] [default to 0]

### Return type

[**CitiesResponse**](CitiesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinents

> ContinentsResponse getContinents(language, opts)

Search all continents or one specific continent

This webservice is providing you the ability to retrieve all informations about continents

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.GeographyAPIsApi();
let language = "language_example"; // String | The language code of the language you want the content to be returned
let opts = {
  'continentcode': "continentcode_example" // String | The code of the continent you want to retrieve, this parameter is not required if you want ot retrieve all continents at once
};
apiInstance.getContinents(language, opts, (error, data, response) => {
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
 **language** | **String**| The language code of the language you want the content to be returned | 
 **continentcode** | **String**| The code of the continent you want to retrieve, this parameter is not required if you want ot retrieve all continents at once | [optional] 

### Return type

[**ContinentsResponse**](ContinentsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCountries

> CountriesResponse getCountries(language, opts)

Search all countries or one specific country

This webservice is providing you the ability to retrieve a list of countries matching your search criterias.&lt;br /&gt;The 2 mains ways to search use this API are&lt;br /&gt;- by countrycode, it will only returns you one country&lt;br /&gt;- without the countrycode parameter which will return the full list of countries

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.GeographyAPIsApi();
let language = "language_example"; // String | the language code of the language you want the content to be returned
let opts = {
  'countrycode': "countrycode_example" // String | The code of the country you want to retrieve
};
apiInstance.getCountries(language, opts, (error, data, response) => {
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
 **language** | **String**| the language code of the language you want the content to be returned | 
 **countrycode** | **String**| The code of the country you want to retrieve | [optional] 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSignificantCities

> CitiesResponse getSignificantCities(language, sort, opts)

Search significant cities from lat/long or countrycode

Search cities according to given criterias. Either lat/long + radius or country code. A limit can be given but cannot exceed 50 results.&lt;br /&gt; A significant city will be defined according to the pourcent of population within a country.

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.GeographyAPIsApi();
let language = "language_example"; // String | the language code of the language you want the content to be returned
let sort = "'population,desc'"; // String | The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
let opts = {
  'pourcent': 0.5, // Number | The pourcent of population the cities need to be in order to appear in results
  'countrycode': "countrycode_example", // String | if you want to limit the result to one country
  'location': "location_example", // String | The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456)
  'radius': 20, // Number | Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed
  'limit': 20, // Number | Limit of the result. Default is 20 rows, and maximum is 50.
  'offset': 0 // Number | offset of the result set
};
apiInstance.getSignificantCities(language, sort, opts, (error, data, response) => {
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
 **language** | **String**| the language code of the language you want the content to be returned | 
 **sort** | **String**| The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point | [default to &#39;population,desc&#39;]
 **pourcent** | **Number**| The pourcent of population the cities need to be in order to appear in results | [optional] [default to 0.5]
 **countrycode** | **String**| if you want to limit the result to one country | [optional] 
 **location** | **String**| The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456) | [optional] 
 **radius** | **Number**| Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed | [optional] [default to 20]
 **limit** | **Number**| Limit of the result. Default is 20 rows, and maximum is 50. | [optional] [default to 20]
 **offset** | **Number**| offset of the result set | [optional] [default to 0]

### Return type

[**CitiesResponse**](CitiesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

