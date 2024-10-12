# TheySaidSoQuotesApi.PrivateQODApi

All URIs are relative to *https://quotes.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qodGet_0**](PrivateQODApi.md#qodGet_0) | **GET** /qod | 
[**qodPatch**](PrivateQODApi.md#qodPatch) | **PATCH** /qod | 
[**qodPut**](PrivateQODApi.md#qodPut) | **PUT** /qod | 



## qodGet_0

> QODResponse qodGet_0(opts)



Gets &#x60;Quote of the Day&#x60; (QOD). Optional &#x60;category&#x60; param determines the category of returned quote of the day 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQODApi();
let opts = {
  'category': "category_example", // String | QOD Category (Used in public QOD only)
  'language': "'en'", // String | Language of the QOD. The language must be supported in our QOD system.
  'id': "id_example" // String | QOD defition id (Used in private QOD only)
};
apiInstance.qodGet_0(opts, (error, data, response) => {
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


## qodPatch

> QuoteResponse qodPatch(title, opts)



Update an existing private &#x60;Quote of the Day&#x60; definition. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQODApi();
let title = "title_example"; // String | Title of the Quote of the day category
let opts = {
  'repeatAfter': 30, // Number | How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
  'authors': "authors_example", // Array | Comma seperated author names. Quotes will be chosen from one of these authors.
  '_private': false, // Boolean | Should apply the filters to the private collection. Default is public quotes in the platform.
  'language': "'en'", // String | Quotes language.
  'sfw': false // Boolean | Consider only quotes marked as \"sfw\" (Safe for work).
};
apiInstance.qodPatch(title, opts, (error, data, response) => {
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
 **title** | **String**| Title of the Quote of the day category | 
 **repeatAfter** | **Number**| How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here. | [optional] [default to 30]
 **authors** | **Array**| Comma seperated author names. Quotes will be chosen from one of these authors. | [optional] 
 **_private** | **Boolean**| Should apply the filters to the private collection. Default is public quotes in the platform. | [optional] [default to false]
 **language** | **String**| Quotes language. | [optional] [default to &#39;en&#39;]
 **sfw** | **Boolean**| Consider only quotes marked as \&quot;sfw\&quot; (Safe for work). | [optional] [default to false]

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## qodPut

> SuccessResponse qodPut(title, opts)



Create a private &#x60;Quote of the Day&#x60; service.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQODApi();
let title = "title_example"; // String | Title of the Quote of the day category
let opts = {
  'repeatAfter': 30, // Number | How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
  'authors': "authors_example", // Array | Comma seperated author names. Quotes will be chosen from one of these authors.
  '_private': false, // Boolean | Should apply the filters to the private collection. Default is public quotes in the platform.
  'language': "'en'", // String | Quotes language.
  'sfw': false // Boolean | Consider only quotes marked as \"sfw\" (Safe for work).
};
apiInstance.qodPut(title, opts, (error, data, response) => {
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
 **title** | **String**| Title of the Quote of the day category | 
 **repeatAfter** | **Number**| How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here. | [optional] [default to 30]
 **authors** | **Array**| Comma seperated author names. Quotes will be chosen from one of these authors. | [optional] 
 **_private** | **Boolean**| Should apply the filters to the private collection. Default is public quotes in the platform. | [optional] [default to false]
 **language** | **String**| Quotes language. | [optional] [default to &#39;en&#39;]
 **sfw** | **Boolean**| Consider only quotes marked as \&quot;sfw\&quot; (Safe for work). | [optional] [default to false]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

