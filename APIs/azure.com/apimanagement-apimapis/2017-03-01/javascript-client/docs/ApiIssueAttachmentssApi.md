# ApiManagementClient.ApiIssueAttachmentssApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiIssuAttachmentHead**](ApiIssueAttachmentssApi.md#apiIssuAttachmentHead) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} | 
[**apiIssueAttachmentCreateOrUpdate**](ApiIssueAttachmentssApi.md#apiIssueAttachmentCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} | 



## apiIssuAttachmentHead

> apiIssuAttachmentHead(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the issue Attachment for an API specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueAttachmentssApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let attachmentId = "attachmentId_example"; // String | Attachment identifier within an Issue. Must be unique in the current Issue.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiIssuAttachmentHead(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | 
 **attachmentId** | **String**| Attachment identifier within an Issue. Must be unique in the current Issue. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiIssueAttachmentCreateOrUpdate

> IssueAttachmentContract apiIssueAttachmentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId, parameters, opts)



Creates a new Attachment for the Issue in an API or updates an existing one.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueAttachmentssApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let attachmentId = "attachmentId_example"; // String | Attachment identifier within an Issue. Must be unique in the current Issue.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.IssueAttachmentContract(); // IssueAttachmentContract | Create parameters.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
};
apiInstance.apiIssueAttachmentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | 
 **attachmentId** | **String**| Attachment identifier within an Issue. Must be unique in the current Issue. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**IssueAttachmentContract**](IssueAttachmentContract.md)| Create parameters. | 
 **ifMatch** | **String**| ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | [optional] 

### Return type

[**IssueAttachmentContract**](IssueAttachmentContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

