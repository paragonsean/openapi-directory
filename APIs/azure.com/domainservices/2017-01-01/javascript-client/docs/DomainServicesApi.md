# DomainServicesResourceProvider.DomainServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainServiceOperationsList**](DomainServicesApi.md#domainServiceOperationsList) | **GET** /providers/Microsoft.AAD/operations | 
[**domainServicesCreateOrUpdate**](DomainServicesApi.md#domainServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Create or Update Domain Service (PUT Resource)
[**domainServicesDelete**](DomainServicesApi.md#domainServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Delete Domain Service (DELETE Resource)
[**domainServicesGet**](DomainServicesApi.md#domainServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Get Domain Service (GET Resources)
[**domainServicesList**](DomainServicesApi.md#domainServicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AAD/domainServices | List Domain Services in Subscription (GET Resources)
[**domainServicesListByResourceGroup**](DomainServicesApi.md#domainServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices | List Domain Services in Resource Group (GET Resources)
[**domainServicesUpdate**](DomainServicesApi.md#domainServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Update Domain Service (PATCH Resource)



## domainServiceOperationsList

> OperationEntityListResult domainServiceOperationsList(apiVersion)



Lists all the available Domain Services operations.

### Example

```javascript
import DomainServicesResourceProvider from 'domain_services_resource_provider';

let apiInstance = new DomainServicesResourceProvider.DomainServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.domainServiceOperationsList(apiVersion, (error, data, response) => {
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

[**OperationEntityListResult**](OperationEntityListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainServicesCreateOrUpdate

> DomainService domainServicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService)

Create or Update Domain Service (PUT Resource)

The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged.

### Example

```javascript
import DomainServicesResourceProvider from 'domain_services_resource_provider';

let apiInstance = new DomainServicesResourceProvider.DomainServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
let domainService = new DomainServicesResourceProvider.DomainService(); // DomainService | Properties supplied to the Create or Update a Domain Service operation.
apiInstance.domainServicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **domainServiceName** | **String**| The name of the domain service. | 
 **domainService** | [**DomainService**](DomainService.md)| Properties supplied to the Create or Update a Domain Service operation. | 

### Return type

[**DomainService**](DomainService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainServicesDelete

> domainServicesDelete(apiVersion, subscriptionId, resourceGroupName, domainServiceName)

Delete Domain Service (DELETE Resource)

The Delete Domain Service operation deletes an existing Domain Service.

### Example

```javascript
import DomainServicesResourceProvider from 'domain_services_resource_provider';

let apiInstance = new DomainServicesResourceProvider.DomainServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
apiInstance.domainServicesDelete(apiVersion, subscriptionId, resourceGroupName, domainServiceName, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **domainServiceName** | **String**| The name of the domain service. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainServicesGet

> DomainService domainServicesGet(apiVersion, subscriptionId, resourceGroupName, domainServiceName)

Get Domain Service (GET Resources)

The Get Domain Service operation retrieves a json representation of the Domain Service.

### Example

```javascript
import DomainServicesResourceProvider from 'domain_services_resource_provider';

let apiInstance = new DomainServicesResourceProvider.DomainServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
apiInstance.domainServicesGet(apiVersion, subscriptionId, resourceGroupName, domainServiceName, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **domainServiceName** | **String**| The name of the domain service. | 

### Return type

[**DomainService**](DomainService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainServicesList

> DomainServiceListResult domainServicesList(apiVersion, subscriptionId)

List Domain Services in Subscription (GET Resources)

The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription).

### Example

```javascript
import DomainServicesResourceProvider from 'domain_services_resource_provider';

let apiInstance = new DomainServicesResourceProvider.DomainServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.domainServicesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DomainServiceListResult**](DomainServiceListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainServicesListByResourceGroup

> DomainServiceListResult domainServicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

List Domain Services in Resource Group (GET Resources)

The List Domain Services in Resource Group operation lists all the domain services available under the given resource group.

### Example

```javascript
import DomainServicesResourceProvider from 'domain_services_resource_provider';

let apiInstance = new DomainServicesResourceProvider.DomainServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
apiInstance.domainServicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 

### Return type

[**DomainServiceListResult**](DomainServiceListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainServicesUpdate

> DomainService domainServicesUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService)

Update Domain Service (PATCH Resource)

The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body.

### Example

```javascript
import DomainServicesResourceProvider from 'domain_services_resource_provider';

let apiInstance = new DomainServicesResourceProvider.DomainServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
let domainService = new DomainServicesResourceProvider.DomainService(); // DomainService | Properties supplied to the Update a Domain Service operation.
apiInstance.domainServicesUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **domainServiceName** | **String**| The name of the domain service. | 
 **domainService** | [**DomainService**](DomainService.md)| Properties supplied to the Update a Domain Service operation. | 

### Return type

[**DomainService**](DomainService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

