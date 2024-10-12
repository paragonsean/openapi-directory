# BungieNetApi.ContentApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentGetContentById**](ContentApi.md#contentGetContentById) | **GET** /Content/GetContentById/{id}/{locale}/ | 
[**contentGetContentByTagAndType**](ContentApi.md#contentGetContentByTagAndType) | **GET** /Content/GetContentByTagAndType/{tag}/{type}/{locale}/ | 
[**contentGetContentType**](ContentApi.md#contentGetContentType) | **GET** /Content/GetContentType/{type}/ | 
[**contentRssNewsArticles**](ContentApi.md#contentRssNewsArticles) | **GET** /Content/Rss/NewsArticles/{pageToken}/ | 
[**contentSearchContentByTagAndType**](ContentApi.md#contentSearchContentByTagAndType) | **GET** /Content/SearchContentByTagAndType/{tag}/{type}/{locale}/ | 
[**contentSearchContentWithText**](ContentApi.md#contentSearchContentWithText) | **GET** /Content/Search/{locale}/ | 
[**contentSearchHelpArticles**](ContentApi.md#contentSearchHelpArticles) | **GET** /Content/SearchHelpArticles/{searchtext}/{size}/ | 



## contentGetContentById

> ContentGetContentById200Response contentGetContentById(id, locale, opts)



Returns a content item referenced by id

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ContentApi();
let id = 789; // Number | 
let locale = "locale_example"; // String | 
let opts = {
  'head': true // Boolean | false
};
apiInstance.contentGetContentById(id, locale, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **locale** | **String**|  | 
 **head** | **Boolean**| false | [optional] 

### Return type

[**ContentGetContentById200Response**](ContentGetContentById200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentGetContentByTagAndType

> ContentGetContentById200Response contentGetContentByTagAndType(locale, tag, type, opts)



Returns the newest item that matches a given tag and Content Type.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ContentApi();
let locale = "locale_example"; // String | 
let tag = "tag_example"; // String | 
let type = "type_example"; // String | 
let opts = {
  'head': true // Boolean | Not used.
};
apiInstance.contentGetContentByTagAndType(locale, tag, type, opts, (error, data, response) => {
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
 **locale** | **String**|  | 
 **tag** | **String**|  | 
 **type** | **String**|  | 
 **head** | **Boolean**| Not used. | [optional] 

### Return type

[**ContentGetContentById200Response**](ContentGetContentById200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentGetContentType

> ContentGetContentType200Response contentGetContentType(type)



Gets an object describing a particular variant of content.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ContentApi();
let type = "type_example"; // String | 
apiInstance.contentGetContentType(type, (error, data, response) => {
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
 **type** | **String**|  | 

### Return type

[**ContentGetContentType200Response**](ContentGetContentType200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentRssNewsArticles

> ContentRssNewsArticles200Response contentRssNewsArticles(pageToken, opts)



Returns a JSON string response that is the RSS feed for news articles.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ContentApi();
let pageToken = "pageToken_example"; // String | Zero-based pagination token for paging through result sets.
let opts = {
  'categoryfilter': "categoryfilter_example", // String | Optionally filter response to only include news items in a certain category.
  'includebody': true // Boolean | Optionally include full content body for each news item.
};
apiInstance.contentRssNewsArticles(pageToken, opts, (error, data, response) => {
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
 **pageToken** | **String**| Zero-based pagination token for paging through result sets. | 
 **categoryfilter** | **String**| Optionally filter response to only include news items in a certain category. | [optional] 
 **includebody** | **Boolean**| Optionally include full content body for each news item. | [optional] 

### Return type

[**ContentRssNewsArticles200Response**](ContentRssNewsArticles200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentSearchContentByTagAndType

> ContentSearchContentWithText200Response contentSearchContentByTagAndType(locale, tag, type, opts)



Searches for Content Items that match the given Tag and Content Type.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ContentApi();
let locale = "locale_example"; // String | 
let tag = "tag_example"; // String | 
let type = "type_example"; // String | 
let opts = {
  'currentpage': 56, // Number | Page number for the search results starting with page 1.
  'head': true, // Boolean | Not used.
  'itemsperpage': 56 // Number | Not used.
};
apiInstance.contentSearchContentByTagAndType(locale, tag, type, opts, (error, data, response) => {
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
 **locale** | **String**|  | 
 **tag** | **String**|  | 
 **type** | **String**|  | 
 **currentpage** | **Number**| Page number for the search results starting with page 1. | [optional] 
 **head** | **Boolean**| Not used. | [optional] 
 **itemsperpage** | **Number**| Not used. | [optional] 

### Return type

[**ContentSearchContentWithText200Response**](ContentSearchContentWithText200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentSearchContentWithText

> ContentSearchContentWithText200Response contentSearchContentWithText(locale, opts)



Gets content based on querystring information passed in. Provides basic search and text search capabilities.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ContentApi();
let locale = "locale_example"; // String | 
let opts = {
  'ctype': "ctype_example", // String | Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
  'currentpage': 56, // Number | Page number for the search results, starting with page 1.
  'head': true, // Boolean | Not used.
  'searchtext': "searchtext_example", // String | Word or phrase for the search.
  'source': "source_example", // String | For analytics, hint at the part of the app that triggered the search. Optional.
  'tag': "tag_example" // String | Tag used on the content to be searched.
};
apiInstance.contentSearchContentWithText(locale, opts, (error, data, response) => {
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
 **locale** | **String**|  | 
 **ctype** | **String**| Content type tag: Help, News, etc. Supply multiple ctypes separated by space. | [optional] 
 **currentpage** | **Number**| Page number for the search results, starting with page 1. | [optional] 
 **head** | **Boolean**| Not used. | [optional] 
 **searchtext** | **String**| Word or phrase for the search. | [optional] 
 **source** | **String**| For analytics, hint at the part of the app that triggered the search. Optional. | [optional] 
 **tag** | **String**| Tag used on the content to be searched. | [optional] 

### Return type

[**ContentSearchContentWithText200Response**](ContentSearchContentWithText200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## contentSearchHelpArticles

> ContentSearchHelpArticles200Response contentSearchHelpArticles(searchtext, size)



Search for Help Articles.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.ContentApi();
let searchtext = "searchtext_example"; // String | 
let size = "size_example"; // String | 
apiInstance.contentSearchHelpArticles(searchtext, size, (error, data, response) => {
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
 **searchtext** | **String**|  | 
 **size** | **String**|  | 

### Return type

[**ContentSearchHelpArticles200Response**](ContentSearchHelpArticles200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

