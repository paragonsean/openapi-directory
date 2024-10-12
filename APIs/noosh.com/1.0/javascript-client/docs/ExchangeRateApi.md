# NooshApiApplication.ExchangeRateApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExchangeRateList**](ExchangeRateApi.md#getExchangeRateList) | **GET** /v1/workgroups/{workgroup_id}/exchangeRate | Get Exchange Rate List
[**postExchangeRate**](ExchangeRateApi.md#postExchangeRate) | **POST** /v1/workgroups/{workgroup_id}/exchangeRate | Create Exchange Rates



## getExchangeRateList

> MultiExchangeRateListVO getExchangeRateList(workgroupId)

Get Exchange Rate List

Get Exchange Rate List

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ExchangeRateApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getExchangeRateList(workgroupId, (error, data, response) => {
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

[**MultiExchangeRateListVO**](MultiExchangeRateListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postExchangeRate

> Object postExchangeRate(workgroupId, opts)

Create Exchange Rates

Create Exchange Rates

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ExchangeRateApi();
let workgroupId = "workgroupId_example"; // String | 
let opts = {
  'multiExchangeRatePersistListVO': new NooshApiApplication.MultiExchangeRatePersistListVO() // MultiExchangeRatePersistListVO | 
};
apiInstance.postExchangeRate(workgroupId, opts, (error, data, response) => {
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
 **multiExchangeRatePersistListVO** | [**MultiExchangeRatePersistListVO**](MultiExchangeRatePersistListVO.md)|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

