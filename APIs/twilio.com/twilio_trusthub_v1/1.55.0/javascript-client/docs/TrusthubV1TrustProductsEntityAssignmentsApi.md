# TwilioTrusthub.TrusthubV1TrustProductsEntityAssignmentsApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#createTrustProductEntityAssignment) | **POST** /v1/TrustProducts/{TrustProductSid}/EntityAssignments | 
[**deleteTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#deleteTrustProductEntityAssignment) | **DELETE** /v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid} | 
[**fetchTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#fetchTrustProductEntityAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/EntityAssignments/{Sid} | 
[**listTrustProductEntityAssignment**](TrusthubV1TrustProductsEntityAssignmentsApi.md#listTrustProductEntityAssignment) | **GET** /v1/TrustProducts/{TrustProductSid}/EntityAssignments | 



## createTrustProductEntityAssignment

> TrusthubV1TrustProductTrustProductEntityAssignment createTrustProductEntityAssignment(trustProductSid, objectSid)



Create a new Assigned Item.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsEntityAssignmentsApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
let objectSid = "objectSid_example"; // String | The SID of an object bag that holds information of the different items.
apiInstance.createTrustProductEntityAssignment(trustProductSid, objectSid, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | 
 **objectSid** | **String**| The SID of an object bag that holds information of the different items. | 

### Return type

[**TrusthubV1TrustProductTrustProductEntityAssignment**](TrusthubV1TrustProductTrustProductEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTrustProductEntityAssignment

> deleteTrustProductEntityAssignment(trustProductSid, sid)



Remove an Assignment Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsEntityAssignmentsApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
let sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
apiInstance.deleteTrustProductEntityAssignment(trustProductSid, sid, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | 
 **sid** | **String**| The unique string that we created to identify the Identity resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTrustProductEntityAssignment

> TrusthubV1TrustProductTrustProductEntityAssignment fetchTrustProductEntityAssignment(trustProductSid, sid)



Fetch specific Assigned Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsEntityAssignmentsApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
let sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
apiInstance.fetchTrustProductEntityAssignment(trustProductSid, sid, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | 
 **sid** | **String**| The unique string that we created to identify the Identity resource. | 

### Return type

[**TrusthubV1TrustProductTrustProductEntityAssignment**](TrusthubV1TrustProductTrustProductEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTrustProductEntityAssignment

> ListTrustProductEntityAssignmentResponse listTrustProductEntityAssignment(trustProductSid, opts)



Retrieve a list of all Assigned Items for an account.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1TrustProductsEntityAssignmentsApi();
let trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the TrustProduct resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTrustProductEntityAssignment(trustProductSid, opts, (error, data, response) => {
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
 **trustProductSid** | **String**| The unique string that we created to identify the TrustProduct resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTrustProductEntityAssignmentResponse**](ListTrustProductEntityAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

