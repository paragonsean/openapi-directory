# BotifyApi.ProjectApi

All URIs are relative to *https://api.botify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProjectAnalyses**](ProjectApi.md#getProjectAnalyses) | **GET** /analyses/{username}/{project_slug} | List all analyses for a project
[**getProjectUrlsAggs**](ProjectApi.md#getProjectUrlsAggs) | **POST** /projects/{username}/{project_slug}/urls/aggs | Project Query aggregator
[**getSavedFilter**](ProjectApi.md#getSavedFilter) | **GET** /projects/{username}/{project_slug}/filters/{identifier} | Retrieves a specific saved filter&#39;s name, ID and filter value
[**getSavedFilters**](ProjectApi.md#getSavedFilters) | **GET** /projects/{username}/{project_slug}/filters | List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value)
[**testUrlRewritingRules**](ProjectApi.md#testUrlRewritingRules) | **POST** /projects/{username}/{project_slug}/features/url_rewriting/rules_validator | Match and replace parts of a URL based on rules passed in POST data



## getProjectAnalyses

> GetProjectAnalyses200Response getProjectAnalyses(username, projectSlug, opts)

List all analyses for a project

List all analyses for a project

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.ProjectApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getProjectAnalyses(username, projectSlug, opts, (error, data, response) => {
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
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetProjectAnalyses200Response**](GetProjectAnalyses200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectUrlsAggs

> Object getProjectUrlsAggs(username, projectSlug, opts)

Project Query aggregator

Project Query aggregator. It accepts multiple queries that will be executed on all completed analyses in the project

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.ProjectApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let opts = {
  'area': "'current'", // String | Analysis context to execute the queries
  'lastAnalysisSlug': "lastAnalysisSlug_example", // String | Last analysis on the trend
  'nbAnalyses': 20, // Number | Max number of analysis to return
  'urlsAggsQuery': [new BotifyApi.UrlsAggsQuery()] // [UrlsAggsQuery] | 
};
apiInstance.getProjectUrlsAggs(username, projectSlug, opts, (error, data, response) => {
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
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **area** | **String**| Analysis context to execute the queries | [optional] [default to &#39;current&#39;]
 **lastAnalysisSlug** | **String**| Last analysis on the trend | [optional] 
 **nbAnalyses** | **Number**| Max number of analysis to return | [optional] [default to 20]
 **urlsAggsQuery** | [**[UrlsAggsQuery]**](UrlsAggsQuery.md)|  | [optional] 

### Return type

**Object**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSavedFilter

> ProjectSavedFilter getSavedFilter(username, projectSlug, identifier)

Retrieves a specific saved filter&#39;s name, ID and filter value

Retrieves a specific saved filter&#39;s name, ID and filter value

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.ProjectApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let identifier = "identifier_example"; // String | Saved Filter's identifier
apiInstance.getSavedFilter(username, projectSlug, identifier, (error, data, response) => {
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
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **identifier** | **String**| Saved Filter&#39;s identifier | 

### Return type

[**ProjectSavedFilter**](ProjectSavedFilter.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSavedFilters

> GetSavedFilters200Response getSavedFilters(username, projectSlug, opts)

List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value)

List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value)

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.ProjectApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getSavedFilters(username, projectSlug, opts, (error, data, response) => {
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
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetSavedFilters200Response**](GetSavedFilters200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## testUrlRewritingRules

> URLRewritingRulesSerializer testUrlRewritingRules(username, projectSlug)

Match and replace parts of a URL based on rules passed in POST data

Match and replace parts of a URL based on rules passed in POST data.

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.ProjectApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
apiInstance.testUrlRewritingRules(username, projectSlug, (error, data, response) => {
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
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 

### Return type

[**URLRewritingRulesSerializer**](URLRewritingRulesSerializer.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

