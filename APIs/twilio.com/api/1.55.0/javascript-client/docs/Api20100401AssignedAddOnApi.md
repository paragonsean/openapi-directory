# TwilioApi.Api20100401AssignedAddOnApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#createIncomingPhoneNumberAssignedAddOn) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json | 
[**deleteIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#deleteIncomingPhoneNumberAssignedAddOn) | **DELETE** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json | 
[**fetchIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#fetchIncomingPhoneNumberAssignedAddOn) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json | 
[**listIncomingPhoneNumberAssignedAddOn**](Api20100401AssignedAddOnApi.md#listIncomingPhoneNumberAssignedAddOn) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json | 



## createIncomingPhoneNumberAssignedAddOn

> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn createIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, installedAddOnSid)



Assign an Add-on installation to the Number specified.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AssignedAddOnApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to assign the Add-on.
let installedAddOnSid = "installedAddOnSid_example"; // String | The SID that identifies the Add-on installation.
apiInstance.createIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, installedAddOnSid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | 
 **resourceSid** | **String**| The SID of the Phone Number to assign the Add-on. | 
 **installedAddOnSid** | **String**| The SID that identifies the Add-on installation. | 

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteIncomingPhoneNumberAssignedAddOn

> deleteIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid)



Remove the assignment of an Add-on installation from the Number specified.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AssignedAddOnApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to delete.
let resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the resource to delete.
apiInstance.deleteIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to delete. | 
 **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchIncomingPhoneNumberAssignedAddOn

> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn fetchIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid)



Fetch an instance of an Add-on installation currently assigned to this Number.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AssignedAddOnApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
let resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the resource to fetch.
apiInstance.fetchIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch. | 
 **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the resource to fetch. | 

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIncomingPhoneNumberAssignedAddOn

> ListIncomingPhoneNumberAssignedAddOnResponse listIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, opts)



Retrieve a list of Add-on installations currently assigned to this Number.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AssignedAddOnApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
let resourceSid = "resourceSid_example"; // String | The SID of the Phone Number to which the Add-on is assigned.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listIncomingPhoneNumberAssignedAddOn(accountSid, resourceSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. | 
 **resourceSid** | **String**| The SID of the Phone Number to which the Add-on is assigned. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListIncomingPhoneNumberAssignedAddOnResponse**](ListIncomingPhoneNumberAssignedAddOnResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

