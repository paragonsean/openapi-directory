# NprStationFinderService.StationfinderApi

All URIs are relative to *https://station.api.npr.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStationById**](StationfinderApi.md#getStationById) | **GET** /v3/stations/{stationId} | Retrieve metadata for the station with the given numeric ID
[**searchStations**](StationfinderApi.md#searchStations) | **GET** /v3/stations | List stations close to you or filter by search criteria



## getStationById

> StationDocument getStationById(authorization, stationId)

Retrieve metadata for the station with the given numeric ID

This endpoint retrieves information about a given station, based on its numeric ID, which is consistent across all of NPR&#39;s APIs.  A typical use case for this data is for clients who want to create a dropdown menu, modal/pop-up or dedicated page displaying more information about the station the client is localized to, including, for example, links to the station&#39;s homepage and donation (pledge) page.

### Example

```javascript
import NprStationFinderService from 'npr_station_finder_service';

let apiInstance = new NprStationFinderService.StationfinderApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let stationId = 789; // Number | The numeric ID of a station
apiInstance.getStationById(authorization, stationId, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **stationId** | **Number**| The numeric ID of a station | 

### Return type

[**StationDocument**](StationDocument.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## searchStations

> StationListDocument searchStations(authorization, opts)

List stations close to you or filter by search criteria

This endpoint has two main use cases:  - If no query parameters passed in, it returns a list of stations that are geographically closest to the calling client (based on GeoIP information) - If one or more query parameters are passed in, it performs a search of NPR stations that match those search criteria (not taking into account the client&#39;s physical location)  Clients wanting to implement a &#39;Change Station&#39; UI should use this endpoint to power their search. In most cases, you&#39;ll want to build a search interface that uses one of the 3 provided schemas: &#x60;lat&#x60; and &#x60;lon&#x60; (using e.g. the HTML5 Geolocation API), &#x60;city&#x60; and &#x60;state&#x60;, _or_ the generic &#x60;q&#x60; query which can accept a station name, call letters, network name, or zip code. Technically speaking, &#x60;q&#x60; can also take in either a city name or a state name, but using the &#x60;city&#x60; and &#x60;state&#x60; parameters together will yield more accurate geographic search results than &#x60;q&#x3D;{cityName}&#x60;.  The &#x60;lat&#x60; and &#x60;lon&#x60; query parameters should always be passed in together (otherwise the API will return a 400 error), and if included in the query, they will take precedence over any other search criteria; that is, &#x60;lat&#x60; and &#x60;lon&#x60; will do a purely geographic search and not take into account &#x60;q&#x60;, &#x60;city&#x60; or &#x60;state&#x60;.  Similarly, &#x60;city&#x60; and/or &#x60;state&#x60; will take precedence over (and ignore) &#x60;q&#x60;.  If clients want to be able to offer multiple types of searches (e.g. &#39;Search for a station name, city or zipcode&#39;) using a *single* search input form, &#x60;q&#x60; should be used. But again, be aware that using &#x60;city&#x60; and &#x60;state&#x60; together will yield more accurate search results than &#x60;q&#x3D;{cityName}&#x60;.

### Example

```javascript
import NprStationFinderService from 'npr_station_finder_service';

let apiInstance = new NprStationFinderService.StationfinderApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let opts = {
  'q': "q_example", // String | Search terms to search on; can be a station name, network name, call letters, or zipcode
  'city': "city_example", // String | A city to look for stations from; intended to be paired with `state`
  'state': "state_example", // String | A state to look for stations from (using the 2-letter abbreviation); intended to be paired with `city`
  'lat': 3.4, // Number | A latitude value from a geographic coordinate system; only works if paired with `lon`
  'lon': 3.4 // Number | A longitude value from a geographic coordinate system; only works if paired with `lat`
};
apiInstance.searchStations(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **q** | **String**| Search terms to search on; can be a station name, network name, call letters, or zipcode | [optional] 
 **city** | **String**| A city to look for stations from; intended to be paired with &#x60;state&#x60; | [optional] 
 **state** | **String**| A state to look for stations from (using the 2-letter abbreviation); intended to be paired with &#x60;city&#x60; | [optional] 
 **lat** | **Number**| A latitude value from a geographic coordinate system; only works if paired with &#x60;lon&#x60; | [optional] 
 **lon** | **Number**| A longitude value from a geographic coordinate system; only works if paired with &#x60;lat&#x60; | [optional] 

### Return type

[**StationListDocument**](StationListDocument.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json

