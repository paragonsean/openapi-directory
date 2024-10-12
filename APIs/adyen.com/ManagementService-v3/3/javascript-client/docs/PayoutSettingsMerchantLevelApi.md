# ManagementApi.PayoutSettingsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId**](PayoutSettingsMerchantLevelApi.md#deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId) | **DELETE** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Delete a payout setting
[**getMerchantsMerchantIdPayoutSettings**](PayoutSettingsMerchantLevelApi.md#getMerchantsMerchantIdPayoutSettings) | **GET** /merchants/{merchantId}/payoutSettings | Get a list of payout settings
[**getMerchantsMerchantIdPayoutSettingsPayoutSettingsId**](PayoutSettingsMerchantLevelApi.md#getMerchantsMerchantIdPayoutSettingsPayoutSettingsId) | **GET** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Get a payout setting
[**patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId**](PayoutSettingsMerchantLevelApi.md#patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId) | **PATCH** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Update a payout setting
[**postMerchantsMerchantIdPayoutSettings**](PayoutSettingsMerchantLevelApi.md#postMerchantsMerchantIdPayoutSettings) | **POST** /merchants/{merchantId}/payoutSettings | Add a payout setting



## deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId

> deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId)

Delete a payout setting

Deletes the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PayoutSettingsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let payoutSettingsId = "payoutSettingsId_example"; // String | The unique identifier of the payout setting.
apiInstance.deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **payoutSettingsId** | **String**| The unique identifier of the payout setting. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdPayoutSettings

> PayoutSettingsResponse getMerchantsMerchantIdPayoutSettings(merchantId)

Get a list of payout settings

Returns the list of payout settings for the merchant account identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PayoutSettingsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
apiInstance.getMerchantsMerchantIdPayoutSettings(merchantId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 

### Return type

[**PayoutSettingsResponse**](PayoutSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdPayoutSettingsPayoutSettingsId

> PayoutSettings getMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId)

Get a payout setting

Returns the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PayoutSettingsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let payoutSettingsId = "payoutSettingsId_example"; // String | The unique identifier of the payout setting.
apiInstance.getMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **payoutSettingsId** | **String**| The unique identifier of the payout setting. | 

### Return type

[**PayoutSettings**](PayoutSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId

> PayoutSettings patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId, opts)

Update a payout setting

Updates the payout setting identified in the path. You can enable or disable the payout setting.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PayoutSettingsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let payoutSettingsId = "payoutSettingsId_example"; // String | The unique identifier of the payout setting.
let opts = {
  'updatePayoutSettingsRequest': new ManagementApi.UpdatePayoutSettingsRequest() // UpdatePayoutSettingsRequest | 
};
apiInstance.patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **payoutSettingsId** | **String**| The unique identifier of the payout setting. | 
 **updatePayoutSettingsRequest** | [**UpdatePayoutSettingsRequest**](UpdatePayoutSettingsRequest.md)|  | [optional] 

### Return type

[**PayoutSettings**](PayoutSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdPayoutSettings

> PayoutSettings postMerchantsMerchantIdPayoutSettings(merchantId, opts)

Add a payout setting

Sends a request to add a payout setting for the merchant account specified in the path. A payout setting links the merchant account to the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.  If you&#39;re accepting payments in multiple currencies, you may add multiple payout settings for the merchant account.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.PayoutSettingsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'payoutSettingsRequest': new ManagementApi.PayoutSettingsRequest() // PayoutSettingsRequest | 
};
apiInstance.postMerchantsMerchantIdPayoutSettings(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **payoutSettingsRequest** | [**PayoutSettingsRequest**](PayoutSettingsRequest.md)|  | [optional] 

### Return type

[**PayoutSettings**](PayoutSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

