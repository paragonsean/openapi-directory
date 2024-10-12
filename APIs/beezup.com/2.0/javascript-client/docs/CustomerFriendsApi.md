# BeezUpMerchantApi.CustomerFriendsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFriendInfo**](CustomerFriendsApi.md#getFriendInfo) | **GET** /v2/user/customer/friends/{userId} | Get friend information



## getFriendInfo

> UserFriendInfo getFriendInfo(userId, opts)

Get friend information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerFriendsApi();
let userId = "userId_example"; // String | Your friend user id
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getFriendInfo(userId, opts, (error, data, response) => {
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
 **userId** | **String**| Your friend user id | 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**UserFriendInfo**](UserFriendInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

