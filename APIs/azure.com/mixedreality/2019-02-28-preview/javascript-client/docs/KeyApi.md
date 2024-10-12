# MixedReality.KeyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatialAnchorsAccountsGetKeys**](KeyApi.md#spatialAnchorsAccountsGetKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatialAnchorsAccountName}/keys | 
[**spatialAnchorsAccountsRegenerateKeys**](KeyApi.md#spatialAnchorsAccountsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatialAnchorsAccountName}/keys | 



## spatialAnchorsAccountsGetKeys

> SpatialAnchorsAccountKeys spatialAnchorsAccountsGetKeys(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion)



Get Both of the 2 Keys of a Spatial Anchors Account

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.KeyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let spatialAnchorsAccountName = "spatialAnchorsAccountName_example"; // String | Name of an Mixed Reality Spatial Anchors Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.spatialAnchorsAccountsGetKeys(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **spatialAnchorsAccountName** | **String**| Name of an Mixed Reality Spatial Anchors Account. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**SpatialAnchorsAccountKeys**](SpatialAnchorsAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spatialAnchorsAccountsRegenerateKeys

> SpatialAnchorsAccountKeys spatialAnchorsAccountsRegenerateKeys(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion, spatialAnchorsAccountKeyRegenerate)



Regenerate 1 Key of a Spatial Anchors Account

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.KeyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let spatialAnchorsAccountName = "spatialAnchorsAccountName_example"; // String | Name of an Mixed Reality Spatial Anchors Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let spatialAnchorsAccountKeyRegenerate = new MixedReality.SpatialAnchorsAccountKeyRegenerateRequest(); // SpatialAnchorsAccountKeyRegenerateRequest | Specifying which key to be regenerated.
apiInstance.spatialAnchorsAccountsRegenerateKeys(subscriptionId, resourceGroupName, spatialAnchorsAccountName, apiVersion, spatialAnchorsAccountKeyRegenerate, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **spatialAnchorsAccountName** | **String**| Name of an Mixed Reality Spatial Anchors Account. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **spatialAnchorsAccountKeyRegenerate** | [**SpatialAnchorsAccountKeyRegenerateRequest**](SpatialAnchorsAccountKeyRegenerateRequest.md)| Specifying which key to be regenerated. | 

### Return type

[**SpatialAnchorsAccountKeys**](SpatialAnchorsAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

