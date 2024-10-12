# CallFireApiDocumentation.MeApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApiCredential**](MeApi.md#createApiCredential) | **POST** /me/api/credentials | Create api credentials
[**deleteApiCredential**](MeApi.md#deleteApiCredential) | **DELETE** /me/api/credentials/{id} | Delete api credentials
[**disableApiCredentials**](MeApi.md#disableApiCredentials) | **POST** /me/api/credentials/{id}/disable | Disable specified API credentials
[**enableApiCredentials**](MeApi.md#enableApiCredentials) | **POST** /me/api/credentials/{id}/enable | Enable specified API credentials
[**findApiCredentials**](MeApi.md#findApiCredentials) | **GET** /me/api/credentials | Find api credentials
[**getAccount**](MeApi.md#getAccount) | **GET** /me/account | Find account details
[**getApiCredential**](MeApi.md#getApiCredential) | **GET** /me/api/credentials/{id} | Find a specific api credential
[**getBillingPlanUsage**](MeApi.md#getBillingPlanUsage) | **GET** /me/billing/plan-usage | Find plan usage
[**getCallerIds**](MeApi.md#getCallerIds) | **GET** /me/callerids | Find caller ids
[**getCreditUsage**](MeApi.md#getCreditUsage) | **GET** /me/billing/credit-usage | Find credit usage
[**sendVerificationCodeToCallerId**](MeApi.md#sendVerificationCodeToCallerId) | **POST** /me/callerids/{callerid} | Create a caller id
[**verifyCallerId**](MeApi.md#verifyCallerId) | **POST** /me/callerids/{callerid}/verification-code | Verify a caller id



## createApiCredential

> ApiCredential createApiCredential(opts)

Create api credentials

Creates an API credentials for the CallFire API. This endpoint requires full CallFire account credentials to be used, authenticated using Basic Authentication. At the moment user provides only the name for the credentials. The generated credentials can be used to access any CallFire APIs. For authentication use account credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let opts = {
  'apiCredential': new CallFireApiDocumentation.ApiCredential() // ApiCredential | To create the API credentials
};
apiInstance.createApiCredential(opts, (error, data, response) => {
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
 **apiCredential** | [**ApiCredential**](ApiCredential.md)| To create the API credentials | [optional] 

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApiCredential

> deleteApiCredential(id)

Delete api credentials

Deletes a specified API credential. Currently, removes the ability to access the API. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let id = 789; // Number | An id of an API credential
apiInstance.deleteApiCredential(id, (error, data, response) => {
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
 **id** | **Number**| An id of an API credential | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableApiCredentials

> disableApiCredentials(id)

Disable specified API credentials

Disables a specified API credential. Currently, removes the ability to access the API. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let id = 789; // Number | An id of an API credential
apiInstance.disableApiCredentials(id, (error, data, response) => {
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
 **id** | **Number**| An id of an API credential | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableApiCredentials

> enableApiCredentials(id)

Enable specified API credentials

Enables a specified API credential. Currently, adds the ability to access the API. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let id = 789; // Number | An id of an API credential
apiInstance.enableApiCredentials(id, (error, data, response) => {
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
 **id** | **Number**| An id of an API credential | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findApiCredentials

> ApiCredentialPage findApiCredentials(opts)

Find api credentials

Searches for all credentials generated by user. Returns a paged list of the API credentials. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let opts = {
  'name': "name_example", // String | Filter by name
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0 // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
};
apiInstance.findApiCredentials(opts, (error, data, response) => {
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
 **name** | **String**| Filter by name | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]

### Return type

[**ApiCredentialPage**](ApiCredentialPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccount

> Account getAccount(opts)

Find account details

Searches for the user account details. Details include name, email, and basic account permissions. For authentication use api credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getAccount(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApiCredential

> ApiCredential getApiCredential(id, opts)

Find a specific api credential

Returns an API credential instance for a given api credential id. Only ACCOUNT_HOLDER can invoke this API. For authentication use account credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let id = 789; // Number | An id of an API credential
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getApiCredential(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of an API credential | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBillingPlanUsage

> BillingPlanUsage getBillingPlanUsage()

Find plan usage

Searches for the data of a billing plan usage for the user. Returns the data of a billing plan usage for the current month. For authentication use api credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
apiInstance.getBillingPlanUsage((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BillingPlanUsage**](BillingPlanUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallerIds

> CallerIdList getCallerIds()

Find caller ids

Returns a list of verified caller ids. If the number is not shown in the list, then it is not verified. In this case sending of a verification code is required. For authentication use api credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
apiInstance.getCallerIds((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CallerIdList**](CallerIdList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCreditUsage

> CreditUsage getCreditUsage(opts)

Find credit usage

Find credit usage for the user. Returns credits usage for time period specified or if unspecified then total for all time. For authentication use api credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let opts = {
  'intervalBegin': 789, // Number | Beginning of usage period formatted in unix time milliseconds. Example: 1473781817000
  'intervalEnd': 789 // Number | End of usage period formatted in unix time milliseconds. Example: 1473781817000
};
apiInstance.getCreditUsage(opts, (error, data, response) => {
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
 **intervalBegin** | **Number**| Beginning of usage period formatted in unix time milliseconds. Example: 1473781817000 | [optional] 
 **intervalEnd** | **Number**| End of usage period formatted in unix time milliseconds. Example: 1473781817000 | [optional] 

### Return type

[**CreditUsage**](CreditUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendVerificationCodeToCallerId

> sendVerificationCodeToCallerId(callerid)

Create a caller id

Generates and sends a verification code to the phone number provided in the path. The verification code is delivered via a phone call. This code needs to be submitted to the verify caller id API endpoint to complete verification. For authentication use api credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let callerid = "callerid_example"; // String | A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384
apiInstance.sendVerificationCodeToCallerId(callerid, (error, data, response) => {
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
 **callerid** | **String**| A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384 | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## verifyCallerId

> Boolean verifyCallerId(callerid, opts)

Verify a caller id

With the verification code received from the Create caller id endpoint, a call to this endpoint is required to finish verification. For authentication use api credentials.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MeApi();
let callerid = "callerid_example"; // String | A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384
let opts = {
  'callerIdVerificationRequest': new CallFireApiDocumentation.CallerIdVerificationRequest() // CallerIdVerificationRequest | request
};
apiInstance.verifyCallerId(callerid, opts, (error, data, response) => {
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
 **callerid** | **String**| A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384 | 
 **callerIdVerificationRequest** | [**CallerIdVerificationRequest**](CallerIdVerificationRequest.md)| request | [optional] 

### Return type

**Boolean**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

