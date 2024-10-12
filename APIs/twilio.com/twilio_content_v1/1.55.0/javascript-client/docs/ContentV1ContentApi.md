# TwilioContent.ContentV1ContentApi

All URIs are relative to *https://content.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteContent**](ContentV1ContentApi.md#deleteContent) | **DELETE** /v1/Content/{Sid} | 
[**fetchContent**](ContentV1ContentApi.md#fetchContent) | **GET** /v1/Content/{Sid} | 
[**listContent**](ContentV1ContentApi.md#listContent) | **GET** /v1/Content | 



## deleteContent

> deleteContent(sid)



Deletes a Content resource

### Example

```javascript
import TwilioContent from 'twilio_content';
let defaultClient = TwilioContent.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioContent.ContentV1ContentApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Content resource to fetch.
apiInstance.deleteContent(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Content resource to fetch. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchContent

> ContentV1Content fetchContent(sid)



Fetch a Content resource by its unique Content Sid

### Example

```javascript
import TwilioContent from 'twilio_content';
let defaultClient = TwilioContent.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioContent.ContentV1ContentApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Content resource to fetch.
apiInstance.fetchContent(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Content resource to fetch. | 

### Return type

[**ContentV1Content**](ContentV1Content.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContent

> ListContentResponse listContent(opts)



Retrieve a list of Contents belonging to the account used to make the request

### Example

```javascript
import TwilioContent from 'twilio_content';
let defaultClient = TwilioContent.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioContent.ContentV1ContentApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listContent(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListContentResponse**](ListContentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

