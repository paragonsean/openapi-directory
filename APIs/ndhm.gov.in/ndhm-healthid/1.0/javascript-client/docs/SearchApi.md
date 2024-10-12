# HealthIdService.SearchApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchUserByAccountUsingPOST**](SearchApi.md#searchUserByAccountUsingPOST) | **POST** /v1/search/searchByHealthId | Search a user by Health ID Number.
[**searchUserByMobileUsingPOST**](SearchApi.md#searchUserByMobileUsingPOST) | **POST** /v1/search/searchByMobile | Search users with a mobile number.
[**searchUserByUseridUsingPOST**](SearchApi.md#searchUserByUseridUsingPOST) | **POST** /v1/search/existsByHealthId | Search a user by Health IDs.



## searchUserByAccountUsingPOST

> SearchResponseSingle searchUserByAccountUsingPOST(searchRequest, opts)

Search a user by Health ID Number.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.SearchApi();
let searchRequest = new HealthIdService.SearchByHealthIdRequest(); // SearchByHealthIdRequest | searchRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.searchUserByAccountUsingPOST(searchRequest, opts, (error, data, response) => {
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
 **searchRequest** | [**SearchByHealthIdRequest**](SearchByHealthIdRequest.md)| searchRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**SearchResponseSingle**](SearchResponseSingle.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## searchUserByMobileUsingPOST

> SearchResponseSingle searchUserByMobileUsingPOST(searchRequest, opts)

Search users with a mobile number.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.SearchApi();
let searchRequest = new HealthIdService.SearchByMobileRequest(); // SearchByMobileRequest | searchRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.searchUserByMobileUsingPOST(searchRequest, opts, (error, data, response) => {
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
 **searchRequest** | [**SearchByMobileRequest**](SearchByMobileRequest.md)| searchRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**SearchResponseSingle**](SearchResponseSingle.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## searchUserByUseridUsingPOST

> Object searchUserByUseridUsingPOST(searchDTO, opts)

Search a user by Health IDs.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.SearchApi();
let searchDTO = new HealthIdService.SearchByHealthIdRequest(); // SearchByHealthIdRequest | searchDTO
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.searchUserByUseridUsingPOST(searchDTO, opts, (error, data, response) => {
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
 **searchDTO** | [**SearchByHealthIdRequest**](SearchByHealthIdRequest.md)| searchDTO | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

