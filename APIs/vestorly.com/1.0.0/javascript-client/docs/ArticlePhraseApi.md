# VestorlyApi.ArticlePhraseApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findArticlePhrases**](ArticlePhraseApi.md#findArticlePhrases) | **GET** /article_phrases | 



## findArticlePhrases

> ArticlePhrases findArticlePhrases(vestorlyAuth, opts)



Returns phrases used in Categories

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.ArticlePhraseApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example", // String | OAuth Token
  'textSearch': "textSearch_example", // String | Text to search phrases
  'size': 56, // Number | Number of returned phrases
  'from': 56 // Number | Number of phrases to skip
};
apiInstance.findArticlePhrases(vestorlyAuth, opts, (error, data, response) => {
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
 **textSearch** | **String**| Text to search phrases | [optional] 
 **size** | **Number**| Number of returned phrases | [optional] 
 **from** | **Number**| Number of phrases to skip | [optional] 

### Return type

[**ArticlePhrases**](ArticlePhrases.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

