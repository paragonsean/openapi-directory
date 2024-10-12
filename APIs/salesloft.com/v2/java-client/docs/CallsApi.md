# CallsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ActivitiesCallsIdJsonGet**](CallsApi.md#v2ActivitiesCallsIdJsonGet) | **GET** /v2/activities/calls/{id}.json | Fetch a call |
| [**v2ActivitiesCallsJsonGet**](CallsApi.md#v2ActivitiesCallsJsonGet) | **GET** /v2/activities/calls.json | List calls |
| [**v2ActivitiesCallsJsonPost**](CallsApi.md#v2ActivitiesCallsJsonPost) | **POST** /v2/activities/calls.json | Create a call |


<a id="v2ActivitiesCallsIdJsonGet"></a>
# **v2ActivitiesCallsIdJsonGet**
> Call v2ActivitiesCallsIdJsonGet(id)

Fetch a call

Fetches a call, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Call ID
    try {
      Call result = apiInstance.v2ActivitiesCallsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#v2ActivitiesCallsIdJsonGet");
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
| **id** | **String**| Call ID | |

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ActivitiesCallsJsonGet"></a>
# **v2ActivitiesCallsJsonGet**
> List&lt;Call&gt; v2ActivitiesCallsJsonGet(ids, createdAt, updatedAt, userGuid, personId, sentiment, disposition, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List calls

Fetches multiple call records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CallsApi apiInstance = new CallsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of calls to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<String> createdAt = Arrays.asList(); // List<String> | Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<String> userGuid = Arrays.asList(); // List<String> | Filters list to only include guids
    List<Integer> personId = Arrays.asList(); // List<Integer> | Filters calls by person_id. Multiple person ids can be applied
    List<String> sentiment = Arrays.asList(); // List<String> | Filters calls by sentiment. Sentiment matches are exact and case sensitive. Multiple sentiments are allowed.
    List<String> disposition = Arrays.asList(); // List<String> | Filters calls by disposition. Disposition matches are exact and case sensitive. Multiple dispositions are allowed.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<Call> result = apiInstance.v2ActivitiesCallsJsonGet(ids, createdAt, updatedAt, userGuid, personId, sentiment, disposition, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#v2ActivitiesCallsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of calls to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **createdAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **userGuid** | [**List&lt;String&gt;**](String.md)| Filters list to only include guids | [optional] |
| **personId** | [**List&lt;Integer&gt;**](Integer.md)| Filters calls by person_id. Multiple person ids can be applied | [optional] |
| **sentiment** | [**List&lt;String&gt;**](String.md)| Filters calls by sentiment. Sentiment matches are exact and case sensitive. Multiple sentiments are allowed. | [optional] |
| **disposition** | [**List&lt;String&gt;**](String.md)| Filters calls by disposition. Disposition matches are exact and case sensitive. Multiple dispositions are allowed. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;Call&gt;**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ActivitiesCallsJsonPost"></a>
# **v2ActivitiesCallsJsonPost**
> Call v2ActivitiesCallsJsonPost(personId, actionId, crmParams, disposition, duration, linkedCallDataRecordIds, notes, sentiment, to, userGuid)

Create a call

Creates a call. The parameters of this endpoint can be used to create an action and ensure that the CRM Task is mapped correctly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Integer personId = 56; // Integer | The ID of the person whom this call will be logged for
    Integer actionId = 56; // Integer | Action that this call is being logged for. This will validate that the action is still valid before completing it. The same action can never be successfully passed twice to this endpoint. The action must have a type of 'phone'. 
    Object crmParams = null; // Object | CRM specific parameters. Some parameters are required on a per-team basis. Consume the CrmActivityFields endpoint to receive a list of valid parameters. The \\\"field\\\" property is passed as the key of this object, and the value of this object is the value that you would like to set.  If CrmActivityField has a non-null value, then that value must be submitted, or excluded from API calls, as these values are automatically applied. 
    String disposition = "disposition_example"; // String | The disposition of the call. Can be required on a per-team basis. Must be present in the disposition list.
    Integer duration = 56; // Integer | The length of the call, in seconds
    List<Integer> linkedCallDataRecordIds = Arrays.asList(); // List<Integer> | CallDataRecord associations that will become linked to the created call. It is possible to pass multiple CallDataRecord ids in this field; this can be used to represent multiple phone calls that made up a single call.  Any call data record that is used must not already be linked to a call. It is not possible to link a call data record to multiple calls, and it is not possible to re-assign a call data record to a different call. 
    String notes = "notes_example"; // String | Notes to log for the call. This is similar to the notes endpoint, but ensures that the notes get synced to the user's CRM
    String sentiment = "sentiment_example"; // String | The sentiment of the call. Can be required on a per-team basis. Must be present in the sentiment list.
    String to = "to_example"; // String | The phone number that was called
    String userGuid = "userGuid_example"; // String | Guid of the user whom this call should be logged for. Defaults to the authenticated user. Only team admins can pass another user's guid
    try {
      Call result = apiInstance.v2ActivitiesCallsJsonPost(personId, actionId, crmParams, disposition, duration, linkedCallDataRecordIds, notes, sentiment, to, userGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#v2ActivitiesCallsJsonPost");
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
| **personId** | **Integer**| The ID of the person whom this call will be logged for | |
| **actionId** | **Integer**| Action that this call is being logged for. This will validate that the action is still valid before completing it. The same action can never be successfully passed twice to this endpoint. The action must have a type of &#39;phone&#39;.  | [optional] |
| **crmParams** | [**Object**](Object.md)| CRM specific parameters. Some parameters are required on a per-team basis. Consume the CrmActivityFields endpoint to receive a list of valid parameters. The \\\&quot;field\\\&quot; property is passed as the key of this object, and the value of this object is the value that you would like to set.  If CrmActivityField has a non-null value, then that value must be submitted, or excluded from API calls, as these values are automatically applied.  | [optional] |
| **disposition** | **String**| The disposition of the call. Can be required on a per-team basis. Must be present in the disposition list. | [optional] |
| **duration** | **Integer**| The length of the call, in seconds | [optional] |
| **linkedCallDataRecordIds** | [**List&lt;Integer&gt;**](Integer.md)| CallDataRecord associations that will become linked to the created call. It is possible to pass multiple CallDataRecord ids in this field; this can be used to represent multiple phone calls that made up a single call.  Any call data record that is used must not already be linked to a call. It is not possible to link a call data record to multiple calls, and it is not possible to re-assign a call data record to a different call.  | [optional] |
| **notes** | **String**| Notes to log for the call. This is similar to the notes endpoint, but ensures that the notes get synced to the user&#39;s CRM | [optional] |
| **sentiment** | **String**| The sentiment of the call. Can be required on a per-team basis. Must be present in the sentiment list. | [optional] |
| **to** | **String**| The phone number that was called | [optional] |
| **userGuid** | **String**| Guid of the user whom this call should be logged for. Defaults to the authenticated user. Only team admins can pass another user&#39;s guid | [optional] |

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

