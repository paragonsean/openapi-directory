# NotesApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSlugMembersMemberSlugNotesGet**](NotesApi.md#workspaceSlugMembersMemberSlugNotesGet) | **GET** /{workspace_slug}/members/{member_slug}/notes | Get the member&#39;s notes |
| [**workspaceSlugMembersMemberSlugNotesIdPut**](NotesApi.md#workspaceSlugMembersMemberSlugNotesIdPut) | **PUT** /{workspace_slug}/members/{member_slug}/notes/{id} | Update a note |
| [**workspaceSlugMembersMemberSlugNotesPost**](NotesApi.md#workspaceSlugMembersMemberSlugNotesPost) | **POST** /{workspace_slug}/members/{member_slug}/notes | Create a note |


<a id="workspaceSlugMembersMemberSlugNotesGet"></a>
# **workspaceSlugMembersMemberSlugNotesGet**
> workspaceSlugMembersMemberSlugNotesGet(workspaceSlug, memberSlug, page)

Get the member&#39;s notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    NotesApi apiInstance = new NotesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    String page = "page_example"; // String | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugNotesGet(workspaceSlug, memberSlug, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#workspaceSlugMembersMemberSlugNotesGet");
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
| **workspaceSlug** | **String**|  | |
| **memberSlug** | **String**|  | |
| **page** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugMembersMemberSlugNotesIdPut"></a>
# **workspaceSlugMembersMemberSlugNotesIdPut**
> workspaceSlugMembersMemberSlugNotesIdPut(workspaceSlug, memberSlug, id, note)

Update a note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    NotesApi apiInstance = new NotesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    String id = "id_example"; // String | 
    Note note = new Note(); // Note | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugNotesIdPut(workspaceSlug, memberSlug, id, note);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#workspaceSlugMembersMemberSlugNotesIdPut");
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
| **workspaceSlug** | **String**|  | |
| **memberSlug** | **String**|  | |
| **id** | **String**|  | |
| **note** | [**Note**](Note.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | note updated |  -  |

<a id="workspaceSlugMembersMemberSlugNotesPost"></a>
# **workspaceSlugMembersMemberSlugNotesPost**
> workspaceSlugMembersMemberSlugNotesPost(workspaceSlug, memberSlug, note)

Create a note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    NotesApi apiInstance = new NotesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String memberSlug = "memberSlug_example"; // String | 
    Note note = new Note(); // Note | 
    try {
      apiInstance.workspaceSlugMembersMemberSlugNotesPost(workspaceSlug, memberSlug, note);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotesApi#workspaceSlugMembersMemberSlugNotesPost");
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
| **workspaceSlug** | **String**|  | |
| **memberSlug** | **String**|  | |
| **note** | [**Note**](Note.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | note created |  -  |
| **403** | forbidden |  -  |

