# TwilioApi.Api20100401IpAddressApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipIpAddress**](Api20100401IpAddressApi.md#createSipIpAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json | 
[**deleteSipIpAddress**](Api20100401IpAddressApi.md#deleteSipIpAddress) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json | 
[**fetchSipIpAddress**](Api20100401IpAddressApi.md#fetchSipIpAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json | 
[**listSipIpAddress**](Api20100401IpAddressApi.md#listSipIpAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json | 
[**updateSipIpAddress**](Api20100401IpAddressApi.md#updateSipIpAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json | 



## createSipIpAddress

> ApiV2010AccountSipSipIpAccessControlListSipIpAddress createSipIpAddress(accountSid, ipAccessControlListSid, friendlyName, ipAddress, opts)



Create a new IpAddress resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAddressApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid with which to associate the created IpAddress resource.
let friendlyName = "friendlyName_example"; // String | A human readable descriptive text for this resource, up to 255 characters long.
let ipAddress = "ipAddress_example"; // String | An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
let opts = {
  'cidrPrefixLength': 56 // Number | An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
};
apiInstance.createSipIpAddress(accountSid, ipAccessControlListSid, friendlyName, ipAddress, opts, (error, data, response) => {
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
 **ipAccessControlListSid** | **String**| The IpAccessControlList Sid with which to associate the created IpAddress resource. | 
 **friendlyName** | **String**| A human readable descriptive text for this resource, up to 255 characters long. | 
 **ipAddress** | **String**| An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. | 
 **cidrPrefixLength** | **Number**| An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. | [optional] 

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipIpAddress

> deleteSipIpAddress(accountSid, ipAccessControlListSid, sid)



Delete an IpAddress resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAddressApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to delete.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
apiInstance.deleteSipIpAddress(accountSid, ipAccessControlListSid, sid, (error, data, response) => {
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
 **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to delete. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipIpAddress

> ApiV2010AccountSipSipIpAccessControlListSipIpAddress fetchSipIpAddress(accountSid, ipAccessControlListSid, sid)



Read one IpAddress resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAddressApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the IpAddress resource to fetch.
apiInstance.fetchSipIpAddress(accountSid, ipAccessControlListSid, sid, (error, data, response) => {
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
 **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to fetch. | 
 **sid** | **String**| A 34 character string that uniquely identifies the IpAddress resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipIpAddress

> ListSipIpAddressResponse listSipIpAddress(accountSid, ipAccessControlListSid, opts)



Read multiple IpAddress resources.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAddressApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipIpAddress(accountSid, ipAccessControlListSid, opts, (error, data, response) => {
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
 **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipIpAddressResponse**](ListSipIpAddressResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSipIpAddress

> ApiV2010AccountSipSipIpAccessControlListSipIpAddress updateSipIpAddress(accountSid, ipAccessControlListSid, sid, opts)



Update an IpAddress resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAddressApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The IpAccessControlList Sid that identifies the IpAddress resources to update.
let sid = "sid_example"; // String | A 34 character string that identifies the IpAddress resource to update.
let opts = {
  'cidrPrefixLength': 56, // Number | An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
  'friendlyName': "friendlyName_example", // String | A human readable descriptive text for this resource, up to 255 characters long.
  'ipAddress': "ipAddress_example" // String | An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
};
apiInstance.updateSipIpAddress(accountSid, ipAccessControlListSid, sid, opts, (error, data, response) => {
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
 **ipAccessControlListSid** | **String**| The IpAccessControlList Sid that identifies the IpAddress resources to update. | 
 **sid** | **String**| A 34 character string that identifies the IpAddress resource to update. | 
 **cidrPrefixLength** | **Number**| An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. | [optional] 
 **friendlyName** | **String**| A human readable descriptive text for this resource, up to 255 characters long. | [optional] 
 **ipAddress** | **String**| An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. | [optional] 

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

