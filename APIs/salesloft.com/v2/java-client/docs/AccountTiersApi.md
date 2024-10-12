# AccountTiersApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2AccountTiersIdJsonGet**](AccountTiersApi.md#v2AccountTiersIdJsonGet) | **GET** /v2/account_tiers/{id}.json | Fetch an account tier |
| [**v2AccountTiersJsonGet**](AccountTiersApi.md#v2AccountTiersJsonGet) | **GET** /v2/account_tiers.json | List Account Tiers |


<a id="v2AccountTiersIdJsonGet"></a>
# **v2AccountTiersIdJsonGet**
> AccountTier v2AccountTiersIdJsonGet(id)

Fetch an account tier

Fetches an account tier, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountTiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    AccountTiersApi apiInstance = new AccountTiersApi(defaultClient);
    String id = "id_example"; // String | Account Tier ID
    try {
      AccountTier result = apiInstance.v2AccountTiersIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountTiersApi#v2AccountTiersIdJsonGet");
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
| **id** | **String**| Account Tier ID | |

### Return type

[**AccountTier**](AccountTier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2AccountTiersJsonGet"></a>
# **v2AccountTiersJsonGet**
> List&lt;AccountTier&gt; v2AccountTiersJsonGet(ids, name, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List Account Tiers

Fetches multiple account tier records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountTiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    AccountTiersApi apiInstance = new AccountTiersApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of Account Tiers to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<String> name = Arrays.asList(); // List<String> | Filters Account Tiers by name. Multiple names can be applied
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at, order. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<AccountTier> result = apiInstance.v2AccountTiersJsonGet(ids, name, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountTiersApi#v2AccountTiersJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of Account Tiers to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **name** | [**List&lt;String&gt;**](String.md)| Filters Account Tiers by name. Multiple names can be applied | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, order. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;AccountTier&gt;**](AccountTier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

