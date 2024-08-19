# Data2CrmApi.RequestApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRequestEntity**](RequestApi.md#createRequestEntity) | **POST** /application/request | POST for request



## createRequestEntity

> RequestEntityRelation createRequestEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body)

POST for request

Execute request into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.RequestApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.RequestEntity(); // RequestEntity | Execute request into the system
apiInstance.createRequestEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **body** | [**RequestEntity**](RequestEntity.md)| Execute request into the system | 

### Return type

[**RequestEntityRelation**](RequestEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

