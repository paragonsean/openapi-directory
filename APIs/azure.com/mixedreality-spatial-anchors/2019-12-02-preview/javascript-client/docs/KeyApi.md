# MixedReality.KeyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatialAnchorsAccountsGetKeys**](KeyApi.md#spatialAnchorsAccountsGetKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName}/keys | 
[**spatialAnchorsAccountsRegenerateKeys**](KeyApi.md#spatialAnchorsAccountsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName}/keys | 



## spatialAnchorsAccountsGetKeys

> SpatialAnchorsAccountsGetKeys200Response spatialAnchorsAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



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
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.spatialAnchorsAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **accountName** | **String**| Name of an Mixed Reality Account. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**SpatialAnchorsAccountsGetKeys200Response**](SpatialAnchorsAccountsGetKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spatialAnchorsAccountsRegenerateKeys

> SpatialAnchorsAccountsGetKeys200Response spatialAnchorsAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate)



Regenerate specified Key of a Spatial Anchors Account

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
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let regenerate = new MixedReality.SpatialAnchorsAccountsRegenerateKeysRequest(); // SpatialAnchorsAccountsRegenerateKeysRequest | Required information for key regeneration.
apiInstance.spatialAnchorsAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate, (error, data, response) => {
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
 **accountName** | **String**| Name of an Mixed Reality Account. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **regenerate** | [**SpatialAnchorsAccountsRegenerateKeysRequest**](SpatialAnchorsAccountsRegenerateKeysRequest.md)| Required information for key regeneration. | 

### Return type

[**SpatialAnchorsAccountsGetKeys200Response**](SpatialAnchorsAccountsGetKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

