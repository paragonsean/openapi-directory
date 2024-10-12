# VestorlyApi.ArticlesApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findArticleByID**](ArticlesApi.md#findArticleByID) | **GET** /articles/{id} | 
[**findArticles**](ArticlesApi.md#findArticles) | **GET** /articles | 



## findArticleByID

> Articleresponse findArticleByID(vestorlyAuth, id, opts)



Returns a single article

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.ArticlesApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Article Id to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findArticleByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **id** | **String**| Article Id to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Articleresponse**](Articleresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findArticles

> Articles findArticles(vestorlyAuth, opts)



Returns all articles

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.ArticlesApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example", // String | OAuth Token
  'limit': 56, // Number | Limit on the number of articles to return
  'textQuery': "textQuery_example", // String | Search query parameter
  'sortDirection': "sortDirection_example", // String | Direction of sort (used with sort_by parameter)
  'sortBy': "sortBy_example" // String | Field on model to sort by
};
apiInstance.findArticles(vestorlyAuth, opts, (error, data, response) => {
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
 **accessToken** | **String**| OAuth Token | [optional] 
 **limit** | **Number**| Limit on the number of articles to return | [optional] 
 **textQuery** | **String**| Search query parameter | [optional] 
 **sortDirection** | **String**| Direction of sort (used with sort_by parameter) | [optional] 
 **sortBy** | **String**| Field on model to sort by | [optional] 

### Return type

[**Articles**](Articles.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

