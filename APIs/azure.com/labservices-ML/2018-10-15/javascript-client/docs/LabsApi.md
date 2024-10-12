# ManagedLabsClient.LabsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**labsAddUsers**](LabsApi.md#labsAddUsers) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/addUsers | 
[**labsCreateOrUpdate**](LabsApi.md#labsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} | 
[**labsDelete**](LabsApi.md#labsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} | 
[**labsGet**](LabsApi.md#labsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} | 
[**labsList**](LabsApi.md#labsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs | 
[**labsRegister**](LabsApi.md#labsRegister) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/register | 
[**labsUpdate**](LabsApi.md#labsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} | 



## labsAddUsers

> labsAddUsers(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, addUsersPayload)



Add users to a lab

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let addUsersPayload = new ManagedLabsClient.AddUsersPayload(); // AddUsersPayload | Payload for Add Users operation on a Lab.
apiInstance.labsAddUsers(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, addUsersPayload, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **addUsersPayload** | [**AddUsersPayload**](AddUsersPayload.md)| Payload for Add Users operation on a Lab. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## labsCreateOrUpdate

> Lab labsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab)



Create or replace an existing Lab.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let lab = new ManagedLabsClient.Lab(); // Lab | Represents a lab.
apiInstance.labsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **lab** | [**Lab**](Lab.md)| Represents a lab. | 

### Return type

[**Lab**](Lab.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## labsDelete

> labsDelete(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion)



Delete lab. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.labsDelete(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labsGet

> Lab labsGet(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts)



Get lab

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=maxUsersInLab)'
};
apiInstance.labsGet(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;maxUsersInLab)&#39; | [optional] 

### Return type

[**Lab**](Lab.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labsList

> ResponseWithContinuationLab labsList(subscriptionId, resourceGroupName, labAccountName, apiVersion, opts)



List labs in a given lab account.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=maxUsersInLab)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.labsList(subscriptionId, resourceGroupName, labAccountName, apiVersion, opts, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;maxUsersInLab)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationLab**](ResponseWithContinuationLab.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labsRegister

> labsRegister(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion)



Register to managed lab.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.labsRegister(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labsUpdate

> Lab labsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab)



Modify properties of labs.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let lab = new ManagedLabsClient.LabFragment(); // LabFragment | Represents a lab.
apiInstance.labsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **lab** | [**LabFragment**](LabFragment.md)| Represents a lab. | 

### Return type

[**Lab**](Lab.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

