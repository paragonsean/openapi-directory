# ImportIo.DataImportIoApi

All URIs are relative to *https://data.import.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extractorExtractorIdCsvLatestGet**](DataImportIoApi.md#extractorExtractorIdCsvLatestGet) | **GET** /extractor/{extractorId}/csv/latest | Get the latest crawl run results as a csv
[**extractorExtractorIdJsonLatestGet**](DataImportIoApi.md#extractorExtractorIdJsonLatestGet) | **GET** /extractor/{extractorId}/json/latest | Get the latest crawl run results as json



## extractorExtractorIdCsvLatestGet

> {String: String} extractorExtractorIdCsvLatestGet(extractorId)

Get the latest crawl run results as a csv

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.DataImportIoApi();
let extractorId = "extractorId_example"; // String | the id of the extractor to start get the latest crawl run data
apiInstance.extractorExtractorIdCsvLatestGet(extractorId, (error, data, response) => {
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
 **extractorId** | **String**| the id of the extractor to start get the latest crawl run data | 

### Return type

**{String: String}**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv


## extractorExtractorIdJsonLatestGet

> {String: String} extractorExtractorIdJsonLatestGet(extractorId)

Get the latest crawl run results as json

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.DataImportIoApi();
let extractorId = "extractorId_example"; // String | The id of the extractor to start get the latest crawl run data
apiInstance.extractorExtractorIdJsonLatestGet(extractorId, (error, data, response) => {
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
 **extractorId** | **String**| The id of the extractor to start get the latest crawl run data | 

### Return type

**{String: String}**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; boundary=NL

