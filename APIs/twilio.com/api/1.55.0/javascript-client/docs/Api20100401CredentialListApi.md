# TwilioApi.Api20100401CredentialListApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipCredentialList**](Api20100401CredentialListApi.md#createSipCredentialList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json | 
[**deleteSipCredentialList**](Api20100401CredentialListApi.md#deleteSipCredentialList) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json | 
[**fetchSipCredentialList**](Api20100401CredentialListApi.md#fetchSipCredentialList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json | 
[**listSipCredentialList**](Api20100401CredentialListApi.md#listSipCredentialList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json | 
[**updateSipCredentialList**](Api20100401CredentialListApi.md#updateSipCredentialList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json | 



## createSipCredentialList

> ApiV2010AccountSipSipCredentialList createSipCredentialList(accountSid, friendlyName)



Create a Credential List

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let friendlyName = "friendlyName_example"; // String | A human readable descriptive text that describes the CredentialList, up to 64 characters long.
apiInstance.createSipCredentialList(accountSid, friendlyName, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **friendlyName** | **String**| A human readable descriptive text that describes the CredentialList, up to 64 characters long. | 

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipCredentialList

> deleteSipCredentialList(accountSid, sid)



Delete a Credential List

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let sid = "sid_example"; // String | The credential list Sid that uniquely identifies this resource
apiInstance.deleteSipCredentialList(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **sid** | **String**| The credential list Sid that uniquely identifies this resource | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipCredentialList

> ApiV2010AccountSipSipCredentialList fetchSipCredentialList(accountSid, sid)



Get a Credential List

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let sid = "sid_example"; // String | The credential list Sid that uniquely identifies this resource
apiInstance.fetchSipCredentialList(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **sid** | **String**| The credential list Sid that uniquely identifies this resource | 

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipCredentialList

> ListSipCredentialListResponse listSipCredentialList(accountSid, opts)



Get All Credential Lists

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipCredentialList(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipCredentialListResponse**](ListSipCredentialListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSipCredentialList

> ApiV2010AccountSipSipCredentialList updateSipCredentialList(accountSid, sid, friendlyName)



Update a Credential List

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let sid = "sid_example"; // String | The credential list Sid that uniquely identifies this resource
let friendlyName = "friendlyName_example"; // String | A human readable descriptive text for a CredentialList, up to 64 characters long.
apiInstance.updateSipCredentialList(accountSid, sid, friendlyName, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **sid** | **String**| The credential list Sid that uniquely identifies this resource | 
 **friendlyName** | **String**| A human readable descriptive text for a CredentialList, up to 64 characters long. | 

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

