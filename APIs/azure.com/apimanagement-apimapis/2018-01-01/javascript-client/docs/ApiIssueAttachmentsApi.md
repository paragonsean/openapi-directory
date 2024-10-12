# ApiManagementClient.ApiIssueAttachmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiIssueAttachmentCreateOrUpdate**](ApiIssueAttachmentsApi.md#apiIssueAttachmentCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} | 
[**apiIssueAttachmentDelete**](ApiIssueAttachmentsApi.md#apiIssueAttachmentDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} | 
[**apiIssueAttachmentGet**](ApiIssueAttachmentsApi.md#apiIssueAttachmentGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} | 
[**apiIssueAttachmentGetEntityTag**](ApiIssueAttachmentsApi.md#apiIssueAttachmentGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} | 
[**apiIssueAttachmentListByService**](ApiIssueAttachmentsApi.md#apiIssueAttachmentListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments | 



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

let apiInstance = new ApiManagementClient.ApiIssueAttachmentsApi();
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


## apiIssueAttachmentDelete

> apiIssueAttachmentDelete(resourceGroupName, serviceName, apiId, issueId, attachmentId, ifMatch, apiVersion, subscriptionId)



Deletes the specified comment from an Issue.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueAttachmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let attachmentId = "attachmentId_example"; // String | Attachment identifier within an Issue. Must be unique in the current Issue.
let ifMatch = "ifMatch_example"; // String | ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiIssueAttachmentDelete(resourceGroupName, serviceName, apiId, issueId, attachmentId, ifMatch, apiVersion, subscriptionId, (error, data, response) => {
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
 **ifMatch** | **String**| ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiIssueAttachmentGet

> IssueAttachmentContract apiIssueAttachmentGet(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId)



Gets the details of the issue Attachment for an API specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueAttachmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let attachmentId = "attachmentId_example"; // String | Attachment identifier within an Issue. Must be unique in the current Issue.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiIssueAttachmentGet(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**IssueAttachmentContract**](IssueAttachmentContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiIssueAttachmentGetEntityTag

> apiIssueAttachmentGetEntityTag(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the issue Attachment for an API specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueAttachmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let attachmentId = "attachmentId_example"; // String | Attachment identifier within an Issue. Must be unique in the current Issue.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiIssueAttachmentGetEntityTag(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId, (error, data, response) => {
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


## apiIssueAttachmentListByService

> IssueAttachmentCollection apiIssueAttachmentListByService(resourceGroupName, serviceName, apiId, apiVersion, issueId, subscriptionId, opts)



Lists all comments for the Issue associated with the specified API.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiIssueAttachmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith |
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.apiIssueAttachmentListByService(resourceGroupName, serviceName, apiId, apiVersion, issueId, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**IssueAttachmentCollection**](IssueAttachmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

