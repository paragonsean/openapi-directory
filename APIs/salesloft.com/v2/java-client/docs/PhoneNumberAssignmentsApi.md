# PhoneNumberAssignmentsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2PhoneNumberAssignmentsIdJsonGet**](PhoneNumberAssignmentsApi.md#v2PhoneNumberAssignmentsIdJsonGet) | **GET** /v2/phone_number_assignments/{id}.json | Fetch a phone number assignment |
| [**v2PhoneNumberAssignmentsJsonGet**](PhoneNumberAssignmentsApi.md#v2PhoneNumberAssignmentsJsonGet) | **GET** /v2/phone_number_assignments.json | List phone number assignments |


<a id="v2PhoneNumberAssignmentsIdJsonGet"></a>
# **v2PhoneNumberAssignmentsIdJsonGet**
> PhoneNumberAssignment v2PhoneNumberAssignmentsIdJsonGet(id)

Fetch a phone number assignment

Fetches a phone number assignment, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhoneNumberAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PhoneNumberAssignmentsApi apiInstance = new PhoneNumberAssignmentsApi(defaultClient);
    String id = "id_example"; // String | PhoneNumberAssignment ID
    try {
      PhoneNumberAssignment result = apiInstance.v2PhoneNumberAssignmentsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhoneNumberAssignmentsApi#v2PhoneNumberAssignmentsIdJsonGet");
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
| **id** | **String**| PhoneNumberAssignment ID | |

### Return type

[**PhoneNumberAssignment**](PhoneNumberAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2PhoneNumberAssignmentsJsonGet"></a>
# **v2PhoneNumberAssignmentsJsonGet**
> List&lt;PhoneNumberAssignment&gt; v2PhoneNumberAssignmentsJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List phone number assignments

Fetches multiple phone number assignment records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhoneNumberAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PhoneNumberAssignmentsApi apiInstance = new PhoneNumberAssignmentsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of phone number assignments to fetch
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<PhoneNumberAssignment> result = apiInstance.v2PhoneNumberAssignmentsJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhoneNumberAssignmentsApi#v2PhoneNumberAssignmentsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of phone number assignments to fetch | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;PhoneNumberAssignment&gt;**](PhoneNumberAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

