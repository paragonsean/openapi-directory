# BatchManagement.ApplicationPackageApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationPackageActivate**](ApplicationPackageApi.md#applicationPackageActivate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName}/activate | 
[**applicationPackageCreate**](ApplicationPackageApi.md#applicationPackageCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName} | 
[**applicationPackageDelete**](ApplicationPackageApi.md#applicationPackageDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName} | 
[**applicationPackageGet**](ApplicationPackageApi.md#applicationPackageGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName} | 
[**applicationPackageList**](ApplicationPackageApi.md#applicationPackageList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions | 



## applicationPackageActivate

> ApplicationPackage applicationPackageActivate(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId, parameters)



Activates the specified application package.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationPackageApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let versionName = "versionName_example"; // String | The version of the application.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.ActivateApplicationPackageParameters(); // ActivateApplicationPackageParameters | The parameters for the request.
apiInstance.applicationPackageActivate(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **versionName** | **String**| The version of the application. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**ActivateApplicationPackageParameters**](ActivateApplicationPackageParameters.md)| The parameters for the request. | 

### Return type

[**ApplicationPackage**](ApplicationPackage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationPackageCreate

> ApplicationPackage applicationPackageCreate(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId, opts)



Creates an application package record.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationPackageApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let versionName = "versionName_example"; // String | The version of the application.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let opts = {
  'parameters': new BatchManagement.ApplicationPackage() // ApplicationPackage | The parameters for the request.
};
apiInstance.applicationPackageCreate(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **versionName** | **String**| The version of the application. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**ApplicationPackage**](ApplicationPackage.md)| The parameters for the request. | [optional] 

### Return type

[**ApplicationPackage**](ApplicationPackage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationPackageDelete

> applicationPackageDelete(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId)



Deletes an application package record and its associated binary file.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationPackageApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let versionName = "versionName_example"; // String | The version of the application.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.applicationPackageDelete(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **versionName** | **String**| The version of the application. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationPackageGet

> ApplicationPackage applicationPackageGet(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId)



Gets information about the specified application package.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationPackageApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let versionName = "versionName_example"; // String | The version of the application.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.applicationPackageGet(resourceGroupName, accountName, applicationName, versionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **versionName** | **String**| The version of the application. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**ApplicationPackage**](ApplicationPackage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationPackageList

> ListApplicationPackagesResult applicationPackageList(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, opts)



Lists all of the application packages in the specified application.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.ApplicationPackageApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let applicationName = "applicationName_example"; // String | The name of the application. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let opts = {
  'maxresults': 56 // Number | The maximum number of items to return in the response.
};
apiInstance.applicationPackageList(resourceGroupName, accountName, applicationName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **maxresults** | **Number**| The maximum number of items to return in the response. | [optional] 

### Return type

[**ListApplicationPackagesResult**](ListApplicationPackagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

