# SimpliVpnapi.SimpliVPNAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disableUser**](SimpliVPNAPIApi.md#disableUser) | **POST** /disable-user | DisableUser
[**enableUser**](SimpliVPNAPIApi.md#enableUser) | **POST** /enable-user | EnableUser
[**getServerSummaries**](SimpliVPNAPIApi.md#getServerSummaries) | **GET** /server-summaries | 
[**getServers**](SimpliVPNAPIApi.md#getServers) | **GET** /servers | 
[**login**](SimpliVPNAPIApi.md#login) | **POST** /login | Login
[**register**](SimpliVPNAPIApi.md#register) | **POST** /register | Register
[**usernameAvailable**](SimpliVPNAPIApi.md#usernameAvailable) | **POST** /username-available | UsernameAvailable



## disableUser

> disableUser(disableUser)

DisableUser

This route allows you to disable a user&#39;s vpn access.

### Example

```javascript
import SimpliVpnapi from 'simpli_vpnapi';
let defaultClient = SimpliVpnapi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new SimpliVpnapi.SimpliVPNAPIApi();
let disableUser = new SimpliVpnapi.DisableUser(); // DisableUser | 
apiInstance.disableUser(disableUser, (error, data, response) => {
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
 **disableUser** | [**DisableUser**](DisableUser.md)|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## enableUser

> enableUser(enableUser)

EnableUser

This route allows you to enable a user&#39;s vpn access. This route can only be called using your user&#39;s Bearer Auth token.

### Example

```javascript
import SimpliVpnapi from 'simpli_vpnapi';
let defaultClient = SimpliVpnapi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new SimpliVpnapi.SimpliVPNAPIApi();
let enableUser = new SimpliVpnapi.EnableUser(); // EnableUser | 
apiInstance.enableUser(enableUser, (error, data, response) => {
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
 **enableUser** | [**EnableUser**](EnableUser.md)|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getServerSummaries

> getServerSummaries()



### Example

```javascript
import SimpliVpnapi from 'simpli_vpnapi';
let defaultClient = SimpliVpnapi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new SimpliVpnapi.SimpliVPNAPIApi();
apiInstance.getServerSummaries((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getServers

> getServers()



### Example

```javascript
import SimpliVpnapi from 'simpli_vpnapi';
let defaultClient = SimpliVpnapi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new SimpliVpnapi.SimpliVPNAPIApi();
apiInstance.getServers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## login

> login(userLogin)

Login

This route allows you to login a user. The response will give you a Bearer auth token to use with all rquests pertaining to the user. This token expires in 7 days, so for every request you should check if you get an unauthorized responsve and re-validate the login if needed.

### Example

```javascript
import SimpliVpnapi from 'simpli_vpnapi';
let defaultClient = SimpliVpnapi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new SimpliVpnapi.SimpliVPNAPIApi();
let userLogin = new SimpliVpnapi.UserLogin(); // UserLogin | 
apiInstance.login(userLogin, (error, data, response) => {
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
 **userLogin** | [**UserLogin**](UserLogin.md)|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## register

> register(register)

Register

This route allows VPN Admin user&#39;s with an api key to register a vpn user account. This route can only be called using your api key supplied to you from SimpliVPN. Before calling this you should use your api key to call the /UsernameAvailable route to make sure the username you want is available first. All subsequent user requests following can be done using the user&#39;s api token, their token&#39;s expire every 7 days, so you should occasionally check them and if you get unauthorized, refresh their token by calling /login route. This route will also auto-enable a new user.

### Example

```javascript
import SimpliVpnapi from 'simpli_vpnapi';
let defaultClient = SimpliVpnapi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new SimpliVpnapi.SimpliVPNAPIApi();
let register = new SimpliVpnapi.Register(); // Register | 
apiInstance.register(register, (error, data, response) => {
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
 **register** | [**Register**](Register.md)|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## usernameAvailable

> usernameAvailable(enableUser)

UsernameAvailable

This route allows VPN Admin user&#39;s to check if a specific username is available before registering an account username. This route can only be called using your api key supplied to you from SimpliVPN.

### Example

```javascript
import SimpliVpnapi from 'simpli_vpnapi';
let defaultClient = SimpliVpnapi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new SimpliVpnapi.SimpliVPNAPIApi();
let enableUser = new SimpliVpnapi.EnableUser(); // EnableUser | 
apiInstance.usernameAvailable(enableUser, (error, data, response) => {
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
 **enableUser** | [**EnableUser**](EnableUser.md)|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

