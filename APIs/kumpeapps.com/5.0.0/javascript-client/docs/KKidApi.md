# KumpeAppsApi.KKidApi

All URIs are relative to *https://restapi.kumpeapps.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kkidAllowanceGet**](KKidApi.md#kkidAllowanceGet) | **GET** /kkid/allowance | returns allowance balance and allowance transactions
[**kkidAllowancePost**](KKidApi.md#kkidAllowancePost) | **POST** /kkid/allowance | adds new allowance transaction to kidUserID
[**kkidApnsPost**](KKidApi.md#kkidApnsPost) | **POST** /kkid/apns | subscribes/unsubscribes/registers for apns push notifications
[**kkidChorelistDelete**](KKidApi.md#kkidChorelistDelete) | **DELETE** /kkid/chorelist | deletes chore for given chore id
[**kkidChorelistGet**](KKidApi.md#kkidChorelistGet) | **GET** /kkid/chorelist | returns list of chores for given user
[**kkidChorelistPost**](KKidApi.md#kkidChorelistPost) | **POST** /kkid/chorelist | adds chore for given user
[**kkidChorelistPut**](KKidApi.md#kkidChorelistPut) | **PUT** /kkid/chorelist | updates chore for given chore id
[**kkidMasteruserPost**](KKidApi.md#kkidMasteruserPost) | **POST** /kkid/masteruser | adds new master user account
[**kkidShareGet**](KKidApi.md#kkidShareGet) | **GET** /kkid/share | Create Share Link
[**kkidUserGet**](KKidApi.md#kkidUserGet) | **GET** /kkid/user | Gets user info
[**kkidUserlistDelete**](KKidApi.md#kkidUserlistDelete) | **DELETE** /kkid/userlist | deletes user
[**kkidUserlistGet**](KKidApi.md#kkidUserlistGet) | **GET** /kkid/userlist | returns list of users
[**kkidUserlistPost**](KKidApi.md#kkidUserlistPost) | **POST** /kkid/userlist | adds new child user
[**kkidUserlistPut**](KKidApi.md#kkidUserlistPut) | **PUT** /kkid/userlist | updates user
[**kkidWishlistDelete**](KKidApi.md#kkidWishlistDelete) | **DELETE** /kkid/wishlist | Delete item from wishlist
[**kkidWishlistGet**](KKidApi.md#kkidWishlistGet) | **GET** /kkid/wishlist | Get list of wishlist items
[**kkidWishlistPost**](KKidApi.md#kkidWishlistPost) | **POST** /kkid/wishlist | Add item to kid&#39;s wishlist
[**kkidWishlistPut**](KKidApi.md#kkidWishlistPut) | **PUT** /kkid/wishlist | Update item on kid&#39;s wishlist



## kkidAllowanceGet

> Allowance kkidAllowanceGet(kidUserId, opts)

returns allowance balance and allowance transactions

By passing in the appropriate options, you can view allowance balance and allowance transactions for a given user provided that they are within the masterID account of the authenticated user. 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let kidUserId = 56; // Number | userID of the kid
let opts = {
  'transactionDays': 56 // Number | number of days you wish to search allowance transactions (default is 90 days)
};
apiInstance.kkidAllowanceGet(kidUserId, opts, (error, data, response) => {
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
 **kidUserId** | **Number**| userID of the kid | 
 **transactionDays** | **Number**| number of days you wish to search allowance transactions (default is 90 days) | [optional] 

### Return type

[**Allowance**](Allowance.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidAllowancePost

> Success kkidAllowancePost(kidUserId, amount, description, transactionType)

adds new allowance transaction to kidUserID

By passing in the appropriate options, you can add an allowance transaction to a given user. 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let kidUserId = 56; // Number | userID of the kid
let amount = 3.4; // Number | amount you wish to Add/Subtract (subtract value should be a negative value)
let description = "description_example"; // String | Description (reason) of allowance transaction
let transactionType = "transactionType_example"; // String | Transaction Type (Add/Subtract)
apiInstance.kkidAllowancePost(kidUserId, amount, description, transactionType, (error, data, response) => {
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
 **kidUserId** | **Number**| userID of the kid | 
 **amount** | **Number**| amount you wish to Add/Subtract (subtract value should be a negative value) | 
 **description** | **String**| Description (reason) of allowance transaction | 
 **transactionType** | **String**| Transaction Type (Add/Subtract) | 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidApnsPost

> Success kkidApnsPost(kidUserId, tool, opts)

subscribes/unsubscribes/registers for apns push notifications

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let kidUserId = 56; // Number | userID of the kid
let tool = "tool_example"; // String | tool you wish to talk to
let opts = {
  'token': "token_example", // String | device APNS token (required for register)
  'devicename': "devicename_example", // String | Name of device to associate to token (required for register)
  'title': "title_example", // String | title of APNS message (required for send)
  'message': "message_example", // String | APNS message body (required for send)
  'badge': 56, // Number | Number for badge icon (optional for send)
  'sound': "sound_example", // String | Name of sound file to play for send notification (optional for send)
  'section': "section_example", // String | Notification section name (required for send/subscribe/unsubscribe)
  'priority': "priority_example" // String | Notification section name (optional for send, default is active)
};
apiInstance.kkidApnsPost(kidUserId, tool, opts, (error, data, response) => {
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
 **kidUserId** | **Number**| userID of the kid | 
 **tool** | **String**| tool you wish to talk to | 
 **token** | **String**| device APNS token (required for register) | [optional] 
 **devicename** | **String**| Name of device to associate to token (required for register) | [optional] 
 **title** | **String**| title of APNS message (required for send) | [optional] 
 **message** | **String**| APNS message body (required for send) | [optional] 
 **badge** | **Number**| Number for badge icon (optional for send) | [optional] 
 **sound** | **String**| Name of sound file to play for send notification (optional for send) | [optional] 
 **section** | **String**| Notification section name (required for send/subscribe/unsubscribe) | [optional] 
 **priority** | **String**| Notification section name (optional for send, default is active) | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidChorelistDelete

> Success kkidChorelistDelete(idChoreList)

deletes chore for given chore id

By passing in the appropriate options, you can delete a chore for the given chore id under authenticated user&#39;s master account 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let idChoreList = 56; // Number | id of the chore you wish to delete
apiInstance.kkidChorelistDelete(idChoreList, (error, data, response) => {
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
 **idChoreList** | **Number**| id of the chore you wish to delete | 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidChorelistGet

> Chorelist kkidChorelistGet(opts)

returns list of chores for given user

By passing in the appropriate options, you can search for chores assigned to a given user within the authenticated user&#39;s master account 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let opts = {
  'kidUsername': "kidUsername_example", // String | Username of kid you wish to search
  'day': "day_example", // String | Day of week for chores (Weekly for weekly chores)
  'status': "status_example", // String | Status of Chore to search
  'blockDash': true, // Boolean | Filter results by blockDash parameter
  'optional': true, // Boolean | Filter results by optional parameter
  'canSteal': true, // Boolean | Filter results by canSteal parameter
  'includeCalendar': true // Boolean | include calendar notations (default is false)
};
apiInstance.kkidChorelistGet(opts, (error, data, response) => {
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
 **kidUsername** | **String**| Username of kid you wish to search | [optional] 
 **day** | **String**| Day of week for chores (Weekly for weekly chores) | [optional] 
 **status** | **String**| Status of Chore to search | [optional] 
 **blockDash** | **Boolean**| Filter results by blockDash parameter | [optional] 
 **optional** | **Boolean**| Filter results by optional parameter | [optional] 
 **canSteal** | **Boolean**| Filter results by canSteal parameter | [optional] 
 **includeCalendar** | **Boolean**| include calendar notations (default is false) | [optional] 

### Return type

[**Chorelist**](Chorelist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidChorelistPost

> Success kkidChorelistPost(kidUsername, choreName, opts)

adds chore for given user

By passing in the appropriate options, you can add a chore to given kid username under authenticated user&#39;s master account 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let kidUsername = "kidUsername_example"; // String | username of kid to assign the chore to.
let choreName = "choreName_example"; // String | name of chore
let opts = {
  'day': "day_example", // String | day of week (Monday, Tuesday....) for the chore. For weekly chores put Weekly or leave blank
  'nfcTag': "nfcTag_example", // String | text field of nfc tag required to check off chore
  'status': "status_example", // String | status of chore (default is todo)
  'choreDescription': "choreDescription_example", // String | optional chore description
  'choreNumber': 56, // Number | number priority of chore (default is 5)
  'blockDash': true, // Boolean | block dash option on this chore
  'oneTime': true, // Boolean | mark as one time chore (does not repeat each week)
  'extraAllowance': 56, // Number | ammount of allowance added at end of week for completing this chore
  'optional': true, // Boolean | mark as optional chore
  'reassignable': true, // Boolean | mark as reassignable (default is true)
  'canSteal': true, // Boolean | mark as sibling can steal chore
  'startDate': "startDate_example", // String | date (yyyy-mm-dd) that you wish the chore to start showing up. (default is today)
  'notes': "notes_example", // String | notes added to chore (visable only on reports, kids do not see this note, this is mostly just for the developer)
  'requireObjectDetection': true, // Boolean | require use of camera to detect object detection tag order to check off chore
  'objectDetectionTag': "objectDetectionTag_example", // String | tag for object detection to search for (required if requireObjectDetection is true)
  'updatedByAutomation': true, // Boolean | true if chore updated via API from an Automation System
  'aiIcon': "aiIcon_example", // String | Notes if AI Icons should be used (n for no, y for yes, e for yes- error)
  'isCalendar': true // Boolean | True if this is a calendar note instead of a chore.
};
apiInstance.kkidChorelistPost(kidUsername, choreName, opts, (error, data, response) => {
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
 **kidUsername** | **String**| username of kid to assign the chore to. | 
 **choreName** | **String**| name of chore | 
 **day** | **String**| day of week (Monday, Tuesday....) for the chore. For weekly chores put Weekly or leave blank | [optional] 
 **nfcTag** | **String**| text field of nfc tag required to check off chore | [optional] 
 **status** | **String**| status of chore (default is todo) | [optional] 
 **choreDescription** | **String**| optional chore description | [optional] 
 **choreNumber** | **Number**| number priority of chore (default is 5) | [optional] 
 **blockDash** | **Boolean**| block dash option on this chore | [optional] 
 **oneTime** | **Boolean**| mark as one time chore (does not repeat each week) | [optional] 
 **extraAllowance** | **Number**| ammount of allowance added at end of week for completing this chore | [optional] 
 **optional** | **Boolean**| mark as optional chore | [optional] 
 **reassignable** | **Boolean**| mark as reassignable (default is true) | [optional] 
 **canSteal** | **Boolean**| mark as sibling can steal chore | [optional] 
 **startDate** | **String**| date (yyyy-mm-dd) that you wish the chore to start showing up. (default is today) | [optional] 
 **notes** | **String**| notes added to chore (visable only on reports, kids do not see this note, this is mostly just for the developer) | [optional] 
 **requireObjectDetection** | **Boolean**| require use of camera to detect object detection tag order to check off chore | [optional] 
 **objectDetectionTag** | **String**| tag for object detection to search for (required if requireObjectDetection is true) | [optional] 
 **updatedByAutomation** | **Boolean**| true if chore updated via API from an Automation System | [optional] 
 **aiIcon** | **String**| Notes if AI Icons should be used (n for no, y for yes, e for yes- error) | [optional] 
 **isCalendar** | **Boolean**| True if this is a calendar note instead of a chore. | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidChorelistPut

> Success kkidChorelistPut(idChoreList, opts)

updates chore for given chore id

By passing in the appropriate options, you can update the fields of a specific core within the authenticated user&#39;s master account 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let idChoreList = 56; // Number | id number of chore you wish to update
let opts = {
  'status': "status_example", // String | new status of chore
  'stolen': true, // Boolean | mark chore as stolen by sibling
  'stolenBy': "stolenBy_example", // String | username of sibling that stole the chore (required if stolen is true)
  'nfcTag': "nfcTag_example", // String | text field of NFC tag that is required to be scanned to check off this chore (normally null)
  'notes': "notes_example", // String | notes field for chore
  'latitude': 56, // Number | GPS latitude of where the chore was marked
  'longitude': 56, // Number | GPS longitude of where the chore was marked
  'altitude': 56, // Number | GPS altitude of where the chore was marked
  'updatedByAutomation': true, // Boolean | true if updated via API by automation system
  'whereDay': "whereDay_example", // String | Where day equals...
  'whereStatus': "whereStatus_example", // String | Where status equals...
  'whereName': "whereName_example" // String | Where chore name equals...
};
apiInstance.kkidChorelistPut(idChoreList, opts, (error, data, response) => {
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
 **idChoreList** | **Number**| id number of chore you wish to update | 
 **status** | **String**| new status of chore | [optional] 
 **stolen** | **Boolean**| mark chore as stolen by sibling | [optional] 
 **stolenBy** | **String**| username of sibling that stole the chore (required if stolen is true) | [optional] 
 **nfcTag** | **String**| text field of NFC tag that is required to be scanned to check off this chore (normally null) | [optional] 
 **notes** | **String**| notes field for chore | [optional] 
 **latitude** | **Number**| GPS latitude of where the chore was marked | [optional] 
 **longitude** | **Number**| GPS longitude of where the chore was marked | [optional] 
 **altitude** | **Number**| GPS altitude of where the chore was marked | [optional] 
 **updatedByAutomation** | **Boolean**| true if updated via API by automation system | [optional] 
 **whereDay** | **String**| Where day equals... | [optional] 
 **whereStatus** | **String**| Where status equals... | [optional] 
 **whereName** | **String**| Where chore name equals... | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidMasteruserPost

> AddUserResponse kkidMasteruserPost(username, password, email, firstName, lastName)

adds new master user account

By passing in the appropriate variables this method creates a new user with master account access. (The use of this method is restricted to Superusers ONLY) 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let username = "username_example"; // String | username of user to create
let password = "password_example"; // String | password of user to create
let email = "email_example"; // String | email address of user to create
let firstName = "firstName_example"; // String | First Name of user to create
let lastName = "lastName_example"; // String | Last Name of user to create
apiInstance.kkidMasteruserPost(username, password, email, firstName, lastName, (error, data, response) => {
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
 **username** | **String**| username of user to create | 
 **password** | **String**| password of user to create | 
 **email** | **String**| email address of user to create | 
 **firstName** | **String**| First Name of user to create | 
 **lastName** | **String**| Last Name of user to create | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidShareGet

> Model201Share kkidShareGet(linkUserId, link, scope, opts)

Create Share Link

Create share link

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let linkUserId = "linkUserId_example"; // String | User ID that the link should be authenticated to
let link = "link_example"; // String | Link to share
let scope = "scope_example"; // String | Authentication scope for link
let opts = {
  'scope2': "scope2_example", // String | Authentication scope for link
  'scope3': "scope3_example", // String | Authentication scope for link
  'scope4': "scope4_example" // String | Authentication scope for link
};
apiInstance.kkidShareGet(linkUserId, link, scope, opts, (error, data, response) => {
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
 **linkUserId** | **String**| User ID that the link should be authenticated to | 
 **link** | **String**| Link to share | 
 **scope** | **String**| Authentication scope for link | 
 **scope2** | **String**| Authentication scope for link | [optional] 
 **scope3** | **String**| Authentication scope for link | [optional] 
 **scope4** | **String**| Authentication scope for link | [optional] 

### Return type

[**Model201Share**](Model201Share.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidUserGet

> Userlist kkidUserGet(opts)

Gets user info

Gets user info for authenticated user

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let opts = {
  'enableBool': true // Boolean | Use bool values instead of Int 0/1
};
apiInstance.kkidUserGet(opts, (error, data, response) => {
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
 **enableBool** | **Boolean**| Use bool values instead of Int 0/1 | [optional] 

### Return type

[**Userlist**](Userlist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidUserlistDelete

> kkidUserlistDelete(userID)

deletes user

By passing in the appropriate variables this method deletes the specified user. (This function is restricted to Superusers ONLY) 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let userID = 56; // Number | userID of the user you wish to delete
apiInstance.kkidUserlistDelete(userID, (error, data, response) => {
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
 **userID** | **Number**| userID of the user you wish to delete | 

### Return type

null (empty response body)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidUserlistGet

> Userlist kkidUserlistGet(opts)

returns list of users

By passing in the appropriate options, you can search for users within the authenticated user&#39;s master account 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let opts = {
  'isChild': true, // Boolean | Filter Search by isChild flag
  'isActive': true, // Boolean | Filter Search by isActive flag
  'isAdmin': true, // Boolean | Filter Search by isAdmin flag
  'enableAllowance': true, // Boolean | Filter Search by enableAllowance flag
  'enableChores': true, // Boolean | Filter Search by enableChores flag
  'userID': 56, // Number | userID of user to search
  'username': "username_example", // String | Username of user to search
  'email': "email_example" // String | Email address of user to search
};
apiInstance.kkidUserlistGet(opts, (error, data, response) => {
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
 **isChild** | **Boolean**| Filter Search by isChild flag | [optional] 
 **isActive** | **Boolean**| Filter Search by isActive flag | [optional] 
 **isAdmin** | **Boolean**| Filter Search by isAdmin flag | [optional] 
 **enableAllowance** | **Boolean**| Filter Search by enableAllowance flag | [optional] 
 **enableChores** | **Boolean**| Filter Search by enableChores flag | [optional] 
 **userID** | **Number**| userID of user to search | [optional] 
 **username** | **String**| Username of user to search | [optional] 
 **email** | **String**| Email address of user to search | [optional] 

### Return type

[**Userlist**](Userlist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidUserlistPost

> AddUserResponse kkidUserlistPost(username, password, email, firstName, lastName)

adds new child user

By passing in the appropriate variables this method creates a new user and assigns it to the master account of the authenticated user. By default this user will have chores and allowance access. 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let username = "username_example"; // String | username of user to create
let password = "password_example"; // String | password of user to create
let email = "email_example"; // String | email address of user to create
let firstName = "firstName_example"; // String | First Name of user to create
let lastName = "lastName_example"; // String | Last Name of user to create
apiInstance.kkidUserlistPost(username, password, email, firstName, lastName, (error, data, response) => {
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
 **username** | **String**| username of user to create | 
 **password** | **String**| password of user to create | 
 **email** | **String**| email address of user to create | 
 **firstName** | **String**| First Name of user to create | 
 **lastName** | **String**| Last Name of user to create | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidUserlistPut

> AddUserResponse kkidUserlistPut(userID, username, email, firstName, lastName, opts)

updates user

By passing in the appropriate variables this method updates the user&#39;s profile 

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let userID = 56; // Number | userID of the user you wish to update
let username = "username_example"; // String | username of user to create
let email = "email_example"; // String | email address of user to create
let firstName = "firstName_example"; // String | First Name of user to create
let lastName = "lastName_example"; // String | Last Name of user to create
let opts = {
  'emoji': "emoji_example", // String | emoji character for user
  'tmdbKey': "tmdbKey_example", // String | User's TMdB Session Key
  'enableWishList': true, // Boolean | set status of Wish List module enabled
  'enableChores': true, // Boolean | set status of chores module enabled
  'enableAllowance': true, // Boolean | set status of allowance module enabled
  'enableAdmin': true, // Boolean | set status of isAdmin
  'enableTmdb': true, // Boolean | set status of enableTmdb (movie and tv search)
  'enableObjectDetection': true // Boolean | set status of enableObjectDetection
};
apiInstance.kkidUserlistPut(userID, username, email, firstName, lastName, opts, (error, data, response) => {
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
 **userID** | **Number**| userID of the user you wish to update | 
 **username** | **String**| username of user to create | 
 **email** | **String**| email address of user to create | 
 **firstName** | **String**| First Name of user to create | 
 **lastName** | **String**| Last Name of user to create | 
 **emoji** | **String**| emoji character for user | [optional] 
 **tmdbKey** | **String**| User&#39;s TMdB Session Key | [optional] 
 **enableWishList** | **Boolean**| set status of Wish List module enabled | [optional] 
 **enableChores** | **Boolean**| set status of chores module enabled | [optional] 
 **enableAllowance** | **Boolean**| set status of allowance module enabled | [optional] 
 **enableAdmin** | **Boolean**| set status of isAdmin | [optional] 
 **enableTmdb** | **Boolean**| set status of enableTmdb (movie and tv search) | [optional] 
 **enableObjectDetection** | **Boolean**| set status of enableObjectDetection | [optional] 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidWishlistDelete

> Success kkidWishlistDelete(wishId)

Delete item from wishlist

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let wishId = 56; // Number | ID of wishlist item to delete
apiInstance.kkidWishlistDelete(wishId, (error, data, response) => {
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
 **wishId** | **Number**| ID of wishlist item to delete | 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidWishlistGet

> Wishlist kkidWishlistGet(opts)

Get list of wishlist items

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let opts = {
  'kidUserId': 56 // Number | userID of the kid
};
apiInstance.kkidWishlistGet(opts, (error, data, response) => {
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
 **kidUserId** | **Number**| userID of the kid | [optional] 

### Return type

[**Wishlist**](Wishlist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidWishlistPost

> Success kkidWishlistPost(kidUserId, title, opts)

Add item to kid&#39;s wishlist

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let kidUserId = 56; // Number | userID of the kid
let title = "title_example"; // String | Item title
let opts = {
  'description': "description_example", // String | Item Description
  'priority': 56, // Number | Item Priority
  'link': "link_example" // String | URL Link to item
};
apiInstance.kkidWishlistPost(kidUserId, title, opts, (error, data, response) => {
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
 **kidUserId** | **Number**| userID of the kid | 
 **title** | **String**| Item title | 
 **description** | **String**| Item Description | [optional] 
 **priority** | **Number**| Item Priority | [optional] 
 **link** | **String**| URL Link to item | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kkidWishlistPut

> Success kkidWishlistPut(wishId, opts)

Update item on kid&#39;s wishlist

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.KKidApi();
let wishId = 56; // Number | Wish list item ID to update
let opts = {
  'title': "title_example", // String | Item title
  'description': "description_example", // String | Item Description
  'priority': 56, // Number | Item Priority
  'link': "link_example" // String | URL Link to item
};
apiInstance.kkidWishlistPut(wishId, opts, (error, data, response) => {
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
 **wishId** | **Number**| Wish list item ID to update | 
 **title** | **String**| Item title | [optional] 
 **description** | **String**| Item Description | [optional] 
 **priority** | **Number**| Item Priority | [optional] 
 **link** | **String**| URL Link to item | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

