# SalesLoftPlatform.TeamApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2TeamJsonGet**](TeamApi.md#v2TeamJsonGet) | **GET** /v2/team.json | Fetch current team



## v2TeamJsonGet

> Team v2TeamJsonGet()

Fetch current team

Fetches the team of the authenticated user. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.TeamApi();
apiInstance.v2TeamJsonGet((error, data, response) => {
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

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

