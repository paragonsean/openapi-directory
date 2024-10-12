# ShipEngineApi.ServicePointsApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicePointsGetById**](ServicePointsApi.md#servicePointsGetById) | **GET** /v1/service_points/{carrier_code}/{country_code}/{service_point_id} | Get Service Point By ID
[**servicePointsList**](ServicePointsApi.md#servicePointsList) | **POST** /v1/service_points/list | List Service Points



## servicePointsGetById

> GetServicePointByIdResponseBody servicePointsGetById(carrierCode, countryCode, servicePointId)

Get Service Point By ID

Returns a carrier service point by using the service_point_id

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ServicePointsApi();
let carrierCode = "stamps_com"; // String | Carrier code
let countryCode = "CA"; // String | A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1) 
let servicePointId = "614940"; // String | 
apiInstance.servicePointsGetById(carrierCode, countryCode, servicePointId, (error, data, response) => {
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
 **carrierCode** | **String**| Carrier code | 
 **countryCode** | **String**| A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)  | 
 **servicePointId** | **String**|  | 

### Return type

[**GetServicePointByIdResponseBody**](GetServicePointByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicePointsList

> ListServicePointsResponseBody servicePointsList(getServicePointsRequest)

List Service Points

List carrier service points by location

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ServicePointsApi();
let getServicePointsRequest = new ShipEngineApi.GetServicePointsRequest(); // GetServicePointsRequest | 
apiInstance.servicePointsList(getServicePointsRequest, (error, data, response) => {
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
 **getServicePointsRequest** | [**GetServicePointsRequest**](GetServicePointsRequest.md)|  | 

### Return type

[**ListServicePointsResponseBody**](ListServicePointsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

