# TwilioApi.Api20100401CredentialApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipCredential**](Api20100401CredentialApi.md#createSipCredential) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json | 
[**deleteSipCredential**](Api20100401CredentialApi.md#deleteSipCredential) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json | 
[**fetchSipCredential**](Api20100401CredentialApi.md#fetchSipCredential) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json | 
[**listSipCredential**](Api20100401CredentialApi.md#listSipCredential) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json | 
[**updateSipCredential**](Api20100401CredentialApi.md#updateSipCredential) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json | 



## createSipCredential

> ApiV2010AccountSipSipCredentialListSipCredential createSipCredential(accountSid, credentialListSid, password, username)



Create a new credential resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list to include the created credential.
let password = "password_example"; // String | The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)
let username = "username_example"; // String | The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.
apiInstance.createSipCredential(accountSid, credentialListSid, password, username, (error, data, response) => {
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
 **credentialListSid** | **String**| The unique id that identifies the credential list to include the created credential. | 
 **password** | **String**| The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;) | 
 **username** | **String**| The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio&#39;s challenge of the initial INVITE. It can be up to 32 characters long. | 

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipCredential

> deleteSipCredential(accountSid, credentialListSid, sid)



Delete a credential resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that contains the desired credentials.
let sid = "sid_example"; // String | The unique id that identifies the resource to delete.
apiInstance.deleteSipCredential(accountSid, credentialListSid, sid, (error, data, response) => {
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
 **credentialListSid** | **String**| The unique id that identifies the credential list that contains the desired credentials. | 
 **sid** | **String**| The unique id that identifies the resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipCredential

> ApiV2010AccountSipSipCredentialListSipCredential fetchSipCredential(accountSid, credentialListSid, sid)



Fetch a single credential.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that contains the desired credential.
let sid = "sid_example"; // String | The unique id that identifies the resource to fetch.
apiInstance.fetchSipCredential(accountSid, credentialListSid, sid, (error, data, response) => {
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
 **credentialListSid** | **String**| The unique id that identifies the credential list that contains the desired credential. | 
 **sid** | **String**| The unique id that identifies the resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipCredential

> ListSipCredentialResponse listSipCredential(accountSid, credentialListSid, opts)



Retrieve a list of credentials.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that contains the desired credentials.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipCredential(accountSid, credentialListSid, opts, (error, data, response) => {
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
 **credentialListSid** | **String**| The unique id that identifies the credential list that contains the desired credentials. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipCredentialResponse**](ListSipCredentialResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSipCredential

> ApiV2010AccountSipSipCredentialListSipCredential updateSipCredential(accountSid, credentialListSid, sid, opts)



Update a credential resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that includes this credential.
let sid = "sid_example"; // String | The unique id that identifies the resource to update.
let opts = {
  'password': "password_example" // String | The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)
};
apiInstance.updateSipCredential(accountSid, credentialListSid, sid, opts, (error, data, response) => {
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
 **credentialListSid** | **String**| The unique id that identifies the credential list that includes this credential. | 
 **sid** | **String**| The unique id that identifies the resource to update. | 
 **password** | **String**| The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;) | [optional] 

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

