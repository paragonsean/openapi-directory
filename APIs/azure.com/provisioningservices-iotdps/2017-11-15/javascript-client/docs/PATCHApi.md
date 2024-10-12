# IotDpsClient.PATCHApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotDpsResourceUpdate**](PATCHApi.md#iotDpsResourceUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} | Update an existing provisioning service&#39;s tags.



## iotDpsResourceUpdate

> ProvisioningServiceDescription iotDpsResourceUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, provisioningServiceTags)

Update an existing provisioning service&#39;s tags.

Update an existing provisioning service&#39;s tags. to update other fields use the CreateOrUpdate method

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.PATCHApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to create or update.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let provisioningServiceTags = new IotDpsClient.TagsResource(); // TagsResource | Updated tag information to set into the provisioning service instance.
apiInstance.iotDpsResourceUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, provisioningServiceTags, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **provisioningServiceName** | **String**| Name of provisioning service to create or update. | 
 **apiVersion** | **String**| The version of the API. | 
 **provisioningServiceTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the provisioning service instance. | 

### Return type

[**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

