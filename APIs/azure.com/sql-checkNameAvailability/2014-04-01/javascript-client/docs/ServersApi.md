# AzureSqlDatabase.ServersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serversCheckNameAvailability**](ServersApi.md#serversCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/checkNameAvailability | 



## serversCheckNameAvailability

> CheckNameAvailabilityResponse serversCheckNameAvailability(apiVersion, subscriptionId, parameters)



Determines whether a resource can be created with the specified name.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ServersApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let parameters = new AzureSqlDatabase.CheckNameAvailabilityRequest(); // CheckNameAvailabilityRequest | The parameters to request for name availability.
apiInstance.serversCheckNameAvailability(apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **parameters** | [**CheckNameAvailabilityRequest**](CheckNameAvailabilityRequest.md)| The parameters to request for name availability. | 

### Return type

[**CheckNameAvailabilityResponse**](CheckNameAvailabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

