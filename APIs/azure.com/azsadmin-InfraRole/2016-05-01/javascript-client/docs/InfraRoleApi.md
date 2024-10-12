# FabricAdminClient.InfraRoleApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infraRolesRestart**](InfraRoleApi.md#infraRolesRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoles/{infraRole}/Restart | 



## infraRolesRestart

> infraRolesRestart(subscriptionId, resourceGroupName, location, infraRole, apiVersion)



Restarts the requested infrastructure role.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.InfraRoleApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let infraRole = "infraRole_example"; // String | Infrastructure role name.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.infraRolesRestart(subscriptionId, resourceGroupName, location, infraRole, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **infraRole** | **String**| Infrastructure role name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

