# CrmUsersApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CrmUsersJsonGet**](CrmUsersApi.md#v2CrmUsersJsonGet) | **GET** /v2/crm_users.json | List crm users |


<a id="v2CrmUsersJsonGet"></a>
# **v2CrmUsersJsonGet**
> List&lt;CrmUser&gt; v2CrmUsersJsonGet(ids, crmId, userId, userGuid, perPage, page, includePagingCounts, limitPagingCounts, sortBy, sortDirection)

List crm users

Crm Users 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrmUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CrmUsersApi apiInstance = new CrmUsersApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of crm users to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<String> crmId = Arrays.asList(); // List<String> | Filters crm users by crm_ids
    List<Integer> userId = Arrays.asList(); // List<Integer> | Filters crm users by user_ids
    List<String> userGuid = Arrays.asList(); // List<String> | Filters crm users by user guids
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: id, updated_at. Defaults to id
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    try {
      List<CrmUser> result = apiInstance.v2CrmUsersJsonGet(ids, crmId, userId, userGuid, perPage, page, includePagingCounts, limitPagingCounts, sortBy, sortDirection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrmUsersApi#v2CrmUsersJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of crm users to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **crmId** | [**List&lt;String&gt;**](String.md)| Filters crm users by crm_ids | [optional] |
| **userId** | [**List&lt;Integer&gt;**](Integer.md)| Filters crm users by user_ids | [optional] |
| **userGuid** | [**List&lt;String&gt;**](String.md)| Filters crm users by user guids | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: id, updated_at. Defaults to id | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |

### Return type

[**List&lt;CrmUser&gt;**](CrmUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

