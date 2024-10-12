# TwilioApi.Api20100401IpAccessControlListApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#createSipIpAccessControlList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json | 
[**deleteSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#deleteSipIpAccessControlList) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json | 
[**fetchSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#fetchSipIpAccessControlList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json | 
[**listSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#listSipIpAccessControlList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json | 
[**updateSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#updateSipIpAccessControlList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json | 



## createSipIpAccessControlList

> ApiV2010AccountSipSipIpAccessControlList createSipIpAccessControlList(accountSid, friendlyName)



Create a new IpAccessControlList resource

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let friendlyName = "friendlyName_example"; // String | A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long.
apiInstance.createSipIpAccessControlList(accountSid, friendlyName, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **friendlyName** | **String**| A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long. | 

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipIpAccessControlList

> deleteSipIpAccessControlList(accountSid, sid)



Delete an IpAccessControlList from the requested account

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
apiInstance.deleteSipIpAccessControlList(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipIpAccessControlList

> ApiV2010AccountSipSipIpAccessControlList fetchSipIpAccessControlList(accountSid, sid)



Fetch a specific instance of an IpAccessControlList

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to fetch.
apiInstance.fetchSipIpAccessControlList(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipIpAccessControlList

> ListSipIpAccessControlListResponse listSipIpAccessControlList(accountSid, opts)



Retrieve a list of IpAccessControlLists that belong to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipIpAccessControlList(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipIpAccessControlListResponse**](ListSipIpAccessControlListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSipIpAccessControlList

> ApiV2010AccountSipSipIpAccessControlList updateSipIpAccessControlList(accountSid, sid, friendlyName)



Rename an IpAccessControlList

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to udpate.
let friendlyName = "friendlyName_example"; // String | A human readable descriptive text, up to 255 characters long.
apiInstance.updateSipIpAccessControlList(accountSid, sid, friendlyName, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to udpate. | 
 **friendlyName** | **String**| A human readable descriptive text, up to 255 characters long. | 

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

