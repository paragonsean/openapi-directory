# MagentoB2B.CustomerGroupsIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerGroupRepositoryV1DeleteByIdDelete**](CustomerGroupsIdApi.md#customerGroupRepositoryV1DeleteByIdDelete) | **DELETE** /V1/customerGroups/{id} | customerGroups/{id}
[**customerGroupRepositoryV1GetByIdGet**](CustomerGroupsIdApi.md#customerGroupRepositoryV1GetByIdGet) | **GET** /V1/customerGroups/{id} | customerGroups/{id}
[**customerGroupRepositoryV1SavePut**](CustomerGroupsIdApi.md#customerGroupRepositoryV1SavePut) | **PUT** /V1/customerGroups/{id} | customerGroups/{id}



## customerGroupRepositoryV1DeleteByIdDelete

> Boolean customerGroupRepositoryV1DeleteByIdDelete(id)

customerGroups/{id}

Delete customer group by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsIdApi();
let id = 56; // Number | 
apiInstance.customerGroupRepositoryV1DeleteByIdDelete(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## customerGroupRepositoryV1GetByIdGet

> CustomerDataGroupInterface customerGroupRepositoryV1GetByIdGet(id)

customerGroups/{id}

Get customer group by group ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsIdApi();
let id = 56; // Number | 
apiInstance.customerGroupRepositoryV1GetByIdGet(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## customerGroupRepositoryV1SavePut

> CustomerDataGroupInterface customerGroupRepositoryV1SavePut(id, opts)

customerGroups/{id}

Save customer group.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsIdApi();
let id = "id_example"; // String | 
let opts = {
  'customerGroupRepositoryV1SavePostRequest': new MagentoB2B.CustomerGroupRepositoryV1SavePostRequest() // CustomerGroupRepositoryV1SavePostRequest | 
};
apiInstance.customerGroupRepositoryV1SavePut(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **customerGroupRepositoryV1SavePostRequest** | [**CustomerGroupRepositoryV1SavePostRequest**](CustomerGroupRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

