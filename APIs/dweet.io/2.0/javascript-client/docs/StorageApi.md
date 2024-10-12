# DweetIo.StorageApi

All URIs are relative to *https://dweet.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStoredAlerts**](StorageApi.md#getStoredAlerts) | **GET** /get/stored/alerts/for/{thing} | Read all the saved alerts for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.
[**getStoredDweetsForThingGet**](StorageApi.md#getStoredDweetsForThingGet) | **GET** /get/stored/dweets/for/{thing} | Read all the saved dweets for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.



## getStoredAlerts

> getStoredAlerts(thing, key, date, opts)

Read all the saved alerts for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.StorageApi();
let thing = "thing_example"; // String | A unique name of a thing.
let key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
let date = "date_example"; // String | The calendar date (YYYY-MM-DD) from which you'd like to start your query.  The response will be a maximum of one day.
let opts = {
  'hour': "hour_example", // String | The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour.
  'responseType': "responseType_example" // String | Current valid parameters for this are 'csv' and 'json'.  If this parameter is left blank, all responses default to hapi-json dweet-speak.
};
apiInstance.getStoredAlerts(thing, key, date, opts, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | 
 **date** | **String**| The calendar date (YYYY-MM-DD) from which you&#39;d like to start your query.  The response will be a maximum of one day. | 
 **hour** | **String**| The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour. | [optional] 
 **responseType** | **String**| Current valid parameters for this are &#39;csv&#39; and &#39;json&#39;.  If this parameter is left blank, all responses default to hapi-json dweet-speak. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStoredDweetsForThingGet

> getStoredDweetsForThingGet(thing, key, date, opts)

Read all the saved dweets for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.StorageApi();
let thing = "thing_example"; // String | A unique name of a thing.
let key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
let date = "date_example"; // String | The calendar date (YYYY-MM-DD) from which you'd like to start your query.  The response will be a maximum of one day.
let opts = {
  'hour': "hour_example", // String | The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour.
  'responseType': "responseType_example" // String | Current valid parameters for this are 'csv' and 'json'.  If this parameter is left blank, all responses default to hapi-json dweet-speak.
};
apiInstance.getStoredDweetsForThingGet(thing, key, date, opts, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | 
 **date** | **String**| The calendar date (YYYY-MM-DD) from which you&#39;d like to start your query.  The response will be a maximum of one day. | 
 **hour** | **String**| The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour. | [optional] 
 **responseType** | **String**| Current valid parameters for this are &#39;csv&#39; and &#39;json&#39;.  If this parameter is left blank, all responses default to hapi-json dweet-speak. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

