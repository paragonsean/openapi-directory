# HealthcareApisClient.ResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationResultsGet**](ResourceApi.md#operationResultsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HealthcareApis/locations/{locationName}/operationresults/{operationResultId} | 
[**servicesCreateOrUpdate**](ResourceApi.md#servicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} | 
[**servicesDelete**](ResourceApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} | 
[**servicesGet**](ResourceApi.md#servicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} | 
[**servicesUpdate**](ResourceApi.md#servicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} | 



## operationResultsGet

> OperationResultsDescription operationResultsGet(apiVersion, subscriptionId, locationName, operationResultId)



Get the operation result for a long running operation.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let locationName = "locationName_example"; // String | The location of the operation.
let operationResultId = "operationResultId_example"; // String | The ID of the operation result to get.
apiInstance.operationResultsGet(apiVersion, subscriptionId, locationName, operationResultId, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **locationName** | **String**| The location of the operation. | 
 **operationResultId** | **String**| The ID of the operation result to get. | 

### Return type

[**OperationResultsDescription**](OperationResultsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesCreateOrUpdate

> ServicesDescription servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, serviceDescription)



Create or update the metadata of a service instance.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
let resourceName = "resourceName_example"; // String | The name of the service instance.
let serviceDescription = new HealthcareApisClient.ServicesDescription(); // ServicesDescription | The service instance metadata.
apiInstance.servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, serviceDescription, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | 
 **resourceName** | **String**| The name of the service instance. | 
 **serviceDescription** | [**ServicesDescription**](ServicesDescription.md)| The service instance metadata. | 

### Return type

[**ServicesDescription**](ServicesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesDelete

> servicesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete a service instance.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
let resourceName = "resourceName_example"; // String | The name of the service instance.
apiInstance.servicesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | 
 **resourceName** | **String**| The name of the service instance. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGet

> ServicesDescription servicesGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the metadata of a service instance.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
let resourceName = "resourceName_example"; // String | The name of the service instance.
apiInstance.servicesGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | 
 **resourceName** | **String**| The name of the service instance. | 

### Return type

[**ServicesDescription**](ServicesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesUpdate

> ServicesDescription servicesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, servicePatchDescription)



Update the metadata of a service instance.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.ResourceApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
let resourceName = "resourceName_example"; // String | The name of the service instance.
let servicePatchDescription = new HealthcareApisClient.ServicesPatchDescription(); // ServicesPatchDescription | The service instance metadata and security metadata.
apiInstance.servicesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, servicePatchDescription, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | 
 **resourceName** | **String**| The name of the service instance. | 
 **servicePatchDescription** | [**ServicesPatchDescription**](ServicesPatchDescription.md)| The service instance metadata and security metadata. | 

### Return type

[**ServicesDescription**](ServicesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

