# AdHybridHealthService.ServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addsServicesDelete**](ServicesApi.md#addsServicesDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName} | 
[**addsServicesGet**](ServicesApi.md#addsServicesGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName} | 
[**addsServicesListPremiumServices**](ServicesApi.md#addsServicesListPremiumServices) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/premiumCheck | 
[**addsServicesUpdate**](ServicesApi.md#addsServicesUpdate) | **PATCH** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName} | 
[**servicesAdd**](ServicesApi.md#servicesAdd) | **POST** /providers/Microsoft.ADHybridHealthService/services | 
[**servicesDelete**](ServicesApi.md#servicesDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/services/{serviceName} | 
[**servicesGet**](ServicesApi.md#servicesGet) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName} | 
[**servicesGetFeatureAvailibility**](ServicesApi.md#servicesGetFeatureAvailibility) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/checkServiceFeatureAvailibility/{featureName} | 
[**servicesGetTenantWhitelisting**](ServicesApi.md#servicesGetTenantWhitelisting) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/TenantWhitelisting/{featureName} | 
[**servicesList**](ServicesApi.md#servicesList) | **GET** /providers/Microsoft.ADHybridHealthService/services | 
[**servicesListExportErrors**](ServicesApi.md#servicesListExportErrors) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/exporterrors/counts | 
[**servicesListExportErrorsV2**](ServicesApi.md#servicesListExportErrorsV2) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/exporterrors/listV2 | 
[**servicesListExportStatus**](ServicesApi.md#servicesListExportStatus) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/exportstatus | 
[**servicesListMonitoringConfigurations**](ServicesApi.md#servicesListMonitoringConfigurations) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/monitoringconfigurations | 
[**servicesListPremium**](ServicesApi.md#servicesListPremium) | **GET** /providers/Microsoft.ADHybridHealthService/services/premiumCheck | 
[**servicesUpdate**](ServicesApi.md#servicesUpdate) | **PATCH** /providers/Microsoft.ADHybridHealthService/services/{serviceName} | 
[**servicesUpdateMonitoringConfiguration**](ServicesApi.md#servicesUpdateMonitoringConfiguration) | **PATCH** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/monitoringconfiguration | 



## addsServicesDelete

> addsServicesDelete(serviceName, apiVersion, opts)



Deletes an Active Directory Domain Service which is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'confirm': true // Boolean | Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered.
};
apiInstance.addsServicesDelete(serviceName, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service which needs to be deleted. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **confirm** | **Boolean**| Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addsServicesGet

> ServiceProperties addsServicesGet(serviceName, apiVersion)



Gets the details of an Active Directory Domain Service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesGet(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesListPremiumServices

> Services addsServicesListPremiumServices(apiVersion, opts)



Gets the details of Active Directory Domain Services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The service property filter to apply.
  'serviceType': "serviceType_example", // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
  'skipCount': 56, // Number | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
  'takeCount': 56 // Number | The take count , which specifies the number of elements that can be returned from a sequence.
};
apiInstance.addsServicesListPremiumServices(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The service property filter to apply. | [optional] 
 **serviceType** | **String**| The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] 
 **skipCount** | **Number**| The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements. | [optional] 
 **takeCount** | **Number**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] 

### Return type

[**Services**](Services.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesUpdate

> ServiceProperties addsServicesUpdate(serviceName, apiVersion, service)



Updates an Active Directory Domain Service properties of an onboarded service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let service = new AdHybridHealthService.ServiceProperties(); // ServiceProperties | The service object.
apiInstance.addsServicesUpdate(serviceName, apiVersion, service, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service which needs to be deleted. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **service** | [**ServiceProperties**](ServiceProperties.md)| The service object. | 

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesAdd

> ServiceProperties servicesAdd(apiVersion, service)



Onboards a service for a given tenant in Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let service = new AdHybridHealthService.ServiceProperties(); // ServiceProperties | The service object.
apiInstance.servicesAdd(apiVersion, service, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **service** | [**ServiceProperties**](ServiceProperties.md)| The service object. | 

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesDelete

> servicesDelete(serviceName, apiVersion, opts)



Deletes a service which is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'confirm': true // Boolean | Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered.
};
apiInstance.servicesDelete(serviceName, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service which needs to be deleted. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **confirm** | **Boolean**| Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## servicesGet

> ServiceProperties servicesGet(serviceName, apiVersion)



Gets the details of a service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesGet(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGetFeatureAvailibility

> Result servicesGetFeatureAvailibility(serviceName, featureName, apiVersion)



Checks if the service has all the pre-requisites met to use a feature.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let featureName = "featureName_example"; // String | The name of the feature.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesGetFeatureAvailibility(serviceName, featureName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **featureName** | **String**| The name of the feature. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Result**](Result.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGetTenantWhitelisting

> Result servicesGetTenantWhitelisting(serviceName, featureName, apiVersion)



Checks if the tenant, to which a service is registered, is whitelisted to use a feature.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let featureName = "featureName_example"; // String | The name of the feature.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesGetTenantWhitelisting(serviceName, featureName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **featureName** | **String**| The name of the feature. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Result**](Result.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesList

> Services servicesList(apiVersion, opts)



Gets the details of services, for a tenant, that are onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The service property filter to apply.
  'serviceType': "serviceType_example", // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
  'skipCount': 56, // Number | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
  'takeCount': 56 // Number | The take count , which specifies the number of elements that can be returned from a sequence.
};
apiInstance.servicesList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The service property filter to apply. | [optional] 
 **serviceType** | **String**| The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] 
 **skipCount** | **Number**| The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements. | [optional] 
 **takeCount** | **Number**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] 

### Return type

[**Services**](Services.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListExportErrors

> ErrorCounts servicesListExportErrors(serviceName, apiVersion)



Gets the count of latest AAD export errors.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListExportErrors(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ErrorCounts**](ErrorCounts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListExportErrorsV2

> MergedExportErrors servicesListExportErrorsV2(serviceName, errorBucket, apiVersion)



 Gets the categorized export errors.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let errorBucket = "errorBucket_example"; // String | The error category to query for.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListExportErrorsV2(serviceName, errorBucket, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **errorBucket** | **String**| The error category to query for. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**MergedExportErrors**](MergedExportErrors.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListExportStatus

> ExportStatuses servicesListExportStatus(serviceName, apiVersion)



Gets the export status.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListExportStatus(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ExportStatuses**](ExportStatuses.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListMonitoringConfigurations

> Items servicesListMonitoringConfigurations(serviceName, apiVersion)



Gets the service level monitoring configurations.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListMonitoringConfigurations(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Items**](Items.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListPremium

> Services servicesListPremium(apiVersion, opts)



Gets the details of services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The service property filter to apply.
  'serviceType': "serviceType_example", // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
  'skipCount': 56, // Number | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
  'takeCount': 56 // Number | The take count , which specifies the number of elements that can be returned from a sequence.
};
apiInstance.servicesListPremium(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The service property filter to apply. | [optional] 
 **serviceType** | **String**| The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] 
 **skipCount** | **Number**| The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements. | [optional] 
 **takeCount** | **Number**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] 

### Return type

[**Services**](Services.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesUpdate

> ServiceProperties servicesUpdate(serviceName, apiVersion, service)



Updates the service properties of an onboarded service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let service = new AdHybridHealthService.ServiceProperties(); // ServiceProperties | The service object.
apiInstance.servicesUpdate(serviceName, apiVersion, service, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service which needs to be deleted. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **service** | [**ServiceProperties**](ServiceProperties.md)| The service object. | 

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesUpdateMonitoringConfiguration

> servicesUpdateMonitoringConfiguration(serviceName, apiVersion, configurationSetting)



Updates the service level monitoring configuration.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServicesApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let configurationSetting = new AdHybridHealthService.Item(); // Item | The monitoring configuration to update
apiInstance.servicesUpdateMonitoringConfiguration(serviceName, apiVersion, configurationSetting, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **configurationSetting** | [**Item**](Item.md)| The monitoring configuration to update | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

