# HdInsightManagementClient.RegionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsGetCapabilities**](RegionsApi.md#locationsGetCapabilities) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HDInsight/locations/{location}/capabilities | 
[**locationsListBillingSpecs**](RegionsApi.md#locationsListBillingSpecs) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HDInsight/locations/{location}/billingSpecs | 
[**locationsListUsages**](RegionsApi.md#locationsListUsages) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HDInsight/locations/{location}/usages | 



## locationsGetCapabilities

> CapabilitiesResult locationsGetCapabilities(subscriptionId, location, apiVersion)



Gets the capabilities for the specified location.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.RegionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The Azure location (region) for which to make the request.
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
apiInstance.locationsGetCapabilities(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The Azure location (region) for which to make the request. | 
 **apiVersion** | **String**| The HDInsight client API Version. | 

### Return type

[**CapabilitiesResult**](CapabilitiesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsListBillingSpecs

> BillingResponseListResult locationsListBillingSpecs(subscriptionId, location, apiVersion)



Lists the billingSpecs for the specified subscription and location.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.RegionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The Azure location (region) for which to make the request.
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
apiInstance.locationsListBillingSpecs(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The Azure location (region) for which to make the request. | 
 **apiVersion** | **String**| The HDInsight client API Version. | 

### Return type

[**BillingResponseListResult**](BillingResponseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsListUsages

> UsagesListResult locationsListUsages(subscriptionId, location, apiVersion)



Lists the usages for the specified location.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.RegionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The Azure location (region) for which to make the request.
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
apiInstance.locationsListUsages(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The Azure location (region) for which to make the request. | 
 **apiVersion** | **String**| The HDInsight client API Version. | 

### Return type

[**UsagesListResult**](UsagesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

