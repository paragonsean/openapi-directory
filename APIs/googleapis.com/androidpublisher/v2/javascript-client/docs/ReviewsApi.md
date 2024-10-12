# GooglePlayDeveloper.ReviewsApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherReviewsGet**](ReviewsApi.md#androidpublisherReviewsGet) | **GET** /{packageName}/reviews/{reviewId} | 
[**androidpublisherReviewsList**](ReviewsApi.md#androidpublisherReviewsList) | **GET** /{packageName}/reviews | 
[**androidpublisherReviewsReply**](ReviewsApi.md#androidpublisherReviewsReply) | **POST** /{packageName}/reviews/{reviewId}:reply | 



## androidpublisherReviewsGet

> Review androidpublisherReviewsGet(packageName, reviewId, opts)



Returns a single review.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.ReviewsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app for which we want reviews; for example, \"com.spiffygame\".
let reviewId = "reviewId_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'translationLanguage': "translationLanguage_example" // String | 
};
apiInstance.androidpublisherReviewsGet(packageName, reviewId, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;. | 
 **reviewId** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **translationLanguage** | **String**|  | [optional] 

### Return type

[**Review**](Review.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherReviewsList

> ReviewsListResponse androidpublisherReviewsList(packageName, opts)



Returns a list of reviews. Only reviews from last week will be returned.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.ReviewsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app for which we want reviews; for example, \"com.spiffygame\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 56, // Number | 
  'startIndex': 56, // Number | 
  'token': "token_example", // String | 
  'translationLanguage': "translationLanguage_example" // String | 
};
apiInstance.androidpublisherReviewsList(packageName, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **startIndex** | **Number**|  | [optional] 
 **token** | **String**|  | [optional] 
 **translationLanguage** | **String**|  | [optional] 

### Return type

[**ReviewsListResponse**](ReviewsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherReviewsReply

> ReviewsReplyResponse androidpublisherReviewsReply(packageName, reviewId, opts)



Reply to a single review, or update an existing reply.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.ReviewsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app for which we want reviews; for example, \"com.spiffygame\".
let reviewId = "reviewId_example"; // String | 
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'reviewsReplyRequest': new GooglePlayDeveloper.ReviewsReplyRequest() // ReviewsReplyRequest | 
};
apiInstance.androidpublisherReviewsReply(packageName, reviewId, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;. | 
 **reviewId** | **String**|  | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **reviewsReplyRequest** | [**ReviewsReplyRequest**](ReviewsReplyRequest.md)|  | [optional] 

### Return type

[**ReviewsReplyResponse**](ReviewsReplyResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

