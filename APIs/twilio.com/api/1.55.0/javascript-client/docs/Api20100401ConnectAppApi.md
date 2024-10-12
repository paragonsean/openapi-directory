# TwilioApi.Api20100401ConnectAppApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteConnectApp**](Api20100401ConnectAppApi.md#deleteConnectApp) | **DELETE** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json | 
[**fetchConnectApp**](Api20100401ConnectAppApi.md#fetchConnectApp) | **GET** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json | 
[**listConnectApp**](Api20100401ConnectAppApi.md#listConnectApp) | **GET** /2010-04-01/Accounts/{AccountSid}/ConnectApps.json | 
[**updateConnectApp**](Api20100401ConnectAppApi.md#updateConnectApp) | **POST** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json | 



## deleteConnectApp

> deleteConnectApp(accountSid, sid)



Delete an instance of a connect-app

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ConnectAppApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
apiInstance.deleteConnectApp(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConnectApp

> ApiV2010AccountConnectApp fetchConnectApp(accountSid, sid)



Fetch an instance of a connect-app

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ConnectAppApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
apiInstance.fetchConnectApp(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch. | 

### Return type

[**ApiV2010AccountConnectApp**](ApiV2010AccountConnectApp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConnectApp

> ListConnectAppResponse listConnectApp(accountSid, opts)



Retrieve a list of connect-apps belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ConnectAppApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConnectApp(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConnectAppResponse**](ListConnectAppResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConnectApp

> ApiV2010AccountConnectApp updateConnectApp(accountSid, sid, opts)



Update a connect-app with the specified parameters

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ConnectAppApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
let opts = {
  'authorizeRedirectUrl': "authorizeRedirectUrl_example", // String | The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App.
  'companyName': "companyName_example", // String | The company name to set for the Connect App.
  'deauthorizeCallbackMethod': "deauthorizeCallbackMethod_example", // String | The HTTP method to use when calling `deauthorize_callback_url`.
  'deauthorizeCallbackUrl': "deauthorizeCallbackUrl_example", // String | The URL to call using the `deauthorize_callback_method` to de-authorize the Connect App.
  'description': "description_example", // String | A description of the Connect App.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'homepageUrl': "homepageUrl_example", // String | A public URL where users can obtain more information about this Connect App.
  'permissions': ["null"] // [ConnectAppEnumPermission] | A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: `get-all` and `post-all`.
};
apiInstance.updateConnectApp(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ConnectApp resource to update. | 
 **authorizeRedirectUrl** | **String**| The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App. | [optional] 
 **companyName** | **String**| The company name to set for the Connect App. | [optional] 
 **deauthorizeCallbackMethod** | **String**| The HTTP method to use when calling &#x60;deauthorize_callback_url&#x60;. | [optional] 
 **deauthorizeCallbackUrl** | **String**| The URL to call using the &#x60;deauthorize_callback_method&#x60; to de-authorize the Connect App. | [optional] 
 **description** | **String**| A description of the Connect App. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **homepageUrl** | **String**| A public URL where users can obtain more information about this Connect App. | [optional] 
 **permissions** | [**[ConnectAppEnumPermission]**](ConnectAppEnumPermission.md)| A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: &#x60;get-all&#x60; and &#x60;post-all&#x60;. | [optional] 

### Return type

[**ApiV2010AccountConnectApp**](ApiV2010AccountConnectApp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

