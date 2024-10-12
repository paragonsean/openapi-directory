# AzureStackAzureBridgeClient.RegistrationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registrationsCreateOrUpdate**](RegistrationsApi.md#registrationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} | 
[**registrationsDelete**](RegistrationsApi.md#registrationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} | 
[**registrationsGet**](RegistrationsApi.md#registrationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} | 
[**registrationsGetActivationKey**](RegistrationsApi.md#registrationsGetActivationKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/getactivationkey | 
[**registrationsList**](RegistrationsApi.md#registrationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations | 
[**registrationsUpdate**](RegistrationsApi.md#registrationsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName} | 



## registrationsCreateOrUpdate

> Registration registrationsCreateOrUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token)



Create or update an Azure Stack registration.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.RegistrationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
let token = new AzureStackAzureBridgeClient.RegistrationParameter(); // RegistrationParameter | Registration token
apiInstance.registrationsCreateOrUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]
 **token** | [**RegistrationParameter**](RegistrationParameter.md)| Registration token | 

### Return type

[**Registration**](Registration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registrationsDelete

> registrationsDelete(subscriptionId, resourceGroup, registrationName, apiVersion)



Delete the requested Azure Stack registration.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.RegistrationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.registrationsDelete(subscriptionId, resourceGroup, registrationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationsGet

> Registration registrationsGet(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns the properties of an Azure Stack registration.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.RegistrationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.registrationsGet(subscriptionId, resourceGroup, registrationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**Registration**](Registration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationsGetActivationKey

> ActivationKeyResult registrationsGetActivationKey(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns Azure Stack Activation Key.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.RegistrationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.registrationsGetActivationKey(subscriptionId, resourceGroup, registrationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**ActivationKeyResult**](ActivationKeyResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationsList

> RegistrationList registrationsList(subscriptionId, resourceGroup, apiVersion)



Returns a list of all registrations.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.RegistrationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.registrationsList(subscriptionId, resourceGroup, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**RegistrationList**](RegistrationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationsUpdate

> Registration registrationsUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token)



Patch an Azure Stack registration.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.RegistrationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
let token = new AzureStackAzureBridgeClient.RegistrationParameter(); // RegistrationParameter | Registration token
apiInstance.registrationsUpdate(subscriptionId, resourceGroup, registrationName, apiVersion, token, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]
 **token** | [**RegistrationParameter**](RegistrationParameter.md)| Registration token | 

### Return type

[**Registration**](Registration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

