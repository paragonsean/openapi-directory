# AzureMachineLearningModelManagementService.ProfileApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profilesCreate**](ProfileApi.md#profilesCreate) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{imageId}/profiles | Create a Profile.
[**profilesListQuery**](ProfileApi.md#profilesListQuery) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{imageId}/profiles | Get a list of Image Profiles.
[**profilesQueryById**](ProfileApi.md#profilesQueryById) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{imageId}/profiles/{id} | Get a Profile.



## profilesCreate

> profilesCreate(subscriptionId, resourceGroup, workspace, imageId, inputRequest)

Create a Profile.

Create a Profile for an Image.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ProfileApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let imageId = "imageId_example"; // String | The Image Id.
let inputRequest = new AzureMachineLearningModelManagementService.ProfileRequestBase(); // ProfileRequestBase | The payload that is used to create the Profile.
apiInstance.profilesCreate(subscriptionId, resourceGroup, workspace, imageId, inputRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **imageId** | **String**| The Image Id. | 
 **inputRequest** | [**ProfileRequestBase**](ProfileRequestBase.md)| The payload that is used to create the Profile. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## profilesListQuery

> PaginatedProfileResponseList profilesListQuery(subscriptionId, resourceGroup, workspace, imageId, opts)

Get a list of Image Profiles.

If no filter is passed, the query lists all Profiles for the Image. The returned list is paginated and the count of items in each page is an optional parameter.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ProfileApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let imageId = "imageId_example"; // String | The Image Id.
let opts = {
  'name': "name_example", // String | The Profile name.
  'description': "description_example", // String | The Profile description.
  'tags': "tags_example", // String | A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
  'properties': "properties_example", // String | A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
  'count': 56, // Number | The number of items to retrieve in a page.
  'skipToken': "skipToken_example", // String | The continuation token to retrieve the next page.
  'orderBy': "'CreatedAtDesc'" // String | The option to order the response.
};
apiInstance.profilesListQuery(subscriptionId, resourceGroup, workspace, imageId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **imageId** | **String**| The Image Id. | 
 **name** | **String**| The Profile name. | [optional] 
 **description** | **String**| The Profile description. | [optional] 
 **tags** | **String**| A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3 | [optional] 
 **properties** | **String**| A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3 | [optional] 
 **count** | **Number**| The number of items to retrieve in a page. | [optional] 
 **skipToken** | **String**| The continuation token to retrieve the next page. | [optional] 
 **orderBy** | **String**| The option to order the response. | [optional] [default to &#39;CreatedAtDesc&#39;]

### Return type

[**PaginatedProfileResponseList**](PaginatedProfileResponseList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesQueryById

> ProfileResponse profilesQueryById(subscriptionId, resourceGroup, workspace, imageId, id)

Get a Profile.

Get the Profile for an Image.

### Example

```javascript
import AzureMachineLearningModelManagementService from 'azure_machine_learning_model_management_service';
let defaultClient = AzureMachineLearningModelManagementService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMachineLearningModelManagementService.ProfileApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
let workspace = "workspace_example"; // String | The name of the workspace.
let imageId = "imageId_example"; // String | The Image Id.
let id = "id_example"; // String | The Profile Id.
apiInstance.profilesQueryById(subscriptionId, resourceGroup, workspace, imageId, id, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspace** | **String**| The name of the workspace. | 
 **imageId** | **String**| The Image Id. | 
 **id** | **String**| The Profile Id. | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

