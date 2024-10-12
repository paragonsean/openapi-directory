# MagentoB2B.ReturnsIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaRmaManagementV1SaveRmaPut**](ReturnsIdApi.md#rmaRmaManagementV1SaveRmaPut) | **PUT** /V1/returns/{id} | returns/{id}
[**rmaRmaRepositoryV1DeleteDelete**](ReturnsIdApi.md#rmaRmaRepositoryV1DeleteDelete) | **DELETE** /V1/returns/{id} | returns/{id}
[**rmaRmaRepositoryV1GetGet**](ReturnsIdApi.md#rmaRmaRepositoryV1GetGet) | **GET** /V1/returns/{id} | returns/{id}



## rmaRmaManagementV1SaveRmaPut

> RmaDataRmaInterface rmaRmaManagementV1SaveRmaPut(id, opts)

returns/{id}

Save RMA

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdApi();
let id = "id_example"; // String | 
let opts = {
  'rmaRmaManagementV1SaveRmaPostRequest': new MagentoB2B.RmaRmaManagementV1SaveRmaPostRequest() // RmaRmaManagementV1SaveRmaPostRequest | 
};
apiInstance.rmaRmaManagementV1SaveRmaPut(id, opts, (error, data, response) => {
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
 **rmaRmaManagementV1SaveRmaPostRequest** | [**RmaRmaManagementV1SaveRmaPostRequest**](RmaRmaManagementV1SaveRmaPostRequest.md)|  | [optional] 

### Return type

[**RmaDataRmaInterface**](RmaDataRmaInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## rmaRmaRepositoryV1DeleteDelete

> Boolean rmaRmaRepositoryV1DeleteDelete(id, opts)

returns/{id}

Delete RMA

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdApi();
let id = "id_example"; // String | 
let opts = {
  'rmaRmaManagementV1SaveRmaPostRequest': new MagentoB2B.RmaRmaManagementV1SaveRmaPostRequest() // RmaRmaManagementV1SaveRmaPostRequest | 
};
apiInstance.rmaRmaRepositoryV1DeleteDelete(id, opts, (error, data, response) => {
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
 **rmaRmaManagementV1SaveRmaPostRequest** | [**RmaRmaManagementV1SaveRmaPostRequest**](RmaRmaManagementV1SaveRmaPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## rmaRmaRepositoryV1GetGet

> RmaDataRmaInterface rmaRmaRepositoryV1GetGet(id)

returns/{id}

Return data object for specified RMA id

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdApi();
let id = 56; // Number | 
apiInstance.rmaRmaRepositoryV1GetGet(id, (error, data, response) => {
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

[**RmaDataRmaInterface**](RmaDataRmaInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

