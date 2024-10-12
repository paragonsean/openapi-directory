# WebSiteManagementClient.GlobalDomainRegistrationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalDomainRegistrationCheckDomainAvailability**](GlobalDomainRegistrationApi.md#globalDomainRegistrationCheckDomainAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/checkDomainAvailability | Checks if a domain is available for registration
[**globalDomainRegistrationGetAllDomains**](GlobalDomainRegistrationApi.md#globalDomainRegistrationGetAllDomains) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/domains | Lists all domains in a subscription
[**globalDomainRegistrationGetDomainControlCenterSsoRequest**](GlobalDomainRegistrationApi.md#globalDomainRegistrationGetDomainControlCenterSsoRequest) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/generateSsoRequest | Generates a single sign on request for domain management portal
[**globalDomainRegistrationListDomainRecommendations**](GlobalDomainRegistrationApi.md#globalDomainRegistrationListDomainRecommendations) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/listDomainRecommendations | Lists domain recommendations based on keywords
[**globalDomainRegistrationValidateDomainPurchaseInformation**](GlobalDomainRegistrationApi.md#globalDomainRegistrationValidateDomainPurchaseInformation) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/validateDomainRegistrationInformation | Validates domain registration information



## globalDomainRegistrationCheckDomainAvailability

> DomainAvailablilityCheckResult globalDomainRegistrationCheckDomainAvailability(subscriptionId, apiVersion, identifier)

Checks if a domain is available for registration

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalDomainRegistrationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let identifier = new WebSiteManagementClient.NameIdentifier(); // NameIdentifier | Name of the domain
apiInstance.globalDomainRegistrationCheckDomainAvailability(subscriptionId, apiVersion, identifier, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **identifier** | [**NameIdentifier**](NameIdentifier.md)| Name of the domain | 

### Return type

[**DomainAvailablilityCheckResult**](DomainAvailablilityCheckResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## globalDomainRegistrationGetAllDomains

> DomainCollection globalDomainRegistrationGetAllDomains(subscriptionId, apiVersion)

Lists all domains in a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalDomainRegistrationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalDomainRegistrationGetAllDomains(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainCollection**](DomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalDomainRegistrationGetDomainControlCenterSsoRequest

> DomainControlCenterSsoRequest globalDomainRegistrationGetDomainControlCenterSsoRequest(subscriptionId, apiVersion)

Generates a single sign on request for domain management portal

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalDomainRegistrationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalDomainRegistrationGetDomainControlCenterSsoRequest(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DomainControlCenterSsoRequest**](DomainControlCenterSsoRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## globalDomainRegistrationListDomainRecommendations

> NameIdentifierCollection globalDomainRegistrationListDomainRecommendations(subscriptionId, apiVersion, parameters)

Lists domain recommendations based on keywords

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalDomainRegistrationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let parameters = new WebSiteManagementClient.DomainRecommendationSearchParameters(); // DomainRecommendationSearchParameters | Domain recommendation search parameters
apiInstance.globalDomainRegistrationListDomainRecommendations(subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **parameters** | [**DomainRecommendationSearchParameters**](DomainRecommendationSearchParameters.md)| Domain recommendation search parameters | 

### Return type

[**NameIdentifierCollection**](NameIdentifierCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json


## globalDomainRegistrationValidateDomainPurchaseInformation

> Object globalDomainRegistrationValidateDomainPurchaseInformation(subscriptionId, apiVersion, domainRegistrationInput)

Validates domain registration information

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalDomainRegistrationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let domainRegistrationInput = new WebSiteManagementClient.DomainRegistrationInput(); // DomainRegistrationInput | Domain registration information
apiInstance.globalDomainRegistrationValidateDomainPurchaseInformation(subscriptionId, apiVersion, domainRegistrationInput, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **domainRegistrationInput** | [**DomainRegistrationInput**](DomainRegistrationInput.md)| Domain registration information | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

