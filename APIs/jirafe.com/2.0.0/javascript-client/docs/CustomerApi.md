# JirafeEvents.CustomerApi

All URIs are relative to *https://event.jirafe.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCustomer**](CustomerApi.md#postCustomer) | **POST** /{siteId}/customer | Send a customer for the given site



## postCustomer

> postCustomer(siteId, body)

Send a customer for the given site

### Example

```javascript
import JirafeEvents from 'jirafe_events';
let defaultClient = JirafeEvents.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_accessCode
let oauth2_accessCode = defaultClient.authentications['oauth2_accessCode'];
oauth2_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2_implicit
let oauth2_implicit = defaultClient.authentications['oauth2_implicit'];
oauth2_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new JirafeEvents.CustomerApi();
let siteId = "siteId_example"; // String | ID site to send the event
let body = new JirafeEvents.Customer(); // Customer | customer json for the event
apiInstance.postCustomer(siteId, body, (error, data, response) => {
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
 **siteId** | **String**| ID site to send the event | 
 **body** | [**Customer**](Customer.md)| customer json for the event | 

### Return type

null (empty response body)

### Authorization

[oauth2_accessCode](../README.md#oauth2_accessCode), [oauth2_implicit](../README.md#oauth2_implicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

