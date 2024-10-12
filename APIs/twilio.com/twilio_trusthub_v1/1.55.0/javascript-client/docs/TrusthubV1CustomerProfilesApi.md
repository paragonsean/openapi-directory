# TwilioTrusthub.TrusthubV1CustomerProfilesApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomerProfile**](TrusthubV1CustomerProfilesApi.md#createCustomerProfile) | **POST** /v1/CustomerProfiles | 
[**deleteCustomerProfile**](TrusthubV1CustomerProfilesApi.md#deleteCustomerProfile) | **DELETE** /v1/CustomerProfiles/{Sid} | 
[**fetchCustomerProfile**](TrusthubV1CustomerProfilesApi.md#fetchCustomerProfile) | **GET** /v1/CustomerProfiles/{Sid} | 
[**listCustomerProfile**](TrusthubV1CustomerProfilesApi.md#listCustomerProfile) | **GET** /v1/CustomerProfiles | 
[**updateCustomerProfile**](TrusthubV1CustomerProfilesApi.md#updateCustomerProfile) | **POST** /v1/CustomerProfiles/{Sid} | 



## createCustomerProfile

> TrusthubV1CustomerProfile createCustomerProfile(email, friendlyName, policySid, opts)



Create a new Customer-Profile.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesApi();
let email = "email_example"; // String | The email address that will receive updates when the Customer-Profile resource changes status.
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
let policySid = "policySid_example"; // String | The unique string of a policy that is associated to the Customer-Profile resource.
let opts = {
  'statusCallback': "statusCallback_example" // String | The URL we call to inform your application of status changes.
};
apiInstance.createCustomerProfile(email, friendlyName, policySid, opts, (error, data, response) => {
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
 **email** | **String**| The email address that will receive updates when the Customer-Profile resource changes status. | 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | 
 **policySid** | **String**| The unique string of a policy that is associated to the Customer-Profile resource. | 
 **statusCallback** | **String**| The URL we call to inform your application of status changes. | [optional] 

### Return type

[**TrusthubV1CustomerProfile**](TrusthubV1CustomerProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCustomerProfile

> deleteCustomerProfile(sid)



Delete a specific Customer-Profile.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
apiInstance.deleteCustomerProfile(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Customer-Profile resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCustomerProfile

> TrusthubV1CustomerProfile fetchCustomerProfile(sid)



Fetch a specific Customer-Profile instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
apiInstance.fetchCustomerProfile(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Customer-Profile resource. | 

### Return type

[**TrusthubV1CustomerProfile**](TrusthubV1CustomerProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomerProfile

> ListCustomerProfileResponse listCustomerProfile(opts)



Retrieve a list of all Customer-Profiles for an account.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesApi();
let opts = {
  'status': "status_example", // CustomerProfileEnumStatus | The verification status of the Customer-Profile resource.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource.
  'policySid': "policySid_example", // String | The unique string of a policy that is associated to the Customer-Profile resource.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCustomerProfile(opts, (error, data, response) => {
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
 **status** | **CustomerProfileEnumStatus**| The verification status of the Customer-Profile resource. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 
 **policySid** | **String**| The unique string of a policy that is associated to the Customer-Profile resource. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCustomerProfileResponse**](ListCustomerProfileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCustomerProfile

> TrusthubV1CustomerProfile updateCustomerProfile(sid, opts)



Updates a Customer-Profile in an account.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1CustomerProfilesApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Customer-Profile resource.
let opts = {
  'email': "email_example", // String | The email address that will receive updates when the Customer-Profile resource changes status.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource.
  'status': "status_example", // CustomerProfileEnumStatus | 
  'statusCallback': "statusCallback_example" // String | The URL we call to inform your application of status changes.
};
apiInstance.updateCustomerProfile(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Customer-Profile resource. | 
 **email** | **String**| The email address that will receive updates when the Customer-Profile resource changes status. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 
 **status** | **CustomerProfileEnumStatus**|  | [optional] 
 **statusCallback** | **String**| The URL we call to inform your application of status changes. | [optional] 

### Return type

[**TrusthubV1CustomerProfile**](TrusthubV1CustomerProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

