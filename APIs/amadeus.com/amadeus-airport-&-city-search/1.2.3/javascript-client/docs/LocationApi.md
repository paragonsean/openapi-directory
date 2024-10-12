# AirportCitySearch.LocationApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAirportCity**](LocationApi.md#getAirportCity) | **GET** /reference-data/locations/{locationId} | Returns a specific airports or cities based on its id.
[**getAirportCitySearch**](LocationApi.md#getAirportCitySearch) | **GET** /reference-data/locations | Returns a list of airports and cities matching a given keyword.



## getAirportCity

> Success1 getAirportCity(locationId)

Returns a specific airports or cities based on its id.

### Example

```javascript
import AirportCitySearch from 'airport__city_search';

let apiInstance = new AirportCitySearch.LocationApi();
let locationId = "locationId_example"; // String | identifier of the location
apiInstance.getAirportCity(locationId, (error, data, response) => {
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
 **locationId** | **String**| identifier of the location | 

### Return type

[**Success1**](Success1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json


## getAirportCitySearch

> Success getAirportCitySearch(subType, keyword, opts)

Returns a list of airports and cities matching a given keyword.

### Example

```javascript
import AirportCitySearch from 'airport__city_search';

let apiInstance = new AirportCitySearch.LocationApi();
let subType = ["null"]; // [String] | sub type of the location (AIRPORT and/or CITY)
let keyword = "MUC"; // String | keyword that should represent the start of a word in a city or airport name or code.   Supported charaters are: A-Za-z0-9./:-'()\"
let opts = {
  'countryCode': "countryCode_example", // String | Country code of the location using [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US).
  'pageLimit': 10, // Number | maximum items in one page
  'pageOffset': 0, // Number | start index of the requested page
  'sort': "'analytics.travelers.score'", // String | defines on which attribute the sorting will be done: * analytics.travelers.score - sort by the number of travelers by airport or city, the airports and cities with the highest traffic are on top of the results 
  'view': "'FULL'" // String | select the level of information of the reply: * LIGHT - Gives only the IATACode, name, detailedName, cityName and countryName * FULL - Adds on top of the LIGHT information the timeZoneOffset, geocode, detailed address and travelers.score default option is FULL 
};
apiInstance.getAirportCitySearch(subType, keyword, opts, (error, data, response) => {
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
 **subType** | [**[String]**](String.md)| sub type of the location (AIRPORT and/or CITY) | 
 **keyword** | **String**| keyword that should represent the start of a word in a city or airport name or code.   Supported charaters are: A-Za-z0-9./:-&#39;()\&quot; | 
 **countryCode** | **String**| Country code of the location using [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US). | [optional] 
 **pageLimit** | **Number**| maximum items in one page | [optional] [default to 10]
 **pageOffset** | **Number**| start index of the requested page | [optional] [default to 0]
 **sort** | **String**| defines on which attribute the sorting will be done: * analytics.travelers.score - sort by the number of travelers by airport or city, the airports and cities with the highest traffic are on top of the results  | [optional] [default to &#39;analytics.travelers.score&#39;]
 **view** | **String**| select the level of information of the reply: * LIGHT - Gives only the IATACode, name, detailedName, cityName and countryName * FULL - Adds on top of the LIGHT information the timeZoneOffset, geocode, detailed address and travelers.score default option is FULL  | [optional] [default to &#39;FULL&#39;]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

