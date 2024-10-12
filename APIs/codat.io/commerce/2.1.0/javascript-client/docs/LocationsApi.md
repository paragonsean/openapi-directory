# CommerceApi.LocationsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listLocations**](LocationsApi.md#listLocations) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-locations | List locations



## listLocations

> LocationsResponse listLocations(companyId, connectionId)

List locations

Retrieve a list of locations as seen in the commerce platform.  A &#x60;location&#x60; is a geographic place at which stocks of products may be held, or from where orders were placed.

### Example

```javascript
import CommerceApi from 'commerce_api';
let defaultClient = CommerceApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CommerceApi.LocationsApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let connectionId = "2e9d2c44-f675-40ba-8049-353bfcb5e171"; // String | 
apiInstance.listLocations(companyId, connectionId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **connectionId** | **String**|  | 

### Return type

[**LocationsResponse**](LocationsResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

