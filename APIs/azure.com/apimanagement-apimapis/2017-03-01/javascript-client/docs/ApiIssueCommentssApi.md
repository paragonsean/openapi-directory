# ApiManagementClient.ApiIssueCommentssApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiIssuCommentHead**](ApiIssueCommentssApi.md#apiIssuCommentHead) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/comments/{commentId} | 
[**apiIssueCommentCreateOrUpdate**](ApiIssueCommentssApi.md#apiIssueCommentCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/comments/{commentId} | 



## apiIssuCommentHead

> apiIssuCommentHead(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the issue Comment for an API specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueCommentssApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let commentId = "commentId_example"; // String | Comment identifier within an Issue. Must be unique in the current Issue.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiIssuCommentHead(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId, (error, data, response) => {
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
 **commentId** | **String**| Comment identifier within an Issue. Must be unique in the current Issue. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiIssueCommentCreateOrUpdate

> IssueCommentContract apiIssueCommentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId, parameters, opts)



Creates a new Comment for the Issue in an API or updates an existing one.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueCommentssApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let commentId = "commentId_example"; // String | Comment identifier within an Issue. Must be unique in the current Issue.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.IssueCommentContract(); // IssueCommentContract | Create parameters.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
};
apiInstance.apiIssueCommentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **commentId** | **String**| Comment identifier within an Issue. Must be unique in the current Issue. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**IssueCommentContract**](IssueCommentContract.md)| Create parameters. | 
 **ifMatch** | **String**| ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | [optional] 

### Return type

[**IssueCommentContract**](IssueCommentContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

