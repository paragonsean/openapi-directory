# EventGridManagementClient.DomainsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainsCreateOrUpdate**](DomainsApi.md#domainsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Create or update a domain.
[**domainsDelete**](DomainsApi.md#domainsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Delete a domain.
[**domainsGet**](DomainsApi.md#domainsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Get a domain.
[**domainsListByResourceGroup**](DomainsApi.md#domainsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains | List domains under a resource group.
[**domainsListBySubscription**](DomainsApi.md#domainsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/domains | List domains under an Azure subscription.
[**domainsListSharedAccessKeys**](DomainsApi.md#domainsListSharedAccessKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/listKeys | List keys for a domain.
[**domainsRegenerateKey**](DomainsApi.md#domainsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/regenerateKey | Regenerate key for a domain.
[**domainsUpdate**](DomainsApi.md#domainsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Update a domain.



## domainsCreateOrUpdate

> Domain domainsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainInfo)

Create or update a domain.

Asynchronously creates or updates a new domain with the specified parameters.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let domainInfo = new EventGridManagementClient.Domain(); // Domain | Domain information.
apiInstance.domainsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainInfo, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **domainName** | **String**| Name of the domain. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **domainInfo** | [**Domain**](Domain.md)| Domain information. | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainsDelete

> domainsDelete(subscriptionId, resourceGroupName, domainName, apiVersion)

Delete a domain.

Delete existing domain.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.domainsDelete(subscriptionId, resourceGroupName, domainName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **domainName** | **String**| Name of the domain. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainsGet

> Domain domainsGet(subscriptionId, resourceGroupName, domainName, apiVersion)

Get a domain.

Get properties of a domain.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.domainsGet(subscriptionId, resourceGroupName, domainName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **domainName** | **String**| Name of the domain. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsListByResourceGroup

> DomainsListResult domainsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)

List domains under a resource group.

List all the domains under a resource group.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.domainsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**DomainsListResult**](DomainsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsListBySubscription

> DomainsListResult domainsListBySubscription(subscriptionId, apiVersion, opts)

List domains under an Azure subscription.

List all the domains under an Azure subscription.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.domainsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**DomainsListResult**](DomainsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsListSharedAccessKeys

> DomainSharedAccessKeys domainsListSharedAccessKeys(subscriptionId, resourceGroupName, domainName, apiVersion)

List keys for a domain.

List the two keys used to publish to a domain.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.domainsListSharedAccessKeys(subscriptionId, resourceGroupName, domainName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **domainName** | **String**| Name of the domain. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**DomainSharedAccessKeys**](DomainSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsRegenerateKey

> DomainSharedAccessKeys domainsRegenerateKey(subscriptionId, resourceGroupName, domainName, apiVersion, regenerateKeyRequest)

Regenerate key for a domain.

Regenerate a shared access key for a domain.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let regenerateKeyRequest = new EventGridManagementClient.DomainRegenerateKeyRequest(); // DomainRegenerateKeyRequest | Request body to regenerate key.
apiInstance.domainsRegenerateKey(subscriptionId, resourceGroupName, domainName, apiVersion, regenerateKeyRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **domainName** | **String**| Name of the domain. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **regenerateKeyRequest** | [**DomainRegenerateKeyRequest**](DomainRegenerateKeyRequest.md)| Request body to regenerate key. | 

### Return type

[**DomainSharedAccessKeys**](DomainSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainsUpdate

> Domain domainsUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainUpdateParameters)

Update a domain.

Asynchronously updates a domain with the specified parameters.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let domainUpdateParameters = new EventGridManagementClient.DomainUpdateParameters(); // DomainUpdateParameters | Domain update information.
apiInstance.domainsUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainUpdateParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **domainName** | **String**| Name of the domain. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **domainUpdateParameters** | [**DomainUpdateParameters**](DomainUpdateParameters.md)| Domain update information. | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

