# TheySaidSoQuotesApi.QuoteApi

All URIs are relative to *https://quotes.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteAuthorsPopularGet**](QuoteApi.md#quoteAuthorsPopularGet) | **GET** /quote/authors/popular | 
[**quoteAuthorsSearchGet**](QuoteApi.md#quoteAuthorsSearchGet) | **GET** /quote/authors/search | 
[**quoteBookmarkToggleGet**](QuoteApi.md#quoteBookmarkToggleGet) | **GET** /quote/bookmark/toggle | 
[**quoteCategoriesPopularGet**](QuoteApi.md#quoteCategoriesPopularGet) | **GET** /quote/categories/popular | 
[**quoteCategoriesSearchGet**](QuoteApi.md#quoteCategoriesSearchGet) | **GET** /quote/categories/search | 
[**quoteGet**](QuoteApi.md#quoteGet) | **GET** /quote | 
[**quoteLikeToggleGet**](QuoteApi.md#quoteLikeToggleGet) | **GET** /quote/like/toggle | 
[**quoteRandomGet**](QuoteApi.md#quoteRandomGet) | **GET** /quote/random | 
[**quoteSearchGet**](QuoteApi.md#quoteSearchGet) | **GET** /quote/search | 



## quoteAuthorsPopularGet

> quoteAuthorsPopularGet(opts)



Gets a list of popular author names in the system.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let opts = {
  'language': "'en'", // String | Language. A same author may have quotes in two or more different languages. So for example 'Mahatma Gandhi' may be returned for language \"en\"(English), and \"மஹாத்மா காந்தி\" may be returned when the language is \"ta\" (Tamil).
  'detailed': false, // Boolean | Should return detailed author information such as `birthday`, `death date`, `occupation`, `description` etc. Only available at certain subscription levels.
  'start': 0, // Number | Response is paged. This parameter controls where response starts the listing at
  'limit': 5 // Number | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
};
apiInstance.quoteAuthorsPopularGet(opts, (error, data, response) => {
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
 **language** | **String**| Language. A same author may have quotes in two or more different languages. So for example &#39;Mahatma Gandhi&#39; may be returned for language \&quot;en\&quot;(English), and \&quot;மஹாத்மா காந்தி\&quot; may be returned when the language is \&quot;ta\&quot; (Tamil). | [optional] [default to &#39;en&#39;]
 **detailed** | **Boolean**| Should return detailed author information such as &#x60;birthday&#x60;, &#x60;death date&#x60;, &#x60;occupation&#x60;, &#x60;description&#x60; etc. Only available at certain subscription levels. | [optional] [default to false]
 **start** | **Number**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0]
 **limit** | **Number**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 5]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteAuthorsSearchGet

> quoteAuthorsSearchGet(opts)



Gets a list of author names in the system.  

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let opts = {
  'query': "query_example", // String | Text string to search for in author names
  'language': "'en'", // String | Language. A same author may have quotes in two or more different languages. So for example 'Mahatma Gandhi' may be returned for language \"en\"(English), and \"மஹாத்மா காந்தி\" may be returned when the language is \"ta\" (Tamil).
  'detailed': false, // Boolean | Should return detailed author information such as `birthday`, `death date`, `occupation`, `description` etc. Only available at certain subscription levels.
  'start': 0, // Number | Response is paged. This parameter controls where response starts the listing at
  'limit': 1 // Number | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
};
apiInstance.quoteAuthorsSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Text string to search for in author names | [optional] 
 **language** | **String**| Language. A same author may have quotes in two or more different languages. So for example &#39;Mahatma Gandhi&#39; may be returned for language \&quot;en\&quot;(English), and \&quot;மஹாத்மா காந்தி\&quot; may be returned when the language is \&quot;ta\&quot; (Tamil). | [optional] [default to &#39;en&#39;]
 **detailed** | **Boolean**| Should return detailed author information such as &#x60;birthday&#x60;, &#x60;death date&#x60;, &#x60;occupation&#x60;, &#x60;description&#x60; etc. Only available at certain subscription levels. | [optional] [default to false]
 **start** | **Number**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0]
 **limit** | **Number**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteBookmarkToggleGet

> quoteBookmarkToggleGet(quoteId)



Toggle the user bookmark of the given Quote as a user of the API Key.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let quoteId = "quoteId_example"; // String | Quote ID
apiInstance.quoteBookmarkToggleGet(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| Quote ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteCategoriesPopularGet

> quoteCategoriesPopularGet(opts)



Gets a list of popular &#x60;Quote&#x60; Categories. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let opts = {
  'start': 0, // Number | Response is paged. This parameter controls where response starts the listing at
  'limit': 5 // Number | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
};
apiInstance.quoteCategoriesPopularGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 5]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteCategoriesSearchGet

> quoteCategoriesSearchGet(opts)



Gets a list of &#x60;Quote&#x60; Categories matching the query string. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let opts = {
  'query': "'0'", // String | Text string to search for in the categories
  'start': 0, // Number | Response is paged. This parameter controls where response starts the listing at
  'limit': 2 // Number | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
};
apiInstance.quoteCategoriesSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Text string to search for in the categories | [optional] [default to &#39;0&#39;]
 **start** | **Number**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0]
 **limit** | **Number**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 2]

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteGet

> QuoteResponse quoteGet(opts)



Gets a &#x60;Quote&#x60; with a given &#x60;id&#x60;.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let opts = {
  'id': "id_example" // String | Quote ID
};
apiInstance.quoteGet(opts, (error, data, response) => {
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


## quoteLikeToggleGet

> quoteLikeToggleGet(quoteId)



Toggle the user like of the given Quote as a user of the API Key.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let quoteId = "quoteId_example"; // String | Quote ID
apiInstance.quoteLikeToggleGet(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| Quote ID | 

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteRandomGet

> QuoteResponse quoteRandomGet(opts)



Gets a &#x60;Random Quote&#x60;. When you are in a hurry this is what you call to get a random famous quote.

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let opts = {
  'language': "'en'", // String | Language of the Quote. The language must be supported in our system.
  'limit': 1 // Number | No of quotes to return. The max limit depends on the subscription level.
};
apiInstance.quoteRandomGet(opts, (error, data, response) => {
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
 **language** | **String**| Language of the Quote. The language must be supported in our system. | [optional] [default to &#39;en&#39;]
 **limit** | **Number**| No of quotes to return. The max limit depends on the subscription level. | [optional] [default to 1]

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteSearchGet

> QuoteResponse quoteSearchGet(opts)



Search for a &#x60;Quote&#x60; in They Said So platform. Optional &#x60;category&#x60; , &#x60;author&#x60;, &#x60;minlength&#x60;, &#x60;maxlength&#x60; params determines the filters applied while searching for the quote. 

### Example

```javascript
import TheySaidSoQuotesApi from 'they_said_so_quotes_api';
let defaultClient = TheySaidSoQuotesApi.ApiClient.instance;
// Configure Bearer (bearer token) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheySaidSoQuotesApi.QuoteApi();
let opts = {
  'category': "category_example", // String | Quote Category
  'author': "author_example", // String | Quote Author
  'minlength': 100, // Number | Quote minimum Length
  'maxlength': 300, // Number | Quote maximum Length
  'query': "query_example", // String | keyword to search for in the quote
  '_private': false, // Boolean | Should search private collection? Default searches public collection.
  'language': "'en'", // String | Language of the Quote. The language must be supported in our system.
  'limit': 1, // Number | No of quotes to return. The max limit depends on the subscription level.
  'sfw': false // Boolean | Should search only SFW (Safe For Work) quotes?
};
apiInstance.quoteSearchGet(opts, (error, data, response) => {
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
 **category** | **String**| Quote Category | [optional] 
 **author** | **String**| Quote Author | [optional] 
 **minlength** | **Number**| Quote minimum Length | [optional] [default to 100]
 **maxlength** | **Number**| Quote maximum Length | [optional] [default to 300]
 **query** | **String**| keyword to search for in the quote | [optional] 
 **_private** | **Boolean**| Should search private collection? Default searches public collection. | [optional] [default to false]
 **language** | **String**| Language of the Quote. The language must be supported in our system. | [optional] [default to &#39;en&#39;]
 **limit** | **Number**| No of quotes to return. The max limit depends on the subscription level. | [optional] [default to 1]
 **sfw** | **Boolean**| Should search only SFW (Safe For Work) quotes? | [optional] [default to false]

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

