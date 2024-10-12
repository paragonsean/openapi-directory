# SqlManagementClient.LocationCapabilitiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capabilitiesListByLocation**](LocationCapabilitiesApi.md#capabilitiesListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/capabilities | 



## capabilitiesListByLocation

> LocationCapabilities capabilitiesListByLocation(locationName, subscriptionId, apiVersion, opts)



Gets the subscription capabilities available for the specified location.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.LocationCapabilitiesApi();
let locationName = "locationName_example"; // String | The location name whose capabilities are retrieved.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'include': "include_example" // String | If specified, restricts the response to only include the selected item.
};
apiInstance.capabilitiesListByLocation(locationName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **locationName** | **String**| The location name whose capabilities are retrieved. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **include** | **String**| If specified, restricts the response to only include the selected item. | [optional] 

### Return type

[**LocationCapabilities**](LocationCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

