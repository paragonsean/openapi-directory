# Stellastra.DefaultApi

All URIs are relative to *https://stellastra.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postReviewPost**](DefaultApi.md#postReviewPost) | **POST** /post-review | Posts the user&#39;s review to Stellastra



## postReviewPost

> PostReviewPost200Response postReviewPost(userEmail, rating, postReviewPostRequest, opts)

Posts the user&#39;s review to Stellastra

### Example

```javascript
import Stellastra from 'stellastra';
let defaultClient = Stellastra.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Stellastra.DefaultApi();
let userEmail = "{\"user_email\":\"johnsmith@companyxyz.com\"}"; // String | User's email to which the review verification will be sent. 
let rating = {"rating":5}; // Number | The user's star rating, must be a single integer from [1, 2, 3, 4, 5]
let postReviewPostRequest = new Stellastra.PostReviewPostRequest(); // PostReviewPostRequest | The request body requires the user_email and rating. The parameter use_name is optional. 
let opts = {
  'userName': "{\"user_name\":\"John\"}" // String | The user's name, defaults to empty string \"\".  Thus, if this is omitted, the email to the user will not use the user's name. 
};
apiInstance.postReviewPost(userEmail, rating, postReviewPostRequest, opts, (error, data, response) => {
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
 **userEmail** | **String**| User&#39;s email to which the review verification will be sent.  | 
 **rating** | **Number**| The user&#39;s star rating, must be a single integer from [1, 2, 3, 4, 5] | 
 **postReviewPostRequest** | [**PostReviewPostRequest**](PostReviewPostRequest.md)| The request body requires the user_email and rating. The parameter use_name is optional.  | 
 **userName** | **String**| The user&#39;s name, defaults to empty string \&quot;\&quot;.  Thus, if this is omitted, the email to the user will not use the user&#39;s name.  | [optional] 

### Return type

[**PostReviewPost200Response**](PostReviewPost200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

