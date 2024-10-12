# AkeneoPimRestApi.MeasureFamilyApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measureFamiliesGet**](MeasureFamilyApi.md#measureFamiliesGet) | **GET** /api/rest/v1/measure-families/{code} | Get a measure family
[**measureFamiliesGetList**](MeasureFamilyApi.md#measureFamiliesGetList) | **GET** /api/rest/v1/measure-families | Get list of measure familiy



## measureFamiliesGet

> MeasureFamiliesGet200Response measureFamiliesGet(code)

Get a measure family

This endpoint allows you to get the information about a given measure family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.MeasureFamilyApi();
let code = "code_example"; // String | Code of the resource
apiInstance.measureFamiliesGet(code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

[**MeasureFamiliesGet200Response**](MeasureFamiliesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## measureFamiliesGetList

> MeasureFamilies measureFamiliesGetList()

Get list of measure familiy

This endpoint allows you to get a list of measure families. Measure families are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.MeasureFamilyApi();
apiInstance.measureFamiliesGetList((error, data, response) => {
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

[**MeasureFamilies**](MeasureFamilies.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message

