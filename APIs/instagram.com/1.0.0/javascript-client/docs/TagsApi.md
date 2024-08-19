# InstagramApi.TagsApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagsSearchGet**](TagsApi.md#tagsSearchGet) | **GET** /tags/search | Search for tags by name.
[**tagsTagNameGet**](TagsApi.md#tagsTagNameGet) | **GET** /tags/{tag-name} | Get information about a tag object.
[**tagsTagNameMediaRecentGet**](TagsApi.md#tagsTagNameMediaRecentGet) | **GET** /tags/{tag-name}/media/recent | Get a list of recently tagged media.



## tagsSearchGet

> TagSearchResponse tagsSearchGet(q)

Search for tags by name.

Search for tags by name.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.TagsApi();
let q = "q_example"; // String | A valid tag name without a leading \\#. (eg. snowy, nofilter)
apiInstance.tagsSearchGet(q, (error, data, response) => {
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
 **q** | **String**| A valid tag name without a leading \\#. (eg. snowy, nofilter) | 

### Return type

[**TagSearchResponse**](TagSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsTagNameGet

> TagInfoResponse tagsTagNameGet(tagName)

Get information about a tag object.

Get information about a tag object.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.TagsApi();
let tagName = "tagName_example"; // String | The tag name.
apiInstance.tagsTagNameGet(tagName, (error, data, response) => {
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
 **tagName** | **String**| The tag name. | 

### Return type

[**TagInfoResponse**](TagInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsTagNameMediaRecentGet

> TagMediaListResponse tagsTagNameMediaRecentGet(tagName, opts)

Get a list of recently tagged media.

Get a list of recently tagged media. Use the &#x60;max_tag_id&#x60; and &#x60;min_tag_id&#x60; parameters in the pagination response to paginate through these objects. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.TagsApi();
let tagName = "tagName_example"; // String | The tag name.
let opts = {
  'count': 56, // Number | Count of tagged media to return.
  'minTagId': "minTagId_example", // String | Return media before this `min_tag_id`.
  'maxTagId': "maxTagId_example" // String | Return media after this `max_tag_id`.
};
apiInstance.tagsTagNameMediaRecentGet(tagName, opts, (error, data, response) => {
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
 **tagName** | **String**| The tag name. | 
 **count** | **Number**| Count of tagged media to return. | [optional] 
 **minTagId** | **String**| Return media before this &#x60;min_tag_id&#x60;. | [optional] 
 **maxTagId** | **String**| Return media after this &#x60;max_tag_id&#x60;. | [optional] 

### Return type

[**TagMediaListResponse**](TagMediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

