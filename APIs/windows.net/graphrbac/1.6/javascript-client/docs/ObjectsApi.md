# GraphRbacManagementClient.ObjectsApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**objectsGetObjectsByObjectIds**](ObjectsApi.md#objectsGetObjectsByObjectIds) | **POST** /{tenantID}/getObjectsByObjectIds | 



## objectsGetObjectsByObjectIds

> DirectoryObjectListResult objectsGetObjectsByObjectIds(apiVersion, tenantID, getObjectsParameters)



Gets the directory objects specified in a list of object IDs. You can also specify which resource collections (users, groups, etc.) should be searched by specifying the optional types parameter.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ObjectsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let getObjectsParameters = new GraphRbacManagementClient.GetObjectsParameters(); // GetObjectsParameters | Objects filtering parameters.
apiInstance.objectsGetObjectsByObjectIds(apiVersion, tenantID, getObjectsParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **getObjectsParameters** | [**GetObjectsParameters**](GetObjectsParameters.md)| Objects filtering parameters. | 

### Return type

[**DirectoryObjectListResult**](DirectoryObjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

