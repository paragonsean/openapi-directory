# IsbNdbApi.PublisherApi

All URIs are relative to *https://api.isbndb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publisherNameGet**](PublisherApi.md#publisherNameGet) | **GET** /publisher/{name} | Gets publisher details
[**publishersQueryGet**](PublisherApi.md#publishersQueryGet) | **GET** /publishers/{query} | Search publishers



## publisherNameGet

> Publisher publisherNameGet(name, opts)

Gets publisher details

Returns details and a list of books by the publisher.

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.PublisherApi();
let name = "name_example"; // String | The name of a publisher in the Publisher's database
let opts = {
  'page': "page_example", // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
  'pageSize': "pageSize_example" // String | How many items should be returned per page, maximum of 1,000
};
apiInstance.publisherNameGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of a publisher in the Publisher&#39;s database | 
 **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] 
 **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] 

### Return type

[**Publisher**](Publisher.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishersQueryGet

> publishersQueryGet(query, opts)

Search publishers

This returns a list of publishers that match the given query

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.PublisherApi();
let query = "query_example"; // String | A string to search for in the Publisher’s database
let opts = {
  'pageSize': "pageSize_example", // String | How many items should be returned per page, maximum of 1,000
  'page': "page_example" // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
};
apiInstance.publishersQueryGet(query, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| A string to search for in the Publisher’s database | 
 **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] 
 **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

