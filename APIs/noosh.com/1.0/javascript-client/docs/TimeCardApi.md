# NooshApiApplication.TimeCardApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMyTimeCard**](TimeCardApi.md#getMyTimeCard) | **GET** /v1/workgroups/{workgroup_id}/myTimeCards/{timeCard_id} | Get a specific my time cards
[**getMyTimeCardList**](TimeCardApi.md#getMyTimeCardList) | **GET** /v1/workgroups/{workgroup_id}/myTimeCards | List my time cards
[**getReceivedTimeCard**](TimeCardApi.md#getReceivedTimeCard) | **GET** /v1/workgroups/{workgroup_id}/receivedTimeCards/{timeCard_id} | List a specific received time cards
[**getReceivedTimeCardList**](TimeCardApi.md#getReceivedTimeCardList) | **GET** /v1/workgroups/{workgroup_id}/receivedTimeCards | List received time cards



## getMyTimeCard

> TimeCardDetailVO getMyTimeCard(workgroupId, timeCardId)

Get a specific my time cards

Get a specific my time cards

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TimeCardApi();
let workgroupId = "workgroupId_example"; // String | 
let timeCardId = "timeCardId_example"; // String | 
apiInstance.getMyTimeCard(workgroupId, timeCardId, (error, data, response) => {
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
 **timeCardId** | **String**|  | 

### Return type

[**TimeCardDetailVO**](TimeCardDetailVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getMyTimeCardList

> TimeCardListVO getMyTimeCardList(workgroupId)

List my time cards

List my time cards

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TimeCardApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getMyTimeCardList(workgroupId, (error, data, response) => {
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

[**TimeCardListVO**](TimeCardListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getReceivedTimeCard

> TimeCardReceivedDetailVO getReceivedTimeCard(workgroupId, timeCardId)

List a specific received time cards

List a specific received time cards

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TimeCardApi();
let workgroupId = "workgroupId_example"; // String | 
let timeCardId = "timeCardId_example"; // String | 
apiInstance.getReceivedTimeCard(workgroupId, timeCardId, (error, data, response) => {
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
 **timeCardId** | **String**|  | 

### Return type

[**TimeCardReceivedDetailVO**](TimeCardReceivedDetailVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getReceivedTimeCardList

> TimeCardListVO getReceivedTimeCardList(workgroupId)

List received time cards

List received time cards

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TimeCardApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getReceivedTimeCardList(workgroupId, (error, data, response) => {
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

[**TimeCardListVO**](TimeCardListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

