# ActionsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ActionsIdJsonGet**](ActionsApi.md#v2ActionsIdJsonGet) | **GET** /v2/actions/{id}.json | Fetch an action |
| [**v2ActionsJsonGet**](ActionsApi.md#v2ActionsJsonGet) | **GET** /v2/actions.json | List actions |


<a id="v2ActionsIdJsonGet"></a>
# **v2ActionsIdJsonGet**
> Action v2ActionsIdJsonGet(id)

Fetch an action

Fetches an action, by ID only. This endpoint will only return actions that are in_progress or pending_activity. Once an action is complete, the request for that action will return a 404 status code. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String id = "id_example"; // String | Action ID
    try {
      Action result = apiInstance.v2ActionsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#v2ActionsIdJsonGet");
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
| **id** | **String**| Action ID | |

### Return type

[**Action**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ActionsJsonGet"></a>
# **v2ActionsJsonGet**
> List&lt;Action&gt; v2ActionsJsonGet(ids, stepId, type, dueOn, userGuid, personId, cadenceId, multitouchGroupId, updatedAt, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List actions

Fetches multiple action records. The records can be filtered, paged, and sorted according to the respective parameters. Only actions that are currently \&quot;in_progess\&quot; will be returned by this endpoint.  If the requester is not an admin, this endpoint will only return actions belonging to the requester. If the request is an admin, this endpoint will return actions for the entire team. Additionaly, an admin may use the user_guid parameter to request actions that belong to specific users on the team. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of actions to fetch.
    Integer stepId = 56; // Integer | Fetch actions by step ID
    String type = "type_example"; // String | Filter actions by type
    List<String> dueOn = Arrays.asList(); // List<String> | Equality filters that are applied to the due_on field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<String> userGuid = Arrays.asList(); // List<String> | Filters actions by the user's guid. Multiple user guids can be applied. The user must be a team admin to filter other users' actions
    List<Integer> personId = Arrays.asList(); // List<Integer> | Filters actions by person_id. Multiple person ids can be applied
    List<Integer> cadenceId = Arrays.asList(); // List<Integer> | Filters actions by cadence_id. Multiple cadence ids can be applied
    List<Integer> multitouchGroupId = Arrays.asList(); // List<Integer> | Filters actions by multitouch_group_id. Multiple multitouch group ids can be applied
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<Action> result = apiInstance.v2ActionsJsonGet(ids, stepId, type, dueOn, userGuid, personId, cadenceId, multitouchGroupId, updatedAt, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#v2ActionsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of actions to fetch. | [optional] |
| **stepId** | **Integer**| Fetch actions by step ID | [optional] |
| **type** | **String**| Filter actions by type | [optional] |
| **dueOn** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the due_on field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **userGuid** | [**List&lt;String&gt;**](String.md)| Filters actions by the user&#39;s guid. Multiple user guids can be applied. The user must be a team admin to filter other users&#39; actions | [optional] |
| **personId** | [**List&lt;Integer&gt;**](Integer.md)| Filters actions by person_id. Multiple person ids can be applied | [optional] |
| **cadenceId** | [**List&lt;Integer&gt;**](Integer.md)| Filters actions by cadence_id. Multiple cadence ids can be applied | [optional] |
| **multitouchGroupId** | [**List&lt;Integer&gt;**](Integer.md)| Filters actions by multitouch_group_id. Multiple multitouch group ids can be applied | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;Action&gt;**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

