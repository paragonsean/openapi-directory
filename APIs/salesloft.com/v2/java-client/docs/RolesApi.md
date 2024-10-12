# RolesApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CustomRolesIdJsonGet**](RolesApi.md#v2CustomRolesIdJsonGet) | **GET** /v2/custom_roles/{id}.json | Fetch a custom role |
| [**v2CustomRolesJsonGet**](RolesApi.md#v2CustomRolesJsonGet) | **GET** /v2/custom_roles.json | List custom roles |


<a id="v2CustomRolesIdJsonGet"></a>
# **v2CustomRolesIdJsonGet**
> CustomRole v2CustomRolesIdJsonGet(id)

Fetch a custom role

Fetches a custom role, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String id = "id_example"; // String | Custom Role ID
    try {
      CustomRole result = apiInstance.v2CustomRolesIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#v2CustomRolesIdJsonGet");
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
| **id** | **String**| Custom Role ID | |

### Return type

[**CustomRole**](CustomRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CustomRolesJsonGet"></a>
# **v2CustomRolesJsonGet**
> List&lt;CustomRole&gt; v2CustomRolesJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List custom roles

Fetches multiple custom role records. The records can be filtered, and sorted according to the respective parameters. A custom role is any role that is not Admin or User. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | IDs of roles to fetch.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: id, name. Defaults to id
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<CustomRole> result = apiInstance.v2CustomRolesJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#v2CustomRolesJsonGet");
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
| **ids** | [**List&lt;String&gt;**](String.md)| IDs of roles to fetch. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: id, name. Defaults to id | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;CustomRole&gt;**](CustomRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

