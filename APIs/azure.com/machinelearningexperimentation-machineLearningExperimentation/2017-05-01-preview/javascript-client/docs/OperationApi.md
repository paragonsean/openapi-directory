# MlTeamAccountManagementClient.OperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationApi.md#operationsList) | **GET** /providers/Microsoft.MachineLearningExperimentation/operations | 



## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available Azure Machine Learning Team Accounts REST API operations.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.OperationApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

