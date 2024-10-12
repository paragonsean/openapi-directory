# TwilioAccounts.AccountsV1PublicKeyApi

All URIs are relative to *https://accounts.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCredentialPublicKey**](AccountsV1PublicKeyApi.md#createCredentialPublicKey) | **POST** /v1/Credentials/PublicKeys | 
[**deleteCredentialPublicKey**](AccountsV1PublicKeyApi.md#deleteCredentialPublicKey) | **DELETE** /v1/Credentials/PublicKeys/{Sid} | 
[**fetchCredentialPublicKey**](AccountsV1PublicKeyApi.md#fetchCredentialPublicKey) | **GET** /v1/Credentials/PublicKeys/{Sid} | 
[**listCredentialPublicKey**](AccountsV1PublicKeyApi.md#listCredentialPublicKey) | **GET** /v1/Credentials/PublicKeys | 
[**updateCredentialPublicKey**](AccountsV1PublicKeyApi.md#updateCredentialPublicKey) | **POST** /v1/Credentials/PublicKeys/{Sid} | 



## createCredentialPublicKey

> AccountsV1CredentialCredentialPublicKey createCredentialPublicKey(publicKey, opts)



Create a new Public Key Credential

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1PublicKeyApi();
let publicKey = "publicKey_example"; // String | A URL encoded representation of the public key. For example, `-----BEGIN PUBLIC KEY-----MIIBIjANB.pa9xQIDAQAB-----END PUBLIC KEY-----`
let opts = {
  'accountSid': "accountSid_example", // String | The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
};
apiInstance.createCredentialPublicKey(publicKey, opts, (error, data, response) => {
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
 **publicKey** | **String**| A URL encoded representation of the public key. For example, &#x60;-----BEGIN PUBLIC KEY-----MIIBIjANB.pa9xQIDAQAB-----END PUBLIC KEY-----&#x60; | 
 **accountSid** | **String**| The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 

### Return type

[**AccountsV1CredentialCredentialPublicKey**](AccountsV1CredentialCredentialPublicKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCredentialPublicKey

> deleteCredentialPublicKey(sid)



Delete a Credential from your account

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1PublicKeyApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PublicKey resource to delete.
apiInstance.deleteCredentialPublicKey(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the PublicKey resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCredentialPublicKey

> AccountsV1CredentialCredentialPublicKey fetchCredentialPublicKey(sid)



Fetch the public key specified by the provided Credential Sid

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1PublicKeyApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PublicKey resource to fetch.
apiInstance.fetchCredentialPublicKey(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the PublicKey resource to fetch. | 

### Return type

[**AccountsV1CredentialCredentialPublicKey**](AccountsV1CredentialCredentialPublicKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCredentialPublicKey

> ListCredentialPublicKeyResponse listCredentialPublicKey(opts)



Retrieves a collection of Public Key Credentials belonging to the account used to make the request

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1PublicKeyApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCredentialPublicKey(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCredentialPublicKeyResponse**](ListCredentialPublicKeyResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCredentialPublicKey

> AccountsV1CredentialCredentialPublicKey updateCredentialPublicKey(sid, opts)



Modify the properties of a given Account

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1PublicKeyApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PublicKey resource to update.
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
};
apiInstance.updateCredentialPublicKey(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the PublicKey resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 

### Return type

[**AccountsV1CredentialCredentialPublicKey**](AccountsV1CredentialCredentialPublicKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

