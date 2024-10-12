# EmailsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ActivitiesEmailsIdJsonGet**](EmailsApi.md#v2ActivitiesEmailsIdJsonGet) | **GET** /v2/activities/emails/{id}.json | Fetch an email |
| [**v2ActivitiesEmailsJsonGet**](EmailsApi.md#v2ActivitiesEmailsJsonGet) | **GET** /v2/activities/emails.json | List emails |


<a id="v2ActivitiesEmailsIdJsonGet"></a>
# **v2ActivitiesEmailsIdJsonGet**
> Email v2ActivitiesEmailsIdJsonGet(id)

Fetch an email

Fetches an email, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    EmailsApi apiInstance = new EmailsApi(defaultClient);
    String id = "id_example"; // String | Email ID
    try {
      Email result = apiInstance.v2ActivitiesEmailsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailsApi#v2ActivitiesEmailsIdJsonGet");
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
| **id** | **String**| Email ID | |

### Return type

[**Email**](Email.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ActivitiesEmailsJsonGet"></a>
# **v2ActivitiesEmailsJsonGet**
> List&lt;Email&gt; v2ActivitiesEmailsJsonGet(ids, updatedAt, bounced, crmActivityId, actionId, userId, status, cadenceId, stepId, oneOff, scopedFields, personId, emailAddresses, personalization, sentAt, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List emails

Fetches multiple email records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    EmailsApi apiInstance = new EmailsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of emails to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    Boolean bounced = true; // Boolean | Filters emails by whether they have bounced or not
    List<Integer> crmActivityId = Arrays.asList(); // List<Integer> | Filters emails by crm_activity_id. Multiple crm activty ids can be applied
    List<Integer> actionId = Arrays.asList(); // List<Integer> | Filters emails by action_id. Multiple action ids can be applied
    List<Integer> userId = Arrays.asList(); // List<Integer> | Filters emails by user_id. Multiple User ids can be applied
    List<String> status = Arrays.asList(); // List<String> | Filters emails by status. Multiple status can be applied, possible values are sent, sent_from_gmail, sent_from_external, pending, pending_reply_check, scheduled, sending, delivering, failed, cancelled, pending_through_gmail, pending_through_external
    List<Integer> cadenceId = Arrays.asList(); // List<Integer> | Filters emails by cadence. Multiple cadence ids can be applied
    List<Integer> stepId = Arrays.asList(); // List<Integer> | Filters emails by step. Multiple step ids can be applied
    Boolean oneOff = true; // Boolean | Filters emails by one-off only
    List<String> scopedFields = Arrays.asList(); // List<String> | Specify explicit scoped fields desired on the Email Resource.
    List<Integer> personId = Arrays.asList(); // List<Integer> | Filters emails by person_id. Multiple person ids can be applied
    List<String> emailAddresses = Arrays.asList(); // List<String> | Filters emails by recipient email address. Multiple emails can be applied.
    List<String> personalization = Arrays.asList(); // List<String> | Filters emails by personalization score
    List<String> sentAt = Arrays.asList(); // List<String> | Equality filters that are applied to the sent_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: updated_at, send_time. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<Email> result = apiInstance.v2ActivitiesEmailsJsonGet(ids, updatedAt, bounced, crmActivityId, actionId, userId, status, cadenceId, stepId, oneOff, scopedFields, personId, emailAddresses, personalization, sentAt, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailsApi#v2ActivitiesEmailsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of emails to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **bounced** | **Boolean**| Filters emails by whether they have bounced or not | [optional] |
| **crmActivityId** | [**List&lt;Integer&gt;**](Integer.md)| Filters emails by crm_activity_id. Multiple crm activty ids can be applied | [optional] |
| **actionId** | [**List&lt;Integer&gt;**](Integer.md)| Filters emails by action_id. Multiple action ids can be applied | [optional] |
| **userId** | [**List&lt;Integer&gt;**](Integer.md)| Filters emails by user_id. Multiple User ids can be applied | [optional] |
| **status** | [**List&lt;String&gt;**](String.md)| Filters emails by status. Multiple status can be applied, possible values are sent, sent_from_gmail, sent_from_external, pending, pending_reply_check, scheduled, sending, delivering, failed, cancelled, pending_through_gmail, pending_through_external | [optional] |
| **cadenceId** | [**List&lt;Integer&gt;**](Integer.md)| Filters emails by cadence. Multiple cadence ids can be applied | [optional] |
| **stepId** | [**List&lt;Integer&gt;**](Integer.md)| Filters emails by step. Multiple step ids can be applied | [optional] |
| **oneOff** | **Boolean**| Filters emails by one-off only | [optional] |
| **scopedFields** | [**List&lt;String&gt;**](String.md)| Specify explicit scoped fields desired on the Email Resource. | [optional] |
| **personId** | [**List&lt;Integer&gt;**](Integer.md)| Filters emails by person_id. Multiple person ids can be applied | [optional] |
| **emailAddresses** | [**List&lt;String&gt;**](String.md)| Filters emails by recipient email address. Multiple emails can be applied. | [optional] |
| **personalization** | [**List&lt;String&gt;**](String.md)| Filters emails by personalization score | [optional] |
| **sentAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the sent_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: updated_at, send_time. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;Email&gt;**](Email.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

