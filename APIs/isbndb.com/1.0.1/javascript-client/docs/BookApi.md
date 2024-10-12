# IsbNdbApi.BookApi

All URIs are relative to *https://api.isbndb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookIsbnGet**](BookApi.md#bookIsbnGet) | **GET** /book/{isbn} | Gets book details
[**booksQueryGet**](BookApi.md#booksQueryGet) | **GET** /books/{query} | Search books



## bookIsbnGet

> Book bookIsbnGet(isbn)

Gets book details

Returns the book details

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.BookApi();
let isbn = "isbn_example"; // String | an ISBN 10 or ISBN 13 in the Books database
apiInstance.bookIsbnGet(isbn, (error, data, response) => {
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
 **isbn** | **String**| an ISBN 10 or ISBN 13 in the Books database | 

### Return type

[**Book**](Book.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksQueryGet

> booksQueryGet(query, opts)

Search books

This returns a list of books that match the query

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.BookApi();
let query = "query_example"; // String | A string to search for in the Book’s database
let opts = {
  'page': "page_example", // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
  'author': "author_example", // String | Filters the query results by author
  'pageSize': "pageSize_example" // String | How many items should be returned per page, maximum of 1,000
};
apiInstance.booksQueryGet(query, opts, (error, data, response) => {
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
 **query** | **String**| A string to search for in the Book’s database | 
 **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] 
 **author** | **String**| Filters the query results by author | [optional] 
 **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

