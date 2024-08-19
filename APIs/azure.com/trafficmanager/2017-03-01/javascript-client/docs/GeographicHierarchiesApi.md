# TrafficManagerManagementClient.GeographicHierarchiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geographicHierarchiesGetDefault**](GeographicHierarchiesApi.md#geographicHierarchiesGetDefault) | **GET** /providers/Microsoft.Network/trafficManagerGeographicHierarchies/default | 



## geographicHierarchiesGetDefault

> TrafficManagerGeographicHierarchy geographicHierarchiesGetDefault(apiVersion)



Gets the default Geographic Hierarchy used by the Geographic traffic routing method.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.GeographicHierarchiesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.geographicHierarchiesGetDefault(apiVersion, (error, data, response) => {
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

[**TrafficManagerGeographicHierarchy**](TrafficManagerGeographicHierarchy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

