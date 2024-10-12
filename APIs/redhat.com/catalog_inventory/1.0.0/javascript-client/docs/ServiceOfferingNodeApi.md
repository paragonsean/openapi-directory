# CatalogInventory.ServiceOfferingNodeApi

All URIs are relative to *https://cloud.redhat.com//api/catalog-inventory/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listServiceOfferingNodes**](ServiceOfferingNodeApi.md#listServiceOfferingNodes) | **GET** /service_offering_nodes | List ServiceOfferingNodes
[**showServiceOfferingNode**](ServiceOfferingNodeApi.md#showServiceOfferingNode) | **GET** /service_offering_nodes/{id} | Show an existing ServiceOfferingNode



## listServiceOfferingNodes

> ServiceOfferingNodesCollection listServiceOfferingNodes(opts)

List ServiceOfferingNodes

Returns an array of ServiceOfferingNode objects

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingNodeApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return per page.
  'offset': 0, // Number | The number of items to skip before starting to collect the result set.
  'filter': {key: null}, // Object | Filter for querying collections.
  'sortBy': {key: null} // Object | The list of attribute and order to sort the result set by.
};
apiInstance.listServiceOfferingNodes(opts, (error, data, response) => {
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

[**ServiceOfferingNodesCollection**](ServiceOfferingNodesCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showServiceOfferingNode

> ServiceOfferingNode showServiceOfferingNode(id)

Show an existing ServiceOfferingNode

Returns a ServiceOfferingNode object

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingNodeApi();
let id = "id_example"; // String | ID of the resource
apiInstance.showServiceOfferingNode(id, (error, data, response) => {
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

[**ServiceOfferingNode**](ServiceOfferingNode.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

