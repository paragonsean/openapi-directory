# SubscriptionDefinitionsClient.SubscriptionDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionDefinitionsCreate**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsCreate) | **PUT** /providers/Microsoft.Subscription/subscriptionDefinitions/{subscriptionDefinitionName} | 
[**subscriptionDefinitionsGet**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsGet) | **GET** /providers/Microsoft.Subscription/subscriptionDefinitions/{subscriptionDefinitionName} | 
[**subscriptionDefinitionsGetOperationStatus**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsGetOperationStatus) | **GET** /providers/Microsoft.Subscription/subscriptionOperations/{operationId} | 
[**subscriptionDefinitionsList**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsList) | **GET** /providers/Microsoft.Subscription/subscriptionDefinitions | 
[**subscriptionDefinitionsOperationMetadataList**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsOperationMetadataList) | **GET** /providers/Microsoft.Subscription/operations | 



## subscriptionDefinitionsCreate

> SubscriptionDefinition subscriptionDefinitionsCreate(subscriptionDefinitionName, apiVersion, body)



Create an Azure subscription definition.

### Example

```javascript
import SubscriptionDefinitionsClient from 'subscription_definitions_client';
let defaultClient = SubscriptionDefinitionsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionDefinitionsClient.SubscriptionDefinitionsApi();
let subscriptionDefinitionName = "subscriptionDefinitionName_example"; // String | The name of the Azure subscription definition.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
let body = new SubscriptionDefinitionsClient.SubscriptionDefinition(); // SubscriptionDefinition | The subscription definition creation.
apiInstance.subscriptionDefinitionsCreate(subscriptionDefinitionName, apiVersion, body, (error, data, response) => {
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
 **subscriptionDefinitionName** | **String**| The name of the Azure subscription definition. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | 
 **body** | [**SubscriptionDefinition**](SubscriptionDefinition.md)| The subscription definition creation. | 

### Return type

[**SubscriptionDefinition**](SubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionDefinitionsGet

> SubscriptionDefinition subscriptionDefinitionsGet(subscriptionDefinitionName, apiVersion)



Get an Azure subscription definition.

### Example

```javascript
import SubscriptionDefinitionsClient from 'subscription_definitions_client';
let defaultClient = SubscriptionDefinitionsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionDefinitionsClient.SubscriptionDefinitionsApi();
let subscriptionDefinitionName = "subscriptionDefinitionName_example"; // String | The name of the Azure subscription definition.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
apiInstance.subscriptionDefinitionsGet(subscriptionDefinitionName, apiVersion, (error, data, response) => {
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
 **subscriptionDefinitionName** | **String**| The name of the Azure subscription definition. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | 

### Return type

[**SubscriptionDefinition**](SubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionDefinitionsGetOperationStatus

> SubscriptionDefinition subscriptionDefinitionsGetOperationStatus(apiVersion, operationId)



Retrieves the status of the subscription definition PUT operation. The URI of this API is returned in the Location field of the response header.

### Example

```javascript
import SubscriptionDefinitionsClient from 'subscription_definitions_client';
let defaultClient = SubscriptionDefinitionsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionDefinitionsClient.SubscriptionDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
let operationId = "operationId_example"; // String | The operation ID, which can be found from the Location field in the generate recommendation response header.
apiInstance.subscriptionDefinitionsGetOperationStatus(apiVersion, operationId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | 
 **operationId** | **String**| The operation ID, which can be found from the Location field in the generate recommendation response header. | 

### Return type

[**SubscriptionDefinition**](SubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionDefinitionsList

> SubscriptionDefinitionList subscriptionDefinitionsList(apiVersion)



List an Azure subscription definition by subscriptionId.

### Example

```javascript
import SubscriptionDefinitionsClient from 'subscription_definitions_client';
let defaultClient = SubscriptionDefinitionsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionDefinitionsClient.SubscriptionDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
apiInstance.subscriptionDefinitionsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | 

### Return type

[**SubscriptionDefinitionList**](SubscriptionDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionDefinitionsOperationMetadataList

> OperationListResult subscriptionDefinitionsOperationMetadataList(apiVersion)



Lists all of the available Microsoft.Subscription API operations.

### Example

```javascript
import SubscriptionDefinitionsClient from 'subscription_definitions_client';
let defaultClient = SubscriptionDefinitionsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionDefinitionsClient.SubscriptionDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
apiInstance.subscriptionDefinitionsOperationMetadataList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

