# CatalogInventory.ServiceOfferingApi

All URIs are relative to *https://cloud.redhat.com//api/catalog-inventory/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliedInventoriesTagsForServiceOffering**](ServiceOfferingApi.md#appliedInventoriesTagsForServiceOffering) | **POST** /service_offerings/{id}/applied_inventories_tags | Invokes computing of ServiceInventories tags for given ServiceOffering
[**listServiceOfferingServiceInstances**](ServiceOfferingApi.md#listServiceOfferingServiceInstances) | **GET** /service_offerings/{id}/service_instances | List ServiceInstances for ServiceOffering
[**listServiceOfferingServiceOfferingNodes**](ServiceOfferingApi.md#listServiceOfferingServiceOfferingNodes) | **GET** /service_offerings/{id}/service_offering_nodes | List ServiceOfferingNodes for ServiceOffering
[**listServiceOfferingServicePlans**](ServiceOfferingApi.md#listServiceOfferingServicePlans) | **GET** /service_offerings/{id}/service_plans | List ServicePlans for ServiceOffering
[**listServiceOfferings**](ServiceOfferingApi.md#listServiceOfferings) | **GET** /service_offerings | List ServiceOfferings
[**orderServiceOffering**](ServiceOfferingApi.md#orderServiceOffering) | **POST** /service_offerings/{id}/order | Order an existing ServiceOffering
[**showServiceOffering**](ServiceOfferingApi.md#showServiceOffering) | **GET** /service_offerings/{id} | Show an existing ServiceOffering



## appliedInventoriesTagsForServiceOffering

> [Tag] appliedInventoriesTagsForServiceOffering(id, appliedInventoriesParametersServicePlan)

Invokes computing of ServiceInventories tags for given ServiceOffering

Returns an array of inventories tags

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingApi();
let id = "id_example"; // String | ID of the resource
let appliedInventoriesParametersServicePlan = new CatalogInventory.AppliedInventoriesParametersServicePlan(); // AppliedInventoriesParametersServicePlan | Parameters defining input data for computing inventories
apiInstance.appliedInventoriesTagsForServiceOffering(id, appliedInventoriesParametersServicePlan, (error, data, response) => {
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
 **appliedInventoriesParametersServicePlan** | [**AppliedInventoriesParametersServicePlan**](AppliedInventoriesParametersServicePlan.md)| Parameters defining input data for computing inventories | 

### Return type

[**[Tag]**](Tag.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listServiceOfferingServiceInstances

> ServiceInstancesCollection listServiceOfferingServiceInstances(id, opts)

List ServiceInstances for ServiceOffering

Returns an array of ServiceInstance objects

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingApi();
let id = "id_example"; // String | ID of the resource
let opts = {
  'limit': 100, // Number | The numbers of items to return per page.
  'offset': 0, // Number | The number of items to skip before starting to collect the result set.
  'filter': {key: null}, // Object | Filter for querying collections.
  'sortBy': {key: null} // Object | The list of attribute and order to sort the result set by.
};
apiInstance.listServiceOfferingServiceInstances(id, opts, (error, data, response) => {
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


## listServiceOfferingServiceOfferingNodes

> ServiceOfferingNodesCollection listServiceOfferingServiceOfferingNodes(id, opts)

List ServiceOfferingNodes for ServiceOffering

Returns an array of ServiceOfferingNode objects

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingApi();
let id = "id_example"; // String | ID of the resource
let opts = {
  'limit': 100, // Number | The numbers of items to return per page.
  'offset': 0, // Number | The number of items to skip before starting to collect the result set.
  'filter': {key: null}, // Object | Filter for querying collections.
  'sortBy': {key: null} // Object | The list of attribute and order to sort the result set by.
};
apiInstance.listServiceOfferingServiceOfferingNodes(id, opts, (error, data, response) => {
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


## listServiceOfferingServicePlans

> ServicePlansCollection listServiceOfferingServicePlans(id, opts)

List ServicePlans for ServiceOffering

Returns an array of ServicePlan objects

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingApi();
let id = "id_example"; // String | ID of the resource
let opts = {
  'limit': 100, // Number | The numbers of items to return per page.
  'offset': 0, // Number | The number of items to skip before starting to collect the result set.
  'filter': {key: null}, // Object | Filter for querying collections.
  'sortBy': {key: null} // Object | The list of attribute and order to sort the result set by.
};
apiInstance.listServiceOfferingServicePlans(id, opts, (error, data, response) => {
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
 **limit** | **Number**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**Object**](.md)| Filter for querying collections. | [optional] 
 **sortBy** | [**Object**](.md)| The list of attribute and order to sort the result set by. | [optional] 

### Return type

[**ServicePlansCollection**](ServicePlansCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceOfferings

> ServiceOfferingsCollection listServiceOfferings(opts)

List ServiceOfferings

Returns an array of ServiceOffering objects

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return per page.
  'offset': 0, // Number | The number of items to skip before starting to collect the result set.
  'filter': {key: null}, // Object | Filter for querying collections.
  'sortBy': {key: null} // Object | The list of attribute and order to sort the result set by.
};
apiInstance.listServiceOfferings(opts, (error, data, response) => {
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

[**ServiceOfferingsCollection**](ServiceOfferingsCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderServiceOffering

> OrderServiceOffering200Response orderServiceOffering(id, orderParametersServiceOffering)

Order an existing ServiceOffering

Returns a Task id

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingApi();
let id = "id_example"; // String | ID of the resource
let orderParametersServiceOffering = new CatalogInventory.OrderParametersServiceOffering(); // OrderParametersServiceOffering | Order parameters defining the service and provider control
apiInstance.orderServiceOffering(id, orderParametersServiceOffering, (error, data, response) => {
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
 **orderParametersServiceOffering** | [**OrderParametersServiceOffering**](OrderParametersServiceOffering.md)| Order parameters defining the service and provider control | 

### Return type

[**OrderServiceOffering200Response**](OrderServiceOffering200Response.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## showServiceOffering

> ServiceOffering showServiceOffering(id)

Show an existing ServiceOffering

Returns a ServiceOffering object

### Example

```javascript
import CatalogInventory from 'catalog_inventory';
let defaultClient = CatalogInventory.ApiClient.instance;
// Configure HTTP basic authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.username = 'YOUR USERNAME';
UserSecurity.password = 'YOUR PASSWORD';

let apiInstance = new CatalogInventory.ServiceOfferingApi();
let id = "id_example"; // String | ID of the resource
apiInstance.showServiceOffering(id, (error, data, response) => {
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

[**ServiceOffering**](ServiceOffering.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

