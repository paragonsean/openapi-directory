# BatchManagement.ApplicationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationCreate**](ApplicationApi.md#applicationCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName} | 
[**applicationDelete**](ApplicationApi.md#applicationDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName} | 
[**applicationGet**](ApplicationApi.md#applicationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName} | 
[**applicationList**](ApplicationApi.md#applicationList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications | 
[**applicationUpdate**](ApplicationApi.md#applicationUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName} | 



## applicationCreate

> Application applicationCreate(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, opts)



Adds an application to the specified Batch account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let opts = {
  'parameters': new BatchManagement.Application() // Application | The parameters for the request.
};
apiInstance.applicationCreate(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **applicationName** | **String**| The name of the application. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**Application**](Application.md)| The parameters for the request. | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationDelete

> applicationDelete(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId)



Deletes an application.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.applicationDelete(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **applicationName** | **String**| The name of the application. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGet

> Application applicationGet(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId)



Gets information about the specified application.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.applicationGet(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **applicationName** | **String**| The name of the application. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationList

> ListApplicationsResult applicationList(resourceGroupName, accountName, apiVersion, subscriptionId, opts)



Lists all of the applications in the specified account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let opts = {
  'maxresults': 56 // Number | The maximum number of items to return in the response.
};
apiInstance.applicationList(resourceGroupName, accountName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **maxresults** | **Number**| The maximum number of items to return in the response. | [optional] 

### Return type

[**ListApplicationsResult**](ListApplicationsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationUpdate

> Application applicationUpdate(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, parameters)



Updates settings for the specified application.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.Application(); // Application | The parameters for the request.
apiInstance.applicationUpdate(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **applicationName** | **String**| The name of the application. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**Application**](Application.md)| The parameters for the request. | 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

