# BillsApi.BillNewsApi

All URIs are relative to *https://bills-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNewsArticles**](BillNewsApi.md#getNewsArticles) | **GET** /api/v1/Bills/{billId}/NewsArticles | Returns a list of news articles for a Bill.



## getNewsArticles

> NewsArticlesSummarySearchResult getNewsArticles(billId, opts)

Returns a list of news articles for a Bill.

### Example

```javascript
import BillsApi from 'bills_api';

let apiInstance = new BillsApi.BillNewsApi();
let billId = 56; // Number | 
let opts = {
  'skip': 56, // Number | 
  'take': 56 // Number | 
};
apiInstance.getNewsArticles(billId, opts, (error, data, response) => {
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
 **billId** | **Number**|  | 
 **skip** | **Number**|  | [optional] 
 **take** | **Number**|  | [optional] 

### Return type

[**NewsArticlesSummarySearchResult**](NewsArticlesSummarySearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

