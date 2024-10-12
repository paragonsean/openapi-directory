# SportsDataApi.CompetitorsApi

All URIs are relative to *https://sandbox.whapi.com/v2/sportsdata*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEventCompetitors**](CompetitorsApi.md#getEventCompetitors) | **GET** /events/{eventId}/competitors | Retrieves competitors for a single event by ID.



## getEventCompetitors

> EventCompetitorsWrapper getEventCompetitors(apiKey, eventId, opts)

Retrieves competitors for a single event by ID.

Retrieves competitors for a single event by ID.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.CompetitorsApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let eventId = "eventId_example"; // String | The event ID to retrieve information for.
let opts = {
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"] // [String] | Specify fields from the default to exclude (Comma-Separated List)
};
apiInstance.getEventCompetitors(apiKey, eventId, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **eventId** | **String**| The event ID to retrieve information for. | 
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 

### Return type

[**EventCompetitorsWrapper**](EventCompetitorsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

