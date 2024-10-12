# ShutterstockApiExplorer.UsersApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccessToken**](UsersApi.md#getAccessToken) | **GET** /v2/user/access_token | Get access token details
[**getUser**](UsersApi.md#getUser) | **GET** /v2/user | Get user details
[**getUserSubscriptionList**](UsersApi.md#getUserSubscriptionList) | **GET** /v2/user/subscriptions | List user subscriptions



## getAccessToken

> AccessTokenDetails getAccessToken()

Get access token details

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.UsersApi();
apiInstance.getAccessToken((error, data, response) => {
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

[**AccessTokenDetails**](AccessTokenDetails.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> UserDetails getUser()

Get user details

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.UsersApi();
apiInstance.getUser((error, data, response) => {
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

[**UserDetails**](UserDetails.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserSubscriptionList

> SubscriptionDataList getUserSubscriptionList()

List user subscriptions

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.UsersApi();
apiInstance.getUserSubscriptionList((error, data, response) => {
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

[**SubscriptionDataList**](SubscriptionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

