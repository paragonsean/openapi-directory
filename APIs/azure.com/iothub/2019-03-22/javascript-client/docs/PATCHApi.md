# IotHubClient.PATCHApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotHubResourceUpdate**](PATCHApi.md#iotHubResourceUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Update an existing IoT Hubs tags.



## iotHubResourceUpdate

> IotHubDescription iotHubResourceUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, iotHubTags)

Update an existing IoT Hubs tags.

Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.PATCHApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let resourceName = "resourceName_example"; // String | Name of iot hub to update.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let iotHubTags = new IotHubClient.TagsResource(); // TagsResource | Updated tag information to set into the iot hub instance.
apiInstance.iotHubResourceUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, iotHubTags, (error, data, response) => {
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
 **resourceName** | **String**| Name of iot hub to update. | 
 **apiVersion** | **String**| The version of the API. | 
 **iotHubTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the iot hub instance. | 

### Return type

[**IotHubDescription**](IotHubDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

