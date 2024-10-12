# IoTSpacesClient.ProxyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ioTSpacesCheckNameAvailability**](ProxyApi.md#ioTSpacesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.IoTSpaces/checkNameAvailability | 
[**operationsList**](ProxyApi.md#operationsList) | **GET** /providers/Microsoft.IoTSpaces/operations | 



## ioTSpacesCheckNameAvailability

> IoTSpacesNameAvailabilityInfo ioTSpacesCheckNameAvailability(apiVersion, subscriptionId, operationInputs)



Check if an IoTSpaces instance name is available.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.ProxyApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let operationInputs = new IoTSpacesClient.OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check.
apiInstance.ioTSpacesCheckNameAvailability(apiVersion, subscriptionId, operationInputs, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **operationInputs** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check. | 

### Return type

[**IoTSpacesNameAvailabilityInfo**](IoTSpacesNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available IoTSpaces service REST API operations.

### Example

```javascript
import IoTSpacesClient from 'io_t_spaces_client';
let defaultClient = IoTSpacesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IoTSpacesClient.ProxyApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

