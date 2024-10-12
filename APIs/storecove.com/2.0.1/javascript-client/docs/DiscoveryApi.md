# StorecoveApi.DiscoveryApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discoveryExists**](DiscoveryApi.md#discoveryExists) | **POST** /discovery/exists | Discover Network Participant Existence
[**discoveryIdentifiers**](DiscoveryApi.md#discoveryIdentifiers) | **GET** /discovery/identifiers | Discover Country Identifiers ** EXPERIMENTAL
[**discoveryReceives**](DiscoveryApi.md#discoveryReceives) | **POST** /discovery/receives | Disover Network Participant



## discoveryExists

> DiscoveredParticipant discoveryExists(discoverableParticipant)

Discover Network Participant Existence

Discover if a network participant exists.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.DiscoveryApi();
let discoverableParticipant = new StorecoveApi.DiscoverableParticipant(); // DiscoverableParticipant | The participant to check
apiInstance.discoveryExists(discoverableParticipant, (error, data, response) => {
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
 **discoverableParticipant** | [**DiscoverableParticipant**](DiscoverableParticipant.md)| The participant to check | 

### Return type

[**DiscoveredParticipant**](DiscoveredParticipant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## discoveryIdentifiers

> CountrySpecifications discoveryIdentifiers()

Discover Country Identifiers ** EXPERIMENTAL

Discover the identifiers used in each country, for routing, for legal identification as well as for tax identification purposes. We are currently testing this endpoint with selected Customers. If you would like to participate, please contact us.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.DiscoveryApi();
apiInstance.discoveryIdentifiers((error, data, response) => {
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

[**CountrySpecifications**](CountrySpecifications.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## discoveryReceives

> DiscoveredParticipant discoveryReceives(discoverableParticipant)

Disover Network Participant

Discover a network participant and capabilities.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.DiscoveryApi();
let discoverableParticipant = new StorecoveApi.DiscoverableParticipant(); // DiscoverableParticipant | The participant to check
apiInstance.discoveryReceives(discoverableParticipant, (error, data, response) => {
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
 **discoverableParticipant** | [**DiscoverableParticipant**](DiscoverableParticipant.md)| The participant to check | 

### Return type

[**DiscoveredParticipant**](DiscoveredParticipant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

