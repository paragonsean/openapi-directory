# HereNetworkPositioningApiV2.APIInformationApi

All URIs are relative to *https://positioning.hereapi.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApiVersion**](APIInformationApi.md#getApiVersion) | **GET** /version | API version
[**getHealth**](APIInformationApi.md#getHealth) | **GET** /health | Service health



## getApiVersion

> ApiVersion getApiVersion()

API version

Retrieves API Specification version information

### Example

```javascript
import HereNetworkPositioningApiV2 from 'here_network_positioning_api_v2';
let defaultClient = HereNetworkPositioningApiV2.ApiClient.instance;
// Configure API key authorization: APIKey
let APIKey = defaultClient.authentications['APIKey'];
APIKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: AccessToken
let AccessToken = defaultClient.authentications['AccessToken'];
AccessToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new HereNetworkPositioningApiV2.APIInformationApi();
apiInstance.getApiVersion((error, data, response) => {
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

[**ApiVersion**](ApiVersion.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHealth

> ApiHealthStatus getHealth()

Service health

Tests basic health of the service

### Example

```javascript
import HereNetworkPositioningApiV2 from 'here_network_positioning_api_v2';
let defaultClient = HereNetworkPositioningApiV2.ApiClient.instance;
// Configure API key authorization: APIKey
let APIKey = defaultClient.authentications['APIKey'];
APIKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: AccessToken
let AccessToken = defaultClient.authentications['AccessToken'];
AccessToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new HereNetworkPositioningApiV2.APIInformationApi();
apiInstance.getHealth((error, data, response) => {
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

[**ApiHealthStatus**](ApiHealthStatus.md)

### Authorization

[APIKey](../README.md#APIKey), [AccessToken](../README.md#AccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

