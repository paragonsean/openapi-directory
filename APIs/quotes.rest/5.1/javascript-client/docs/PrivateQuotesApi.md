# TheySaidSoQuotesApi.PrivateQuotesApi

All URIs are relative to *https://quotes.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteDelete**](PrivateQuotesApi.md#quoteDelete) | **DELETE** /quote | 
[**quoteGet_0**](PrivateQuotesApi.md#quoteGet_0) | **GET** /quote | 
[**quoteListGet**](PrivateQuotesApi.md#quoteListGet) | **GET** /quote/list | 
[**quotePatch**](PrivateQuotesApi.md#quotePatch) | **PATCH** /quote | 
[**quotePost**](PrivateQuotesApi.md#quotePost) | **POST** /quote | 
[**quotePut**](PrivateQuotesApi.md#quotePut) | **PUT** /quote | 
[**quoteTagsAddPost**](PrivateQuotesApi.md#quoteTagsAddPost) | **POST** /quote/tags/add | 
[**quoteTagsRemovePost**](PrivateQuotesApi.md#quoteTagsRemovePost) | **POST** /quote/tags/remove | 



## quoteDelete

> quoteDelete(id)



Delete a quote. The user needs to be the owner of the quote to be able to delete it. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let id = "id_example"; // String | Quote ID
apiInstance.quoteDelete(id, (error, data, response) => {
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
 **id** | **String**| Quote ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## quoteGet_0

> QuoteResponse quoteGet_0(opts)



Gets a &#x60;Quote&#x60; with a given &#x60;id&#x60;.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let opts = {
  'id': "id_example" // String | Quote ID
};
apiInstance.quoteGet_0(opts, (error, data, response) => {
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
 **id** | **String**| Quote ID | [optional] 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteListGet

> quoteListGet(opts)



Get the list of quotes in your private collection.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let opts = {
  'start': 0, // Number | Response is paged. This parameter controls where response starts the listing at
  'limit': 10 // Number | Response is paged. This parameter controls how many is returned in the result.
};
apiInstance.quoteListGet(opts, (error, data, response) => {
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
 **start** | **Number**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0]
 **limit** | **Number**| Response is paged. This parameter controls how many is returned in the result. | [optional] [default to 10]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotePatch

> quotePatch(id, opts)



Update a quote

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let id = "id_example"; // String | Quote ID
let opts = {
  'quote': "quote_example", // String | Quote
  'author': "author_example", // String | Quote Author
  'language': "'en'", // String | Language. If not supplied an auto detection mechanism will be used to detect a language.
  'tags': "tags_example" // String | Comma Separated tags
};
apiInstance.quotePatch(id, opts, (error, data, response) => {
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
 **id** | **String**| Quote ID | 
 **quote** | **String**| Quote | [optional] 
 **author** | **String**| Quote Author | [optional] 
 **language** | **String**| Language. If not supplied an auto detection mechanism will be used to detect a language. | [optional] [default to &#39;en&#39;]
 **tags** | **String**| Comma Separated tags | [optional] 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotePost

> quotePost(quote, opts)



Add a new quote to your private collection. Same as &#39;PUT&#39; but added since some clients don&#39;t handle PUT well.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let quote = "quote_example"; // String | Quote
let opts = {
  'author': "author_example", // String | Quote Author
  'tags': "tags_example", // String | Comma Separated tags
  'language': "'en'" // String | Language. If not supplied an auto detection mechanism will be used to detect a language.
};
apiInstance.quotePost(quote, opts, (error, data, response) => {
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
 **quote** | **String**| Quote | 
 **author** | **String**| Quote Author | [optional] 
 **tags** | **String**| Comma Separated tags | [optional] 
 **language** | **String**| Language. If not supplied an auto detection mechanism will be used to detect a language. | [optional] [default to &#39;en&#39;]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotePut

> quotePut(quote, opts)



Add a new quote to your private collection.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let quote = "quote_example"; // String | Quote
let opts = {
  'author': "author_example", // String | Quote Author
  'tags': "tags_example", // String | Comma Separated tags
  'language': "'en'" // String | Language. If not supplied an auto detection mechanism will be used to detect a language.
};
apiInstance.quotePut(quote, opts, (error, data, response) => {
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
 **quote** | **String**| Quote | 
 **author** | **String**| Quote Author | [optional] 
 **tags** | **String**| Comma Separated tags | [optional] 
 **language** | **String**| Language. If not supplied an auto detection mechanism will be used to detect a language. | [optional] [default to &#39;en&#39;]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteTagsAddPost

> quoteTagsAddPost(id, tags)



Add a tag to a given Quote.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let id = "id_example"; // String | Quote ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.quoteTagsAddPost(id, tags, (error, data, response) => {
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
 **id** | **String**| Quote ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteTagsRemovePost

> quoteTagsRemovePost(id, tags)



Remove a tag from a given quote.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.PrivateQuotesApi();
let id = "id_example"; // String | Quote ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.quoteTagsRemovePost(id, tags, (error, data, response) => {
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
 **id** | **String**| Quote ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

