# Semantria.StatisticsApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatistic**](StatisticsApi.md#getStatistic) | **GET** /statistics.{content_type} | Retrieve usage statistics



## getStatistic

> Statistic getStatistic(contentType, opts)

Retrieve usage statistics

This method retrieves overall and per configuration usage statistics for specific timeframe. Statistics ordered per available configurations. Available interval values are current &lt;b&gt;hour&lt;/b&gt;, &lt;b&gt;day&lt;/b&gt;, &lt;b&gt;week&lt;/b&gt;, &lt;b&gt;month&lt;/b&gt; and &lt;b&gt;year&lt;/b&gt;.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.StatisticsApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example", // String | Configuration identifier for usage statistics retrieving.
  'interval': "interval_example" // String | Hour, Day, Week, Month, Year values are supported.
};
apiInstance.getStatistic(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Configuration identifier for usage statistics retrieving. | [optional] 
 **interval** | **String**| Hour, Day, Week, Month, Year values are supported. | [optional] 

### Return type

[**Statistic**](Statistic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

