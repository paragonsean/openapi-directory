# Mailsquad.SubscriptionApi

All URIs are relative to *https://api.inboxroute.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionListidPost**](SubscriptionApi.md#subscriptionListidPost) | **POST** /subscription/{listid} | 



## subscriptionListidPost

> subscriptionListidPost(listid, subscription)



Subscribe an email address to a list. This api call has the same behavior as a regular subscribe form. However, single opt-in is allowed for system integration purposes.  - If email address does not exist, a new contact will be added to the list. - If email address exists custom fields will be updated and status will be put   to unconfirmed or active depending of singleoptin value. - If current status if Active, this operation will only update the custom fields. - If singleoptin is true, no email confirmation will be sent. In that case,   you must provide the subscribe&#39;s origin ip and confirmation date-time. 

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.SubscriptionApi();
let listid = "listid_example"; // String | Unique 16 characters ID of the contact list
let subscription = new Mailsquad.SubscriptionRequest(); // SubscriptionRequest | Subscription request
apiInstance.subscriptionListidPost(listid, subscription, (error, data, response) => {
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
 **listid** | **String**| Unique 16 characters ID of the contact list | 
 **subscription** | [**SubscriptionRequest**](SubscriptionRequest.md)| Subscription request | 

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

