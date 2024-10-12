# BeezUpMerchantApi.CatalogsAutoApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoConfigureAutoImportInterval**](CatalogsAutoApi.md#autoConfigureAutoImportInterval) | **POST** /v2/user/catalogs/{storeId}/autoImport/scheduling/interval | Configure Auto Import Interval
[**autoDeleteAutoImport**](CatalogsAutoApi.md#autoDeleteAutoImport) | **DELETE** /v2/user/catalogs/{storeId}/autoImport | Delete Auto Import
[**autoGetAutoImportConfiguration**](CatalogsAutoApi.md#autoGetAutoImportConfiguration) | **GET** /v2/user/catalogs/{storeId}/autoImport | Get the auto import configuration
[**autoPauseAutoImport**](CatalogsAutoApi.md#autoPauseAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/pause | Pause Auto Import
[**autoResumeAutoImport**](CatalogsAutoApi.md#autoResumeAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/resume | Resume Auto Import
[**autoScheduleAutoImport**](CatalogsAutoApi.md#autoScheduleAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/scheduling/schedules | Configure Auto Import Schedules
[**autoStartAutoImport**](CatalogsAutoApi.md#autoStartAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/start | Start Auto Import Manually
[**importationActivateAutoImport**](CatalogsAutoApi.md#importationActivateAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/activate | Activate the auto importation of the last successful manual catalog importation.



## autoConfigureAutoImportInterval

> autoConfigureAutoImportInterval(storeId, configureAutoImportIntervalRequest)

Configure Auto Import Interval

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
let configureAutoImportIntervalRequest = new BeezUpMerchantApi.ConfigureAutoImportIntervalRequest(); // ConfigureAutoImportIntervalRequest | 
apiInstance.autoConfigureAutoImportInterval(storeId, configureAutoImportIntervalRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **configureAutoImportIntervalRequest** | [**ConfigureAutoImportIntervalRequest**](ConfigureAutoImportIntervalRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## autoDeleteAutoImport

> autoDeleteAutoImport(storeId)

Delete Auto Import

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.autoDeleteAutoImport(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoGetAutoImportConfiguration

> AutoImportConfiguration autoGetAutoImportConfiguration(storeId)

Get the auto import configuration

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.autoGetAutoImportConfiguration(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**AutoImportConfiguration**](AutoImportConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoPauseAutoImport

> autoPauseAutoImport(storeId)

Pause Auto Import

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.autoPauseAutoImport(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoResumeAutoImport

> autoResumeAutoImport(storeId)

Resume Auto Import

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.autoResumeAutoImport(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoScheduleAutoImport

> autoScheduleAutoImport(storeId, scheduleAutoImportRequest)

Configure Auto Import Schedules

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
let scheduleAutoImportRequest = new BeezUpMerchantApi.ScheduleAutoImportRequest(); // ScheduleAutoImportRequest | 
apiInstance.autoScheduleAutoImport(storeId, scheduleAutoImportRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **scheduleAutoImportRequest** | [**ScheduleAutoImportRequest**](ScheduleAutoImportRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## autoStartAutoImport

> LinksImportationGetImportationMonitoringLink autoStartAutoImport(storeId)

Start Auto Import Manually

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.autoStartAutoImport(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**LinksImportationGetImportationMonitoringLink**](LinksImportationGetImportationMonitoringLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationActivateAutoImport

> importationActivateAutoImport(storeId)

Activate the auto importation of the last successful manual catalog importation.

Once you have made your fist manual catalog importation with success, you can call this operation to import it automatically. No parameter required, we know which one it is.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsAutoApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.importationActivateAutoImport(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

