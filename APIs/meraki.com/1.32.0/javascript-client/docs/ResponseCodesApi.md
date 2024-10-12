# MerakiDashboardApi.ResponseCodesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationApiRequestsOverviewResponseCodesByInterval_3**](ResponseCodesApi.md#getOrganizationApiRequestsOverviewResponseCodesByInterval_3) | **GET** /organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval | Tracks organizations&#39; API requests by response code across a given time period



## getOrganizationApiRequestsOverviewResponseCodesByInterval_3

> [GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner] getOrganizationApiRequestsOverviewResponseCodesByInterval_3(organizationId, opts)

Tracks organizations&#39; API requests by response code across a given time period

Tracks organizations&#39; API requests by response code across a given time period

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ResponseCodesApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
  'interval': 56, // Number | The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
  'version': 56, // Number | Filter by API version of the endpoint. Allowable values are: [0, 1]
  'operationIds': ["null"], // [String] | Filter by operation ID of the endpoint
  'sourceIps': ["null"], // [String] | Filter by source IP that made the API request
  'adminIds': ["null"], // [String] | Filter by admin ID of user that made the API request
  'userAgent': "userAgent_example" // String | Filter by user agent string for API request. This will filter by a complete or partial match.
};
apiInstance.getOrganizationApiRequestsOverviewResponseCodesByInterval_3(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated. | [optional] 
 **interval** | **Number**| The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided. | [optional] 
 **version** | **Number**| Filter by API version of the endpoint. Allowable values are: [0, 1] | [optional] 
 **operationIds** | [**[String]**](String.md)| Filter by operation ID of the endpoint | [optional] 
 **sourceIps** | [**[String]**](String.md)| Filter by source IP that made the API request | [optional] 
 **adminIds** | [**[String]**](String.md)| Filter by admin ID of user that made the API request | [optional] 
 **userAgent** | **String**| Filter by user agent string for API request. This will filter by a complete or partial match. | [optional] 

### Return type

[**[GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner]**](GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

