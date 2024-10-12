# PromotionsTaxesApi.NotificationsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usagenotification**](NotificationsApi.md#usagenotification) | **POST** /api/rnb/pub/notifications | Usage notification



## usagenotification

> usagenotification(contentType, accept, usagenotificationRequest)

Usage notification

Usage notification

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.NotificationsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let usagenotificationRequest = {"accountId":"ffffffff-gggg-hhhh-iiii-jjjjjjjjjjjj","calculatorIds":["discount_basetestqa_1"],"coupon":"cupom","itemsCount":4,"orderId":"vbbbbbb-1","profileId":"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee","used":true}; // UsagenotificationRequest | 
apiInstance.usagenotification(contentType, accept, usagenotificationRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **usagenotificationRequest** | [**UsagenotificationRequest**](UsagenotificationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

