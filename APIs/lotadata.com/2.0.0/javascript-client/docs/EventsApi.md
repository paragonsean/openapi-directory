# LotaData.EventsApi

All URIs are relative to *https://api2.lotadata.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsGet**](EventsApi.md#eventsGet) | **GET** /events | Find event occurrences in the area. Returns results at specific place and time, event groups are expanded for every occurrence.
[**eventsIdGet**](EventsApi.md#eventsIdGet) | **GET** /events/{id} | Get Specific event details.



## eventsGet

> EventsSearchResponse eventsGet(fieldset, opts)

Find event occurrences in the area. Returns results at specific place and time, event groups are expanded for every occurrence.

### Example

```javascript
import LotaData from 'lota_data';
let defaultClient = LotaData.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new LotaData.EventsApi();
let fieldset = "'context'"; // String | Return results starting at specified offset (summary, context, detail)
let opts = {
  'category': ["null"], // [String] | List of required EventCategory ids (Tier 1)
  'activity': "activity_example", // String | List of required activity type ids (compliment to category)
  'ambience': "ambience_example", // String | List of required ambience ids
  'genre': "genre_example", // String | List of required genre ids
  'name': "name_example", // String | Matching on event and place names
  'q': "q_example", // String | Text query matching titles, description, various text, tags, category
  'fromDay': "fromDay_example", // String | Start on or after date specified (2015-10-16)
  'toDay': "toDay_example", // String | Start on or before date specified (2015-10-16)
  'capacityMin': 3.4, // Number | Min capacity at location
  'capacityMax': 3.4, // Number | Min capacity at location
  'center': "center_example", // String | latitude,longitude of the origin point
  'radius': 56, // Number | Distance from origin in meters
  'bbox': ["null"], // [String] | Corner of a bounding box (lat,lng). Requires 0 or 2 pairs
  'polygon': ["null"], // [String] | Closed custom polygon. Ordered list of lat,lng pairs
  'within': "within_example", // String | Search within specified geopolitical place id
  'offset': 56, // Number | Return results starting at specified offset
  'limit': 56 // Number | Max results to return
};
apiInstance.eventsGet(fieldset, opts, (error, data, response) => {
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
 **fieldset** | **String**| Return results starting at specified offset (summary, context, detail) | [default to &#39;context&#39;]
 **category** | [**[String]**](String.md)| List of required EventCategory ids (Tier 1) | [optional] 
 **activity** | **String**| List of required activity type ids (compliment to category) | [optional] 
 **ambience** | **String**| List of required ambience ids | [optional] 
 **genre** | **String**| List of required genre ids | [optional] 
 **name** | **String**| Matching on event and place names | [optional] 
 **q** | **String**| Text query matching titles, description, various text, tags, category | [optional] 
 **fromDay** | **String**| Start on or after date specified (2015-10-16) | [optional] 
 **toDay** | **String**| Start on or before date specified (2015-10-16) | [optional] 
 **capacityMin** | **Number**| Min capacity at location | [optional] 
 **capacityMax** | **Number**| Min capacity at location | [optional] 
 **center** | **String**| latitude,longitude of the origin point | [optional] 
 **radius** | **Number**| Distance from origin in meters | [optional] 
 **bbox** | [**[String]**](String.md)| Corner of a bounding box (lat,lng). Requires 0 or 2 pairs | [optional] 
 **polygon** | [**[String]**](String.md)| Closed custom polygon. Ordered list of lat,lng pairs | [optional] 
 **within** | **String**| Search within specified geopolitical place id | [optional] 
 **offset** | **Number**| Return results starting at specified offset | [optional] 
 **limit** | **Number**| Max results to return | [optional] 

### Return type

[**EventsSearchResponse**](EventsSearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsIdGet

> EventOccurenceDetail eventsIdGet(id, opts)

Get Specific event details.

### Example

```javascript
import LotaData from 'lota_data';
let defaultClient = LotaData.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new LotaData.EventsApi();
let id = "id_example"; // String | event @id
let opts = {
  'fieldset': "'summary'" // String | 
};
apiInstance.eventsIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| event @id | 
 **fieldset** | **String**|  | [optional] [default to &#39;summary&#39;]

### Return type

[**EventOccurenceDetail**](EventOccurenceDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

