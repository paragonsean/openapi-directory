# DomainsApiClient.DomainsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainsCheckAvailability**](DomainsApi.md#domainsCheckAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/checkDomainAvailability | Check if a domain is available for registration.
[**domainsCreateOrUpdate**](DomainsApi.md#domainsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Creates or updates a domain.
[**domainsCreateOrUpdateOwnershipIdentifier**](DomainsApi.md#domainsCreateOrUpdateOwnershipIdentifier) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/domainOwnershipIdentifiers/{name} | Creates an ownership identifier for a domain or updates identifier details for an existing identifer
[**domainsDelete**](DomainsApi.md#domainsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Delete a domain.
[**domainsDeleteOwnershipIdentifier**](DomainsApi.md#domainsDeleteOwnershipIdentifier) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/domainOwnershipIdentifiers/{name} | Delete ownership identifier for domain
[**domainsGet**](DomainsApi.md#domainsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Get a domain.
[**domainsGetControlCenterSsoRequest**](DomainsApi.md#domainsGetControlCenterSsoRequest) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/generateSsoRequest | Generate a single sign-on request for the domain management portal.
[**domainsGetOwnershipIdentifier**](DomainsApi.md#domainsGetOwnershipIdentifier) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/domainOwnershipIdentifiers/{name} | Get ownership identifier for domain
[**domainsList**](DomainsApi.md#domainsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/domains | Get all domains in a subscription.
[**domainsListByResourceGroup**](DomainsApi.md#domainsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains | Get all domains in a resource group.
[**domainsListOwnershipIdentifiers**](DomainsApi.md#domainsListOwnershipIdentifiers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/domainOwnershipIdentifiers | Lists domain ownership identifiers.
[**domainsListRecommendations**](DomainsApi.md#domainsListRecommendations) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/listDomainRecommendations | Get domain name recommendations based on keywords.
[**domainsRenew**](DomainsApi.md#domainsRenew) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/renew | Renew a domain.
[**domainsUpdate**](DomainsApi.md#domainsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Creates or updates a domain.
[**domainsUpdateOwnershipIdentifier**](DomainsApi.md#domainsUpdateOwnershipIdentifier) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/domainOwnershipIdentifiers/{name} | Creates an ownership identifier for a domain or updates identifier details for an existing identifer



## domainsCheckAvailability

> DomainAvailabilityCheckResult domainsCheckAvailability(subscriptionId, apiVersion, identifier)

Check if a domain is available for registration.

Description for Check if a domain is available for registration.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let identifier = new DomainsApiClient.DomainsCheckAvailabilityRequest(); // DomainsCheckAvailabilityRequest | Name of the domain.
apiInstance.domainsCheckAvailability(subscriptionId, apiVersion, identifier, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **identifier** | [**DomainsCheckAvailabilityRequest**](DomainsCheckAvailabilityRequest.md)| Name of the domain. | 

### Return type

[**DomainAvailabilityCheckResult**](DomainAvailabilityCheckResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainsCreateOrUpdate

> Domain domainsCreateOrUpdate(resourceGroupName, domainName, subscriptionId, apiVersion, domain)

Creates or updates a domain.

Description for Creates or updates a domain.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of the domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domain = new DomainsApiClient.Domain(); // Domain | Domain registration information.
apiInstance.domainsCreateOrUpdate(resourceGroupName, domainName, subscriptionId, apiVersion, domain, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of the domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domain** | [**Domain**](Domain.md)| Domain registration information. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainsCreateOrUpdateOwnershipIdentifier

> DomainOwnershipIdentifier domainsCreateOrUpdateOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion, domainOwnershipIdentifier)

Creates an ownership identifier for a domain or updates identifier details for an existing identifer

Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifer

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of domain.
let name = "name_example"; // String | Name of identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domainOwnershipIdentifier = new DomainsApiClient.DomainOwnershipIdentifier(); // DomainOwnershipIdentifier | A JSON representation of the domain ownership properties.
apiInstance.domainsCreateOrUpdateOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion, domainOwnershipIdentifier, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of domain. | 
 **name** | **String**| Name of identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domainOwnershipIdentifier** | [**DomainOwnershipIdentifier**](DomainOwnershipIdentifier.md)| A JSON representation of the domain ownership properties. | 

### Return type

[**DomainOwnershipIdentifier**](DomainOwnershipIdentifier.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainsDelete

> domainsDelete(resourceGroupName, domainName, subscriptionId, apiVersion, opts)

Delete a domain.

Description for Delete a domain.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of the domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'forceHardDeleteDomain': true // Boolean | Specify <code>true</code> to delete the domain immediately. The default is <code>false</code> which deletes the domain after 24 hours.
};
apiInstance.domainsDelete(resourceGroupName, domainName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of the domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **forceHardDeleteDomain** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to delete the domain immediately. The default is &lt;code&gt;false&lt;/code&gt; which deletes the domain after 24 hours. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsDeleteOwnershipIdentifier

> domainsDeleteOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion)

Delete ownership identifier for domain

Description for Delete ownership identifier for domain

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of domain.
let name = "name_example"; // String | Name of identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsDeleteOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of domain. | 
 **name** | **String**| Name of identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsGet

> Domain domainsGet(resourceGroupName, domainName, subscriptionId, apiVersion)

Get a domain.

Description for Get a domain.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of the domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsGet(resourceGroupName, domainName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of the domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsGetControlCenterSsoRequest

> DomainControlCenterSsoRequest domainsGetControlCenterSsoRequest(subscriptionId, apiVersion)

Generate a single sign-on request for the domain management portal.

Description for Generate a single sign-on request for the domain management portal.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsGetControlCenterSsoRequest(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainControlCenterSsoRequest**](DomainControlCenterSsoRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsGetOwnershipIdentifier

> DomainOwnershipIdentifier domainsGetOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion)

Get ownership identifier for domain

Description for Get ownership identifier for domain

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of domain.
let name = "name_example"; // String | Name of identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsGetOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of domain. | 
 **name** | **String**| Name of identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainOwnershipIdentifier**](DomainOwnershipIdentifier.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsList

> DomainCollection domainsList(subscriptionId, apiVersion)

Get all domains in a subscription.

Description for Get all domains in a subscription.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainCollection**](DomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsListByResourceGroup

> DomainCollection domainsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get all domains in a resource group.

Description for Get all domains in a resource group.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainCollection**](DomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsListOwnershipIdentifiers

> DomainOwnershipIdentifierCollection domainsListOwnershipIdentifiers(resourceGroupName, domainName, subscriptionId, apiVersion)

Lists domain ownership identifiers.

Description for Lists domain ownership identifiers.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsListOwnershipIdentifiers(resourceGroupName, domainName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainOwnershipIdentifierCollection**](DomainOwnershipIdentifierCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsListRecommendations

> NameIdentifierCollection domainsListRecommendations(subscriptionId, apiVersion, parameters)

Get domain name recommendations based on keywords.

Description for Get domain name recommendations based on keywords.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let parameters = new DomainsApiClient.DomainRecommendationSearchParameters(); // DomainRecommendationSearchParameters | Search parameters for domain name recommendations.
apiInstance.domainsListRecommendations(subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **parameters** | [**DomainRecommendationSearchParameters**](DomainRecommendationSearchParameters.md)| Search parameters for domain name recommendations. | 

### Return type

[**NameIdentifierCollection**](NameIdentifierCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainsRenew

> domainsRenew(resourceGroupName, domainName, subscriptionId, apiVersion)

Renew a domain.

Description for Renew a domain.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of the domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainsRenew(resourceGroupName, domainName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of the domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsUpdate

> Domain domainsUpdate(resourceGroupName, domainName, subscriptionId, apiVersion, domain)

Creates or updates a domain.

Description for Creates or updates a domain.

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of the domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domain = new DomainsApiClient.DomainPatchResource(); // DomainPatchResource | Domain registration information.
apiInstance.domainsUpdate(resourceGroupName, domainName, subscriptionId, apiVersion, domain, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of the domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domain** | [**DomainPatchResource**](DomainPatchResource.md)| Domain registration information. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## domainsUpdateOwnershipIdentifier

> DomainOwnershipIdentifier domainsUpdateOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion, domainOwnershipIdentifier)

Creates an ownership identifier for a domain or updates identifier details for an existing identifer

Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifer

### Example

```javascript
import DomainsApiClient from 'domains_api_client';
let defaultClient = DomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainsApiClient.DomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let domainName = "domainName_example"; // String | Name of domain.
let name = "name_example"; // String | Name of identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domainOwnershipIdentifier = new DomainsApiClient.DomainOwnershipIdentifier(); // DomainOwnershipIdentifier | A JSON representation of the domain ownership properties.
apiInstance.domainsUpdateOwnershipIdentifier(resourceGroupName, domainName, name, subscriptionId, apiVersion, domainOwnershipIdentifier, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **domainName** | **String**| Name of domain. | 
 **name** | **String**| Name of identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domainOwnershipIdentifier** | [**DomainOwnershipIdentifier**](DomainOwnershipIdentifier.md)| A JSON representation of the domain ownership properties. | 

### Return type

[**DomainOwnershipIdentifier**](DomainOwnershipIdentifier.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

