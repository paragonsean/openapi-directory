# MagentoB2B.CreditmemoIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesCreditmemoManagementV1CancelPut**](CreditmemoIdApi.md#salesCreditmemoManagementV1CancelPut) | **PUT** /V1/creditmemo/{id} | creditmemo/{id}
[**salesCreditmemoRepositoryV1GetGet**](CreditmemoIdApi.md#salesCreditmemoRepositoryV1GetGet) | **GET** /V1/creditmemo/{id} | creditmemo/{id}



## salesCreditmemoManagementV1CancelPut

> Boolean salesCreditmemoManagementV1CancelPut(id)

creditmemo/{id}

Cancels a specified credit memo.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CreditmemoIdApi();
let id = 56; // Number | The credit memo ID.
apiInstance.salesCreditmemoManagementV1CancelPut(id, (error, data, response) => {
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
 **id** | **Number**| The credit memo ID. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## salesCreditmemoRepositoryV1GetGet

> SalesDataCreditmemoInterface salesCreditmemoRepositoryV1GetGet(id)

creditmemo/{id}

Loads a specified credit memo.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CreditmemoIdApi();
let id = 56; // Number | The credit memo ID.
apiInstance.salesCreditmemoRepositoryV1GetGet(id, (error, data, response) => {
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
 **id** | **Number**| The credit memo ID. | 

### Return type

[**SalesDataCreditmemoInterface**](SalesDataCreditmemoInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

