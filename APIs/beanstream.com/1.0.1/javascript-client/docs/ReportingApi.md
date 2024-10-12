# BeanstreamPayments.ReportingApi

All URIs are relative to *https://www.beanstream.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsPost**](ReportingApi.md#reportsPost) | **POST** /reports | Search Query



## reportsPost

> SearchResult reportsPost(opts)

Search Query

Query for transactions using a date range and optional search criteria. This method allows you to page your search results if you are expecting a lot of results to be returned. The page start value begins at 1. If no records are found the API will return a 404 error message. For details on the parameters and allowed values for Criteria please visit the documentation http://developer.beanstream.com/documentation/analyze-payments/search-specific-criteria/

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.ReportingApi();
let opts = {
  'searchQuery': new BeanstreamPayments.SearchQuery() // SearchQuery | 
};
apiInstance.reportsPost(opts, (error, data, response) => {
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
 **searchQuery** | [**SearchQuery**](SearchQuery.md)|  | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

