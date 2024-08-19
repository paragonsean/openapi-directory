# WeatherbitInteractiveSwaggerUiDocumentation.BulkDownloadsApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkFilesFileGet**](BulkDownloadsApi.md#bulkFilesFileGet) | **GET** /bulk/files/{file} | Download pre-generated bulk datasets



## bulkFilesFileGet

> Error bulkFilesFileGet(file, key)

Download pre-generated bulk datasets

Downloads bulk data files - OPTIONS: ( current.csv.gz, forecast_hourly.csv.gz, forecast_daily.csv.gz). Units are Metric (Celcius, m/s, etc).

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.BulkDownloadsApi();
let file = "file_example"; // String | Filename (ie. current.csv.gz)
let key = "key_example"; // String | Your registered API key.
apiInstance.bulkFilesFileGet(file, key, (error, data, response) => {
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
 **file** | **String**| Filename (ie. current.csv.gz) | 
 **key** | **String**| Your registered API key. | 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

