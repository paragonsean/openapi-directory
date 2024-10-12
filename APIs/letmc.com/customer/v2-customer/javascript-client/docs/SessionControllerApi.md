# AgentOsApiV2CustomerLoginCallGroup.SessionControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessionControllerChangePassword**](SessionControllerApi.md#sessionControllerChangePassword) | **PUT** /v2/customer/{shortName}/session/password | Change the password of a customer given their existing and new password.
[**sessionControllerCreateLandlordLogin**](SessionControllerApi.md#sessionControllerCreateLandlordLogin) | **POST** /v2/customer/{shortName}/session/createlandlordlogin | Send a request to the in-tray to create a landlord login.
[**sessionControllerGetSessionInfo**](SessionControllerApi.md#sessionControllerGetSessionInfo) | **GET** /v2/customer/{shortName}/session | Gets information about the currently logged on customer.
[**sessionControllerLogin**](SessionControllerApi.md#sessionControllerLogin) | **POST** /v2/customer/{shortName}/session | Login as a customer given their username and password.
[**sessionControllerLogout**](SessionControllerApi.md#sessionControllerLogout) | **DELETE** /v2/customer/{shortName}/session | Logout a customer previously logged in via the Login endpoint.
[**sessionControllerResetPassword**](SessionControllerApi.md#sessionControllerResetPassword) | **POST** /v2/customer/{shortName}/session/resetpassword | Reset the customer&#39;s password. An email will be sent out to reset.



## sessionControllerChangePassword

> sessionControllerChangePassword(shortName, token, oldPassword, newPassword)

Change the password of a customer given their existing and new password.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.SessionControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let oldPassword = "oldPassword_example"; // String | The customer's existing password.
let newPassword = "newPassword_example"; // String | The customer's new password.
apiInstance.sessionControllerChangePassword(shortName, token, oldPassword, newPassword, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **oldPassword** | **String**| The customer&#39;s existing password. | 
 **newPassword** | **String**| The customer&#39;s new password. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sessionControllerCreateLandlordLogin

> sessionControllerCreateLandlordLogin(shortName, email, title, forename, surname, propertyAddress, contactDetails, opts)

Send a request to the in-tray to create a landlord login.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.SessionControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let email = "email_example"; // String | The email address of the landlord
let title = "title_example"; // String | The title of the landlord
let forename = "forename_example"; // String | The forename of the landlord
let surname = "surname_example"; // String | The surname of the landlord
let propertyAddress = "propertyAddress_example"; // String | Address of the property linked to the landlord
let contactDetails = "contactDetails_example"; // String | Contact details of the landlord
let opts = {
  'branchID': "branchID_example" // String | (Optional) The branch ID linked to the login. This will determine which in tray the request display in
};
apiInstance.sessionControllerCreateLandlordLogin(shortName, email, title, forename, surname, propertyAddress, contactDetails, opts, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **email** | **String**| The email address of the landlord | 
 **title** | **String**| The title of the landlord | 
 **forename** | **String**| The forename of the landlord | 
 **surname** | **String**| The surname of the landlord | 
 **propertyAddress** | **String**| Address of the property linked to the landlord | 
 **contactDetails** | **String**| Contact details of the landlord | 
 **branchID** | **String**| (Optional) The branch ID linked to the login. This will determine which in tray the request display in | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sessionControllerGetSessionInfo

> String sessionControllerGetSessionInfo(shortName, token)

Gets information about the currently logged on customer.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.SessionControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.sessionControllerGetSessionInfo(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## sessionControllerLogin

> String sessionControllerLogin(shortName, username, password)

Login as a customer given their username and password.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.SessionControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let username = "username_example"; // String | The user's username.
let password = "password_example"; // String | The user's password.
apiInstance.sessionControllerLogin(shortName, username, password, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **username** | **String**| The user&#39;s username. | 
 **password** | **String**| The user&#39;s password. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## sessionControllerLogout

> sessionControllerLogout(shortName, token)

Logout a customer previously logged in via the Login endpoint.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.SessionControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.sessionControllerLogout(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sessionControllerResetPassword

> sessionControllerResetPassword(shortName, email)

Reset the customer&#39;s password. An email will be sent out to reset.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.SessionControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let email = "email_example"; // String | The login Email Address.
apiInstance.sessionControllerResetPassword(shortName, email, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **email** | **String**| The login Email Address. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

