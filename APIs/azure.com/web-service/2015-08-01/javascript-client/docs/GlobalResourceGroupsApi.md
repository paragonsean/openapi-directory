# WebSiteManagementClient.GlobalResourceGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalResourceGroupsMoveResources**](GlobalResourceGroupsApi.md#globalResourceGroupsMoveResources) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources | 



## globalResourceGroupsMoveResources

> globalResourceGroupsMoveResources(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope)



### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalResourceGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let moveResourceEnvelope = new WebSiteManagementClient.CsmMoveResourceEnvelope(); // CsmMoveResourceEnvelope | 
apiInstance.globalResourceGroupsMoveResources(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**|  | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **moveResourceEnvelope** | [**CsmMoveResourceEnvelope**](CsmMoveResourceEnvelope.md)|  | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: Not defined

