# TwilioAccounts.AccountsV1AwsApi

All URIs are relative to *https://accounts.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCredentialAws**](AccountsV1AwsApi.md#createCredentialAws) | **POST** /v1/Credentials/AWS | 
[**deleteCredentialAws**](AccountsV1AwsApi.md#deleteCredentialAws) | **DELETE** /v1/Credentials/AWS/{Sid} | 
[**fetchCredentialAws**](AccountsV1AwsApi.md#fetchCredentialAws) | **GET** /v1/Credentials/AWS/{Sid} | 
[**listCredentialAws**](AccountsV1AwsApi.md#listCredentialAws) | **GET** /v1/Credentials/AWS | 
[**updateCredentialAws**](AccountsV1AwsApi.md#updateCredentialAws) | **POST** /v1/Credentials/AWS/{Sid} | 



## createCredentialAws

> AccountsV1CredentialCredentialAws createCredentialAws(credentials, opts)



Create a new AWS Credential

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1AwsApi();
let credentials = "credentials_example"; // String | A string that contains the AWS access credentials in the format `<AWS_ACCESS_KEY_ID>:<AWS_SECRET_ACCESS_KEY>`. For example, `AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
let opts = {
  'accountSid': "accountSid_example", // String | The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request.
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
};
apiInstance.createCredentialAws(credentials, opts, (error, data, response) => {
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
 **credentials** | **String**| A string that contains the AWS access credentials in the format &#x60;&lt;AWS_ACCESS_KEY_ID&gt;:&lt;AWS_SECRET_ACCESS_KEY&gt;&#x60;. For example, &#x60;AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY&#x60; | 
 **accountSid** | **String**| The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 

### Return type

[**AccountsV1CredentialCredentialAws**](AccountsV1CredentialCredentialAws.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCredentialAws

> deleteCredentialAws(sid)



Delete a Credential from your account

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1AwsApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the AWS resource to delete.
apiInstance.deleteCredentialAws(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the AWS resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCredentialAws

> AccountsV1CredentialCredentialAws fetchCredentialAws(sid)



Fetch the AWS credentials specified by the provided Credential Sid

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1AwsApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the AWS resource to fetch.
apiInstance.fetchCredentialAws(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the AWS resource to fetch. | 

### Return type

[**AccountsV1CredentialCredentialAws**](AccountsV1CredentialCredentialAws.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCredentialAws

> ListCredentialAwsResponse listCredentialAws(opts)



Retrieves a collection of AWS Credentials belonging to the account used to make the request

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1AwsApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCredentialAws(opts, (error, data, response) => {
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

[**ListCredentialAwsResponse**](ListCredentialAwsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCredentialAws

> AccountsV1CredentialCredentialAws updateCredentialAws(sid, opts)



Modify the properties of a given Account

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1AwsApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the AWS resource to update.
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
};
apiInstance.updateCredentialAws(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the AWS resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 

### Return type

[**AccountsV1CredentialCredentialAws**](AccountsV1CredentialCredentialAws.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

