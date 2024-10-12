# ActivityHistoriesApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ActivityHistoriesGet**](ActivityHistoriesApi.md#v2ActivityHistoriesGet) | **GET** /v2/activity_histories | List Past Activities |


<a id="v2ActivityHistoriesGet"></a>
# **v2ActivityHistoriesGet**
> ActivityHistory v2ActivityHistoriesGet(perPage, page, includePagingCounts, sortBy, sortDirection, type, resource, occurredAt, pinned, resourceType, resourceId, updatedAt, userGuid)

List Past Activities

Fetches all of the customer&#39;s past activities for your application. Returns all the Activities that are found on the Salesloft Activity Feed. &lt;a href&#x3D;\&quot;/activity-history.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;Visit here for more details&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityHistoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ActivityHistoriesApi apiInstance = new ActivityHistoriesApi(defaultClient);
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: occurred_at, updated_at. Defaults to occurred_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    String type = "type_example"; // String | Filter by the type of activity. Must be one of: added_to_cadence, completed_action, call, requested_email, sent_email, received_email, email_reply, note, success, dnc_event, residency_change, meeting, meeting_held, message_conversation, task, voicemail, opportunity_stage_change, opportunity_amount_change, opportunity_close_date_change. Can be provided as an array, or as an object of type[resource_type][]=type
    String resource = "resource_example"; // String | For internal use only. This field does not comply with our backwards compatibility policies. This filter is for authenticated users of Salesloft only and will not work for OAuth Applications. Filter by the {resource_type, resource_id} of activity. Provide this in the format resource[]=person,1234
    Object occurredAt = null; // Object | Equality filters that are applied to the occurred_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\"keys\":[{\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"gt\",\"type\":\"iso8601 string\"},{\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"gte\",\"type\":\"iso8601 string\"},{\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"lt\",\"type\":\"iso8601 string\"},{\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"lte\",\"type\":\"iso8601 string\"}],\"type\":\"object\"} 
    Boolean pinned = true; // Boolean | Filter by the pinned status of activity. Must be 'true' or 'false'
    String resourceType = "resourceType_example"; // String | Filter by the resource type. A resource is a Salesloft object that the activity is attributed to. A valid resource types must be one of person, account, crm_opportunity. Can be provided as an array
    List<String> resourceId = Arrays.asList(); // List<String> | Filter by the resource id. \"resource_type\" filter is required to use this filter.
    Object updatedAt = null; // Object | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\"keys\":[{\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"gt\",\"type\":\"iso8601 string\"},{\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"gte\",\"type\":\"iso8601 string\"},{\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"lt\",\"type\":\"iso8601 string\"},{\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\",\"name\":\"lte\",\"type\":\"iso8601 string\"}],\"type\":\"object\"} 
    String userGuid = "userGuid_example"; // String | Filter activities by a user's guid.
    try {
      ActivityHistory result = apiInstance.v2ActivityHistoriesGet(perPage, page, includePagingCounts, sortBy, sortDirection, type, resource, occurredAt, pinned, resourceType, resourceId, updatedAt, userGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityHistoriesApi#v2ActivityHistoriesGet");
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
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: occurred_at, updated_at. Defaults to occurred_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **type** | **String**| Filter by the type of activity. Must be one of: added_to_cadence, completed_action, call, requested_email, sent_email, received_email, email_reply, note, success, dnc_event, residency_change, meeting, meeting_held, message_conversation, task, voicemail, opportunity_stage_change, opportunity_amount_change, opportunity_close_date_change. Can be provided as an array, or as an object of type[resource_type][]&#x3D;type | [optional] |
| **resource** | **String**| For internal use only. This field does not comply with our backwards compatibility policies. This filter is for authenticated users of Salesloft only and will not work for OAuth Applications. Filter by the {resource_type, resource_id} of activity. Provide this in the format resource[]&#x3D;person,1234 | [optional] |
| **occurredAt** | [**Object**](.md)| Equality filters that are applied to the occurred_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\&quot;keys\&quot;:[{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;}],\&quot;type\&quot;:\&quot;object\&quot;}  | [optional] |
| **pinned** | **Boolean**| Filter by the pinned status of activity. Must be &#39;true&#39; or &#39;false&#39; | [optional] |
| **resourceType** | **String**| Filter by the resource type. A resource is a Salesloft object that the activity is attributed to. A valid resource types must be one of person, account, crm_opportunity. Can be provided as an array | [optional] |
| **resourceId** | [**List&lt;String&gt;**](String.md)| Filter by the resource id. \&quot;resource_type\&quot; filter is required to use this filter. | [optional] |
| **updatedAt** | [**Object**](.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\&quot;keys\&quot;:[{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;},{\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;,\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;}],\&quot;type\&quot;:\&quot;object\&quot;}  | [optional] |
| **userGuid** | **String**| Filter activities by a user&#39;s guid. | [optional] |

### Return type

[**ActivityHistory**](ActivityHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

