# BeezUpMerchantApi.OMInvoiceAPISettingsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrderInvoiceDesignSettings**](OMInvoiceAPISettingsApi.md#getOrderInvoiceDesignSettings) | **GET** /v2/user/marketplaces/orders/invoices/settings/design | Get Order Invoice design settings
[**getOrderInvoiceDesignSettingsPreview**](OMInvoiceAPISettingsApi.md#getOrderInvoiceDesignSettingsPreview) | **POST** /v2/user/marketplaces/orders/invoices/settings/design/preview | View a preview an Order Invoice using custom design settings
[**getOrderInvoiceGeneralSettings**](OMInvoiceAPISettingsApi.md#getOrderInvoiceGeneralSettings) | **GET** /v2/user/marketplaces/orders/invoices/settings/general | Get Order Invoice general settings
[**saveOrderInvoiceDesignSettings**](OMInvoiceAPISettingsApi.md#saveOrderInvoiceDesignSettings) | **PUT** /v2/user/marketplaces/orders/invoices/settings/design | Save Order Invoice design settings
[**saveOrderInvoiceGeneralSettings**](OMInvoiceAPISettingsApi.md#saveOrderInvoiceGeneralSettings) | **PUT** /v2/user/marketplaces/orders/invoices/settings/general | Save Order Invoice general settings



## getOrderInvoiceDesignSettings

> OrderInvoiceDesignSettings getOrderInvoiceDesignSettings()

Get Order Invoice design settings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPISettingsApi();
apiInstance.getOrderInvoiceDesignSettings((error, data, response) => {
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

[**OrderInvoiceDesignSettings**](OrderInvoiceDesignSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrderInvoiceDesignSettingsPreview

> GetOrderInvoiceDesignPreviewResponse getOrderInvoiceDesignSettingsPreview(acceptEncoding, orderInvoiceDesignSettings)

View a preview an Order Invoice using custom design settings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPISettingsApi();
let acceptEncoding = ["null"]; // [String] | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
let orderInvoiceDesignSettings = new BeezUpMerchantApi.OrderInvoiceDesignSettings(); // OrderInvoiceDesignSettings | 
apiInstance.getOrderInvoiceDesignSettingsPreview(acceptEncoding, orderInvoiceDesignSettings, (error, data, response) => {
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
 **acceptEncoding** | [**[String]**](String.md)| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | 
 **orderInvoiceDesignSettings** | [**OrderInvoiceDesignSettings**](OrderInvoiceDesignSettings.md)|  | 

### Return type

[**GetOrderInvoiceDesignPreviewResponse**](GetOrderInvoiceDesignPreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrderInvoiceGeneralSettings

> GetOrderInvoiceGeneralSettingsResponse getOrderInvoiceGeneralSettings()

Get Order Invoice general settings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPISettingsApi();
apiInstance.getOrderInvoiceGeneralSettings((error, data, response) => {
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

[**GetOrderInvoiceGeneralSettingsResponse**](GetOrderInvoiceGeneralSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveOrderInvoiceDesignSettings

> saveOrderInvoiceDesignSettings(orderInvoiceDesignSettings)

Save Order Invoice design settings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPISettingsApi();
let orderInvoiceDesignSettings = new BeezUpMerchantApi.OrderInvoiceDesignSettings(); // OrderInvoiceDesignSettings | 
apiInstance.saveOrderInvoiceDesignSettings(orderInvoiceDesignSettings, (error, data, response) => {
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
 **orderInvoiceDesignSettings** | [**OrderInvoiceDesignSettings**](OrderInvoiceDesignSettings.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveOrderInvoiceGeneralSettings

> saveOrderInvoiceGeneralSettings(orderInvoiceGeneralSettings)

Save Order Invoice general settings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPISettingsApi();
let orderInvoiceGeneralSettings = new BeezUpMerchantApi.OrderInvoiceGeneralSettings(); // OrderInvoiceGeneralSettings | 
apiInstance.saveOrderInvoiceGeneralSettings(orderInvoiceGeneralSettings, (error, data, response) => {
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
 **orderInvoiceGeneralSettings** | [**OrderInvoiceGeneralSettings**](OrderInvoiceGeneralSettings.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

