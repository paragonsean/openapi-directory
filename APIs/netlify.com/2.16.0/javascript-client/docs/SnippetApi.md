# NetlifysApiDocumentation.SnippetApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSiteSnippet**](SnippetApi.md#createSiteSnippet) | **POST** /sites/{site_id}/snippets | 
[**deleteSiteSnippet**](SnippetApi.md#deleteSiteSnippet) | **DELETE** /sites/{site_id}/snippets/{snippet_id} | 
[**getSiteSnippet**](SnippetApi.md#getSiteSnippet) | **GET** /sites/{site_id}/snippets/{snippet_id} | 
[**listSiteSnippets**](SnippetApi.md#listSiteSnippets) | **GET** /sites/{site_id}/snippets | 
[**updateSiteSnippet**](SnippetApi.md#updateSiteSnippet) | **PUT** /sites/{site_id}/snippets/{snippet_id} | 



## createSiteSnippet

> Snippet createSiteSnippet(siteId, snippet)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SnippetApi();
let siteId = "siteId_example"; // String | 
let snippet = new NetlifysApiDocumentation.Snippet(); // Snippet | 
apiInstance.createSiteSnippet(siteId, snippet, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **snippet** | [**Snippet**](Snippet.md)|  | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSiteSnippet

> deleteSiteSnippet(siteId, snippetId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SnippetApi();
let siteId = "siteId_example"; // String | 
let snippetId = "snippetId_example"; // String | 
apiInstance.deleteSiteSnippet(siteId, snippetId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **snippetId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteSnippet

> Snippet getSiteSnippet(siteId, snippetId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SnippetApi();
let siteId = "siteId_example"; // String | 
let snippetId = "snippetId_example"; // String | 
apiInstance.getSiteSnippet(siteId, snippetId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **snippetId** | **String**|  | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSiteSnippets

> [Snippet] listSiteSnippets(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SnippetApi();
let siteId = "siteId_example"; // String | 
apiInstance.listSiteSnippets(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**[Snippet]**](Snippet.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSiteSnippet

> updateSiteSnippet(siteId, snippetId, snippet)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SnippetApi();
let siteId = "siteId_example"; // String | 
let snippetId = "snippetId_example"; // String | 
let snippet = new NetlifysApiDocumentation.Snippet(); // Snippet | 
apiInstance.updateSiteSnippet(siteId, snippetId, snippet, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **snippetId** | **String**|  | 
 **snippet** | [**Snippet**](Snippet.md)|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

