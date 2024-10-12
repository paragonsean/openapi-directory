# HighwaysEnglandApi.QualityApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qualityGetDailyDataQualityForSite**](QualityApi.md#qualityGetDailyDataQualityForSite) | **GET** /v{version}/quality/daily | Get Site DailyQuality
[**qualityGetOverallDataQualityForSites**](QualityApi.md#qualityGetOverallDataQualityForSites) | **GET** /v{version}/quality/overall | Get Site OverallQuality



## qualityGetDailyDataQualityForSite

> DailyQualityResponse qualityGetDailyDataQualityForSite(siteId, startDate, endDate, version)

Get Site DailyQuality

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.QualityApi();
let siteId = "siteId_example"; // String | 
let startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
let endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
let version = "version_example"; // String | 
apiInstance.qualityGetDailyDataQualityForSite(siteId, startDate, endDate, version, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | 
 **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | 
 **version** | **String**|  | 

### Return type

[**DailyQualityResponse**](DailyQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qualityGetOverallDataQualityForSites

> OverallQualityResponse qualityGetOverallDataQualityForSites(sites, startDate, endDate, version)

Get Site OverallQuality

### Example

```javascript
import HighwaysEnglandApi from 'highways_england_api';

let apiInstance = new HighwaysEnglandApi.QualityApi();
let sites = "sites_example"; // String | Get site quality by site id delimited by ,
let startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
let endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
let version = "version_example"; // String | 
apiInstance.qualityGetOverallDataQualityForSites(sites, startDate, endDate, version, (error, data, response) => {
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
 **sites** | **String**| Get site quality by site id delimited by , | 
 **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | 
 **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | 
 **version** | **String**|  | 

### Return type

[**OverallQualityResponse**](OverallQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

