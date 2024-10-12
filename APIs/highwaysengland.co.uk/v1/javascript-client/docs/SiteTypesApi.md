# HighwaysEnglandApi.SiteTypesApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**siteTypesGetSitesForPublicFacingAPI**](SiteTypesApi.md#siteTypesGetSitesForPublicFacingAPI) | **GET** /v{version}/sitetypes/{siteType_Id}/sites | Returns the layer metadata for the LayerId specified.
[**siteTypesIndex**](SiteTypesApi.md#siteTypesIndex) | **GET** /v{version}/sitetypes | Return list of site types



## siteTypesGetSitesForPublicFacingAPI

> SiteTypeLayer siteTypesGetSitesForPublicFacingAPI(siteTypeId, version)

Returns the layer metadata for the LayerId specified.

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.SiteTypesApi();
let siteTypeId = 56; // Number | 1 = MIDAS, 2 = TAME, 3 = TMU, 4 = TRADS Legacy
let version = "version_example"; // String | 
apiInstance.siteTypesGetSitesForPublicFacingAPI(siteTypeId, version, (error, data, response) => {
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
 **siteTypeId** | **Number**| 1 &#x3D; MIDAS, 2 &#x3D; TAME, 3 &#x3D; TMU, 4 &#x3D; TRADS Legacy | 
 **version** | **String**|  | 

### Return type

[**SiteTypeLayer**](SiteTypeLayer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## siteTypesIndex

> SiteTypeResponse siteTypesIndex(version)

Return list of site types

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.SiteTypesApi();
let version = "version_example"; // String | 
apiInstance.siteTypesIndex(version, (error, data, response) => {
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

[**SiteTypeResponse**](SiteTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

