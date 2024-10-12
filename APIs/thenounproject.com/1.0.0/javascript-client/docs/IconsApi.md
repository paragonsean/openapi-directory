# TheNounProject.IconsApi

All URIs are relative to *http://api.thenounproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIconsByTerm**](IconsApi.md#getIconsByTerm) | **GET** /icons/{term} | Get icons by term
[**getRecentIcons**](IconsApi.md#getRecentIcons) | **GET** /icons/recent_uploads | Get recent icons



## getIconsByTerm

> getIconsByTerm(term, opts)

Get icons by term

Returns a list of icons

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.IconsApi();
let term = "term_example"; // String | Icon term
let opts = {
  'limitToPublicDomain': 56, // Number | Limit results to public domain icons only
  'limit': 56, // Number | Maximum number of results
  'offset': 56, // Number | Number of results to displace or skip over
  'page': 56 // Number | Number of results of limit length to displace or skip over
};
apiInstance.getIconsByTerm(term, opts, (error, data, response) => {
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
 **term** | **String**| Icon term | 
 **limitToPublicDomain** | **Number**| Limit results to public domain icons only | [optional] 
 **limit** | **Number**| Maximum number of results | [optional] 
 **offset** | **Number**| Number of results to displace or skip over | [optional] 
 **page** | **Number**| Number of results of limit length to displace or skip over | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRecentIcons

> getRecentIcons(opts)

Get recent icons

Returns list of most recently uploaded icons

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.IconsApi();
let opts = {
  'limit': 56, // Number | Maximum number of results
  'offset': 56, // Number | Number of results to displace or skip over
  'page': 56 // Number | Number of results of limit length to displace or skip over
};
apiInstance.getRecentIcons(opts, (error, data, response) => {
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
 **limit** | **Number**| Maximum number of results | [optional] 
 **offset** | **Number**| Number of results to displace or skip over | [optional] 
 **page** | **Number**| Number of results of limit length to displace or skip over | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

