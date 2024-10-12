# CallControlApi.EnterpriseApiApi

All URIs are relative to *https://api.callcontrol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseApiGetUser**](EnterpriseApiApi.md#enterpriseApiGetUser) | **GET** /api/2015-11-01/Enterprise/GetUser/{phoneNumber} | Enterprise  GET: GetUser  Returns the current information from the user;  try 12066194123 as demo
[**enterpriseApiShouldBlock**](EnterpriseApiApi.md#enterpriseApiShouldBlock) | **GET** /api/2015-11-01/Enterprise/ShouldBlock/{phoneNumber}/{userPhoneNumber} | Enterprise  GET: ShouldBlock  Simple Enteprise which returns a call block proceed decision.
[**enterpriseApiUpsertUser**](EnterpriseApiApi.md#enterpriseApiUpsertUser) | **POST** /api/2015-11-01/Enterprise/UpsertUser | UpsertUser: insert or update all properties from a user  PhoneNumber  WhiteList (list of phone numbers to whitelist)  BlackList (list of phone numbers to blacklist)  QuietHourList (list of quiet hour objects)  UseCommunityBlacklist (enable / disable community blacklist) default true  BreakThroughQhWithMultipleCalls (break through quiet hours with two calls in 3 minutes)  WhiteListBreaksQh (break through quiet hours for whitelist)



## enterpriseApiGetUser

> CallControlUser enterpriseApiGetUser(phoneNumber)

Enterprise  GET: GetUser  Returns the current information from the user;  try 12066194123 as demo

### Example

```javascript
import CallControlApi from 'call_control_api';

let apiInstance = new CallControlApi.EnterpriseApiApi();
let phoneNumber = "phoneNumber_example"; // String | 
apiInstance.enterpriseApiGetUser(phoneNumber, (error, data, response) => {
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
 **phoneNumber** | **String**|  | 

### Return type

[**CallControlUser**](CallControlUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## enterpriseApiShouldBlock

> String enterpriseApiShouldBlock(phoneNumber, userPhoneNumber)

Enterprise  GET: ShouldBlock  Simple Enteprise which returns a call block proceed decision.

This returns information required to perform basic call blocking behaviors              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

### Example

```javascript
import CallControlApi from 'call_control_api';

let apiInstance = new CallControlApi.EnterpriseApiApi();
let phoneNumber = "phoneNumber_example"; // String | phone number to search
let userPhoneNumber = "userPhoneNumber_example"; // String | (OPTIONAL) phone number of user to look up block rules
apiInstance.enterpriseApiShouldBlock(phoneNumber, userPhoneNumber, (error, data, response) => {
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
 **phoneNumber** | **String**| phone number to search | 
 **userPhoneNumber** | **String**| (OPTIONAL) phone number of user to look up block rules | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## enterpriseApiUpsertUser

> Object enterpriseApiUpsertUser(user)

UpsertUser: insert or update all properties from a user  PhoneNumber  WhiteList (list of phone numbers to whitelist)  BlackList (list of phone numbers to blacklist)  QuietHourList (list of quiet hour objects)  UseCommunityBlacklist (enable / disable community blacklist) default true  BreakThroughQhWithMultipleCalls (break through quiet hours with two calls in 3 minutes)  WhiteListBreaksQh (break through quiet hours for whitelist)

### Example

```javascript
import CallControlApi from 'call_control_api';

let apiInstance = new CallControlApi.EnterpriseApiApi();
let user = new CallControlApi.CallControlUser(); // CallControlUser | [FromBody] User               <remarks>This returns information required to perform basic call blocking behaviors.  The demo key will return ok, but will not save the data.<br /></remarks>
apiInstance.enterpriseApiUpsertUser(user, (error, data, response) => {
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
 **user** | [**CallControlUser**](CallControlUser.md)| [FromBody] User               &lt;remarks&gt;This returns information required to perform basic call blocking behaviors.  The demo key will return ok, but will not save the data.&lt;br /&gt;&lt;/remarks&gt; | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

