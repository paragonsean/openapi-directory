# Apacta.OfferStatusesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offerStatusesBulkDeleteDelete**](OfferStatusesApi.md#offerStatusesBulkDeleteDelete) | **DELETE** /offer_statuses/bulkDelete | Bulk delete offer statuses
[**offerStatusesGet**](OfferStatusesApi.md#offerStatusesGet) | **GET** /offer_statuses | Get list of offer statuses
[**offerStatusesOfferStatusIdDelete**](OfferStatusesApi.md#offerStatusesOfferStatusIdDelete) | **DELETE** /offer_statuses/{offer_status_id} | Delete a offer status
[**offerStatusesOfferStatusIdGet**](OfferStatusesApi.md#offerStatusesOfferStatusIdGet) | **GET** /offer_statuses/{offer_status_id} | Get a single offer status
[**offerStatusesOfferStatusIdPut**](OfferStatusesApi.md#offerStatusesOfferStatusIdPut) | **PUT** /offer_statuses/{offer_status_id} | Edit a offer status
[**offerStatusesPost**](OfferStatusesApi.md#offerStatusesPost) | **POST** /offer_statuses | Create a new offer status



## offerStatusesBulkDeleteDelete

> EmptySuccessResponse offerStatusesBulkDeleteDelete(bulkActionRequestBody)

Bulk delete offer statuses

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.OfferStatusesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Offer statuses ids
apiInstance.offerStatusesBulkDeleteDelete(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Offer statuses ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offerStatusesGet

> OfferStatusesGet200Response offerStatusesGet()

Get list of offer statuses

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.OfferStatusesApi();
apiInstance.offerStatusesGet((error, data, response) => {
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

[**OfferStatusesGet200Response**](OfferStatusesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offerStatusesOfferStatusIdDelete

> EmptySuccessResponse offerStatusesOfferStatusIdDelete(offerStatusId)

Delete a offer status

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.OfferStatusesApi();
let offerStatusId = "offerStatusId_example"; // String | 
apiInstance.offerStatusesOfferStatusIdDelete(offerStatusId, (error, data, response) => {
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
 **offerStatusId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offerStatusesOfferStatusIdGet

> OfferStatusesOfferStatusIdGet200Response offerStatusesOfferStatusIdGet(offerStatusId)

Get a single offer status

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.OfferStatusesApi();
let offerStatusId = "offerStatusId_example"; // String | 
apiInstance.offerStatusesOfferStatusIdGet(offerStatusId, (error, data, response) => {
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
 **offerStatusId** | **String**|  | 

### Return type

[**OfferStatusesOfferStatusIdGet200Response**](OfferStatusesOfferStatusIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offerStatusesOfferStatusIdPut

> EmptySuccessResponse offerStatusesOfferStatusIdPut(offerStatusId)

Edit a offer status

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.OfferStatusesApi();
let offerStatusId = "offerStatusId_example"; // String | 
apiInstance.offerStatusesOfferStatusIdPut(offerStatusId, (error, data, response) => {
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
 **offerStatusId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offerStatusesPost

> EmptySuccessResponse offerStatusesPost(offerStatusesPostRequest)

Create a new offer status

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.OfferStatusesApi();
let offerStatusesPostRequest = new Apacta.OfferStatusesPostRequest(); // OfferStatusesPostRequest | 
apiInstance.offerStatusesPost(offerStatusesPostRequest, (error, data, response) => {
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
 **offerStatusesPostRequest** | [**OfferStatusesPostRequest**](OfferStatusesPostRequest.md)|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

