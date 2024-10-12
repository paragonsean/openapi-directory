# GooglePlayDeveloper.OrdersApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherOrdersRefund**](OrdersApi.md#androidpublisherOrdersRefund) | **POST** /{packageName}/orders/{orderId}:refund | 



## androidpublisherOrdersRefund

> androidpublisherOrdersRefund(packageName, orderId, opts)



Refund a user&#39;s subscription or in-app purchase order.

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

let apiInstance = new GooglePlayDeveloper.OrdersApi();
let packageName = "packageName_example"; // String | The package name of the application for which this subscription or in-app item was purchased (for example, 'com.some.thing').
let orderId = "orderId_example"; // String | The order ID provided to the user when the subscription or in-app order was purchased.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'revoke': true // Boolean | Whether to revoke the purchased item. If set to true, access to the subscription or in-app item will be terminated immediately. If the item is a recurring subscription, all future payments will also be terminated. Consumed in-app items need to be handled by developer's app. (optional)
};
apiInstance.androidpublisherOrdersRefund(packageName, orderId, opts, (error, data, response) => {
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
 **packageName** | **String**| The package name of the application for which this subscription or in-app item was purchased (for example, &#39;com.some.thing&#39;). | 
 **orderId** | **String**| The order ID provided to the user when the subscription or in-app order was purchased. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **revoke** | **Boolean**| Whether to revoke the purchased item. If set to true, access to the subscription or in-app item will be terminated immediately. If the item is a recurring subscription, all future payments will also be terminated. Consumed in-app items need to be handled by developer&#39;s app. (optional) | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

