# RandomLovecraft.BooksApi

All URIs are relative to *https://randomlovecraft.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBooks**](BooksApi.md#getBooks) | **GET** /books | List all books



## getBooks

> GetBooks200Response getBooks()

List all books



### Example

```javascript
import RandomLovecraft from 'random_lovecraft';

let apiInstance = new RandomLovecraft.BooksApi();
apiInstance.getBooks((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBooks200Response**](GetBooks200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

