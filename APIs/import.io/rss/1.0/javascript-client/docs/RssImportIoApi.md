# ImportIo.RssImportIoApi

All URIs are relative to *https://rss.import.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extractorExtractorIdRunsGet**](RssImportIoApi.md#extractorExtractorIdRunsGet) | **GET** /extractor/{extractorId}/runs | Get a feed of the runs performed on an extractor



## extractorExtractorIdRunsGet

> {String: String} extractorExtractorIdRunsGet(extractorId)

Get a feed of the runs performed on an extractor

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.RssImportIoApi();
let extractorId = "extractorId_example"; // String | The id of the extractor to start get the crawl run data
apiInstance.extractorExtractorIdRunsGet(extractorId, (error, data, response) => {
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
 **extractorId** | **String**| The id of the extractor to start get the crawl run data | 

### Return type

**{String: String}**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml

