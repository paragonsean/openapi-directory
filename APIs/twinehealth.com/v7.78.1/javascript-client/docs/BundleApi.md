# FitbitPlusApi.BundleApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBundle**](BundleApi.md#createBundle) | **POST** /bundle | Create bundle
[**fetchBundle**](BundleApi.md#fetchBundle) | **GET** /bundle/{id} | Get a bundle
[**updateBundle**](BundleApi.md#updateBundle) | **PATCH** /bundle/{id} | Update a bundle



## createBundle

> CreateBundleResponse createBundle(createBundleRequest)

Create bundle

Create a bundle in a patient&#39;s plan

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.BundleApi();
let createBundleRequest = new FitbitPlusApi.CreateBundleRequest(); // CreateBundleRequest | 
apiInstance.createBundle(createBundleRequest, (error, data, response) => {
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
 **createBundleRequest** | [**CreateBundleRequest**](CreateBundleRequest.md)|  | 

### Return type

[**CreateBundleResponse**](CreateBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchBundle

> FetchBundleResponse fetchBundle(id)

Get a bundle

Get a bundle from a patient&#39;s plan.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.BundleApi();
let id = "id_example"; // String | Bundle identifier
apiInstance.fetchBundle(id, (error, data, response) => {
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
 **id** | **String**| Bundle identifier | 

### Return type

[**FetchBundleResponse**](FetchBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## updateBundle

> UpdateBundleResponse updateBundle(id, updateBundleRequest)

Update a bundle

Updte a bundle from a patient&#39;s plan.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.BundleApi();
let id = "id_example"; // String | Bundle identifier
let updateBundleRequest = new FitbitPlusApi.UpdateBundleRequest(); // UpdateBundleRequest | 
apiInstance.updateBundle(id, updateBundleRequest, (error, data, response) => {
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
 **id** | **String**| Bundle identifier | 
 **updateBundleRequest** | [**UpdateBundleRequest**](UpdateBundleRequest.md)|  | 

### Return type

[**UpdateBundleResponse**](UpdateBundleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json

