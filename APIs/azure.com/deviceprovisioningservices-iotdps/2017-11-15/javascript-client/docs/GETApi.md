# IotDpsClient.GETApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dpsCertificateGet**](GETApi.md#dpsCertificateGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName} | 
[**dpsCertificateList**](GETApi.md#dpsCertificateList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates | 
[**iotDpsResourceGet**](GETApi.md#iotDpsResourceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} | Get the non-security related metadata of the provisioning service.
[**iotDpsResourceGetOperationResult**](GETApi.md#iotDpsResourceGetOperationResult) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/operationresults/{operationId} | 
[**iotDpsResourceListByResourceGroup**](GETApi.md#iotDpsResourceListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices | 
[**iotDpsResourceListBySubscription**](GETApi.md#iotDpsResourceListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/provisioningServices | Get all the provisioning services in a subscription.
[**iotDpsResourceListValidSkus**](GETApi.md#iotDpsResourceListValidSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/skus | Get the list of valid SKUs for a provisioning service.



## dpsCertificateGet

> CertificateResponse dpsCertificateGet(certificateName, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, opts)



Get the certificate from the provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.GETApi();
let certificateName = "certificateName_example"; // String | Name of the certificate to retrieve.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of the provisioning service the certificate is associated with.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the certificate.
};
apiInstance.dpsCertificateGet(certificateName, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, opts, (error, data, response) => {
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
 **certificateName** | **String**| Name of the certificate to retrieve. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **provisioningServiceName** | **String**| Name of the provisioning service the certificate is associated with. | 
 **apiVersion** | **String**| The version of the API. | 
 **ifMatch** | **String**| ETag of the certificate. | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dpsCertificateList

> CertificateListDescription dpsCertificateList(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion)



Get all the certificates tied to the provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.GETApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group.
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to retrieve certificates for.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.dpsCertificateList(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Name of resource group. | 
 **provisioningServiceName** | **String**| Name of provisioning service to retrieve certificates for. | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**CertificateListDescription**](CertificateListDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotDpsResourceGet

> ProvisioningServiceDescription iotDpsResourceGet(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)

Get the non-security related metadata of the provisioning service.

Get the metadata of the provisioning service without SAS keys.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.GETApi();
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of the provisioning service to retrieve.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceGet(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **provisioningServiceName** | **String**| Name of the provisioning service to retrieve. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotDpsResourceGetOperationResult

> AsyncOperationResult iotDpsResourceGetOperationResult(operationId, subscriptionId, resourceGroupName, provisioningServiceName, asyncinfo, apiVersion)



Gets the status of a long running operation, such as create, update or delete a provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.GETApi();
let operationId = "operationId_example"; // String | Operation id corresponding to long running operation. Use this to poll for the status.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service that the operation is running on.
let asyncinfo = "'true'"; // String | Async header used to poll on the status of the operation, obtained while creating the long running operation.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceGetOperationResult(operationId, subscriptionId, resourceGroupName, provisioningServiceName, asyncinfo, apiVersion, (error, data, response) => {
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
 **operationId** | **String**| Operation id corresponding to long running operation. Use this to poll for the status. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **provisioningServiceName** | **String**| Name of provisioning service that the operation is running on. | 
 **asyncinfo** | **String**| Async header used to poll on the status of the operation, obtained while creating the long running operation. | [default to &#39;true&#39;]
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**AsyncOperationResult**](AsyncOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotDpsResourceListByResourceGroup

> ProvisioningServiceDescriptionListResult iotDpsResourceListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get a list of all provisioning services in the given resource group.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.GETApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**ProvisioningServiceDescriptionListResult**](ProvisioningServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotDpsResourceListBySubscription

> ProvisioningServiceDescriptionListResult iotDpsResourceListBySubscription(subscriptionId, apiVersion)

Get all the provisioning services in a subscription.

List all the provisioning services for a given subscription id.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.GETApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**ProvisioningServiceDescriptionListResult**](ProvisioningServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotDpsResourceListValidSkus

> IotDpsSkuDefinitionListResult iotDpsResourceListValidSkus(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)

Get the list of valid SKUs for a provisioning service.

Gets the list of valid SKUs and tiers for a provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.GETApi();
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceListValidSkus(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **provisioningServiceName** | **String**| Name of provisioning service. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Name of resource group. | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**IotDpsSkuDefinitionListResult**](IotDpsSkuDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

