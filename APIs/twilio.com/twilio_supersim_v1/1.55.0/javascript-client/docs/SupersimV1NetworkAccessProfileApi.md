# TwilioSupersim.SupersimV1NetworkAccessProfileApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#createNetworkAccessProfile) | **POST** /v1/NetworkAccessProfiles | 
[**fetchNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#fetchNetworkAccessProfile) | **GET** /v1/NetworkAccessProfiles/{Sid} | 
[**listNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#listNetworkAccessProfile) | **GET** /v1/NetworkAccessProfiles | 
[**updateNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#updateNetworkAccessProfile) | **POST** /v1/NetworkAccessProfiles/{Sid} | 



## createNetworkAccessProfile

> SupersimV1NetworkAccessProfile createNetworkAccessProfile(opts)



Create a new Network Access Profile

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileApi();
let opts = {
  'networks': ["null"], // [String] | List of Network SIDs that this Network Access Profile will allow connections to.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
};
apiInstance.createNetworkAccessProfile(opts, (error, data, response) => {
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
 **networks** | [**[String]**](String.md)| List of Network SIDs that this Network Access Profile will allow connections to. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] 

### Return type

[**SupersimV1NetworkAccessProfile**](SupersimV1NetworkAccessProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchNetworkAccessProfile

> SupersimV1NetworkAccessProfile fetchNetworkAccessProfile(sid)



Fetch a Network Access Profile instance from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileApi();
let sid = "sid_example"; // String | The SID of the Network Access Profile resource to fetch.
apiInstance.fetchNetworkAccessProfile(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Network Access Profile resource to fetch. | 

### Return type

[**SupersimV1NetworkAccessProfile**](SupersimV1NetworkAccessProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkAccessProfile

> ListNetworkAccessProfileResponse listNetworkAccessProfile(opts)



Retrieve a list of Network Access Profiles from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listNetworkAccessProfile(opts, (error, data, response) => {
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

[**ListNetworkAccessProfileResponse**](ListNetworkAccessProfileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkAccessProfile

> SupersimV1NetworkAccessProfile updateNetworkAccessProfile(sid, opts)



Updates the given properties of a Network Access Profile in your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileApi();
let sid = "sid_example"; // String | The SID of the Network Access Profile to update.
let opts = {
  'uniqueName': "uniqueName_example" // String | The new unique name of the Network Access Profile.
};
apiInstance.updateNetworkAccessProfile(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Network Access Profile to update. | 
 **uniqueName** | **String**| The new unique name of the Network Access Profile. | [optional] 

### Return type

[**SupersimV1NetworkAccessProfile**](SupersimV1NetworkAccessProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

