# QuickStartTelematicsSdk.ConsolidatedSafeScoringApi

All URIs are relative to *https://api.telematicssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1ScoringsConsolidatedDaily_0**](ConsolidatedSafeScoringApi.md#v1ScoringsConsolidatedDaily_0) | **GET** /statistics/v1/Scorings/consolidated/daily | /v1/Scorings/consolidated/daily
[**v1ScoringsConsolidated_0**](ConsolidatedSafeScoringApi.md#v1ScoringsConsolidated_0) | **GET** /statistics/v1/Scorings/consolidated | /v1/Scorings/consolidated



## v1ScoringsConsolidatedDaily_0

> V1ScoringsConsolidatedDaily200Response v1ScoringsConsolidatedDaily_0(opts)

/v1/Scorings/consolidated/daily

/v1/Scorings/consolidated/daily

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.ConsolidatedSafeScoringApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-17T01:04:22.840Z", // String | 
  'endDate': "2021-01-18T01:04:22.840Z", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1ScoringsConsolidatedDaily_0(opts, (error, data, response) => {
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
 **deviceToken** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **instanceId** | **String**|  | [optional] 
 **appId** | **String**|  | [optional] 
 **companyId** | **String**|  | [optional] 

### Return type

[**V1ScoringsConsolidatedDaily200Response**](V1ScoringsConsolidatedDaily200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1ScoringsConsolidated_0

> v1ScoringsConsolidated_0(opts)

/v1/Scorings/consolidated

/v1/Scorings/consolidated

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.ConsolidatedSafeScoringApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-17T01:04:22.840Z", // String | 
  'endDate': "2021-01-18T01:04:22.840Z", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1ScoringsConsolidated_0(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceToken** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **instanceId** | **String**|  | [optional] 
 **appId** | **String**|  | [optional] 
 **companyId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

