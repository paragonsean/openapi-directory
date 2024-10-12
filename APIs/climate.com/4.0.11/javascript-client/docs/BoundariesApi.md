# ClimateFieldViewPlatformApis.BoundariesApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchBoundaries**](BoundariesApi.md#fetchBoundaries) | **POST** /v4/boundaries/query | Retrieve Boundaries in batch
[**fetchBoundaryById**](BoundariesApi.md#fetchBoundaryById) | **GET** /v4/boundaries/{boundaryId} | Retrieve a Boundary by ID
[**uploadBoundary**](BoundariesApi.md#uploadBoundary) | **POST** /v4/boundaries | Upload a boundary



## fetchBoundaries

> Boundaries fetchBoundaries(opts)

Retrieve Boundaries in batch

Retrieve multiple **Boundaries** (up to 10 per request).

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.BoundariesApi();
let opts = {
  'boundariesQuery': new ClimateFieldViewPlatformApis.BoundariesQuery() // BoundariesQuery | 
};
apiInstance.fetchBoundaries(opts, (error, data, response) => {
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
 **boundariesQuery** | [**BoundariesQuery**](BoundariesQuery.md)|  | [optional] 

### Return type

[**Boundaries**](Boundaries.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fetchBoundaryById

> Boundary fetchBoundaryById(boundaryId)

Retrieve a Boundary by ID

Retrieve a **Boundary** by ID.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.BoundariesApi();
let boundaryId = "boundaryId_example"; // String | Unique identifier of the Boundary
apiInstance.fetchBoundaryById(boundaryId, (error, data, response) => {
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
 **boundaryId** | **String**| Unique identifier of the Boundary | 

### Return type

[**Boundary**](Boundary.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadBoundary

> UploadedBoundaryId uploadBoundary(opts)

Upload a boundary

Upload a **Boundary** entry by passing the geometry of the boundary. This will store the boundary but will not create field in Climate FieldView and will not link to an existing field in Climate FieldView. This is restricted to callers with **boundaries:write** scope. To upload a field boundary for field creation in Climate FieldView, please use **POST /v4/uploads**.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.BoundariesApi();
let opts = {
  'boundaryUpload': new ClimateFieldViewPlatformApis.BoundaryUpload() // BoundaryUpload | 
};
apiInstance.uploadBoundary(opts, (error, data, response) => {
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
 **boundaryUpload** | [**BoundaryUpload**](BoundaryUpload.md)|  | [optional] 

### Return type

[**UploadedBoundaryId**](UploadedBoundaryId.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

