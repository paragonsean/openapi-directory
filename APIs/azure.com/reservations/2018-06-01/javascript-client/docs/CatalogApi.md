# AzureReservation.CatalogApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCatalog**](CatalogApi.md#getCatalog) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Capacity/catalogs | Get the regions and skus that are available for RI purchase for the specified Azure subscription.



## getCatalog

> [Catalog] getCatalog(apiVersion, subscriptionId, reservedResourceType, opts)

Get the regions and skus that are available for RI purchase for the specified Azure subscription.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.CatalogApi();
let apiVersion = "apiVersion_example"; // String | Supported version.
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription
let reservedResourceType = "reservedResourceType_example"; // String | The type of the resource for which the skus should be provided.
let opts = {
  'location': "location_example" // String | Filters the skus based on the location specified in this parameter. This can be an azure region or global
};
apiInstance.getCatalog(apiVersion, subscriptionId, reservedResourceType, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version. | 
 **subscriptionId** | **String**| Id of the subscription | 
 **reservedResourceType** | **String**| The type of the resource for which the skus should be provided. | 
 **location** | **String**| Filters the skus based on the location specified in this parameter. This can be an azure region or global | [optional] 

### Return type

[**[Catalog]**](Catalog.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

