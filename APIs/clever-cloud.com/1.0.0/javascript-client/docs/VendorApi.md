# CleverCloudApi.VendorApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVendorAppsAddonId_0**](VendorApi.md#getVendorAppsAddonId_0) | **GET** /vendor/apps/{addonId} | 
[**getVendorApps_0**](VendorApi.md#getVendorApps_0) | **GET** /vendor/apps | 
[**postVendorBillingOwnerId_0**](VendorApi.md#postVendorBillingOwnerId_0) | **POST** /vendor/apps/{addonId}/consumptions | 
[**putVendorAppsAddonId_0**](VendorApi.md#putVendorAppsAddonId_0) | **PUT** /vendor/apps/{addonId} | 
[**vendorAddonsPost_1**](VendorApi.md#vendorAddonsPost_1) | **POST** /vendor//addons | 
[**vendorAppsAddonIdLogscollectorGet_0**](VendorApi.md#vendorAppsAddonIdLogscollectorGet_0) | **GET** /vendor//apps/{addonId}/logscollector | 
[**vendorAppsAddonIdMigrationCallbackPut_0**](VendorApi.md#vendorAppsAddonIdMigrationCallbackPut_0) | **PUT** /vendor/apps/{addonId}/migration_callback | 



## getVendorAppsAddonId_0

> getVendorAppsAddonId_0(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.VendorApi();
let addonId = "addonId_example"; // String | 
apiInstance.getVendorAppsAddonId_0(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVendorApps_0

> [Application] getVendorApps_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.VendorApi();
let opts = {
  'offset': 56 // Number | 
};
apiInstance.getVendorApps_0(opts, (error, data, response) => {
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
 **offset** | **Number**|  | [optional] 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postVendorBillingOwnerId_0

> postVendorBillingOwnerId_0(addonId, wannabeAddonBilling)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.VendorApi();
let addonId = "addonId_example"; // String | 
let wannabeAddonBilling = new CleverCloudApi.WannabeAddonBilling(); // WannabeAddonBilling | 
apiInstance.postVendorBillingOwnerId_0(addonId, wannabeAddonBilling, (error, data, response) => {
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
 **addonId** | **String**|  | 
 **wannabeAddonBilling** | [**WannabeAddonBilling**](WannabeAddonBilling.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putVendorAppsAddonId_0

> putVendorAppsAddonId_0(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.VendorApi();
let addonId = "addonId_example"; // String | 
apiInstance.putVendorAppsAddonId_0(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vendorAddonsPost_1

> vendorAddonsPost_1()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.VendorApi();
apiInstance.vendorAddonsPost_1((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vendorAppsAddonIdLogscollectorGet_0

> vendorAppsAddonIdLogscollectorGet_0(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.VendorApi();
let addonId = "addonId_example"; // String | 
apiInstance.vendorAppsAddonIdLogscollectorGet_0(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vendorAppsAddonIdMigrationCallbackPut_0

> vendorAppsAddonIdMigrationCallbackPut_0(addonId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.VendorApi();
let addonId = "addonId_example"; // String | 
let opts = {
  'planId': "planId_example", // String | 
  'region': "region_example" // String | 
};
apiInstance.vendorAppsAddonIdMigrationCallbackPut_0(addonId, opts, (error, data, response) => {
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
 **addonId** | **String**|  | 
 **planId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

