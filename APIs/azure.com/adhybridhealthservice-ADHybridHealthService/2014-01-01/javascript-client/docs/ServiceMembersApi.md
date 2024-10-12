# AdHybridHealthService.ServiceMembersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceMembersAdd**](ServiceMembersApi.md#serviceMembersAdd) | **POST** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers | 
[**serviceMembersDelete**](ServiceMembersApi.md#serviceMembersDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId} | 
[**serviceMembersDeleteData**](ServiceMembersApi.md#serviceMembersDeleteData) | **DELETE** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/data | 
[**serviceMembersGet**](ServiceMembersApi.md#serviceMembersGet) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId} | 
[**serviceMembersGetServiceConfiguration**](ServiceMembersApi.md#serviceMembersGetServiceConfiguration) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/serviceconfiguration | 
[**serviceMembersList**](ServiceMembersApi.md#serviceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers | 
[**serviceMembersListConnectors**](ServiceMembersApi.md#serviceMembersListConnectors) | **GET** /providers/Microsoft.ADHybridHealthService/service/{serviceName}/servicemembers/{serviceMemberId}/connectors | 
[**serviceMembersListCredentials**](ServiceMembersApi.md#serviceMembersListCredentials) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/credentials | 
[**serviceMembersListDataFreshness**](ServiceMembersApi.md#serviceMembersListDataFreshness) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/datafreshness | 
[**serviceMembersListExportStatus**](ServiceMembersApi.md#serviceMembersListExportStatus) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/exportstatus | 
[**serviceMembersListGlobalConfiguration**](ServiceMembersApi.md#serviceMembersListGlobalConfiguration) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/globalconfiguration | 



## serviceMembersAdd

> ServiceMember serviceMembersAdd(serviceName, apiVersion, serviceMember)



Onboards  a server, for a given service, to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service under which the server is to be onboarded.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let serviceMember = new AdHybridHealthService.ServiceMember(); // ServiceMember | The server object.
apiInstance.serviceMembersAdd(serviceName, apiVersion, serviceMember, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service under which the server is to be onboarded. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **serviceMember** | [**ServiceMember**](ServiceMember.md)| The server object. | 

### Return type

[**ServiceMember**](ServiceMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceMembersDelete

> serviceMembersDelete(serviceName, serviceMemberId, apiVersion, opts)



Deletes a server that has been onboarded to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'confirm': true // Boolean | Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered.
};
apiInstance.serviceMembersDelete(serviceName, serviceMemberId, apiVersion, opts, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **confirm** | **Boolean**| Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serviceMembersDeleteData

> serviceMembersDeleteData(serviceName, serviceMemberId, apiVersion)



Deletes the data uploaded by the server to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersDeleteData(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serviceMembersGet

> ServiceMember serviceMembersGet(serviceName, serviceMemberId, apiVersion)



Gets the details of a server, for a given service, that are onboarded to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersGet(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ServiceMember**](ServiceMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersGetServiceConfiguration

> ServiceConfiguration serviceMembersGetServiceConfiguration(serviceName, serviceMemberId, apiVersion)



Gets the service configuration.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersGetServiceConfiguration(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ServiceConfiguration**](ServiceConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersList

> ServiceMembers serviceMembersList(serviceName, apiVersion, opts)



Gets the details of the servers, for a given service, that are onboarded to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The server property filter to apply.
  'dimensionType': "dimensionType_example", // String | The server specific dimension.
  'dimensionSignature': "dimensionSignature_example" // String | The value of the dimension.
};
apiInstance.serviceMembersList(serviceName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The server property filter to apply. | [optional] 
 **dimensionType** | **String**| The server specific dimension. | [optional] 
 **dimensionSignature** | **String**| The value of the dimension. | [optional] 

### Return type

[**ServiceMembers**](ServiceMembers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersListConnectors

> Connectors serviceMembersListConnectors(serviceName, serviceMemberId, apiVersion)



Gets the connector details for a service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersListConnectors(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Connectors**](Connectors.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersListCredentials

> Credentials serviceMembersListCredentials(serviceName, serviceMemberId, apiVersion, opts)



Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example" // String | The property filter to apply.
};
apiInstance.serviceMembersListCredentials(serviceName, serviceMemberId, apiVersion, opts, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The property filter to apply. | [optional] 

### Return type

[**Credentials**](Credentials.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersListDataFreshness

> DataFreshnessDetails serviceMembersListDataFreshness(serviceName, serviceMemberId, apiVersion)



Gets the last time when the server uploaded data to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersListDataFreshness(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**DataFreshnessDetails**](DataFreshnessDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersListExportStatus

> ExportStatuses serviceMembersListExportStatus(serviceName, serviceMemberId, apiVersion)



Gets the export status.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersListExportStatus(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ExportStatuses**](ExportStatuses.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersListGlobalConfiguration

> GlobalConfigurations serviceMembersListGlobalConfiguration(serviceName, serviceMemberId, apiVersion)



Gets the global configuration.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ServiceMembersApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersListGlobalConfiguration(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**GlobalConfigurations**](GlobalConfigurations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

