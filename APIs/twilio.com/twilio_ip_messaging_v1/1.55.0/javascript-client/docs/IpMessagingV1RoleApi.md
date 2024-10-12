# TwilioIpMessaging.IpMessagingV1RoleApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRole**](IpMessagingV1RoleApi.md#createRole) | **POST** /v1/Services/{ServiceSid}/Roles | 
[**deleteRole**](IpMessagingV1RoleApi.md#deleteRole) | **DELETE** /v1/Services/{ServiceSid}/Roles/{Sid} | 
[**fetchRole**](IpMessagingV1RoleApi.md#fetchRole) | **GET** /v1/Services/{ServiceSid}/Roles/{Sid} | 
[**listRole**](IpMessagingV1RoleApi.md#listRole) | **GET** /v1/Services/{ServiceSid}/Roles | 
[**updateRole**](IpMessagingV1RoleApi.md#updateRole) | **POST** /v1/Services/{ServiceSid}/Roles/{Sid} | 



## createRole

> IpMessagingV1ServiceRole createRole(serviceSid, friendlyName, permission, type)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1RoleApi();
let serviceSid = "serviceSid_example"; // String | 
let friendlyName = "friendlyName_example"; // String | 
let permission = ["null"]; // [String] | 
let type = "type_example"; // RoleEnumRoleType | 
apiInstance.createRole(serviceSid, friendlyName, permission, type, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **friendlyName** | **String**|  | 
 **permission** | [**[String]**](String.md)|  | 
 **type** | **RoleEnumRoleType**|  | 

### Return type

[**IpMessagingV1ServiceRole**](IpMessagingV1ServiceRole.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteRole

> deleteRole(serviceSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1RoleApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.deleteRole(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchRole

> IpMessagingV1ServiceRole fetchRole(serviceSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1RoleApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchRole(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **sid** | **String**|  | 

### Return type

[**IpMessagingV1ServiceRole**](IpMessagingV1ServiceRole.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRole

> ListRoleResponse listRole(serviceSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1RoleApi();
let serviceSid = "serviceSid_example"; // String | 
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRole(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRoleResponse**](ListRoleResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRole

> IpMessagingV1ServiceRole updateRole(serviceSid, sid, permission)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1RoleApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
let permission = ["null"]; // [String] | 
apiInstance.updateRole(serviceSid, sid, permission, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **sid** | **String**|  | 
 **permission** | [**[String]**](String.md)|  | 

### Return type

[**IpMessagingV1ServiceRole**](IpMessagingV1ServiceRole.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

