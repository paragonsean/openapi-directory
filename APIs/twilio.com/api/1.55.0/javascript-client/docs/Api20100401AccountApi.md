# TwilioApi.Api20100401AccountApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccount**](Api20100401AccountApi.md#createAccount) | **POST** /2010-04-01/Accounts.json | 
[**fetchAccount**](Api20100401AccountApi.md#fetchAccount) | **GET** /2010-04-01/Accounts/{Sid}.json | 
[**listAccount**](Api20100401AccountApi.md#listAccount) | **GET** /2010-04-01/Accounts.json | 
[**updateAccount**](Api20100401AccountApi.md#updateAccount) | **POST** /2010-04-01/Accounts/{Sid}.json | 



## createAccount

> ApiV2010Account createAccount(opts)



Create a new Twilio Subaccount from the account making the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AccountApi();
let opts = {
  'friendlyName': "friendlyName_example" // String | A human readable description of the account to create, defaults to `SubAccount Created at {YYYY-MM-DD HH:MM meridian}`
};
apiInstance.createAccount(opts, (error, data, response) => {
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
 **friendlyName** | **String**| A human readable description of the account to create, defaults to &#x60;SubAccount Created at {YYYY-MM-DD HH:MM meridian}&#x60; | [optional] 

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchAccount

> ApiV2010Account fetchAccount(sid)



Fetch the account specified by the provided Account Sid

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AccountApi();
let sid = "sid_example"; // String | The Account Sid that uniquely identifies the account to fetch
apiInstance.fetchAccount(sid, (error, data, response) => {
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
 **sid** | **String**| The Account Sid that uniquely identifies the account to fetch | 

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccount

> ListAccountResponse listAccount(opts)



Retrieves a collection of Accounts belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AccountApi();
let opts = {
  'friendlyName': "friendlyName_example", // String | Only return the Account resources with friendly names that exactly match this name.
  'status': "status_example", // AccountEnumStatus | Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAccount(opts, (error, data, response) => {
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
 **friendlyName** | **String**| Only return the Account resources with friendly names that exactly match this name. | [optional] 
 **status** | **AccountEnumStatus**| Only return Account resources with the given status. Can be &#x60;closed&#x60;, &#x60;suspended&#x60; or &#x60;active&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListAccountResponse**](ListAccountResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccount

> ApiV2010Account updateAccount(sid, opts)



Modify the properties of a given Account

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AccountApi();
let sid = "sid_example"; // String | The Account Sid that uniquely identifies the account to update
let opts = {
  'friendlyName': "friendlyName_example", // String | Update the human-readable description of this Account
  'status': "status_example" // AccountEnumStatus | 
};
apiInstance.updateAccount(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Account Sid that uniquely identifies the account to update | 
 **friendlyName** | **String**| Update the human-readable description of this Account | [optional] 
 **status** | **AccountEnumStatus**|  | [optional] 

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

