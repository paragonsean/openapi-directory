# HealthcareApisClient.ProxyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](ProxyApi.md#operationsList) | **GET** /providers/Microsoft.HealthcareApis/operations | 
[**servicesCheckNameAvailability**](ProxyApi.md#servicesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.HealthcareApis/checkNameAvailability | 



## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available Healthcare service REST API operations.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.ProxyApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesCheckNameAvailability

> ServicesNameAvailabilityInfo servicesCheckNameAvailability(apiVersion, subscriptionId, checkNameAvailabilityInputs)



Check if a service instance name is available.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.ProxyApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let checkNameAvailabilityInputs = new HealthcareApisClient.CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Set the name parameter in the CheckNameAvailabilityParameters structure to the name of the service instance to check.
apiInstance.servicesCheckNameAvailability(apiVersion, subscriptionId, checkNameAvailabilityInputs, (error, data, response) => {
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
 **checkNameAvailabilityInputs** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Set the name parameter in the CheckNameAvailabilityParameters structure to the name of the service instance to check. | 

### Return type

[**ServicesNameAvailabilityInfo**](ServicesNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

