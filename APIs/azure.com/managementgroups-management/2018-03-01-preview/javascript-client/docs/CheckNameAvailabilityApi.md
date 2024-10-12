# ManagementGroups.CheckNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkNameAvailability**](CheckNameAvailabilityApi.md#checkNameAvailability) | **POST** /providers/Microsoft.Management/checkNameAvailability | 



## checkNameAvailability

> CheckNameAvailabilityResult checkNameAvailability(apiVersion, checkNameAvailabilityRequest)



Checks if the specified management group name is valid and unique

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.CheckNameAvailabilityApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let checkNameAvailabilityRequest = new ManagementGroups.CheckNameAvailabilityRequest(); // CheckNameAvailabilityRequest | Management group name availability check parameters.
apiInstance.checkNameAvailability(apiVersion, checkNameAvailabilityRequest, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **checkNameAvailabilityRequest** | [**CheckNameAvailabilityRequest**](CheckNameAvailabilityRequest.md)| Management group name availability check parameters. | 

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

