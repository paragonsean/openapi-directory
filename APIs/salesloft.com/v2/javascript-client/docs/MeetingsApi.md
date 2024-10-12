# SalesLoftPlatform.MeetingsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2MeetingsIdJsonPut**](MeetingsApi.md#v2MeetingsIdJsonPut) | **PUT** /v2/meetings/{id}.json | Update a meeting
[**v2MeetingsJsonGet**](MeetingsApi.md#v2MeetingsJsonGet) | **GET** /v2/meetings.json | List meetings



## v2MeetingsIdJsonPut

> Meeting v2MeetingsIdJsonPut(id, opts)

Update a meeting

Updates a meeting, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.MeetingsApi();
let id = "id_example"; // String | Meeting ID
let opts = {
  'eventId': "eventId_example", // String | Meeting ID from the calendar provider
  'iCalUid': "iCalUid_example", // String | Meeting unique identifier (iCalUID)
  'noShow': true, // Boolean | Whether the meeting is a No Show meeting
  'rescheduleStatus': "rescheduleStatus_example", // String | Status of the meeting rescheduling progress. Possible values are: pending, booked, failed, retry
  'status': "status_example" // String | Status of the meeting creation progress. Possible values are: pending, booked, failed, retry
};
apiInstance.v2MeetingsIdJsonPut(id, opts, (error, data, response) => {
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
 **id** | **String**| Meeting ID | 
 **eventId** | **String**| Meeting ID from the calendar provider | [optional] 
 **iCalUid** | **String**| Meeting unique identifier (iCalUID) | [optional] 
 **noShow** | **Boolean**| Whether the meeting is a No Show meeting | [optional] 
 **rescheduleStatus** | **String**| Status of the meeting rescheduling progress. Possible values are: pending, booked, failed, retry | [optional] 
 **status** | **String**| Status of the meeting creation progress. Possible values are: pending, booked, failed, retry | [optional] 

### Return type

[**Meeting**](Meeting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2MeetingsJsonGet

> [Meeting] v2MeetingsJsonGet(opts)

List meetings

Fetches multiple meeting records. The records can be filtered, paged, and sorted according to the respective parameters. Meetings resource is responsible for events created via the Salesloft platform using calendaring features. These events can relate to cadences, people, and accounts. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.MeetingsApi();
let opts = {
  'ids': [null], // [Number] | IDs of meetings to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'status': "status_example", // String | Filters meetings by status. Possible values are: pending, booked, failed, retry
  'personId': "personId_example", // String | Filters meetings by person_id. Multiple person ids can be applied
  'accountId': "accountId_example", // String | Filters meetings by account_id. Multiple account ids can be applied
  'personIds': [null], // [Number] | Filters meetings by person_id. Multiple person ids can be applied
  'eventIds': ["null"], // [String] | List of event IDs. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can't be found, that record won't be returned and your request will be successful
  'iCalUids': ["null"], // [String] | List of UIDs provided by calendar provider. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can't be found, that record won't be returned and your request will be successful
  'taskIds': [null], // [Number] | Filters meetings by task_id. Multiple task ids can be applied
  'includeMeetingsSettings': true, // Boolean | Flag to indicate whether to include owned_by_meetings_settings and booked_by_meetings_settings objects
  'startTime': ["null"], // [String] | Equality filters that are applied to the start_time field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'createdAt': ["null"], // [String] | Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'userGuids': ["null"], // [String] | Filters meetings by user_guid. Multiple user guids can be applied
  'showDeleted': true, // Boolean | Whether to include deleted events in the result
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: start_time, created_at, updated_at. Defaults to start_time
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2MeetingsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of meetings to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **status** | **String**| Filters meetings by status. Possible values are: pending, booked, failed, retry | [optional] 
 **personId** | **String**| Filters meetings by person_id. Multiple person ids can be applied | [optional] 
 **accountId** | **String**| Filters meetings by account_id. Multiple account ids can be applied | [optional] 
 **personIds** | [**[Number]**](Number.md)| Filters meetings by person_id. Multiple person ids can be applied | [optional] 
 **eventIds** | [**[String]**](String.md)| List of event IDs. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **iCalUids** | [**[String]**](String.md)| List of UIDs provided by calendar provider. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **taskIds** | [**[Number]**](Number.md)| Filters meetings by task_id. Multiple task ids can be applied | [optional] 
 **includeMeetingsSettings** | **Boolean**| Flag to indicate whether to include owned_by_meetings_settings and booked_by_meetings_settings objects | [optional] 
 **startTime** | [**[String]**](String.md)| Equality filters that are applied to the start_time field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **createdAt** | [**[String]**](String.md)| Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **userGuids** | [**[String]**](String.md)| Filters meetings by user_guid. Multiple user guids can be applied | [optional] 
 **showDeleted** | **Boolean**| Whether to include deleted events in the result | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: start_time, created_at, updated_at. Defaults to start_time | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Meeting]**](Meeting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

