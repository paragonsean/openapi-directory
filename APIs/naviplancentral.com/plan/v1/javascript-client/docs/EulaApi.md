# NaviPlanApi.EulaApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eulaAccept**](EulaApi.md#eulaAccept) | **POST** /api/Eula/Accept | Accepts the EULA



## eulaAccept

> eulaAccept()

Accepts the EULA

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.EulaApi();
apiInstance.eulaAccept((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

