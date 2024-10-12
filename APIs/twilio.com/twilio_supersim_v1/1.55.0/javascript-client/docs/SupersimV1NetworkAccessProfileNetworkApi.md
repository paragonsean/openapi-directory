# TwilioSupersim.SupersimV1NetworkAccessProfileNetworkApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#createNetworkAccessProfileNetwork) | **POST** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks | 
[**deleteNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#deleteNetworkAccessProfileNetwork) | **DELETE** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks/{Sid} | 
[**fetchNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#fetchNetworkAccessProfileNetwork) | **GET** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks/{Sid} | 
[**listNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#listNetworkAccessProfileNetwork) | **GET** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks | 



## createNetworkAccessProfileNetwork

> SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork createNetworkAccessProfileNetwork(networkAccessProfileSid, network)



Add a Network resource to the Network Access Profile resource.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileNetworkApi();
let networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
let network = "network_example"; // String | The SID of the Network resource to be added to the Network Access Profile resource.
apiInstance.createNetworkAccessProfileNetwork(networkAccessProfileSid, network, (error, data, response) => {
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
 **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | 
 **network** | **String**| The SID of the Network resource to be added to the Network Access Profile resource. | 

### Return type

[**SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteNetworkAccessProfileNetwork

> deleteNetworkAccessProfileNetwork(networkAccessProfileSid, sid)



Remove a Network resource from the Network Access Profile resource&#39;s.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileNetworkApi();
let networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
let sid = "sid_example"; // String | The SID of the Network resource to be removed from the Network Access Profile resource.
apiInstance.deleteNetworkAccessProfileNetwork(networkAccessProfileSid, sid, (error, data, response) => {
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
 **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | 
 **sid** | **String**| The SID of the Network resource to be removed from the Network Access Profile resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchNetworkAccessProfileNetwork

> SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork fetchNetworkAccessProfileNetwork(networkAccessProfileSid, sid)



Fetch a Network Access Profile resource&#39;s Network resource.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileNetworkApi();
let networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
let sid = "sid_example"; // String | The SID of the Network resource to fetch.
apiInstance.fetchNetworkAccessProfileNetwork(networkAccessProfileSid, sid, (error, data, response) => {
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
 **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | 
 **sid** | **String**| The SID of the Network resource to fetch. | 

### Return type

[**SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkAccessProfileNetwork

> ListNetworkAccessProfileNetworkResponse listNetworkAccessProfileNetwork(networkAccessProfileSid, opts)



Retrieve a list of Network Access Profile resource&#39;s Network resource.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1NetworkAccessProfileNetworkApi();
let networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listNetworkAccessProfileNetwork(networkAccessProfileSid, opts, (error, data, response) => {
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
 **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListNetworkAccessProfileNetworkResponse**](ListNetworkAccessProfileNetworkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

