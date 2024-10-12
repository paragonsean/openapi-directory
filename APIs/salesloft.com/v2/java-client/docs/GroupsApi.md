# GroupsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2GroupsIdJsonGet**](GroupsApi.md#v2GroupsIdJsonGet) | **GET** /v2/groups/{id}.json | Fetch a group |
| [**v2GroupsJsonGet**](GroupsApi.md#v2GroupsJsonGet) | **GET** /v2/groups.json | List groups |


<a id="v2GroupsIdJsonGet"></a>
# **v2GroupsIdJsonGet**
> Group v2GroupsIdJsonGet(id)

Fetch a group

Fetches a group, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | Group ID
    try {
      Group result = apiInstance.v2GroupsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#v2GroupsIdJsonGet");
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
| **id** | **String**| Group ID | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2GroupsJsonGet"></a>
# **v2GroupsJsonGet**
> List&lt;Group&gt; v2GroupsJsonGet(ids, sortBy, sortDirection)

List groups

Fetches multiple group records. The records can be filtered, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of groups to fetch.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    try {
      List<Group> result = apiInstance.v2GroupsJsonGet(ids, sortBy, sortDirection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#v2GroupsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of groups to fetch. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

