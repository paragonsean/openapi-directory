# VMwareCloudSimple.PrivateCloudsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateCloudsGet**](PrivateCloudsApi.md#privateCloudsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName} | Implements private cloud GET method
[**privateCloudsList**](PrivateCloudsApi.md#privateCloudsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds | Implements private cloud list GET method



## privateCloudsGet

> PrivateCloud privateCloudsGet(subscriptionId, pcName, regionId, apiVersion)

Implements private cloud GET method

Returns private cloud by its name

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.PrivateCloudsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let pcName = "pcName_example"; // String | The private cloud name
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.privateCloudsGet(subscriptionId, pcName, regionId, apiVersion, (error, data, response) => {
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
 **pcName** | **String**| The private cloud name | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**PrivateCloud**](PrivateCloud.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCloudsList

> PrivateCloudList privateCloudsList(subscriptionId, regionId, apiVersion)

Implements private cloud list GET method

Returns list of private clouds in particular region

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.PrivateCloudsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.privateCloudsList(subscriptionId, regionId, apiVersion, (error, data, response) => {
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

### Return type

[**PrivateCloudList**](PrivateCloudList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

