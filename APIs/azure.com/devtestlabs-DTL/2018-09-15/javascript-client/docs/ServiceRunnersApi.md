# DevTestLabsClient.ServiceRunnersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceRunnersCreateOrUpdate**](ServiceRunnersApi.md#serviceRunnersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/servicerunners/{name} | 
[**serviceRunnersDelete**](ServiceRunnersApi.md#serviceRunnersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/servicerunners/{name} | 
[**serviceRunnersGet**](ServiceRunnersApi.md#serviceRunnersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/servicerunners/{name} | 



## serviceRunnersCreateOrUpdate

> ServiceRunner serviceRunnersCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, serviceRunner)



Create or replace an existing service runner.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceRunnersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the service runner.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let serviceRunner = new DevTestLabsClient.ServiceRunner(); // ServiceRunner | A container for a managed identity to execute DevTest lab services.
apiInstance.serviceRunnersCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, serviceRunner, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the service runner. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **serviceRunner** | [**ServiceRunner**](ServiceRunner.md)| A container for a managed identity to execute DevTest lab services. | 

### Return type

[**ServiceRunner**](ServiceRunner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceRunnersDelete

> serviceRunnersDelete(subscriptionId, resourceGroupName, labName, name, apiVersion)



Delete service runner.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceRunnersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the service runner.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceRunnersDelete(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the service runner. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceRunnersGet

> ServiceRunner serviceRunnersGet(subscriptionId, resourceGroupName, labName, name, apiVersion)



Get service runner.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceRunnersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the service runner.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceRunnersGet(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the service runner. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

[**ServiceRunner**](ServiceRunner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

