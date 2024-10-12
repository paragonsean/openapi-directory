# TwilioBulkexports.BulkexportsV1DayApi

All URIs are relative to *https://bulkexports.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDay**](BulkexportsV1DayApi.md#fetchDay) | **GET** /v1/Exports/{ResourceType}/Days/{Day} | 
[**listDay**](BulkexportsV1DayApi.md#listDay) | **GET** /v1/Exports/{ResourceType}/Days | 



## fetchDay

> fetchDay(resourceType, day)



Fetch a specific Day.

### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1DayApi();
let resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
let day = "day_example"; // String | The ISO 8601 format date of the resources in the file, for a UTC day
apiInstance.fetchDay(resourceType, day, (error, data, response) => {
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
 **resourceType** | **String**| The type of communication – Messages, Calls, Conferences, and Participants | 
 **day** | **String**| The ISO 8601 format date of the resources in the file, for a UTC day | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDay

> ListDayResponse listDay(resourceType, opts)



Retrieve a list of all Days for a resource.

### Example

```javascript
import TwilioBulkexports from 'twilio_bulkexports';
let defaultClient = TwilioBulkexports.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioBulkexports.BulkexportsV1DayApi();
let resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDay(resourceType, opts, (error, data, response) => {
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
 **resourceType** | **String**| The type of communication – Messages, Calls, Conferences, and Participants | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDayResponse**](ListDayResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

