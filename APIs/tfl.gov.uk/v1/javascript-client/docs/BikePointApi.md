# TransportForLondonUnifiedApi.BikePointApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bikePointGet**](BikePointApi.md#bikePointGet) | **GET** /BikePoint/{id} | Gets the bike point with the given id.
[**bikePointGetAll**](BikePointApi.md#bikePointGetAll) | **GET** /BikePoint | Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces              numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) !&#x3D; 0 indicates broken docks.
[**bikePointSearch**](BikePointApi.md#bikePointSearch) | **GET** /BikePoint/Search | Search for bike stations by their name, a bike point&#39;s name often contains information about the name of the street              or nearby landmarks, for example. Note that the search result does not contain the PlaceProperties i.e. the status              or occupancy of the BikePoint, to get that information you should retrieve the BikePoint by its id on /BikePoint/id.



## bikePointGet

> TflApiPresentationEntitiesPlace bikePointGet(id)

Gets the bike point with the given id.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.BikePointApi();
let id = "id_example"; // String | A bike point id (a list of ids can be obtained from the above BikePoint call)
apiInstance.bikePointGet(id, (error, data, response) => {
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
 **id** | **String**| A bike point id (a list of ids can be obtained from the above BikePoint call) | 

### Return type

[**TflApiPresentationEntitiesPlace**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## bikePointGetAll

> [TflApiPresentationEntitiesPlace] bikePointGetAll()

Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces              numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) !&#x3D; 0 indicates broken docks.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.BikePointApi();
apiInstance.bikePointGetAll((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## bikePointSearch

> [TflApiPresentationEntitiesPlace] bikePointSearch(query)

Search for bike stations by their name, a bike point&#39;s name often contains information about the name of the street              or nearby landmarks, for example. Note that the search result does not contain the PlaceProperties i.e. the status              or occupancy of the BikePoint, to get that information you should retrieve the BikePoint by its id on /BikePoint/id.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.BikePointApi();
let query = "query_example"; // String | The search term e.g. \"St. James\"
apiInstance.bikePointSearch(query, (error, data, response) => {
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
 **query** | **String**| The search term e.g. \&quot;St. James\&quot; | 

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

