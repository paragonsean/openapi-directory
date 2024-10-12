# WebSiteManagementClient.DomainsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainsCreateOrUpdateDomain**](DomainsApi.md#domainsCreateOrUpdateDomain) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Creates a domain
[**domainsDeleteDomain**](DomainsApi.md#domainsDeleteDomain) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Deletes a domain
[**domainsGetDomain**](DomainsApi.md#domainsGetDomain) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Gets details of a domain
[**domainsGetDomainOperation**](DomainsApi.md#domainsGetDomainOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/operationresults/{operationId} | Retrieves the latest status of a domain purchase operation
[**domainsGetDomains**](DomainsApi.md#domainsGetDomains) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains | Lists domains under a resource group
[**domainsUpdateDomain**](DomainsApi.md#domainsUpdateDomain) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Creates a domain



## domainsCreateOrUpdateDomain

> Domain domainsCreateOrUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain)

Creates a domain

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | &gt;Name of the resource group
let domainName = "domainName_example"; // String | Name of the domain
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let domain = new WebSiteManagementClient.Domain(); // Domain | Domain registration information
apiInstance.domainsCreateOrUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain, (error, data, response) => {
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
 **resourceGroupName** | **String**| &amp;gt;Name of the resource group | 
 **domainName** | **String**| Name of the domain | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **domain** | [**Domain**](Domain.md)| Domain registration information | 

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## domainsDeleteDomain

> Object domainsDeleteDomain(resourceGroupName, domainName, subscriptionId, apiVersion, opts)

Deletes a domain

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let domainName = "domainName_example"; // String | Name of the domain
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'forceHardDeleteDomain': true // Boolean | If true then the domain will be deleted immediately instead of after 24 hours
};
apiInstance.domainsDeleteDomain(resourceGroupName, domainName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **domainName** | **String**| Name of the domain | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **forceHardDeleteDomain** | **Boolean**| If true then the domain will be deleted immediately instead of after 24 hours | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## domainsGetDomain

> Domain domainsGetDomain(resourceGroupName, domainName, subscriptionId, apiVersion)

Gets details of a domain

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let domainName = "domainName_example"; // String | Name of the domain
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsGetDomain(resourceGroupName, domainName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **domainName** | **String**| Name of the domain | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## domainsGetDomainOperation

> Domain domainsGetDomainOperation(resourceGroupName, domainName, operationId, subscriptionId, apiVersion)

Retrieves the latest status of a domain purchase operation

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let domainName = "domainName_example"; // String | Name of the domain
let operationId = "operationId_example"; // String | Domain purchase operation Id
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsGetDomainOperation(resourceGroupName, domainName, operationId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **domainName** | **String**| Name of the domain | 
 **operationId** | **String**| Domain purchase operation Id | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## domainsGetDomains

> DomainCollection domainsGetDomains(resourceGroupName, subscriptionId, apiVersion)

Lists domains under a resource group

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsGetDomains(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainCollection**](DomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## domainsUpdateDomain

> Domain domainsUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain)

Creates a domain

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | &gt;Name of the resource group
let domainName = "domainName_example"; // String | Name of the domain
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let domain = new WebSiteManagementClient.Domain(); // Domain | Domain registration information
apiInstance.domainsUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain, (error, data, response) => {
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
 **resourceGroupName** | **String**| &amp;gt;Name of the resource group | 
 **domainName** | **String**| Name of the domain | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **domain** | [**Domain**](Domain.md)| Domain registration information | 

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

