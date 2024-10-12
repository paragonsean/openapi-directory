# AzureSqlDatabaseCapabilities.CapabilitiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capabilitiesListByLocation**](CapabilitiesApi.md#capabilitiesListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationId}/capabilities | 



## capabilitiesListByLocation

> LocationCapabilities capabilitiesListByLocation(apiVersion, subscriptionId, locationId)



Gets the capabilities available for the specified location.

### Example

```javascript
import AzureSqlDatabaseCapabilities from 'azure_sql_database_capabilities';

let apiInstance = new AzureSqlDatabaseCapabilities.CapabilitiesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let locationId = "locationId_example"; // String | The location id whose capabilities are retrieved.
apiInstance.capabilitiesListByLocation(apiVersion, subscriptionId, locationId, (error, data, response) => {
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
 **locationId** | **String**| The location id whose capabilities are retrieved. | 

### Return type

[**LocationCapabilities**](LocationCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

