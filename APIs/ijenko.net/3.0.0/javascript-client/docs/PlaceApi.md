# IoEIoTApiToCreateEndUserApplications.PlaceApi

All URIs are relative to *https://ioe2api.ijenko.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**placeBuses**](PlaceApi.md#placeBuses) | **GET** /places/{placeId}/buses | List Buses
[**placeGetMetadata**](PlaceApi.md#placeGetMetadata) | **GET** /places/{placeId}/metadata | List metadata
[**placeOpenPairing**](PlaceApi.md#placeOpenPairing) | **PUT** /places/{placeId}/buses/{busId}/pairing | Open/Close the pairing window
[**placePairing**](PlaceApi.md#placePairing) | **GET** /places/{placeId}/buses/{busId}/pairing | State of the pairing window
[**placePatch**](PlaceApi.md#placePatch) | **PATCH** /places/{placeId} | Update a Place
[**placePatchMetadata**](PlaceApi.md#placePatchMetadata) | **PATCH** /places/{placeId}/metadata | Modify metadata
[**placesGet**](PlaceApi.md#placesGet) | **GET** /places/{placeId} | Information about a Place



## placeBuses

> [BusItem] placeBuses(placeId, opts)

List Buses

Get the list of *Buses* available on the gateway of this *Place*. If &#x60;withPairing&#x60; is &#x60;true&#x60;, return only buses that allow device pairing (see &#x60;/places/{placeId}/buses/{busId}/pairing&#x60;).

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.PlaceApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let opts = {
  'withPairing': false // Boolean | Filter out buses that have no pairing window
};
apiInstance.placeBuses(placeId, opts, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **withPairing** | **Boolean**| Filter out buses that have no pairing window | [optional] [default to false]

### Return type

[**[BusItem]**](BusItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placeGetMetadata

> {String: Object} placeGetMetadata(placeId)

List metadata

Get the metadata.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.PlaceApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
apiInstance.placeGetMetadata(placeId, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 

### Return type

**{String: Object}**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placeOpenPairing

> BusPairing placeOpenPairing(placeId, busId, pairing)

Open/Close the pairing window

Open/Close the pairing window.  **Note**: requires full access to the *Account*. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.PlaceApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let busId = "busId_example"; // String | Unique identifier of a *Bus*.
let pairing = new IoEIoTApiToCreateEndUserApplications.BusPairing(); // BusPairing | 
apiInstance.placeOpenPairing(placeId, busId, pairing, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **busId** | **String**| Unique identifier of a *Bus*. | 
 **pairing** | [**BusPairing**](BusPairing.md)|  | 

### Return type

[**BusPairing**](BusPairing.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## placePairing

> BusPairing placePairing(placeId, busId)

State of the pairing window

Get the state of the pairing window of the *Bus*.  **Note**: requires full access to the *Account*. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.PlaceApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let busId = "busId_example"; // String | Unique identifier of a *Bus*.
apiInstance.placePairing(placeId, busId, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **busId** | **String**| Unique identifier of a *Bus*. | 

### Return type

[**BusPairing**](BusPairing.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placePatch

> placePatch(placeId, placePatch)

Update a Place

Change information about a *Place*.  **Note**: requires full access to the *Account*. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.PlaceApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let placePatch = new IoEIoTApiToCreateEndUserApplications.PlacePatch(); // PlacePatch | 
apiInstance.placePatch(placeId, placePatch, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **placePatch** | [**PlacePatch**](PlacePatch.md)|  | 

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## placePatchMetadata

> {String: Object} placePatchMetadata(placeId, metadataPatch)

Modify metadata

Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.PlaceApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let metadataPatch = new IoEIoTApiToCreateEndUserApplications.MetadataPatch(); // MetadataPatch | Modifications to apply to the metadata of the resource. 
apiInstance.placePatchMetadata(placeId, metadataPatch, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **metadataPatch** | [**MetadataPatch**](MetadataPatch.md)| Modifications to apply to the metadata of the resource.  | 

### Return type

**{String: Object}**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## placesGet

> Place placesGet(placeId)

Information about a Place

Get information about a *Place*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.PlaceApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
apiInstance.placesGet(placeId, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 

### Return type

[**Place**](Place.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

