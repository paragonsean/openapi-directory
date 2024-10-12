# EmailTemplateAttachmentsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2EmailTemplateAttachmentsJsonGet**](EmailTemplateAttachmentsApi.md#v2EmailTemplateAttachmentsJsonGet) | **GET** /v2/email_template_attachments.json | List email template attachments |


<a id="v2EmailTemplateAttachmentsJsonGet"></a>
# **v2EmailTemplateAttachmentsJsonGet**
> List&lt;EmailTemplateAttachment&gt; v2EmailTemplateAttachmentsJsonGet(ids, emailTemplateId, perPage, page, includePagingCounts, limitPagingCounts)

List email template attachments

Fetches multiple email template attachment records. The records can be filtered and paged according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplateAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    EmailTemplateAttachmentsApi apiInstance = new EmailTemplateAttachmentsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of email template attachments to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<Integer> emailTemplateId = Arrays.asList(); // List<Integer> | Filters email template attachments by email template IDs
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<EmailTemplateAttachment> result = apiInstance.v2EmailTemplateAttachmentsJsonGet(ids, emailTemplateId, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplateAttachmentsApi#v2EmailTemplateAttachmentsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of email template attachments to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **emailTemplateId** | [**List&lt;Integer&gt;**](Integer.md)| Filters email template attachments by email template IDs | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;EmailTemplateAttachment&gt;**](EmailTemplateAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

