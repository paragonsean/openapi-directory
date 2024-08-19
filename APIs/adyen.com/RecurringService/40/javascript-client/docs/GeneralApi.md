# AdyenRecurringApi.GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Recurring/v40*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCreatePermit**](GeneralApi.md#postCreatePermit) | **POST** /createPermit | Create new permits linked to a recurring contract.
[**postDisable**](GeneralApi.md#postDisable) | **POST** /disable | Disable stored payment details
[**postListRecurringDetails**](GeneralApi.md#postListRecurringDetails) | **POST** /listRecurringDetails | Get stored payment details
[**postNotifyShopper**](GeneralApi.md#postNotifyShopper) | **POST** /notifyShopper | Ask issuer to notify the shopper
[**postScheduleAccountUpdater**](GeneralApi.md#postScheduleAccountUpdater) | **POST** /scheduleAccountUpdater | Schedule running the Account Updater



## postCreatePermit

> CreatePermitResult postCreatePermit(opts)

Create new permits linked to a recurring contract.

Create permits for a recurring contract, including support for defining restrictions.

### Example

```javascript
import AdyenRecurringApi from 'adyen_recurring_api';
let defaultClient = AdyenRecurringApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenRecurringApi.GeneralApi();
let opts = {
  'createPermitRequest': new AdyenRecurringApi.CreatePermitRequest() // CreatePermitRequest | 
};
apiInstance.postCreatePermit(opts, (error, data, response) => {
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
 **createPermitRequest** | [**CreatePermitRequest**](CreatePermitRequest.md)|  | [optional] 

### Return type

[**CreatePermitResult**](CreatePermitResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDisable

> DisableResult postDisable(opts)

Disable stored payment details

Disables stored payment details to stop charging a shopper with this particular recurring detail ID.  For more information, refer to [Disable stored details](https://docs.adyen.com/classic-integration/recurring-payments/disable-stored-details/).

### Example

```javascript
import AdyenRecurringApi from 'adyen_recurring_api';
let defaultClient = AdyenRecurringApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenRecurringApi.GeneralApi();
let opts = {
  'disableRequest': new AdyenRecurringApi.DisableRequest() // DisableRequest | 
};
apiInstance.postDisable(opts, (error, data, response) => {
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
 **disableRequest** | [**DisableRequest**](DisableRequest.md)|  | [optional] 

### Return type

[**DisableResult**](DisableResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postListRecurringDetails

> RecurringDetailsResult postListRecurringDetails(opts)

Get stored payment details

Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for presentation to the shopper.  For more information, refer to [Retrieve stored details](https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/).

### Example

```javascript
import AdyenRecurringApi from 'adyen_recurring_api';
let defaultClient = AdyenRecurringApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenRecurringApi.GeneralApi();
let opts = {
  'recurringDetailsRequest': new AdyenRecurringApi.RecurringDetailsRequest() // RecurringDetailsRequest | 
};
apiInstance.postListRecurringDetails(opts, (error, data, response) => {
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
 **recurringDetailsRequest** | [**RecurringDetailsRequest**](RecurringDetailsRequest.md)|  | [optional] 

### Return type

[**RecurringDetailsResult**](RecurringDetailsResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNotifyShopper

> NotifyShopperResult postNotifyShopper(opts)

Ask issuer to notify the shopper

Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This endpoint is used only for local acquiring in India. For more information, refer to [Recurring card payments in India](https://docs.adyen.com/payment-methods/cards/cards-recurring-india).

### Example

```javascript
import AdyenRecurringApi from 'adyen_recurring_api';
let defaultClient = AdyenRecurringApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenRecurringApi.GeneralApi();
let opts = {
  'notifyShopperRequest': new AdyenRecurringApi.NotifyShopperRequest() // NotifyShopperRequest | 
};
apiInstance.postNotifyShopper(opts, (error, data, response) => {
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
 **notifyShopperRequest** | [**NotifyShopperRequest**](NotifyShopperRequest.md)|  | [optional] 

### Return type

[**NotifyShopperResult**](NotifyShopperResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postScheduleAccountUpdater

> ScheduleAccountUpdaterResult postScheduleAccountUpdater(opts)

Schedule running the Account Updater

When making the API call, you can submit either the credit card information, or the recurring detail reference and the shopper reference: * If the card information is provided, all the sub-fields for &#x60;card&#x60; are mandatory. * If the recurring detail reference is provided, the fields for &#x60;shopperReference&#x60; and &#x60;selectedRecurringDetailReference&#x60; are mandatory.

### Example

```javascript
import AdyenRecurringApi from 'adyen_recurring_api';
let defaultClient = AdyenRecurringApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenRecurringApi.GeneralApi();
let opts = {
  'scheduleAccountUpdaterRequest': new AdyenRecurringApi.ScheduleAccountUpdaterRequest() // ScheduleAccountUpdaterRequest | 
};
apiInstance.postScheduleAccountUpdater(opts, (error, data, response) => {
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
 **scheduleAccountUpdaterRequest** | [**ScheduleAccountUpdaterRequest**](ScheduleAccountUpdaterRequest.md)|  | [optional] 

### Return type

[**ScheduleAccountUpdaterResult**](ScheduleAccountUpdaterResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

