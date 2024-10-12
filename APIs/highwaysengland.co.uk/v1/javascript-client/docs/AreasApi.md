# HighwaysEnglandApi.AreasApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areasGet**](AreasApi.md#areasGet) | **GET** /v{version}/areas | Returns list of areas
[**vversionAreasAreaIdsGet**](AreasApi.md#vversionAreasAreaIdsGet) | **GET** /v{version}/areas/{area_Ids} | Returns details of selected area



## areasGet

> AreaResponse areasGet(version)

Returns list of areas

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.AreasApi();
let version = "version_example"; // String | 
apiInstance.areasGet(version, (error, data, response) => {
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
 **version** | **String**|  | 

### Return type

[**AreaResponse**](AreaResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vversionAreasAreaIdsGet

> AreaResponse vversionAreasAreaIdsGet(areaIds, version)

Returns details of selected area

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.AreasApi();
let areaIds = "areaIds_example"; // String | 
let version = "version_example"; // String | 
apiInstance.vversionAreasAreaIdsGet(areaIds, version, (error, data, response) => {
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
 **areaIds** | **String**|  | 
 **version** | **String**|  | 

### Return type

[**AreaResponse**](AreaResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

