# MeetingsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2MeetingsIdJsonPut**](MeetingsApi.md#v2MeetingsIdJsonPut) | **PUT** /v2/meetings/{id}.json | Update a meeting |
| [**v2MeetingsJsonGet**](MeetingsApi.md#v2MeetingsJsonGet) | **GET** /v2/meetings.json | List meetings |


<a id="v2MeetingsIdJsonPut"></a>
# **v2MeetingsIdJsonPut**
> Meeting v2MeetingsIdJsonPut(id, eventId, iCalUid, noShow, rescheduleStatus, status)

Update a meeting

Updates a meeting, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String id = "id_example"; // String | Meeting ID
    String eventId = "eventId_example"; // String | Meeting ID from the calendar provider
    String iCalUid = "iCalUid_example"; // String | Meeting unique identifier (iCalUID)
    Boolean noShow = true; // Boolean | Whether the meeting is a No Show meeting
    String rescheduleStatus = "rescheduleStatus_example"; // String | Status of the meeting rescheduling progress. Possible values are: pending, booked, failed, retry
    String status = "status_example"; // String | Status of the meeting creation progress. Possible values are: pending, booked, failed, retry
    try {
      Meeting result = apiInstance.v2MeetingsIdJsonPut(id, eventId, iCalUid, noShow, rescheduleStatus, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#v2MeetingsIdJsonPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Meeting ID | |
| **eventId** | **String**| Meeting ID from the calendar provider | [optional] |
| **iCalUid** | **String**| Meeting unique identifier (iCalUID) | [optional] |
| **noShow** | **Boolean**| Whether the meeting is a No Show meeting | [optional] |
| **rescheduleStatus** | **String**| Status of the meeting rescheduling progress. Possible values are: pending, booked, failed, retry | [optional] |
| **status** | **String**| Status of the meeting creation progress. Possible values are: pending, booked, failed, retry | [optional] |

### Return type

[**Meeting**](Meeting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2MeetingsJsonGet"></a>
# **v2MeetingsJsonGet**
> List&lt;Meeting&gt; v2MeetingsJsonGet(ids, status, personId, accountId, personIds, eventIds, iCalUids, taskIds, includeMeetingsSettings, startTime, createdAt, userGuids, showDeleted, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List meetings

Fetches multiple meeting records. The records can be filtered, paged, and sorted according to the respective parameters. Meetings resource is responsible for events created via the Salesloft platform using calendaring features. These events can relate to cadences, people, and accounts. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of meetings to fetch. If a record can't be found, that record won't be returned and your request will be successful
    String status = "status_example"; // String | Filters meetings by status. Possible values are: pending, booked, failed, retry
    String personId = "personId_example"; // String | Filters meetings by person_id. Multiple person ids can be applied
    String accountId = "accountId_example"; // String | Filters meetings by account_id. Multiple account ids can be applied
    List<Integer> personIds = Arrays.asList(); // List<Integer> | Filters meetings by person_id. Multiple person ids can be applied
    List<String> eventIds = Arrays.asList(); // List<String> | List of event IDs. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can't be found, that record won't be returned and your request will be successful
    List<String> iCalUids = Arrays.asList(); // List<String> | List of UIDs provided by calendar provider. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can't be found, that record won't be returned and your request will be successful
    List<Integer> taskIds = Arrays.asList(); // List<Integer> | Filters meetings by task_id. Multiple task ids can be applied
    Boolean includeMeetingsSettings = true; // Boolean | Flag to indicate whether to include owned_by_meetings_settings and booked_by_meetings_settings objects
    List<String> startTime = Arrays.asList(); // List<String> | Equality filters that are applied to the start_time field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<String> createdAt = Arrays.asList(); // List<String> | Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<String> userGuids = Arrays.asList(); // List<String> | Filters meetings by user_guid. Multiple user guids can be applied
    Boolean showDeleted = true; // Boolean | Whether to include deleted events in the result
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: start_time, created_at, updated_at. Defaults to start_time
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<Meeting> result = apiInstance.v2MeetingsJsonGet(ids, status, personId, accountId, personIds, eventIds, iCalUids, taskIds, includeMeetingsSettings, startTime, createdAt, userGuids, showDeleted, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#v2MeetingsJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of meetings to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **status** | **String**| Filters meetings by status. Possible values are: pending, booked, failed, retry | [optional] |
| **personId** | **String**| Filters meetings by person_id. Multiple person ids can be applied | [optional] |
| **accountId** | **String**| Filters meetings by account_id. Multiple account ids can be applied | [optional] |
| **personIds** | [**List&lt;Integer&gt;**](Integer.md)| Filters meetings by person_id. Multiple person ids can be applied | [optional] |
| **eventIds** | [**List&lt;String&gt;**](String.md)| List of event IDs. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **iCalUids** | [**List&lt;String&gt;**](String.md)| List of UIDs provided by calendar provider. If both event_ids and i_cal_uids params are passed, this filters will be ORed. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **taskIds** | [**List&lt;Integer&gt;**](Integer.md)| Filters meetings by task_id. Multiple task ids can be applied | [optional] |
| **includeMeetingsSettings** | **Boolean**| Flag to indicate whether to include owned_by_meetings_settings and booked_by_meetings_settings objects | [optional] |
| **startTime** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the start_time field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **createdAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **userGuids** | [**List&lt;String&gt;**](String.md)| Filters meetings by user_guid. Multiple user guids can be applied | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted events in the result | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: start_time, created_at, updated_at. Defaults to start_time | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;Meeting&gt;**](Meeting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

