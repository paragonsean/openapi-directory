# VestorlyApi.CustomFeedArticlesApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findCustomFeedArticles**](CustomFeedArticlesApi.md#findCustomFeedArticles) | **GET** /custom_feeds/{id}/articles | 



## findCustomFeedArticles

> Articles findCustomFeedArticles(vestorlyAuth, id, opts)



Returns Articles by Category

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedArticlesApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Category Id to fetch
let opts = {
  'accessToken': "accessToken_example", // String | OAuth Token
  'limit': 56, // Number | Limit on the number of articles to return
  'sortBy': "sortBy_example", // String | Field on model to sort by
  'start': 56, // Number | Field where the fetch will start from
  'createdAtGteDaysAgo': "createdAtGteDaysAgo_example", // String | Filter retrieved articles since this date
  'textQuery': "textQuery_example" // String | Search query parameter
};
apiInstance.findCustomFeedArticles(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| Category Id to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 
 **limit** | **Number**| Limit on the number of articles to return | [optional] 
 **sortBy** | **String**| Field on model to sort by | [optional] 
 **start** | **Number**| Field where the fetch will start from | [optional] 
 **createdAtGteDaysAgo** | **String**| Filter retrieved articles since this date | [optional] 
 **textQuery** | **String**| Search query parameter | [optional] 

### Return type

[**Articles**](Articles.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

