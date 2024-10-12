# AkeneoPimRestApi.MeasurementFamilyApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measurementFamiliesGetList**](MeasurementFamilyApi.md#measurementFamiliesGetList) | **GET** /api/rest/v1/measurement-families | Get list of measurement families
[**patchMeasurementFamilies**](MeasurementFamilyApi.md#patchMeasurementFamilies) | **PATCH** /api/rest/v1/measurement-families | Update/create several measurement families



## measurementFamiliesGetList

> MeasurementFamiliesGetList200Response measurementFamiliesGetList()

Get list of measurement families

This endpoint allows you to get a list of measurement families.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.MeasurementFamilyApi();
apiInstance.measurementFamiliesGetList((error, data, response) => {
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

[**MeasurementFamiliesGetList200Response**](MeasurementFamiliesGetList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchMeasurementFamilies

> [PatchMeasurementFamilies200ResponseInner] patchMeasurementFamilies(opts)

Update/create several measurement families

This endpoint allows you to update and/or create several measurement families at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.MeasurementFamilyApi();
let opts = {
  'body': [new AkeneoPimRestApi.MeasurementFamiliesGetList200Response()] // [MeasurementFamiliesGetList200Response] | 
};
apiInstance.patchMeasurementFamilies(opts, (error, data, response) => {
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
 **body** | [**[MeasurementFamiliesGetList200Response]**](MeasurementFamiliesGetList200Response.md)|  | [optional] 

### Return type

[**[PatchMeasurementFamilies200ResponseInner]**](PatchMeasurementFamilies200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message

