# ClassicPlatformsNotifications.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postACCOUNTCLOSED**](AccountsApi.md#postACCOUNTCLOSED) | **POST** /ACCOUNT_CLOSED | Account closed
[**postACCOUNTCREATED**](AccountsApi.md#postACCOUNTCREATED) | **POST** /ACCOUNT_CREATED | Account created
[**postACCOUNTUPDATED**](AccountsApi.md#postACCOUNTUPDATED) | **POST** /ACCOUNT_UPDATED | Account updated



## postACCOUNTCLOSED

> NotificationResponse postACCOUNTCLOSED(opts)

Account closed

Adyen sends this webhook when [an account is closed](https://docs.adyen.com/api-explorer/#/Account/latest/post/closeAccount).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountsApi();
let opts = {
  'accountCloseNotification': new ClassicPlatformsNotifications.AccountCloseNotification() // AccountCloseNotification | 
};
apiInstance.postACCOUNTCLOSED(opts, (error, data, response) => {
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
 **accountCloseNotification** | [**AccountCloseNotification**](AccountCloseNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTCREATED

> NotificationResponse postACCOUNTCREATED(opts)

Account created

Adyen sends this webhook when [an account is created](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccount).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountsApi();
let opts = {
  'accountCreateNotification': new ClassicPlatformsNotifications.AccountCreateNotification() // AccountCreateNotification | 
};
apiInstance.postACCOUNTCREATED(opts, (error, data, response) => {
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
 **accountCreateNotification** | [**AccountCreateNotification**](AccountCreateNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTUPDATED

> NotificationResponse postACCOUNTUPDATED(opts)

Account updated

Adyen sends this webhook when [an account is updated](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccount).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountsApi();
let opts = {
  'accountUpdateNotification': new ClassicPlatformsNotifications.AccountUpdateNotification() // AccountUpdateNotification | 
};
apiInstance.postACCOUNTUPDATED(opts, (error, data, response) => {
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
 **accountUpdateNotification** | [**AccountUpdateNotification**](AccountUpdateNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

