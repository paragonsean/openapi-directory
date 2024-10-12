# ImportIo.ExtractionImportIoApi

All URIs are relative to *https://extraction.import.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extractorExtractorIdGet**](ExtractionImportIoApi.md#extractorExtractorIdGet) | **GET** /extractor/{extractorId} | Query by extractor endpoint, adhoc runs only.



## extractorExtractorIdGet

> QueryResponse extractorExtractorIdGet(extractorId, url)

Query by extractor endpoint, adhoc runs only.

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.ExtractionImportIoApi();
let extractorId = "extractorId_example"; // String | extractorId
let url = "url_example"; // String | url
apiInstance.extractorExtractorIdGet(extractorId, url, (error, data, response) => {
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
 **url** | **String**| url | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

