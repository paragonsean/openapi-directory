# ShortenRestApiDocumentation.StatisticsApi

All URIs are relative to *https://api.shorten.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatistics**](StatisticsApi.md#getStatistics) | **POST** /clicks/pg | Get clicks statistics



## getStatistics

> ClickModelPg getStatistics(clicksFilterModel)

Get clicks statistics

Retrieve the raw click statistics for your account. Clicks are retrieved by creation date in descending order.

### Example

```javascript
import ShortenRestApiDocumentation from 'shorten_rest_api_documentation';
let defaultClient = ShortenRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ShortenRestApiDocumentation.StatisticsApi();
let clicksFilterModel = new ShortenRestApiDocumentation.ClicksFilterModel(); // ClicksFilterModel | Filter
apiInstance.getStatistics(clicksFilterModel, (error, data, response) => {
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
 **clicksFilterModel** | [**ClicksFilterModel**](ClicksFilterModel.md)| Filter | 

### Return type

[**ClickModelPg**](ClickModelPg.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

