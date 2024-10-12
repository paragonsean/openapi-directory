# WwwZoomconnectCom.AccountApi

All URIs are relative to *https://www.zoomconnect.com/app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRestV1AccountUserPut**](AccountApi.md#apiRestV1AccountUserPut) | **PUT** /api/rest/v1/account/user | create
[**apiRestV1AccountUserUserIdPost**](AccountApi.md#apiRestV1AccountUserUserIdPost) | **POST** /api/rest/v1/account/user/{userId} | update
[**getBalance**](AccountApi.md#getBalance) | **GET** /api/rest/v1/account/balance | balance
[**getStatistics**](AccountApi.md#getStatistics) | **GET** /api/rest/v1/account/statistics | statistics
[**getUser**](AccountApi.md#getUser) | **GET** /api/rest/v1/account/user/{userId} | getUser
[**search**](AccountApi.md#search) | **GET** /api/rest/v1/account/user | search
[**transfer**](AccountApi.md#transfer) | **POST** /api/rest/v1/account/transfer | transfer



## apiRestV1AccountUserPut

> WebServiceUser apiRestV1AccountUserPut(opts)

create

Creates a new sub-account in your team. The following fields are required &lt;i&gt;firstname, lastname, email address, contact number&lt;/i&gt; and &lt;i&gt;password.&lt;/i&gt;

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.AccountApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceUser() // WebServiceUser | request
};
apiInstance.apiRestV1AccountUserPut(opts, (error, data, response) => {
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
 **body** | [**WebServiceUser**](WebServiceUser.md)| request | [optional] 

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## apiRestV1AccountUserUserIdPost

> WebServiceUser apiRestV1AccountUserUserIdPost(userId, opts)

update

Updates a sub-account in your team. The following fields can be updated &lt;i&gt;firstname, lastname, contact number&lt;/i&gt; and &lt;i&gt;password.&lt;/i&gt;

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.AccountApi();
let userId = 789; // Number | userId
let opts = {
  'body': new WwwZoomconnectCom.WebServiceUser() // WebServiceUser | request
};
apiInstance.apiRestV1AccountUserUserIdPost(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| userId | 
 **body** | [**WebServiceUser**](WebServiceUser.md)| request | [optional] 

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## getBalance

> WebServiceAccount getBalance()

balance

Returns your account&#39;s credit balance

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.AccountApi();
apiInstance.getBalance((error, data, response) => {
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

[**WebServiceAccount**](WebServiceAccount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getStatistics

> WebServiceAccountStatistics getStatistics(opts)

statistics

Returns data from the statistics report. Note that by default the statistics shown are based on the number of messages, use the calculateCreditValue should you wish to calculate the statistics based on credit value.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.AccountApi();
let opts = {
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: dd-MM-yyyy
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: dd-MM-yyyy
  'userEmailAddress': "userEmailAddress_example", // String | optional email address of user to return statistics for a single user, default is to return statistics for all users if administrator, or statistics for your own account if not an administrator
  'campaign': "campaign_example", // String | optional campaign name
  'includeRefundedAndOptout': true, // Boolean | optionally include refunded and optout counts, default is false
  'calculateCreditValue': true // Boolean | optionally calculate using credit value rather than message count, default is false
};
apiInstance.getStatistics(opts, (error, data, response) => {
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
 **from** | **Date**| date format: dd-MM-yyyy | [optional] 
 **to** | **Date**| date format: dd-MM-yyyy | [optional] 
 **userEmailAddress** | **String**| optional email address of user to return statistics for a single user, default is to return statistics for all users if administrator, or statistics for your own account if not an administrator | [optional] 
 **campaign** | **String**| optional campaign name | [optional] 
 **includeRefundedAndOptout** | **Boolean**| optionally include refunded and optout counts, default is false | [optional] 
 **calculateCreditValue** | **Boolean**| optionally calculate using credit value rather than message count, default is false | [optional] 

### Return type

[**WebServiceAccountStatistics**](WebServiceAccountStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getUser

> WebServiceUser getUser(userId)

getUser

Gets a user from a given user id

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.AccountApi();
let userId = 789; // Number | userId
apiInstance.getUser(userId, (error, data, response) => {
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
 **userId** | **Number**| userId | 

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## search

> WebServiceUsers search(searchEmail)

search

Find a user for a particular email address

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.AccountApi();
let searchEmail = "searchEmail_example"; // String | search by email address
apiInstance.search(searchEmail, (error, data, response) => {
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
 **searchEmail** | **String**| search by email address | 

### Return type

[**WebServiceUsers**](WebServiceUsers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## transfer

> WebServiceUser transfer(opts)

transfer

Transfers credits between two users in the same team. The &lt;i&gt;account email address&lt;/i&gt; fields as well as the &lt;i&gt;number of credits to transfer&lt;/i&gt; are required. 

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.AccountApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceTransferCreditsRequest() // WebServiceTransferCreditsRequest | request
};
apiInstance.transfer(opts, (error, data, response) => {
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
 **body** | [**WebServiceTransferCreditsRequest**](WebServiceTransferCreditsRequest.md)| request | [optional] 

### Return type

[**WebServiceUser**](WebServiceUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

