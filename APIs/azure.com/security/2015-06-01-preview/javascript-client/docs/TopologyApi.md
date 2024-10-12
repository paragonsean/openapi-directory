# SecurityCenter.TopologyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topologyGet**](TopologyApi.md#topologyGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/topologies/{topologyResourceName} | 
[**topologyList**](TopologyApi.md#topologyList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/topologies | 
[**topologyListByHomeRegion**](TopologyApi.md#topologyListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/topologies | 



## topologyGet

> TopologyResource topologyGet(subscriptionId, resourceGroupName, ascLocation, topologyResourceName, apiVersion)



Gets a specific topology component.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TopologyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let topologyResourceName = "topologyResourceName_example"; // String | Name of a topology resources collection.
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.topologyGet(subscriptionId, resourceGroupName, ascLocation, topologyResourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **topologyResourceName** | **String**| Name of a topology resources collection. | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**TopologyResource**](TopologyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topologyList

> TopologyList topologyList(subscriptionId, apiVersion)



Gets a list that allows to build a topology view of a subscription.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TopologyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.topologyList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**TopologyList**](TopologyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topologyListByHomeRegion

> TopologyList topologyListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets a list that allows to build a topology view of a subscription and location.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TopologyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.topologyListByHomeRegion(subscriptionId, ascLocation, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**TopologyList**](TopologyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

