# TwilioTrusthub.TrusthubV1TrustProductsChannelEndpointAssignmentApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#createTrustProductChannelEndpointAssignment) | **POST** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments | 
[**deleteTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#deleteTrustProductChannelEndpointAssignment) | **DELETE** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments/{Sid} | 
[**fetchTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#fetchTrustProductChannelEndpointAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments/{Sid} | 
[**listTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductsChannelEndpointAssignmentApi.md#listTrustProductChannelEndpointAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/ChannelEndpointAssignments | 



## createTrustProductChannelEndpointAssignment

> TrusthubV1TrustProductTrustProductChannelEndpointAssignment createTrustProductChannelEndpointAssignment(trustProductSid, channelEndpointSid, channelEndpointType)



Create a new Assigned Item.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsChannelEndpointAssignmentApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let channelEndpointSid = "channelEndpointSid_example"; // String | The SID of an channel endpoint
let channelEndpointType = "channelEndpointType_example"; // String | The type of channel endpoint. eg: phone-number
apiInstance.createTrustProductChannelEndpointAssignment(trustProductSid, channelEndpointSid, channelEndpointType, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **channelEndpointSid** | **String**| The SID of an channel endpoint | 
 **channelEndpointType** | **String**| The type of channel endpoint. eg: phone-number | 

### Return type

[**TrusthubV1TrustProductTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductTrustProductChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTrustProductChannelEndpointAssignment

> deleteTrustProductChannelEndpointAssignment(trustProductSid, sid)



Remove an Assignment Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsChannelEndpointAssignmentApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let sid = "sid_example"; // String | The unique string that we created to identify the resource.
apiInstance.deleteTrustProductChannelEndpointAssignment(trustProductSid, sid, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **sid** | **String**| The unique string that we created to identify the resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTrustProductChannelEndpointAssignment

> TrusthubV1TrustProductTrustProductChannelEndpointAssignment fetchTrustProductChannelEndpointAssignment(trustProductSid, sid)



Fetch specific Assigned Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsChannelEndpointAssignmentApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let sid = "sid_example"; // String | The unique string that we created to identify the resource.
apiInstance.fetchTrustProductChannelEndpointAssignment(trustProductSid, sid, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **sid** | **String**| The unique string that we created to identify the resource. | 

### Return type

[**TrusthubV1TrustProductTrustProductChannelEndpointAssignment**](TrusthubV1TrustProductTrustProductChannelEndpointAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTrustProductChannelEndpointAssignment

> ListTrustProductChannelEndpointAssignmentResponse listTrustProductChannelEndpointAssignment(trustProductSid, opts)



Retrieve a list of all Assigned Items for an account.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsChannelEndpointAssignmentApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let opts = {
  'channelEndpointSid': "channelEndpointSid_example", // String | The SID of an channel endpoint
  'channelEndpointSids': "channelEndpointSids_example", // String | comma separated list of channel endpoint sids
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTrustProductChannelEndpointAssignment(trustProductSid, opts, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | 
 **channelEndpointSid** | **String**| The SID of an channel endpoint | [optional] 
 **channelEndpointSids** | **String**| comma separated list of channel endpoint sids | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTrustProductChannelEndpointAssignmentResponse**](ListTrustProductChannelEndpointAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

