# TheySaidSoQuotesApi.QuoteOfTheDayApi

All URIs are relative to *https://quotes.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qodCategoriesGet**](QuoteOfTheDayApi.md#qodCategoriesGet) | **GET** /qod/categories | 
[**qodGet**](QuoteOfTheDayApi.md#qodGet) | **GET** /qod | 
[**qodLanguagesGet**](QuoteOfTheDayApi.md#qodLanguagesGet) | **GET** /qod/languages | 



## qodCategoriesGet

> qodCategoriesGet(opts)



Gets a list of &#x60;Quote of the Day&#x60; Categories. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteOfTheDayApi();
let opts = {
  'language': "'en'", // String | Language of the QOD category. The language must be supported in our QOD system.
  'detailed': false // Boolean | Return detailed information of the categories. Note the data format changes between the two values of this switch.
};
apiInstance.qodCategoriesGet(opts, (error, data, response) => {
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
 **language** | **String**| Language of the QOD category. The language must be supported in our QOD system. | [optional] [default to &#39;en&#39;]
 **detailed** | **Boolean**| Return detailed information of the categories. Note the data format changes between the two values of this switch. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qodGet

> QODResponse qodGet(opts)



Gets &#x60;Quote of the Day&#x60; (QOD). Optional &#x60;category&#x60; param determines the category of returned quote of the day 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteOfTheDayApi();
let opts = {
  'category': "category_example", // String | QOD Category (Used in public QOD only)
  'language': "'en'", // String | Language of the QOD. The language must be supported in our QOD system.
  'id': "id_example" // String | QOD defition id (Used in private QOD only)
};
apiInstance.qodGet(opts, (error, data, response) => {
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
 **category** | **String**| QOD Category (Used in public QOD only) | [optional] 
 **language** | **String**| Language of the QOD. The language must be supported in our QOD system. | [optional] [default to &#39;en&#39;]
 **id** | **String**| QOD defition id (Used in private QOD only) | [optional] 

### Return type

[**QODResponse**](QODResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## qodLanguagesGet

> qodLanguagesGet()



Gets a list of supported languages for &#x60;Quote of the Day&#x60;.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteOfTheDayApi();
apiInstance.qodLanguagesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

