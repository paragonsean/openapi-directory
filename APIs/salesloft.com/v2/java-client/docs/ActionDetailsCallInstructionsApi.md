# ActionDetailsCallInstructionsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ActionDetailsCallInstructionsIdJsonGet**](ActionDetailsCallInstructionsApi.md#v2ActionDetailsCallInstructionsIdJsonGet) | **GET** /v2/action_details/call_instructions/{id}.json | Fetch a call instructions |
| [**v2ActionDetailsCallInstructionsJsonGet**](ActionDetailsCallInstructionsApi.md#v2ActionDetailsCallInstructionsJsonGet) | **GET** /v2/action_details/call_instructions.json | List call instructions |


<a id="v2ActionDetailsCallInstructionsIdJsonGet"></a>
# **v2ActionDetailsCallInstructionsIdJsonGet**
> CallInstruction v2ActionDetailsCallInstructionsIdJsonGet(id)

Fetch a call instructions

Fetches a call instruction, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionDetailsCallInstructionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ActionDetailsCallInstructionsApi apiInstance = new ActionDetailsCallInstructionsApi(defaultClient);
    String id = "id_example"; // String | Call instructions ID
    try {
      CallInstruction result = apiInstance.v2ActionDetailsCallInstructionsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionDetailsCallInstructionsApi#v2ActionDetailsCallInstructionsIdJsonGet");
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
| **id** | **String**| Call instructions ID | |

### Return type

[**CallInstruction**](CallInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ActionDetailsCallInstructionsJsonGet"></a>
# **v2ActionDetailsCallInstructionsJsonGet**
> List&lt;CallInstruction&gt; v2ActionDetailsCallInstructionsJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List call instructions

Fetches multiple call instruction records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionDetailsCallInstructionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ActionDetailsCallInstructionsApi apiInstance = new ActionDetailsCallInstructionsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of call instructions to fetch.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<CallInstruction> result = apiInstance.v2ActionDetailsCallInstructionsJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionDetailsCallInstructionsApi#v2ActionDetailsCallInstructionsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of call instructions to fetch. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;CallInstruction&gt;**](CallInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

