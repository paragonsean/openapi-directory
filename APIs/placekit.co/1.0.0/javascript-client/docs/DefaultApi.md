# PlaceKitApiReference.DefaultApi

All URIs are relative to *https://api.placekit.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reverse**](DefaultApi.md#reverse) | **POST** /reverse | Reverse geocoding
[**search**](DefaultApi.md#search) | **POST** /search | Search for addresses



## reverse

> Results reverse(opts)

Reverse geocoding

Performs a reverse geocoding search.  It will return the closest results around &#x60;coordinates&#x60;.\\ If &#x60;coordinates&#x60; are not set, it will use the user&#39;s IP to approximate its coordinates but results will be less accurate (city level accuracy instead of street level accuracy). 

### Example

```javascript
import PlaceKitApiReference from 'place_kit_api_reference';
let defaultClient = PlaceKitApiReference.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new PlaceKitApiReference.DefaultApi();
let opts = {
  'payload': new PlaceKitApiReference.ReverseRequest() // ReverseRequest | Request parameters
};
apiInstance.reverse(opts, (error, data, response) => {
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
 **payload** | [**ReverseRequest**](ReverseRequest.md)| Request parameters | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## search

> Results search(opts)

Search for addresses

Performs a forward geocoding search.  It will return results around &#x60;coordinates&#x60; (if provided) and the best matching textual relevance.  **It is highly recommended** to set the &#x60;countries&#x60; parameter with the country you need results from for the best accuracy and revelance possible. 

### Example

```javascript
import PlaceKitApiReference from 'place_kit_api_reference';
let defaultClient = PlaceKitApiReference.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new PlaceKitApiReference.DefaultApi();
let opts = {
  'payload': new PlaceKitApiReference.SearchRequest() // SearchRequest | Request parameters
};
apiInstance.search(opts, (error, data, response) => {
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
 **payload** | [**SearchRequest**](SearchRequest.md)| Request parameters | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

