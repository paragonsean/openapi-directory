# TeamTemplateAttachmentsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2TeamTemplateAttachmentsJsonGet**](TeamTemplateAttachmentsApi.md#v2TeamTemplateAttachmentsJsonGet) | **GET** /v2/team_template_attachments.json | List team template attachments |


<a id="v2TeamTemplateAttachmentsJsonGet"></a>
# **v2TeamTemplateAttachmentsJsonGet**
> List&lt;TeamTemplateAttachment&gt; v2TeamTemplateAttachmentsJsonGet(ids, teamTemplateId, perPage, page, includePagingCounts, limitPagingCounts)

List team template attachments

Fetches multiple team template attachment records. The records can be filtered and paged according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamTemplateAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    TeamTemplateAttachmentsApi apiInstance = new TeamTemplateAttachmentsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of team template attachments to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<Integer> teamTemplateId = Arrays.asList(); // List<Integer> | Filters template attachments by team template IDs
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<TeamTemplateAttachment> result = apiInstance.v2TeamTemplateAttachmentsJsonGet(ids, teamTemplateId, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamTemplateAttachmentsApi#v2TeamTemplateAttachmentsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of team template attachments to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **teamTemplateId** | [**List&lt;Integer&gt;**](Integer.md)| Filters template attachments by team template IDs | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;TeamTemplateAttachment&gt;**](TeamTemplateAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

