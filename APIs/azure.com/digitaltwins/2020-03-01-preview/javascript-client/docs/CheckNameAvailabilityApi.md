# AzureDigitalTwinsManagementClient.CheckNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**digitalTwinsCheckNameAvailability**](CheckNameAvailabilityApi.md#digitalTwinsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DigitalTwins/locations/{location}/checkNameAvailability | 



## digitalTwinsCheckNameAvailability

> CheckNameResult digitalTwinsCheckNameAvailability(apiVersion, subscriptionId, location, digitalTwinsInstanceCheckName)



Check if a DigitalTwinsInstance name is available.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.CheckNameAvailabilityApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let location = "location_example"; // String | Location of DigitalTwinsInstance.
let digitalTwinsInstanceCheckName = new AzureDigitalTwinsManagementClient.CheckNameRequest(); // CheckNameRequest | Set the name parameter in the DigitalTwinsInstanceCheckName structure to the name of the DigitalTwinsInstance to check.
apiInstance.digitalTwinsCheckNameAvailability(apiVersion, subscriptionId, location, digitalTwinsInstanceCheckName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **location** | **String**| Location of DigitalTwinsInstance. | 
 **digitalTwinsInstanceCheckName** | [**CheckNameRequest**](CheckNameRequest.md)| Set the name parameter in the DigitalTwinsInstanceCheckName structure to the name of the DigitalTwinsInstance to check. | 

### Return type

[**CheckNameResult**](CheckNameResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

