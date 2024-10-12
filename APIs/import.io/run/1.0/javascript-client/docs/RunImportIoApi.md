# ImportIo.RunImportIoApi

All URIs are relative to *https://run.import.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extractorExtractorIdCancelPost**](RunImportIoApi.md#extractorExtractorIdCancelPost) | **POST** /extractor/{extractorId}/cancel | Cancel an existing crawl.
[**extractorExtractorIdStartPost**](RunImportIoApi.md#extractorExtractorIdStartPost) | **POST** /extractor/{extractorId}/start | Launch a crawl from an extractor that a user owns.



## extractorExtractorIdCancelPost

> {String: String} extractorExtractorIdCancelPost(extractorId)

Cancel an existing crawl.

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.RunImportIoApi();
let extractorId = "extractorId_example"; // String | extractorId
apiInstance.extractorExtractorIdCancelPost(extractorId, (error, data, response) => {
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
 **extractorId** | **String**| extractorId | 

### Return type

**{String: String}**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## extractorExtractorIdStartPost

> {String: String} extractorExtractorIdStartPost(extractorId)

Launch a crawl from an extractor that a user owns.

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.RunImportIoApi();
let extractorId = "extractorId_example"; // String | the id of the extractor to start crawling with
apiInstance.extractorExtractorIdStartPost(extractorId, (error, data, response) => {
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
 **extractorId** | **String**| the id of the extractor to start crawling with | 

### Return type

**{String: String}**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

