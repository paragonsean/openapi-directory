# VisageCloud.AnalyticsForPresenceAndAudienceApi

All URIs are relative to *https://visagecloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**counterUsingPOST**](AnalyticsForPresenceAndAudienceApi.md#counterUsingPOST) | **POST** /rest/v1.1/analytics/counting | Count individuals in streams or collections
[**presenceTimeseriesUsingPOST**](AnalyticsForPresenceAndAudienceApi.md#presenceTimeseriesUsingPOST) | **POST** /rest/v1.1/analytics/presence/timeseries | Show audience (based on number of occurrences of each person) breakdown per declared attribute (age, gender).
[**presenceTotalUsingPOST**](AnalyticsForPresenceAndAudienceApi.md#presenceTotalUsingPOST) | **POST** /rest/v1.1/analytics/presence/total | Show presence (based on number of occurences of each face) breakdown per declared attribute (age, gender)



## counterUsingPOST

> RestResponse counterUsingPOST(accessKey, secretKey, opts)

Count individuals in streams or collections

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalyticsForPresenceAndAudienceApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let opts = {
  'collectionIds': ["null"], // [String] | Collection ids
  'streamIds': ["null"], // [String] | Stream Ids
  'startDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | startDateTime
  'endDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | endDateTime
  'visitDuration': 3600000, // Number | visitDuration
  'maxIterations': 1, // Number | maxIterations
  'maxBatchIterations': 1, // Number | maxBatchIterations
  'minNeighborsMergedPerIteration': 5, // Number | minNeighborsMergedPerIteration
  'mergingStep': 1.0, // Number | mergingStep
  'shuffling': false // Boolean | shuffling
};
apiInstance.counterUsingPOST(accessKey, secretKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **collectionIds** | [**[String]**](String.md)| Collection ids | [optional] 
 **streamIds** | [**[String]**](String.md)| Stream Ids | [optional] 
 **startDateTime** | **Date**| startDateTime | [optional] 
 **endDateTime** | **Date**| endDateTime | [optional] 
 **visitDuration** | **Number**| visitDuration | [optional] [default to 3600000]
 **maxIterations** | **Number**| maxIterations | [optional] [default to 1]
 **maxBatchIterations** | **Number**| maxBatchIterations | [optional] [default to 1]
 **minNeighborsMergedPerIteration** | **Number**| minNeighborsMergedPerIteration | [optional] [default to 5]
 **mergingStep** | **Number**| mergingStep | [optional] [default to 1.0]
 **shuffling** | **Boolean**| shuffling | [optional] [default to false]

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## presenceTimeseriesUsingPOST

> RestResponse presenceTimeseriesUsingPOST(accessKey, secretKey, attributes, opts)

Show audience (based on number of occurrences of each person) breakdown per declared attribute (age, gender).

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalyticsForPresenceAndAudienceApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let attributes = ["null"]; // [String] | attributes
let opts = {
  'streamIds': ["null"], // [String] | Stream Ids
  'startDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | startDateTime
  'endDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | endDateTime
  'step': 3600 // Number | step
};
apiInstance.presenceTimeseriesUsingPOST(accessKey, secretKey, attributes, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **attributes** | [**[String]**](String.md)| attributes | 
 **streamIds** | [**[String]**](String.md)| Stream Ids | [optional] 
 **startDateTime** | **Date**| startDateTime | [optional] 
 **endDateTime** | **Date**| endDateTime | [optional] 
 **step** | **Number**| step | [optional] [default to 3600]

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## presenceTotalUsingPOST

> RestResponse presenceTotalUsingPOST(accessKey, secretKey, streamIds, attributes, opts)

Show presence (based on number of occurences of each face) breakdown per declared attribute (age, gender)

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.AnalyticsForPresenceAndAudienceApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let streamIds = ["null"]; // [String] | Stream Ids
let attributes = ["null"]; // [String] | attributes
let opts = {
  'startDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | startDateTime
  'endDateTime': new Date("2013-10-20T19:20:30+01:00") // Date | endDateTime
};
apiInstance.presenceTotalUsingPOST(accessKey, secretKey, streamIds, attributes, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **streamIds** | [**[String]**](String.md)| Stream Ids | 
 **attributes** | [**[String]**](String.md)| attributes | 
 **startDateTime** | **Date**| startDateTime | [optional] 
 **endDateTime** | **Date**| endDateTime | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

