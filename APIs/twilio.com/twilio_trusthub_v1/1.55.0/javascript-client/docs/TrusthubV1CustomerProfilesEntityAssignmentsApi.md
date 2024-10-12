# TwilioTrusthub.TrusthubV1CustomerProfilesEntityAssignmentsApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#createCustomerProfileEntityAssignment) | **POST** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments | 
[**deleteCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#deleteCustomerProfileEntityAssignment) | **DELETE** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid} | 
[**fetchCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#fetchCustomerProfileEntityAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments/{Sid} | 
[**listCustomerProfileEntityAssignment**](TrusthubV1CustomerProfilesEntityAssignmentsApi.md#listCustomerProfileEntityAssignment) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/EntityAssignments | 



## createCustomerProfileEntityAssignment

> TrusthubV1CustomerProfileCustomerProfileEntityAssignment createCustomerProfileEntityAssignment(customerProfileSid, objectSid)



Create a new Assigned Item.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesEntityAssignmentsApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let objectSid = "objectSid_example"; // String | The SID of an object bag that holds information of the different items.
apiInstance.createCustomerProfileEntityAssignment(customerProfileSid, objectSid, (error, data, response) => {
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
 **objectSid** | **String**| The SID of an object bag that holds information of the different items. | 

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEntityAssignment**](TrusthubV1CustomerProfileCustomerProfileEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCustomerProfileEntityAssignment

> deleteCustomerProfileEntityAssignment(customerProfileSid, sid)



Remove an Assignment Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesEntityAssignmentsApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
apiInstance.deleteCustomerProfileEntityAssignment(customerProfileSid, sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Identity resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCustomerProfileEntityAssignment

> TrusthubV1CustomerProfileCustomerProfileEntityAssignment fetchCustomerProfileEntityAssignment(customerProfileSid, sid)



Fetch specific Assigned Item Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesEntityAssignmentsApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let sid = "sid_example"; // String | The unique string that we created to identify the Identity resource.
apiInstance.fetchCustomerProfileEntityAssignment(customerProfileSid, sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Identity resource. | 

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEntityAssignment**](TrusthubV1CustomerProfileCustomerProfileEntityAssignment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomerProfileEntityAssignment

> ListCustomerProfileEntityAssignmentResponse listCustomerProfileEntityAssignment(customerProfileSid, opts)



Retrieve a list of all Assigned Items for an account.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesEntityAssignmentsApi();
let customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCustomerProfileEntityAssignment(customerProfileSid, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCustomerProfileEntityAssignmentResponse**](ListCustomerProfileEntityAssignmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

