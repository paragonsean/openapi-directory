# NaviPlanApi.ServiceInformationApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceInformationStatistics**](ServiceInformationApi.md#serviceInformationStatistics) | **GET** /api/ServiceInformation/Statistics | This resource can be used to check the status of the service.



## serviceInformationStatistics

> ServiceInformation serviceInformationStatistics()

This resource can be used to check the status of the service.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ServiceInformationApi();
apiInstance.serviceInformationStatistics((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceInformation**](ServiceInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

