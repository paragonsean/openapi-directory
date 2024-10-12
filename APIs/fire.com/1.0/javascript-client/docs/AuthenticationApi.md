# FireFinancialServicesBusinessApi.AuthenticationApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /v1/apps/accesstokens | Authenticate with the API.



## authenticate

> AccessToken authenticate(authentication)

Authenticate with the API.

Access to the API is by Bearer Tokens. The process is somewhat similar to OAuth2.0, but with some changes to improve security.    1. You must first log into the firework online application and create a new Application in the Profile &gt; API page. (You will need your PIN digits and 2-Factor Authentication device).      2. Give your application a Name and select the scope/permissions you need the application to have (more on Scopes below).      3. You will be provided with three pieces of information - the App Refresh Token, Client ID and Client Key. You need to take note of the Client Key when it is displayed - it will not be shown again.         You now use these pieces of data to retrieve a short-term Access Token which you can use to access the API. The Access Token expires within a relatively short time, so even if it is compromised, the attacker will not have long to use it. The Client Key is the most important piece of information to keep secret. This should only ever be stored on a backend server, and never in a front end client or mobile app.     **If you ever accidentally reveal the Client Key (or accidentally commit it to Github for instance) it is vital that you log into firework online and delete/recreate the App Tokens as soon as possible. Anyone who has these three pieces of data can access the API to view your data and set up payments from your account (depending on the scope of the tokens).**         Once you have the access token, pass it as a header for every call, like so:    &#x60;Authorization: Bearer $ACCESS_TOKEN&#x60;    Whenever it expires, create a new nonce and get a new access token again. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';

let apiInstance = new FireFinancialServicesBusinessApi.AuthenticationApi();
let authentication = new FireFinancialServicesBusinessApi.Authentication(); // Authentication | Authentication data
apiInstance.authenticate(authentication, (error, data, response) => {
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
 **authentication** | [**Authentication**](Authentication.md)| Authentication data | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

