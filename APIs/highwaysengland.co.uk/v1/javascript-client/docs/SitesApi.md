# HighwaysEnglandApi.SitesApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sitesIndex**](SitesApi.md#sitesIndex) | **GET** /v{version}/sites | Get a list of sites
[**vversionSitesSiteIdsGet**](SitesApi.md#vversionSitesSiteIdsGet) | **GET** /v{version}/sites/{site_Ids} | Get selected sites



## sitesIndex

> SiteResponse sitesIndex(version)

Get a list of sites

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.SitesApi();
let version = "version_example"; // String | 
apiInstance.sitesIndex(version, (error, data, response) => {
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

[**SiteResponse**](SiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vversionSitesSiteIdsGet

> SiteResponse vversionSitesSiteIdsGet(siteIds, version)

Get selected sites

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.SitesApi();
let siteIds = "siteIds_example"; // String | site id
let version = "version_example"; // String | 
apiInstance.vversionSitesSiteIdsGet(siteIds, version, (error, data, response) => {
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
 **siteIds** | **String**| site id | 
 **version** | **String**|  | 

### Return type

[**SiteResponse**](SiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

