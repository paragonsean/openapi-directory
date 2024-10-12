# TwilioTrusthub.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#createCustomerProfileChannelEndpointAssignment) | **POST** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments | 
[**deleteCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#deleteCustomerProfileChannelEndpointAssignment) | **DELETE** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid} | 
[**fetchCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#fetchCustomerProfileChannelEndpointAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments/{Sid} | 
[**listCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfilesChannelEndpointAssignmentApi.md#listCustomerProfileChannelEndpointAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/ChannelEndpointAssignments | 



## createCustomerProfileChannelEndpointAssignment

> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment createCustomerProfileChannelEndpointAssignment(customerProfileSid, channelEndpointSid, channelEndpointType)



Create a new Assigned Item.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let channelEndpointSid = "channelEndpointSid_example"; // String | The SID of an channel endpoint
let channelEndpointType = "channelEndpointType_example"; // String | The type of channel endpoint. eg: phone-number
apiInstance.createCustomerProfileChannelEndpointAssignment(customerProfileSid, channelEndpointSid, channelEndpointType, (error, data, response) => {
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
 **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **channelEndpointSid** | **String**| The SID of an channel endpoint | 
 **channelEndpointType** | **String**| The type of channel endpoint. eg: phone-number | 

### Return type

[**TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCustomerProfileChannelEndpointAssignment

> deleteCustomerProfileChannelEndpointAssignment(customerProfileSid, sid)



Remove an Assignment Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let sid = "sid_example"; // String | The unique string that we created to identify the resource.
apiInstance.deleteCustomerProfileChannelEndpointAssignment(customerProfileSid, sid, (error, data, response) => {
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
 **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **sid** | **String**| The unique string that we created to identify the resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCustomerProfileChannelEndpointAssignment

> TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment fetchCustomerProfileChannelEndpointAssignment(customerProfileSid, sid)



Fetch specific Assigned Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let sid = "sid_example"; // String | The unique string that we created to identify the resource.
apiInstance.fetchCustomerProfileChannelEndpointAssignment(customerProfileSid, sid, (error, data, response) => {
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
 **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **sid** | **String**| The unique string that we created to identify the resource. | 

### Return type

[**TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment**](TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomerProfileChannelEndpointAssignment

> ListCustomerProfileChannelEndpointAssignmentResponse listCustomerProfileChannelEndpointAssignment(customerProfileSid, opts)



Retrieve a list of all Assigned Items for an account.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesChannelEndpointAssignmentApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let opts = {
  'channelEndpointSid': "channelEndpointSid_example", // String | The SID of an channel endpoint
  'channelEndpointSids': "channelEndpointSids_example", // String | comma separated list of channel endpoint sids
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCustomerProfileChannelEndpointAssignment(customerProfileSid, opts, (error, data, response) => {
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
 **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **channelEndpointSid** | **String**| The SID of an channel endpoint | [optional] 
 **channelEndpointSids** | **String**| comma separated list of channel endpoint sids | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCustomerProfileChannelEndpointAssignmentResponse**](ListCustomerProfileChannelEndpointAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

