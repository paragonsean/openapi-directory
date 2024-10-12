# TurbineLabsApi.DomainApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainDomainKeyDelete**](DomainApi.md#domainDomainKeyDelete) | **DELETE** /domain/{domainKey} | delete domain
[**domainDomainKeyGet**](DomainApi.md#domainDomainKeyGet) | **GET** /domain/{domainKey} | get domain
[**domainGet**](DomainApi.md#domainGet) | **GET** /domain | get domains
[**domainPost**](DomainApi.md#domainPost) | **POST** /domain | create domain



## domainDomainKeyDelete

> Object domainDomainKeyDelete(domainKey, checksum)

delete domain

Delete an existing domain

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.DomainApi();
let domainKey = "48cf1c9b-f027-4223-b405-d48018ffb900"; // String | the domain key
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the domain to be deleted
apiInstance.domainDomainKeyDelete(domainKey, checksum, (error, data, response) => {
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
 **domainKey** | **String**| the domain key | 
 **checksum** | **String**| the current checksum of the domain to be deleted | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainDomainKeyGet

> DomainResult domainDomainKeyGet(domainKey)

get domain

Get details for a single domain

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.DomainApi();
let domainKey = "48cf1c9b-f027-4223-b405-d48018ffb900"; // String | the domain key
apiInstance.domainDomainKeyGet(domainKey, (error, data, response) => {
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
 **domainKey** | **String**| the domain key | 

### Return type

[**DomainResult**](DomainResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainGet

> MultiDomainResult domainGet(opts)

get domains

Get a list of domains

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.DomainApi();
let opts = {
  'filters': "filters_example" // String | A JSON encoded array of DomainFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any DomainFilter will be included. 
};
apiInstance.domainGet(opts, (error, data, response) => {
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
 **filters** | **String**| A JSON encoded array of DomainFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any DomainFilter will be included.  | [optional] 

### Return type

[**MultiDomainResult**](MultiDomainResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainPost

> DomainResult domainPost(domain)

create domain

Create a new domain

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.DomainApi();
let domain = new TurbineLabsApi.DomainCreate(); // DomainCreate | the domain to create
apiInstance.domainPost(domain, (error, data, response) => {
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
 **domain** | [**DomainCreate**](DomainCreate.md)| the domain to create | 

### Return type

[**DomainResult**](DomainResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

