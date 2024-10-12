# MostPopularApi.DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/mostpopular/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETMostemailedSectionTimePeriodJson**](DefaultApi.md#gETMostemailedSectionTimePeriodJson) | **GET** /mostemailed/{section}/{time-period}.json | Most Emailed by Section &amp; Time Period
[**gETMostsharedSectionTimePeriodJson**](DefaultApi.md#gETMostsharedSectionTimePeriodJson) | **GET** /mostshared/{section}/{time-period}.json | Most Shared by Section &amp; Time Period
[**gETMostviewedSectionTimePeriodJson**](DefaultApi.md#gETMostviewedSectionTimePeriodJson) | **GET** /mostviewed/{section}/{time-period}.json | Most Viewed by Section &amp; Time Period



## gETMostemailedSectionTimePeriodJson

> GETMostemailedSectionTimePeriodJson200Response gETMostemailedSectionTimePeriodJson(section, timePeriod)

Most Emailed by Section &amp; Time Period



### Example

```javascript
import MostPopularApi from 'most_popular_api';
let defaultClient = MostPopularApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new MostPopularApi.DefaultApi();
let section = "section_example"; // String | Limits the results by one or more sections. You can use `all-sections` or one or more section names seperated by semicolons. See `viewed/sections.json` call to get a list of sections.  
let timePeriod = "timePeriod_example"; // String | Number of days `1 | 7 | 30 ` corresponds to a day, a week, or a month of content.
apiInstance.gETMostemailedSectionTimePeriodJson(section, timePeriod, (error, data, response) => {
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
 **section** | **String**| Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.   | 
 **timePeriod** | **String**| Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content. | 

### Return type

[**GETMostemailedSectionTimePeriodJson200Response**](GETMostemailedSectionTimePeriodJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## gETMostsharedSectionTimePeriodJson

> GETMostsharedSectionTimePeriodJson200Response gETMostsharedSectionTimePeriodJson(section, timePeriod)

Most Shared by Section &amp; Time Period



### Example

```javascript
import MostPopularApi from 'most_popular_api';
let defaultClient = MostPopularApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new MostPopularApi.DefaultApi();
let section = "section_example"; // String | Limits the results by one or more sections. You can use `all-sections` or one or more section names seperated by semicolons. See `viewed/sections.json` call to get a list of sections.  
let timePeriod = "timePeriod_example"; // String | Number of days `1 | 7 | 30 ` corresponds to a day, a week, or a month of content.
apiInstance.gETMostsharedSectionTimePeriodJson(section, timePeriod, (error, data, response) => {
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
 **section** | **String**| Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.   | 
 **timePeriod** | **String**| Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content. | 

### Return type

[**GETMostsharedSectionTimePeriodJson200Response**](GETMostsharedSectionTimePeriodJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETMostviewedSectionTimePeriodJson

> GETMostsharedSectionTimePeriodJson200Response gETMostviewedSectionTimePeriodJson(section, timePeriod)

Most Viewed by Section &amp; Time Period



### Example

```javascript
import MostPopularApi from 'most_popular_api';
let defaultClient = MostPopularApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new MostPopularApi.DefaultApi();
let section = "section_example"; // String | Limits the results by one or more sections. You can use `all-sections` or one or more section names seperated by semicolons. See `viewed/sections.json` call to get a list of sections.  
let timePeriod = "timePeriod_example"; // String | Number of days `1 | 7 | 30 ` corresponds to a day, a week, or a month of content.
apiInstance.gETMostviewedSectionTimePeriodJson(section, timePeriod, (error, data, response) => {
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
 **section** | **String**| Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.   | 
 **timePeriod** | **String**| Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content. | 

### Return type

[**GETMostsharedSectionTimePeriodJson200Response**](GETMostsharedSectionTimePeriodJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

