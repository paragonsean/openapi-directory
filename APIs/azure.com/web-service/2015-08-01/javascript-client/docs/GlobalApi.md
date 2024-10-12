# WebSiteManagementClient.GlobalApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalCheckNameAvailability**](GlobalApi.md#globalCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/checknameavailability | Check if resource name is available
[**globalGetAllCertificates**](GlobalApi.md#globalGetAllCertificates) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/certificates | Get all certificates for a subscription
[**globalGetAllClassicMobileServices**](GlobalApi.md#globalGetAllClassicMobileServices) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/classicMobileServices | Gets all mobile services for a subscription
[**globalGetAllHostingEnvironments**](GlobalApi.md#globalGetAllHostingEnvironments) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/hostingEnvironments | Gets all hostingEnvironments (App Service Environment) for a subscription
[**globalGetAllManagedHostingEnvironments**](GlobalApi.md#globalGetAllManagedHostingEnvironments) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/managedHostingEnvironments | Gets all managed hosting environments for a subscription
[**globalGetAllServerFarms**](GlobalApi.md#globalGetAllServerFarms) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/serverfarms | Gets all App Service Plans for a subscription
[**globalGetAllSites**](GlobalApi.md#globalGetAllSites) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/sites | Gets all Web Apps for a subscription
[**globalGetSubscriptionGeoRegions**](GlobalApi.md#globalGetSubscriptionGeoRegions) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/geoRegions | Gets list of available geo regions
[**globalGetSubscriptionPublishingCredentials**](GlobalApi.md#globalGetSubscriptionPublishingCredentials) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/publishingCredentials | Gets publishing credentials for the subscription owner
[**globalIsHostingEnvironmentNameAvailable**](GlobalApi.md#globalIsHostingEnvironmentNameAvailable) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/ishostingenvironmentnameavailable | Whether hosting environment name is available
[**globalIsHostingEnvironmentWithLegacyNameAvailable**](GlobalApi.md#globalIsHostingEnvironmentWithLegacyNameAvailable) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/ishostingenvironmentnameavailable/{name} | Whether hosting environment name is available
[**globalListPremierAddOnOffers**](GlobalApi.md#globalListPremierAddOnOffers) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/premieraddonoffers | List premier add on offers
[**globalUpdateSubscriptionPublishingCredentials**](GlobalApi.md#globalUpdateSubscriptionPublishingCredentials) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Web/publishingCredentials | Updates publishing credentials for the subscription owner



## globalCheckNameAvailability

> ResourceNameAvailability globalCheckNameAvailability(subscriptionId, apiVersion, request)

Check if resource name is available

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebSiteManagementClient.ResourceNameAvailabilityRequest(); // ResourceNameAvailabilityRequest | Name availability request
apiInstance.globalCheckNameAvailability(subscriptionId, apiVersion, request, (error, data, response) => {
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
 **request** | [**ResourceNameAvailabilityRequest**](ResourceNameAvailabilityRequest.md)| Name availability request | 

### Return type

[**ResourceNameAvailability**](ResourceNameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## globalGetAllCertificates

> CertificateCollection globalGetAllCertificates(subscriptionId, apiVersion)

Get all certificates for a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalGetAllCertificates(subscriptionId, apiVersion, (error, data, response) => {
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

[**CertificateCollection**](CertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalGetAllClassicMobileServices

> ClassicMobileServiceCollection globalGetAllClassicMobileServices(subscriptionId, apiVersion)

Gets all mobile services for a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalGetAllClassicMobileServices(subscriptionId, apiVersion, (error, data, response) => {
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

[**ClassicMobileServiceCollection**](ClassicMobileServiceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalGetAllHostingEnvironments

> HostingEnvironmentCollection globalGetAllHostingEnvironments(subscriptionId, apiVersion)

Gets all hostingEnvironments (App Service Environment) for a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalGetAllHostingEnvironments(subscriptionId, apiVersion, (error, data, response) => {
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

[**HostingEnvironmentCollection**](HostingEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalGetAllManagedHostingEnvironments

> ManagedHostingEnvironmentCollection globalGetAllManagedHostingEnvironments(subscriptionId, apiVersion)

Gets all managed hosting environments for a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalGetAllManagedHostingEnvironments(subscriptionId, apiVersion, (error, data, response) => {
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

[**ManagedHostingEnvironmentCollection**](ManagedHostingEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalGetAllServerFarms

> ServerFarmCollection globalGetAllServerFarms(subscriptionId, apiVersion, opts)

Gets all App Service Plans for a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'detailed': true // Boolean | False to return a subset of App Service Plan properties, true to return all of the properties.              Retrieval of all properties may increase the API latency.
};
apiInstance.globalGetAllServerFarms(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **detailed** | **Boolean**| False to return a subset of App Service Plan properties, true to return all of the properties.              Retrieval of all properties may increase the API latency. | [optional] 

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalGetAllSites

> SiteCollection globalGetAllSites(subscriptionId, apiVersion)

Gets all Web Apps for a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalGetAllSites(subscriptionId, apiVersion, (error, data, response) => {
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

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalGetSubscriptionGeoRegions

> GeoRegionCollection globalGetSubscriptionGeoRegions(subscriptionId, apiVersion, opts)

Gets list of available geo regions

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'sku': "sku_example", // String | Filter only to regions that support this sku
  'linuxWorkersEnabled': true // Boolean | Filter only to regions that support linux workers
};
apiInstance.globalGetSubscriptionGeoRegions(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **sku** | **String**| Filter only to regions that support this sku | [optional] 
 **linuxWorkersEnabled** | **Boolean**| Filter only to regions that support linux workers | [optional] 

### Return type

[**GeoRegionCollection**](GeoRegionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalGetSubscriptionPublishingCredentials

> User globalGetSubscriptionPublishingCredentials(subscriptionId, apiVersion)

Gets publishing credentials for the subscription owner

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalGetSubscriptionPublishingCredentials(subscriptionId, apiVersion, (error, data, response) => {
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

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## globalIsHostingEnvironmentNameAvailable

> Object globalIsHostingEnvironmentNameAvailable(name, subscriptionId, apiVersion)

Whether hosting environment name is available

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let name = "name_example"; // String | Hosting environment name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalIsHostingEnvironmentNameAvailable(name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Hosting environment name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## globalIsHostingEnvironmentWithLegacyNameAvailable

> Object globalIsHostingEnvironmentWithLegacyNameAvailable(name, subscriptionId, apiVersion)

Whether hosting environment name is available

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let name = "name_example"; // String | Hosting environment name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalIsHostingEnvironmentWithLegacyNameAvailable(name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Hosting environment name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## globalListPremierAddOnOffers

> Object globalListPremierAddOnOffers(subscriptionId, apiVersion)

List premier add on offers

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalListPremierAddOnOffers(subscriptionId, apiVersion, (error, data, response) => {
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

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## globalUpdateSubscriptionPublishingCredentials

> User globalUpdateSubscriptionPublishingCredentials(subscriptionId, apiVersion, requestMessage)

Updates publishing credentials for the subscription owner

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let requestMessage = new WebSiteManagementClient.User(); // User | requestMessage with new publishing credentials
apiInstance.globalUpdateSubscriptionPublishingCredentials(subscriptionId, apiVersion, requestMessage, (error, data, response) => {
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
 **requestMessage** | [**User**](User.md)| requestMessage with new publishing credentials | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

