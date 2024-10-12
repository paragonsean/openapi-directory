# TwilioNumbers.NumbersV2ItemAssignmentApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createItemAssignment**](NumbersV2ItemAssignmentApi.md#createItemAssignment) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments | 
[**deleteItemAssignment**](NumbersV2ItemAssignmentApi.md#deleteItemAssignment) | **DELETE** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid} | 
[**fetchItemAssignment**](NumbersV2ItemAssignmentApi.md#fetchItemAssignment) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments/{Sid} | 
[**listItemAssignment**](NumbersV2ItemAssignmentApi.md#listItemAssignment) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ItemAssignments | 



## createItemAssignment

> NumbersV2RegulatoryComplianceBundleItemAssignment createItemAssignment(bundleSid, objectSid)



Create a new Assigned Item.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2ItemAssignmentApi();
let bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
let objectSid = "objectSid_example"; // String | The SID of an object bag that holds information of the different items.
apiInstance.createItemAssignment(bundleSid, objectSid, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | 
 **objectSid** | **String**| The SID of an object bag that holds information of the different items. | 

### Return type

[**NumbersV2RegulatoryComplianceBundleItemAssignment**](NumbersV2RegulatoryComplianceBundleItemAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteItemAssignment

> deleteItemAssignment(bundleSid, sid)



Remove an Assignment Item Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2ItemAssignmentApi();
let bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
let sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
apiInstance.deleteItemAssignment(bundleSid, sid, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | 
 **sid** | **String**| The unique string that we created to identify the Identity resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchItemAssignment

> NumbersV2RegulatoryComplianceBundleItemAssignment fetchItemAssignment(bundleSid, sid)



Fetch specific Assigned Item Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2ItemAssignmentApi();
let bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
let sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
apiInstance.fetchItemAssignment(bundleSid, sid, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | 
 **sid** | **String**| The unique string that we created to identify the Identity resource. | 

### Return type

[**NumbersV2RegulatoryComplianceBundleItemAssignment**](NumbersV2RegulatoryComplianceBundleItemAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listItemAssignment

> ListItemAssignmentResponse listItemAssignment(bundleSid, opts)



Retrieve a list of all Assigned Items for an account.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2ItemAssignmentApi();
let bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listItemAssignment(bundleSid, opts, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListItemAssignmentResponse**](ListItemAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

