# VMwareCloudSimple.AvailabilityUsagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skusAvailabilityList**](AvailabilityUsagesApi.md#skusAvailabilityList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/availabilities | Implements SkuAvailability List method
[**usagesList**](AvailabilityUsagesApi.md#usagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/usages | Implements Usages List method



## skusAvailabilityList

> SkuAvailabilityListResponse skusAvailabilityList(subscriptionId, regionId, apiVersion, opts)

Implements SkuAvailability List method

Returns list of available resources in region

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.AvailabilityUsagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'skuId': "skuId_example" // String | sku id, if no sku is passed availability for all skus will be returned
};
apiInstance.skusAvailabilityList(subscriptionId, regionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **apiVersion** | **String**| Client API version. | 
 **skuId** | **String**| sku id, if no sku is passed availability for all skus will be returned | [optional] 

### Return type

[**SkuAvailabilityListResponse**](SkuAvailabilityListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usagesList

> UsageListResponse usagesList(subscriptionId, regionId, apiVersion, opts)

Implements Usages List method

Returns list of usage in region

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.AvailabilityUsagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the list operation. only name.value is allowed here as a filter e.g. $filter=name.value eq 'xxxx'
};
apiInstance.usagesList(subscriptionId, regionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **apiVersion** | **String**| Client API version. | 
 **filter** | **String**| The filter to apply on the list operation. only name.value is allowed here as a filter e.g. $filter&#x3D;name.value eq &#39;xxxx&#39; | [optional] 

### Return type

[**UsageListResponse**](UsageListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

