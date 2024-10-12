# TheySaidSoQuotesApi.QshowApi

All URIs are relative to *https://quotes.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qshowDelete**](QshowApi.md#qshowDelete) | **DELETE** /qshow | 
[**qshowGet**](QshowApi.md#qshowGet) | **GET** /qshow | 
[**qshowListGet**](QshowApi.md#qshowListGet) | **GET** /qshow/list | 
[**qshowPatch**](QshowApi.md#qshowPatch) | **PATCH** /qshow | 
[**qshowPut**](QshowApi.md#qshowPut) | **PUT** /qshow | 
[**qshowQuotesAddPost**](QshowApi.md#qshowQuotesAddPost) | **POST** /qshow/quotes/add | 
[**qshowQuotesGet**](QshowApi.md#qshowQuotesGet) | **GET** /qshow/quotes | 
[**qshowQuotesRemovePost**](QshowApi.md#qshowQuotesRemovePost) | **POST** /qshow/quotes/remove | 



## qshowDelete

> qshowDelete(id)



Delete a qshow. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let id = "id_example"; // String | Qshow ID
apiInstance.qshowDelete(id, (error, data, response) => {
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
 **id** | **String**| Qshow ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## qshowGet

> qshowGet(id)



Gets a details about a qshow. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let id = "id_example"; // String | Qshow ID
apiInstance.qshowGet(id, (error, data, response) => {
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
 **id** | **String**| Qshow ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## qshowListGet

> qshowListGet(opts)



Get the list of Qshows in They Said So platform.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let opts = {
  'start': 0, // Number | Response is paged. This parameter controls where response starts the listing at
  '_public': false // Boolean | Should include public qshows or not in the list
};
apiInstance.qshowListGet(opts, (error, data, response) => {
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
 **start** | **Number**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0]
 **_public** | **Boolean**| Should include public qshows or not in the list | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qshowPatch

> qshowPatch(id, opts)



Update an existing qshow.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let id = "id_example"; // String | Qshow ID
let opts = {
  'title': "title_example", // String | Qshow title
  'description': "description_example", // String | Qshow description
  'tags': ["null"] // [String] | Tags for the qshow
};
apiInstance.qshowPatch(id, opts, (error, data, response) => {
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
 **id** | **String**| Qshow ID | 
 **title** | **String**| Qshow title | [optional] 
 **description** | **String**| Qshow description | [optional] 
 **tags** | [**[String]**](String.md)| Tags for the qshow | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qshowPut

> qshowPut(title, opts)



Create and add a new qshow to your private collection.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let title = "title_example"; // String | Qshow title
let opts = {
  'description': "description_example", // String | Qshow description
  'tags': ["null"] // [String] | Tags for the qshow
};
apiInstance.qshowPut(title, opts, (error, data, response) => {
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
 **title** | **String**| Qshow title | 
 **description** | **String**| Qshow description | [optional] 
 **tags** | [**[String]**](String.md)| Tags for the qshow | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qshowQuotesAddPost

> qshowQuotesAddPost(id, quoteid)



Add a quote to a given Qshow.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let id = "id_example"; // String | Qshow ID
let quoteid = "quoteid_example"; // String | Quote ID to add the qshow collection
apiInstance.qshowQuotesAddPost(id, quoteid, (error, data, response) => {
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
 **id** | **String**| Qshow ID | 
 **quoteid** | **String**| Quote ID to add the qshow collection | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qshowQuotesGet

> qshowQuotesGet(id)



Get the quotes in a given Qshow.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let id = "id_example"; // String | Qshow ID
apiInstance.qshowQuotesGet(id, (error, data, response) => {
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
 **id** | **String**| Qshow ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qshowQuotesRemovePost

> qshowQuotesRemovePost(id, quoteid)



Remove a quote to a given Qshow.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QshowApi();
let id = "id_example"; // String | Qshow ID
let quoteid = "quoteid_example"; // String | Quote ID to remove from the qshow collection
apiInstance.qshowQuotesRemovePost(id, quoteid, (error, data, response) => {
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
 **id** | **String**| Qshow ID | 
 **quoteid** | **String**| Quote ID to remove from the qshow collection | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

