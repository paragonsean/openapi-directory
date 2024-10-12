# GoogIoUnofficalGoogleSearchApi.DefaultApi

All URIs are relative to *https://api.goog.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crawl**](DefaultApi.md#crawl) | **GET** /v1/crawl/{query} | Crawl
[**getTheStatusOfTheAPIService**](DefaultApi.md#getTheStatusOfTheAPIService) | **GET** / | Status
[**images**](DefaultApi.md#images) | **GET** /v1/images/{query} | Images
[**news**](DefaultApi.md#news) | **GET** /v1/news/{query} | News
[**search**](DefaultApi.md#search) | **GET** /v1/search/{query} | Search
[**serp**](DefaultApi.md#serp) | **POST** /v1/serp/ | SERP



## crawl

> Crawl200Response crawl(query)

Crawl

Perform Google Search   Parameters ---------- query : the string query to perform search. supports advance queries. Check out https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters guide for formating  Returns ------- json: a the html source of the results page

### Example

```javascript
import GoogIoUnofficalGoogleSearchApi from 'goog_io___unoffical_google_search_api';
let defaultClient = GoogIoUnofficalGoogleSearchApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GoogIoUnofficalGoogleSearchApi.DefaultApi();
let query = "q=google+search+api"; // String | 
apiInstance.crawl(query, (error, data, response) => {
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
 **query** | **String**|  | 

### Return type

[**Crawl200Response**](Crawl200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheStatusOfTheAPIService

> GetTheStatusOfTheAPIService200Response getTheStatusOfTheAPIService()

Status

It \&quot;status\&quot; &#x3D;&#x3D; true then API is up, else the API is down

### Example

```javascript
import GoogIoUnofficalGoogleSearchApi from 'goog_io___unoffical_google_search_api';
let defaultClient = GoogIoUnofficalGoogleSearchApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GoogIoUnofficalGoogleSearchApi.DefaultApi();
apiInstance.getTheStatusOfTheAPIService((error, data, response) => {
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

[**GetTheStatusOfTheAPIService200Response**](GetTheStatusOfTheAPIService200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## images

> Images200Response images(query)

Images

Perform Google Image Search  Parameters ---------- query : the string query to perform search. supports advance queries.  Returns ------- json: a list of results with the link, description, and title for each result

### Example

```javascript
import GoogIoUnofficalGoogleSearchApi from 'goog_io___unoffical_google_search_api';
let defaultClient = GoogIoUnofficalGoogleSearchApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GoogIoUnofficalGoogleSearchApi.DefaultApi();
let query = "query_example"; // String | 
apiInstance.images(query, (error, data, response) => {
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
 **query** | **String**|  | 

### Return type

[**Images200Response**](Images200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## news

> News200Response news(query)

News

Perform Google News Search   Parameters ---------- query : the string query to perform search for Google news. A simple query for &#x60;president&#x60; will be &#x60;q&#x3D;president&#x60;. An example of multiple keyword would be &#x60;q&#x3D;news+about+presdient+trump&#x60;. News can also be filtered by country and language. For &#x60;US&#x60; news and in English the query will be &#x60;q&#x3D;trump&amp;ceid&#x3D;US:en&#x60; for news in Great Britian the query will be &#x60;q&#x3D;trump&amp;ceid&#x3D;GB:en&#x60;  Returns ------- json: {\&quot;feed\&quot;: { \&quot;title\&quot; : \&quot;trump\&quot; ...} , \&quot;entites\&quot;: [ {\&quot;title\&quot; : \&quot;Trump doubles down on divisive messaging in speech to honor Independence Day - CNN\&quot;, \&quot;links\&quot;: []} ...]}

### Example

```javascript
import GoogIoUnofficalGoogleSearchApi from 'goog_io___unoffical_google_search_api';
let defaultClient = GoogIoUnofficalGoogleSearchApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GoogIoUnofficalGoogleSearchApi.DefaultApi();
let query = "query_example"; // String | 
apiInstance.news(query, (error, data, response) => {
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
 **query** | **String**|  | 

### Return type

[**News200Response**](News200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## search

> Search200Response search(query)

Search

Perform Google Search  Parameters ---------- query : the string query to perform search. supports advance queries. Check out https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters guide for formating  Returns ------- json: a list of results with the link, description, and title for each result

### Example

```javascript
import GoogIoUnofficalGoogleSearchApi from 'goog_io___unoffical_google_search_api';
let defaultClient = GoogIoUnofficalGoogleSearchApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GoogIoUnofficalGoogleSearchApi.DefaultApi();
let query = "q=google+search+api"; // String | 
apiInstance.search(query, (error, data, response) => {
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
 **query** | **String**|  | 

### Return type

[**Search200Response**](Search200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serp

> Serp200Response serp(serpData)

SERP

Perform Google Search and search for website in Search Engine Results Pages (SERP)  Parameters ---------- query : the string query to perform search. supports advance queries. Check out https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters guide for formatting, it is recommended to set the query &#x60;&amp;num&#x3D;100&#x60;  Returns ------- json: a list of results with the query, website, searched_results, and position. json[\&quot;position\&quot;] will be set to -1 if website is not found in results

### Example

```javascript
import GoogIoUnofficalGoogleSearchApi from 'goog_io___unoffical_google_search_api';
let defaultClient = GoogIoUnofficalGoogleSearchApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GoogIoUnofficalGoogleSearchApi.DefaultApi();
let serpData = new GoogIoUnofficalGoogleSearchApi.SerpData(); // SerpData | 
apiInstance.serp(serpData, (error, data, response) => {
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
 **serpData** | [**SerpData**](SerpData.md)|  | 

### Return type

[**Serp200Response**](Serp200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

