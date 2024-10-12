# NotesApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2NotesIdJsonDelete**](NotesApi.md#v2NotesIdJsonDelete) | **DELETE** /v2/notes/{id}.json | Delete a note |
| [**v2NotesIdJsonGet**](NotesApi.md#v2NotesIdJsonGet) | **GET** /v2/notes/{id}.json | Fetch a note |
| [**v2NotesIdJsonPut**](NotesApi.md#v2NotesIdJsonPut) | **PUT** /v2/notes/{id}.json | Update a note |
| [**v2NotesJsonGet**](NotesApi.md#v2NotesJsonGet) | **GET** /v2/notes.json | List notes |
| [**v2NotesJsonPost**](NotesApi.md#v2NotesJsonPost) | **POST** /v2/notes.json | Create a note |


<a id="v2NotesIdJsonDelete"></a>
# **v2NotesIdJsonDelete**
> v2NotesIdJsonDelete(id)

Delete a note

Deletes a note owned by authorized account. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    NotesApi apiInstance = new NotesApi(defaultClient);
    String id = "id_example"; // String | Note ID
    try {
      apiInstance.v2NotesIdJsonDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#v2NotesIdJsonDelete");
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
| **id** | **String**| Note ID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The Note has been deleted successfully |  -  |

<a id="v2NotesIdJsonGet"></a>
# **v2NotesIdJsonGet**
> Note v2NotesIdJsonGet(id)

Fetch a note

Fetches a note, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    NotesApi apiInstance = new NotesApi(defaultClient);
    String id = "id_example"; // String | Note ID
    try {
      Note result = apiInstance.v2NotesIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#v2NotesIdJsonGet");
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
| **id** | **String**| Note ID | |

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2NotesIdJsonPut"></a>
# **v2NotesIdJsonPut**
> Person v2NotesIdJsonPut(id, content, callId)

Update a note

Updates a note. Any changes to the note or associated records will not reflect in your CRM. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    NotesApi apiInstance = new NotesApi(defaultClient);
    String id = "id_example"; // String | Note ID
    String content = "content_example"; // String | The content of the note
    Integer callId = 56; // Integer | ID of the call with which the note is associated. The call cannot already have a note. If the note is associated to a call already, it will become associated to the requested call
    try {
      Person result = apiInstance.v2NotesIdJsonPut(id, content, callId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#v2NotesIdJsonPut");
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
| **id** | **String**| Note ID | |
| **content** | **String**| The content of the note | |
| **callId** | **Integer**| ID of the call with which the note is associated. The call cannot already have a note. If the note is associated to a call already, it will become associated to the requested call | [optional] |

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2NotesJsonGet"></a>
# **v2NotesJsonGet**
> List&lt;Note&gt; v2NotesJsonGet(associatedWithType, associatedWithId, updatedAt, ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List notes

Fetches multiple note records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    NotesApi apiInstance = new NotesApi(defaultClient);
    String associatedWithType = "associatedWithType_example"; // String | Case insensitive type of item with which the note is associated.  Value must be one of: person, account
    Integer associatedWithId = 56; // Integer | ID of the item with which the note is associated.  The associated_with_type must also be present if this parameter is used
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of notes to fetch. If a record can't be found, that record won't be returned and your request will be successful
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<Note> result = apiInstance.v2NotesJsonGet(associatedWithType, associatedWithId, updatedAt, ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#v2NotesJsonGet");
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
| **associatedWithType** | **String**| Case insensitive type of item with which the note is associated.  Value must be one of: person, account | [optional] |
| **associatedWithId** | **Integer**| ID of the item with which the note is associated.  The associated_with_type must also be present if this parameter is used | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of notes to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;Note&gt;**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2NotesJsonPost"></a>
# **v2NotesJsonPost**
> Note v2NotesJsonPost(associatedWithId, associatedWithType, content, callId, skipCrmSync, subject, userGuid)

Create a note

Creates a note. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    NotesApi apiInstance = new NotesApi(defaultClient);
    Integer associatedWithId = 56; // Integer | ID of the item with which the note is associated
    String associatedWithType = "associatedWithType_example"; // String | Case insensitive type of item with which the note is associated.  Value must be one of: person, account
    String content = "content_example"; // String | The content of the note
    Integer callId = 56; // Integer | ID of the call with which the note is associated. The call cannot already have a note
    Boolean skipCrmSync = true; // Boolean | Boolean indicating if the CRM sync should be skipped.  No syncing will occur if true
    String subject = "subject_example"; // String | The subject of the note's crm activity, defaults to 'Note'
    String userGuid = "userGuid_example"; // String | The user to create the note for. Only team admins may create notes on behalf of other users. Defaults to the requesting user
    try {
      Note result = apiInstance.v2NotesJsonPost(associatedWithId, associatedWithType, content, callId, skipCrmSync, subject, userGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#v2NotesJsonPost");
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
| **associatedWithId** | **Integer**| ID of the item with which the note is associated | |
| **associatedWithType** | **String**| Case insensitive type of item with which the note is associated.  Value must be one of: person, account | |
| **content** | **String**| The content of the note | |
| **callId** | **Integer**| ID of the call with which the note is associated. The call cannot already have a note | [optional] |
| **skipCrmSync** | **Boolean**| Boolean indicating if the CRM sync should be skipped.  No syncing will occur if true | [optional] |
| **subject** | **String**| The subject of the note&#39;s crm activity, defaults to &#39;Note&#39; | [optional] |
| **userGuid** | **String**| The user to create the note for. Only team admins may create notes on behalf of other users. Defaults to the requesting user | [optional] |

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

