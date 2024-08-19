# JokesOneApi.JokeApi

All URIs are relative to *https://api.jokes.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jokeCategoriesSearchGet**](JokeApi.md#jokeCategoriesSearchGet) | **GET** /joke/categories/search | 
[**jokeDelete**](JokeApi.md#jokeDelete) | **DELETE** /joke | 
[**jokeGet**](JokeApi.md#jokeGet) | **GET** /joke | 
[**jokeListGet**](JokeApi.md#jokeListGet) | **GET** /joke/list | 
[**jokePatch**](JokeApi.md#jokePatch) | **PATCH** /joke | 
[**jokePut**](JokeApi.md#jokePut) | **PUT** /joke | 
[**jokeRandomGet**](JokeApi.md#jokeRandomGet) | **GET** /joke/random | 
[**jokeSearchGet**](JokeApi.md#jokeSearchGet) | **GET** /joke/search | 
[**jokeTagsAddPost**](JokeApi.md#jokeTagsAddPost) | **POST** /joke/tags/add | 
[**jokeTagsRemovePost**](JokeApi.md#jokeTagsRemovePost) | **POST** /joke/tags/remove | 



## jokeCategoriesSearchGet

> jokeCategoriesSearchGet(query, opts)



Gets a list of &#x60;Joke&#x60; Categories, based on a query term. 

### Example

```javascript
import JokesOneApi from 'jokes_one_api';
let defaultClient = JokesOneApi.ApiClient.instance;
// Configure API key authorization: X-JokesOne-Api-Secret
let X-JokesOne-Api-Secret = defaultClient.authentications['X-JokesOne-Api-Secret'];
X-JokesOne-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-JokesOne-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new JokesOneApi.JokeApi();
let query = "query_example"; // String | Search Query
let opts = {
  'start': 0 // Number | Response is paged. This parameter controls where response starts the listing at
};
apiInstance.jokeCategoriesSearchGet(query, opts, (error, data, response) => {
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
 **query** | **String**| Search Query | 
 **start** | **Number**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0]

### Return type

null (empty response body)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jokeDelete

> jokeDelete(id)



Delete a joke. The user needs to be the owner of the joke to be able to delete it. 

### Example

```javascript
import JokesOneApi from 'jokes_one_api';
let defaultClient = JokesOneApi.ApiClient.instance;
// Configure API key authorization: X-JokesOne-Api-Secret
let X-JokesOne-Api-Secret = defaultClient.authentications['X-JokesOne-Api-Secret'];
X-JokesOne-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-JokesOne-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new JokesOneApi.JokeApi();
let id = "id_example"; // String | Joke ID
apiInstance.jokeDelete(id, (error, data, response) => {
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
 **id** | **String**| Joke ID | 

### Return type

null (empty response body)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## jokeGet

> JokeResponse jokeGet(opts)



Gets a &#x60;Joke&#x60; with a given &#x60;id&#x60;.

### Example

```javascript
import JokesOneApi from 'jokes_one_api';
let defaultClient = JokesOneApi.ApiClient.instance;
// Configure API key authorization: X-JokesOne-Api-Secret
let X-JokesOne-Api-Secret = defaultClient.authentications['X-JokesOne-Api-Secret'];
X-JokesOne-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-JokesOne-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new JokesOneApi.JokeApi();
let opts = {
  'id': "id_example" // String | Joke ID
};
apiInstance.jokeGet(opts, (error, data, response) => {
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
 **id** | **String**| Joke ID | [optional] 

### Return type

[**JokeResponse**](JokeResponse.md)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## jokeListGet

> jokeListGet(opts)



Get the list of jokes in your private collection.

### Example

```javascript
import JokesOneApi from 'jokes_one_api';

let apiInstance = new JokesOneApi.JokeApi();
let opts = {
  'start': 0 // Number | Response is paged. This parameter controls where response starts the listing at
};
apiInstance.jokeListGet(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jokePatch

> jokePatch(id, opts)



Update a joke

### Example

```javascript
import JokesOneApi from 'jokes_one_api';

let apiInstance = new JokesOneApi.JokeApi();
let id = "id_example"; // String | Joke ID
let opts = {
  'title': "title_example", // String | title
  'text': "text_example", // String | text
  'author': "author_example", // String | Joke Author
  'tags': "tags_example" // String | Comma Separated tags
};
apiInstance.jokePatch(id, opts, (error, data, response) => {
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
 **id** | **String**| Joke ID | 
 **title** | **String**| title | [optional] 
 **text** | **String**| text | [optional] 
 **author** | **String**| Joke Author | [optional] 
 **tags** | **String**| Comma Separated tags | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jokePut

> jokePut(title, text, opts)



Add a new joke to your private collection.

### Example

```javascript
import JokesOneApi from 'jokes_one_api';

let apiInstance = new JokesOneApi.JokeApi();
let title = "title_example"; // String | Joke Title
let text = "text_example"; // String | Joke Text
let opts = {
  'author': "author_example", // String | Joke Author
  'tags': "tags_example" // String | Comma Separated tags
};
apiInstance.jokePut(title, text, opts, (error, data, response) => {
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
 **title** | **String**| Joke Title | 
 **text** | **String**| Joke Text | 
 **author** | **String**| Joke Author | [optional] 
 **tags** | **String**| Comma Separated tags | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jokeRandomGet

> JokeResponse jokeRandomGet()



Gets a &#x60;Random Joke&#x60;. When you are in a hurry this is what you call to get a random famous joke.

### Example

```javascript
import JokesOneApi from 'jokes_one_api';

let apiInstance = new JokesOneApi.JokeApi();
apiInstance.jokeRandomGet((error, data, response) => {
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

[**JokeResponse**](JokeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, application/js


## jokeSearchGet

> JokeResponse jokeSearchGet(opts)



Search for a &#x60;Joke&#x60; in Jokes One platform. Optional &#x60;category&#x60; , &#x60;author&#x60;, &#x60;minlength&#x60;, &#x60;maxlength&#x60; params determines the filters applied while searching for the joke. 

### Example

```javascript
import JokesOneApi from 'jokes_one_api';
let defaultClient = JokesOneApi.ApiClient.instance;
// Configure API key authorization: X-JokesOne-Api-Secret
let X-JokesOne-Api-Secret = defaultClient.authentications['X-JokesOne-Api-Secret'];
X-JokesOne-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-JokesOne-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new JokesOneApi.JokeApi();
let opts = {
  'category': "category_example", // String | Joke Category
  'query': "query_example", // String | keyword to search for in the joke
  'minlength': 100, // Number | Joke minimum Length
  'maxlength': 300, // Number | Joke maximum Length
  'author': "author_example", // String | Joke Author
  '_private': false // Boolean | Should search private collection? Default searches public collection.
};
apiInstance.jokeSearchGet(opts, (error, data, response) => {
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
 **category** | **String**| Joke Category | [optional] 
 **query** | **String**| keyword to search for in the joke | [optional] 
 **minlength** | **Number**| Joke minimum Length | [optional] [default to 100]
 **maxlength** | **Number**| Joke maximum Length | [optional] [default to 300]
 **author** | **String**| Joke Author | [optional] 
 **_private** | **Boolean**| Should search private collection? Default searches public collection. | [optional] [default to false]

### Return type

[**JokeResponse**](JokeResponse.md)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## jokeTagsAddPost

> jokeTagsAddPost(id, tags)



Add a tag to a given Joke.

### Example

```javascript
import JokesOneApi from 'jokes_one_api';

let apiInstance = new JokesOneApi.JokeApi();
let id = "id_example"; // String | Joke ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.jokeTagsAddPost(id, tags, (error, data, response) => {
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
 **id** | **String**| Joke ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jokeTagsRemovePost

> jokeTagsRemovePost(id, tags)



Remove a tag from a given joke.

### Example

```javascript
import JokesOneApi from 'jokes_one_api';

let apiInstance = new JokesOneApi.JokeApi();
let id = "id_example"; // String | Joke ID
let tags = "tags_example"; // String | Comma Separated tags
apiInstance.jokeTagsRemovePost(id, tags, (error, data, response) => {
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
 **id** | **String**| Joke ID | 
 **tags** | **String**| Comma Separated tags | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

