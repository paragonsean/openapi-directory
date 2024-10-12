# ManagedLabsClient.LabAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**labAccountsCreateLab**](LabAccountsApi.md#labAccountsCreateLab) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/createLab | 
[**labAccountsCreateOrUpdate**](LabAccountsApi.md#labAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} | 
[**labAccountsDelete**](LabAccountsApi.md#labAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} | 
[**labAccountsGet**](LabAccountsApi.md#labAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} | 
[**labAccountsGetRegionalAvailability**](LabAccountsApi.md#labAccountsGetRegionalAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/getRegionalAvailability | 
[**labAccountsListByResourceGroup**](LabAccountsApi.md#labAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts | 
[**labAccountsListBySubscription**](LabAccountsApi.md#labAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.LabServices/labaccounts | 
[**labAccountsUpdate**](LabAccountsApi.md#labAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} | 



## labAccountsCreateLab

> labAccountsCreateLab(subscriptionId, resourceGroupName, labAccountName, apiVersion, createLabProperties)



Create a lab in a lab account.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let createLabProperties = new ManagedLabsClient.CreateLabProperties(); // CreateLabProperties | Properties for creating a managed lab and a default environment setting
apiInstance.labAccountsCreateLab(subscriptionId, resourceGroupName, labAccountName, apiVersion, createLabProperties, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **createLabProperties** | [**CreateLabProperties**](CreateLabProperties.md)| Properties for creating a managed lab and a default environment setting | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## labAccountsCreateOrUpdate

> LabAccount labAccountsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount)



Create or replace an existing Lab Account.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let labAccount = new ManagedLabsClient.LabAccount(); // LabAccount | Represents a lab account.
apiInstance.labAccountsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount, (error, data, response) => {
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
 **labAccount** | [**LabAccount**](LabAccount.md)| Represents a lab account. | 

### Return type

[**LabAccount**](LabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## labAccountsDelete

> labAccountsDelete(subscriptionId, resourceGroupName, labAccountName, apiVersion)



Delete lab account. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.labAccountsDelete(subscriptionId, resourceGroupName, labAccountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labAccountsGet

> LabAccount labAccountsGet(subscriptionId, resourceGroupName, labAccountName, apiVersion, opts)



Get lab account

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($expand=sizeConfiguration)'
};
apiInstance.labAccountsGet(subscriptionId, resourceGroupName, labAccountName, apiVersion, opts, (error, data, response) => {
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
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39; | [optional] 

### Return type

[**LabAccount**](LabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labAccountsGetRegionalAvailability

> GetRegionalAvailabilityResponse labAccountsGetRegionalAvailability(subscriptionId, resourceGroupName, labAccountName, apiVersion)



Get regional availability information for each size category configured under a lab account

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.labAccountsGetRegionalAvailability(subscriptionId, resourceGroupName, labAccountName, apiVersion, (error, data, response) => {
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

### Return type

[**GetRegionalAvailabilityResponse**](GetRegionalAvailabilityResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labAccountsListByResourceGroup

> ResponseWithContinuationLabAccount labAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



List lab accounts in a resource group.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($expand=sizeConfiguration)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.labAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationLabAccount**](ResponseWithContinuationLabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labAccountsListBySubscription

> ResponseWithContinuationLabAccount labAccountsListBySubscription(subscriptionId, apiVersion, opts)



List lab accounts in a subscription.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($expand=sizeConfiguration)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.labAccountsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationLabAccount**](ResponseWithContinuationLabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## labAccountsUpdate

> LabAccount labAccountsUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount)



Modify properties of lab accounts.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.LabAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let labAccount = new ManagedLabsClient.LabAccountFragment(); // LabAccountFragment | Represents a lab account.
apiInstance.labAccountsUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount, (error, data, response) => {
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
 **labAccount** | [**LabAccountFragment**](LabAccountFragment.md)| Represents a lab account. | 

### Return type

[**LabAccount**](LabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

