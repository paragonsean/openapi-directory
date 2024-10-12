# AzureLocationBasedServicesResourceProvider.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCreateOrUpdate**](DefaultApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName} | 
[**accountsDelete**](DefaultApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName} | 
[**accountsGet**](DefaultApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName} | 
[**accountsListByResourceGroup**](DefaultApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts | 
[**accountsListBySubscription**](DefaultApi.md#accountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.LocationBasedServices/accounts | 
[**accountsListKeys**](DefaultApi.md#accountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}/listKeys | 
[**accountsListOperations**](DefaultApi.md#accountsListOperations) | **GET** /providers/Microsoft.LocationBasedServices/operations | 
[**accountsMove**](DefaultApi.md#accountsMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources | 
[**accountsRegenerateKeys**](DefaultApi.md#accountsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}/regenerateKey | 
[**accountsUpdate**](DefaultApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName} | 



## accountsCreateOrUpdate

> LocationBasedServicesAccount accountsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, locationBasedServicesAccountCreateParameters)



Create or update a Location Based Services Account. A Location Based Services Account holds the keys which allow access to the Location Based Services REST APIs.

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Location Based Services Account.
let locationBasedServicesAccountCreateParameters = new AzureLocationBasedServicesResourceProvider.LocationBasedServicesAccountCreateParameters(); // LocationBasedServicesAccountCreateParameters | The new or updated parameters for the Location Based Services Account.
apiInstance.accountsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, locationBasedServicesAccountCreateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Location Based Services Account. | 
 **locationBasedServicesAccountCreateParameters** | [**LocationBasedServicesAccountCreateParameters**](LocationBasedServicesAccountCreateParameters.md)| The new or updated parameters for the Location Based Services Account. | 

### Return type

[**LocationBasedServicesAccount**](LocationBasedServicesAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDelete

> accountsDelete(apiVersion, subscriptionId, resourceGroupName, accountName)



Delete a Location Based Services Account

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Location Based Services Account.
apiInstance.accountsDelete(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Location Based Services Account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsGet

> LocationBasedServicesAccount accountsGet(apiVersion, subscriptionId, resourceGroupName, accountName)



Get a Location Based Services Account

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Location Based Services Account.
apiInstance.accountsGet(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Location Based Services Account. | 

### Return type

[**LocationBasedServicesAccount**](LocationBasedServicesAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListByResourceGroup

> LocationBasedServicesAccounts accountsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all Location Based Services Accounts in a Resource Group

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
apiInstance.accountsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 

### Return type

[**LocationBasedServicesAccounts**](LocationBasedServicesAccounts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListBySubscription

> LocationBasedServicesAccounts accountsListBySubscription(apiVersion, subscriptionId)



Get all Location Based Services Accounts in a Subscription

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LocationBasedServicesAccounts**](LocationBasedServicesAccounts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListKeys

> LocationBasedServicesAccountKeys accountsListKeys(apiVersion, subscriptionId, resourceGroupName, accountName)



Get the keys to use with the Location Based Services APIs. A key is used to authenticate and authorize access to the Location Based Services REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Location Based Services Account.
apiInstance.accountsListKeys(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Location Based Services Account. | 

### Return type

[**LocationBasedServicesAccountKeys**](LocationBasedServicesAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListOperations

> LocationBasedServicesOperations accountsListOperations(apiVersion)



List operations available for the Location Based Services Resource Provider

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.accountsListOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**LocationBasedServicesOperations**](LocationBasedServicesOperations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsMove

> accountsMove(apiVersion, subscriptionId, resourceGroupName, moveRequest)



Moves Location Based Services Accounts from one ResourceGroup (or Subscription) to another

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains Location Based Services Account to move.
let moveRequest = new AzureLocationBasedServicesResourceProvider.LocationBasedServicesAccountsMoveRequest(); // LocationBasedServicesAccountsMoveRequest | The details of the Location Based Services Account move.
apiInstance.accountsMove(apiVersion, subscriptionId, resourceGroupName, moveRequest, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains Location Based Services Account to move. | 
 **moveRequest** | [**LocationBasedServicesAccountsMoveRequest**](LocationBasedServicesAccountsMoveRequest.md)| The details of the Location Based Services Account move. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsRegenerateKeys

> LocationBasedServicesAccountKeys accountsRegenerateKeys(apiVersion, subscriptionId, resourceGroupName, accountName, keySpecification)



Regenerate either the primary or secondary key for use with the Location Based Services APIs. The old key will stop working immediately.

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Location Based Services Account.
let keySpecification = new AzureLocationBasedServicesResourceProvider.LocationBasedServicesKeySpecification(); // LocationBasedServicesKeySpecification | Which key to regenerate:  primary or secondary.
apiInstance.accountsRegenerateKeys(apiVersion, subscriptionId, resourceGroupName, accountName, keySpecification, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Location Based Services Account. | 
 **keySpecification** | [**LocationBasedServicesKeySpecification**](LocationBasedServicesKeySpecification.md)| Which key to regenerate:  primary or secondary. | 

### Return type

[**LocationBasedServicesAccountKeys**](LocationBasedServicesAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsUpdate

> LocationBasedServicesAccount accountsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, locationBasedServicesAccountUpdateParameters)



Updates a Location Based Services Account. Only a subset of the parameters may be updated after creation, such as Sku and Tags.

### Example

```javascript
import AzureLocationBasedServicesResourceProvider from 'azure_location_based_services_resource_provider';
let defaultClient = AzureLocationBasedServicesResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLocationBasedServicesResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Location Based Services Account.
let locationBasedServicesAccountUpdateParameters = new AzureLocationBasedServicesResourceProvider.LocationBasedServicesAccountUpdateParameters(); // LocationBasedServicesAccountUpdateParameters | The updated parameters for the Location Based Services Account.
apiInstance.accountsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, locationBasedServicesAccountUpdateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Location Based Services Account. | 
 **locationBasedServicesAccountUpdateParameters** | [**LocationBasedServicesAccountUpdateParameters**](LocationBasedServicesAccountUpdateParameters.md)| The updated parameters for the Location Based Services Account. | 

### Return type

[**LocationBasedServicesAccount**](LocationBasedServicesAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

