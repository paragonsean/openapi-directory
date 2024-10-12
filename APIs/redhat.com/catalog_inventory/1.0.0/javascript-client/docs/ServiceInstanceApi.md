# CatalogInventory.ServiceInstanceApi

All URIs are relative to *https://cloud.redhat.com//api/catalog-inventory/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listServiceInstances**](ServiceInstanceApi.md#listServiceInstances) | **GET** /service_instances | List ServiceInstances
[**showServiceInstance**](ServiceInstanceApi.md#showServiceInstance) | **GET** /service_instances/{id} | Show an existing ServiceInstance



## listServiceInstances

> ServiceInstancesCollection listServiceInstances(opts)

List ServiceInstances

Returns an array of ServiceInstance objects

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceInstanceApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return per page.
  'offset': 0, // Number | The number of items to skip before starting to collect the result set.
  'filter': {key: null}, // Object | Filter for querying collections.
  'sortBy': {key: null} // Object | The list of attribute and order to sort the result set by.
};
apiInstance.listServiceInstances(opts, (error, data, response) => {
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
 **limit** | **Number**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**Object**](.md)| Filter for querying collections. | [optional] 
 **sortBy** | [**Object**](.md)| The list of attribute and order to sort the result set by. | [optional] 

### Return type

[**ServiceInstancesCollection**](ServiceInstancesCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showServiceInstance

> ServiceInstance showServiceInstance(id)

Show an existing ServiceInstance

Returns a ServiceInstance object

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceInstanceApi();
let id = "id_example"; // String | ID of the resource
apiInstance.showServiceInstance(id, (error, data, response) => {
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
 **id** | **String**| ID of the resource | 

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

