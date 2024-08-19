# ClassicPlatformsNotifications.AccountHoldersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postACCOUNTHOLDERCREATED**](AccountHoldersApi.md#postACCOUNTHOLDERCREATED) | **POST** /ACCOUNT_HOLDER_CREATED | Account holder created
[**postACCOUNTHOLDERSTATUSCHANGE**](AccountHoldersApi.md#postACCOUNTHOLDERSTATUSCHANGE) | **POST** /ACCOUNT_HOLDER_STATUS_CHANGE | Account holder status changed
[**postACCOUNTHOLDERSTORESTATUSCHANGE**](AccountHoldersApi.md#postACCOUNTHOLDERSTORESTATUSCHANGE) | **POST** /ACCOUNT_HOLDER_STORE_STATUS_CHANGE | Store status changed
[**postACCOUNTHOLDERUPCOMINGDEADLINE**](AccountHoldersApi.md#postACCOUNTHOLDERUPCOMINGDEADLINE) | **POST** /ACCOUNT_HOLDER_UPCOMING_DEADLINE | Upcoming deadline
[**postACCOUNTHOLDERUPDATED**](AccountHoldersApi.md#postACCOUNTHOLDERUPDATED) | **POST** /ACCOUNT_HOLDER_UPDATED | Account holder updated
[**postACCOUNTHOLDERVERIFICATION**](AccountHoldersApi.md#postACCOUNTHOLDERVERIFICATION) | **POST** /ACCOUNT_HOLDER_VERIFICATION | Verification results received



## postACCOUNTHOLDERCREATED

> NotificationResponse postACCOUNTHOLDERCREATED(opts)

Account holder created

Adyen sends this webhook when [an account holder is created](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountHoldersApi();
let opts = {
  'accountHolderCreateNotification': new ClassicPlatformsNotifications.AccountHolderCreateNotification() // AccountHolderCreateNotification | 
};
apiInstance.postACCOUNTHOLDERCREATED(opts, (error, data, response) => {
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
 **accountHolderCreateNotification** | [**AccountHolderCreateNotification**](AccountHolderCreateNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTHOLDERSTATUSCHANGE

> NotificationResponse postACCOUNTHOLDERSTATUSCHANGE(opts)

Account holder status changed

Adyen sends this webhook when [the status of an account holder is changed](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccountHolderState).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountHoldersApi();
let opts = {
  'accountHolderStatusChangeNotification': new ClassicPlatformsNotifications.AccountHolderStatusChangeNotification() // AccountHolderStatusChangeNotification | 
};
apiInstance.postACCOUNTHOLDERSTATUSCHANGE(opts, (error, data, response) => {
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
 **accountHolderStatusChangeNotification** | [**AccountHolderStatusChangeNotification**](AccountHolderStatusChangeNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTHOLDERSTORESTATUSCHANGE

> NotificationResponse postACCOUNTHOLDERSTORESTATUSCHANGE(opts)

Store status changed

Adyen sends this webhook when [the status of a store](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__reqParam_accountHolderDetails-storeDetails-status) associated with an account holder is changed.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountHoldersApi();
let opts = {
  'accountHolderStoreStatusChangeNotification': new ClassicPlatformsNotifications.AccountHolderStoreStatusChangeNotification() // AccountHolderStoreStatusChangeNotification | 
};
apiInstance.postACCOUNTHOLDERSTORESTATUSCHANGE(opts, (error, data, response) => {
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
 **accountHolderStoreStatusChangeNotification** | [**AccountHolderStoreStatusChangeNotification**](AccountHolderStoreStatusChangeNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTHOLDERUPCOMINGDEADLINE

> NotificationResponse postACCOUNTHOLDERUPCOMINGDEADLINE(opts)

Upcoming deadline

Adyen sends this notification when an account holder&#39;s deadline to fulfill the requirements of a specific event is coming up.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountHoldersApi();
let opts = {
  'accountHolderUpcomingDeadlineNotification': new ClassicPlatformsNotifications.AccountHolderUpcomingDeadlineNotification() // AccountHolderUpcomingDeadlineNotification | 
};
apiInstance.postACCOUNTHOLDERUPCOMINGDEADLINE(opts, (error, data, response) => {
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
 **accountHolderUpcomingDeadlineNotification** | [**AccountHolderUpcomingDeadlineNotification**](AccountHolderUpcomingDeadlineNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTHOLDERUPDATED

> NotificationResponse postACCOUNTHOLDERUPDATED(opts)

Account holder updated

Adyen sends this webhook when [an account holder is updated](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccountHolder).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountHoldersApi();
let opts = {
  'accountHolderUpdateNotification': new ClassicPlatformsNotifications.AccountHolderUpdateNotification() // AccountHolderUpdateNotification | 
};
apiInstance.postACCOUNTHOLDERUPDATED(opts, (error, data, response) => {
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
 **accountHolderUpdateNotification** | [**AccountHolderUpdateNotification**](AccountHolderUpdateNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTHOLDERVERIFICATION

> NotificationResponse postACCOUNTHOLDERVERIFICATION(opts)

Verification results received

Adyen sends this webhook when verification results are available.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.AccountHoldersApi();
let opts = {
  'accountHolderVerificationNotification': new ClassicPlatformsNotifications.AccountHolderVerificationNotification() // AccountHolderVerificationNotification | 
};
apiInstance.postACCOUNTHOLDERVERIFICATION(opts, (error, data, response) => {
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
 **accountHolderVerificationNotification** | [**AccountHolderVerificationNotification**](AccountHolderVerificationNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

