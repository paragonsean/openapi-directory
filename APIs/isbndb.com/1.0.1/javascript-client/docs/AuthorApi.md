# IsbNdbApi.AuthorApi

All URIs are relative to *https://api.isbndb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorNameGet**](AuthorApi.md#authorNameGet) | **GET** /author/{name} | Gets author details
[**authorsQueryGet**](AuthorApi.md#authorsQueryGet) | **GET** /authors/{query} | Search authors



## authorNameGet

> Author authorNameGet(name, opts)

Gets author details

Returns the name and a list of books by the author.

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.AuthorApi();
let name = "name_example"; // String | The name of an author in the Author's database
let opts = {
  'page': "page_example", // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
  'pageSize': "pageSize_example" // String | How many items should be returned per page, maximum of 1,000
};
apiInstance.authorNameGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of an author in the Author&#39;s database | 
 **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] 
 **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] 

### Return type

[**Author**](Author.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authorsQueryGet

> AuthorQueryResults authorsQueryGet(query, opts)

Search authors

This returns a list of authors whos name matches the given query

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.AuthorApi();
let query = "query_example"; // String | A string to search for in the Author’s database
let opts = {
  'pageSize': "pageSize_example", // String | How many items should be returned per page, maximum of 1,000
  'page': "page_example" // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
};
apiInstance.authorsQueryGet(query, opts, (error, data, response) => {
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
 **query** | **String**| A string to search for in the Author’s database | 
 **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] 
 **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] 

### Return type

[**AuthorQueryResults**](AuthorQueryResults.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

