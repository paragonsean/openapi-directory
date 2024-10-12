# NooshApiApplication.WorkgroupApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getClientWorkgroupList**](WorkgroupApi.md#getClientWorkgroupList) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups | List client workgroups
[**getSpecificClientWorkgroup**](WorkgroupApi.md#getSpecificClientWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id} | Get a specific client workgroups
[**getSupplierWorkgroupDetail**](WorkgroupApi.md#getSupplierWorkgroupDetail) | **GET** /v1/workgroups/{workgroup_id}/supplierWorkgroups/{bu_supplier_workgroup_id} | Get the specific supplier of My Group
[**getSupplierWorkgroupList**](WorkgroupApi.md#getSupplierWorkgroupList) | **GET** /v1/workgroups/{workgroup_id}/supplierWorkgroups | List supplier workgroups
[**getWorkgroupDetail**](WorkgroupApi.md#getWorkgroupDetail) | **GET** /v1/workgroups/{workgroup_id}/detail | Detail workgroup info
[**getWorkgroupList**](WorkgroupApi.md#getWorkgroupList) | **GET** /v1/workgroups | List the workgroups
[**putWorkgroup**](WorkgroupApi.md#putWorkgroup) | **PUT** /v1/workgroups/{workgroup_id}/detail | Update a specific Workgroup



## getClientWorkgroupList

> ClientWorkgroupListVO getClientWorkgroupList(workgroupId)

List client workgroups

List client workgroups

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getClientWorkgroupList(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**ClientWorkgroupListVO**](ClientWorkgroupListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSpecificClientWorkgroup

> ClientWorkgroupExpandVO getSpecificClientWorkgroup(workgroupId, clientWorkgroupId)

Get a specific client workgroups

Get a specific client workgroups

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupApi();
let workgroupId = "workgroupId_example"; // String | 
let clientWorkgroupId = "clientWorkgroupId_example"; // String | 
apiInstance.getSpecificClientWorkgroup(workgroupId, clientWorkgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **clientWorkgroupId** | **String**|  | 

### Return type

[**ClientWorkgroupExpandVO**](ClientWorkgroupExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSupplierWorkgroupDetail

> SupplierWorkgroupExpandVO getSupplierWorkgroupDetail(workgroupId, buSupplierWorkgroupId)

Get the specific supplier of My Group

Get the specific supplier of My Group

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupApi();
let workgroupId = "workgroupId_example"; // String | 
let buSupplierWorkgroupId = "buSupplierWorkgroupId_example"; // String | 
apiInstance.getSupplierWorkgroupDetail(workgroupId, buSupplierWorkgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **buSupplierWorkgroupId** | **String**|  | 

### Return type

[**SupplierWorkgroupExpandVO**](SupplierWorkgroupExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSupplierWorkgroupList

> SupplierWorkgroupListVO getSupplierWorkgroupList(workgroupId)

List supplier workgroups

List supplier workgroups

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getSupplierWorkgroupList(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**SupplierWorkgroupListVO**](SupplierWorkgroupListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getWorkgroupDetail

> WorkgroupExpandVO getWorkgroupDetail(workgroupId)

Detail workgroup info

Detail workgroup info

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getWorkgroupDetail(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**WorkgroupExpandVO**](WorkgroupExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getWorkgroupList

> WorkgroupListVO getWorkgroupList(opts)

List the workgroups

List the workgroups

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupApi();
let opts = {
  'workgroupName': "workgroupName_example", // String | Workgroup Name
  'workgroupTypes': ["null"] // [String] | 1000001 for Buyer, 1000002 for supplier, 1000003 for agent, 1000004 for Broker/Outsourcer and 1000005 for Partner
};
apiInstance.getWorkgroupList(opts, (error, data, response) => {
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
 **workgroupName** | **String**| Workgroup Name | [optional] 
 **workgroupTypes** | [**[String]**](String.md)| 1000001 for Buyer, 1000002 for supplier, 1000003 for agent, 1000004 for Broker/Outsourcer and 1000005 for Partner | [optional] 

### Return type

[**WorkgroupListVO**](WorkgroupListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## putWorkgroup

> WorkgroupHTTPStatusVO putWorkgroup(workgroupId, opts)

Update a specific Workgroup

Update a specific Workgroup

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupApi();
let workgroupId = "workgroupId_example"; // String | 
let opts = {
  'workgroupUpdPersistVO': new NooshApiApplication.WorkgroupUpdPersistVO() // WorkgroupUpdPersistVO | 
};
apiInstance.putWorkgroup(workgroupId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **workgroupUpdPersistVO** | [**WorkgroupUpdPersistVO**](WorkgroupUpdPersistVO.md)|  | [optional] 

### Return type

[**WorkgroupHTTPStatusVO**](WorkgroupHTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

